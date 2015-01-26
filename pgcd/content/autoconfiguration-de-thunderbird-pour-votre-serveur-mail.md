Title: Autoconfiguration de Thunderbird pour votre serveur mail
Date: 2014-11-27 19:58
Category: Auto-hébergement
Author: Matlink
Slug: autoconfiguration-de-thunderbird-pour-votre-serveur-mail

<span class="float-left">
  ![thunderbird]({filename}/images/thunderbird-head.png)
</span>


Si vous gérez un serveur mail, qu'il soit chez vous ou bien hébergé chez
un fournisseur, vous vous êtes sûrement rendus compte quand vous
configuriez un logiciel de messagerie comme Thunderbird, que vous deviez
rentrer toutes les infos à la main (serveur entrant, serveur sortant,
ports, type de connexion chiffrée, ...). Quand on connaît ces infos, au
final, c'est pas très grave. Le problème est que si nous ne sommes pas
le seul à utiliser notre serveur mail (dans le cas où nous fournissons
une ou plusieurs adresses à d'autres personnes), les autres utilisateurs
ne sont pas forcément avertis concernant la configuration à entrer pour
leur client mail.

Sachez donc que Thunderbird (que j'utilise et adore) propose un système
d'auto-configuration. En réalité, il procède en plusieurs étapes
(supposons que l'adresse mail est foo@example.com):

1. recherche du fichier example.com.xml dans le dossier d'installation
   de Thunderbird (*dossierinstallation*/isp/example.com.xml exactement)
2. recherche du nom de domaine autoconfig.example.com
3. recherche "example.com" dans la base de données de Mozilla concernant
   les fournisseurs de mail
4. recherche de "MX example.com" au niveau du DNS, et pour
   mx1.mail.hoster.com, recherche de "hoster.com" dans la base de
   données de Mozilla
5. essaye de deviner des noms courants (imap.example.com,
   smtp.example.com, ...)

Je vais pas détailler chaque point, mais il faut savoir que dès que
Thunderbird trouve une configuration dans l'un des points, il s'arrête
et la propose à l'utilisateur.

Le premier point n'est pas envisageable car évidement cela requiert que
chaque utilisateur récupère le fichier de configuration et le mette dans
le bon dossier. Le deuxième demande de toucher aux configurations DNS,
choses auxquelles nous n'avons pas toujours accès (et que parfois nous
voulons laisser telles quelles). La troisième demande de faire une
demande à Mozilla pour l'ajouter dans sa base de données, pas pratique
et peut prendre du temps, sachant que Mozilla privilégie les plus gros.

Il nous reste que la quatrième solution (la cinquième n'en est pas une
car ceci est une recherche des noms courants). Il y a un moyen simple de
proposer l'auto-configuration pour Thunderbird, c'est de placer le
fichier de configuration du client mail à cette adresse :
http://example.com/.well-known/autoconfig/mail/config-v1.1.xml.

Et le fichier doit être ainsi :



    <clientConfig version="1.0">
        <emailProvider id="matlink.fr">
              <domain>matlink.fr</domain>
              <displayName>Messagerie Matlink</displayName>
              <displayShortName>MATLINK</displayShortName>
              <incomingServer type="imap">
                    <hostname>fr.matlink.fr</hostname>
                    <port>993</port>
                    <socketType>SSL</socketType>
                    <username>%EMAILLOCALPART%</username>
                    <authentication>plain</authentication>
              </incomingServer>
              <outgoingServer type="smtp">
                    <hostname>fr.matlink.fr</hostname>
                    <port>465</port>
                    <socketType>SSL</socketType>
                    <authentication>plain</authentication>
                    <username>%EMAILLOCALPART%</username>
              </outgoingServer>
        </emailProvider>
    </clientConfig>

en remplaçant bien sûr les données de mon serveur par celles du votre.
Et voilà, les nouveaux comptes pour ce nom de domaine seront
automatiquement configurés pour Thunderbird (et à priori c'est le seul
bon client mail à pouvoir faire ça, avec Outlook de
Microsoft).

<center>![config-found]({filename}/images/config-found.png)</center>

[sources](https://developer.mozilla.org/en-US/docs/Mozilla/Thunderbird/Autoconfiguration)

