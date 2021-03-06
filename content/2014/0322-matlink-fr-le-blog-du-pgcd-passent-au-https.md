Title: Matlink.fr & le blog du PGCD passent au HTTPS !
Date: 2014-03-22 18:11
Category: Annonces
Author: Matlink
Slug: matlink-fr-le-blog-du-pgcd-passent-au-https

Eh oui ! En ces temps de surveillance numérique massive, nous nous
devons tous de protéger nos données qui trafiquent sur les réseaux.

C'est pourquoi je viens tout juste de passer le serveur
[NGINX](https://fr.wikipedia.org/wiki/Nginx) sur lequel est hébergé
ce blog, en mode
[HTTPS](https://fr.wikipedia.org/wiki/HyperText_Transfer_Protocol_Secure):
désormais, il force les utilisateurs à utiliser ce protocole sécurisé
qui permet un
[chiffrement](<https://fr.m.wikipedia.org/wiki/Principe_de_bout-%C3%A0-bout) [end-to-end](https://fr.m.wikipedia.org/wiki/Principe_de_bout-%C3%A0-bout>), ce
qui veut dire que tout est chiffré entre le serveur et le client.
Autrement dit, vos mots de passe, les pages demandées, et tout le reste
de votre communication entre ce serveur (plus exactement le Nginx) et
votre navigateur web est indéchiffrable (sauf malheureusement le nom de domaine qui passe en clair) !

<s>
Cependant, [mon certificat SSL étant
auto-signé](https://en.wikipedia.org/wiki/Self-signed_certificate)</s>,
il n'est donc approuvé par aucune autorité apte à le signer, c'est ce
qui explique que votre navigateur web vous alerte à propos de l'identité
du certificat qu'il reçoit. Il faudrait payer un service de confiance
pour faire signer ce dernier, moyennant de l'argent.

Plus de problème, il est maintenant signé par
[StartSSL](https://www.startssl.com).

Si jamais vous avez des soucis liés à ce changement ou des questions,
n'hésitez pas à en parler dans les commentaires.

Pour vous servir,

Matlink
