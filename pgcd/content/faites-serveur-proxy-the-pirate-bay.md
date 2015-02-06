Title: Faites de votre serveur un proxy pour The Pirate Bay
Date: 2014-12-06 13:22
Category: Auto-hébergement
Author: Matlink
Tags: tutoriel, neutralité du net, censure, liberté
Image: 543px-The_Pirate_Bay_logo.svg.png


Après la [magnifique nouvelle que nous annonce la
SCPP](http://www.numerama.com/magazine/31495-the-pirate-bay-sera-bloque-en-france-avec-ses-miroirs.html),
c'est [l'effet
Streisand](https://fr.wikipedia.org/wiki/Effet_Streisand). On peut
penser que ces génies vont nous filtrer tout ce beau petit monde en
tapant dans les DNS (comme l'idée [révolutionnaire de la loi Lutte
contre le
terrorisme](http://www.linformaticien.com/actualites/id/34237/le-blocage-dns-retenu-par-les-deputes-pour-lutter-contre-le-terrorisme.aspx)).
Dans ce cas, il suffit de créer des centaines voire des milliers de
proxies pour The Pirate Bay qui n'auront donc pas le même nom de
domaine. Ainsi, l'adresse http://tpb.matlink.fr fera en sorte de
communiquer avec le vrai serveur de TPB, directement via son IP.

Et pour vous montrer à quel point c'est simple de faire ceci, je vous
explique :

- pour Nginx, ajouter ce code dans le fichier de déclaration des serveurs virtuels :


        #The Pirate Bay Proxy 
        server{
          listen 80;
          listen [::]:80;
          server_name tpb.xxxx.xx; #domaine que l'on souhaite donner au proxy
          location / {
             proxy_pass https://194.71.107.27/;
             proxy_set_header Host thepiratebay.se;
          }
        }

- pour Apache :


        <VirtualHost *:80>
           ServerName      tpb.xxx.xx
           ProxyPreserveHost   On
           RequestHeader set Host  thepiratebay.se
           ProxyPass    /  https://194.71.107.27/
           ProxyPassReverse /  https://194.71.107.27/
        </VirtualHost>

ensuite, il vous suffit de redémarrer votre serveur Nginx/Apache :
``/etc/init.d/nginx reload`` ou ``/etc/init.d/apache2 reload``

n'oubliez pas d'ajouter dans votre zone DNS le tpb.xxxx.xx CNAME xxxx.xx
que vous avez mis dans votre fichier de config.

À vos proxies !
