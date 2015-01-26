Comprendre la faille OpenSSL HeartBleed
#######################################
:date: 2014-04-09 19:28
:category: PGCD
:author: Matlink
:slug: comprendre-faille-openssl-heartbleed

|image0|\ Pour ceux qui ne le savent pas encore, une faille de sécurité
viens d'être dévoilée au grand public, remettant en cause beaucoup de
serveurs web utilisant le paquet OpenSSL.

OpenSSL est un paquet de sécurité qui permet de créer des clés privées
et publiques utiles à la génération de certificats, permettant la
connexion chiffrée entre un client et un serveur web. Le certificat d'un
site web est un fichier, signé par une clé privée (que seul le
propriétaire du site web possède, en toute logique), qui certifie
l'authenticité de la connexion en stipulant que le site que vous visitez
est bien celui que vous pensez être et pas une usurpation.

OpenSSL utilise une extension nommée HeartBeat depuis la version 1.0.1 .
Cependant, cette extension possède une faille qui permet de récupérer la
clé privée du serveur auquel le client se connecte, et ce sans aucune
trace. Avec cette clé, il est donc possible de se faire passer pour le
propriétaire du site web, et aussi de décrypter tous les messages
cryptés avec la clé publique associée à celle-ci. C'est potentiellement
toutes les communications établies entre le serveur et ses clients
depuis qu'OpenSSL utilise HeartBeat qui sont remises en cause, car il
suffit qu'un seul client récupère la clé et sniffe (man-in-the-middle)
les communications pour pouvoir les déchiffrer.

 

Heureusement, le paquet OpenSSL vient d'être mis à jour, comblant la
faille. Mais il faut bien comprendre que cette mise à jour ne suffit
pas, car si la clé a été récupérée, elle peut encore être utilisée
contre vous. Il faut donc révoquer la clé publique associée (et par
conséquent la privée aussi, en la rangeant bien au chaud pour ne plus
l'utiliser) et générer un nouveau couple privée/publique, régénérer un
certificat avec celles-ci et le refaire signer par une autorité de
certificats pour ainsi l'utiliser sur votre serveur.

Si vous voulez des détails, des tonnes d'articles sont disponibles sur
le web. Aussi, il existe des outils en ligne pour tester votre serveur
web, `tels que celui-ci <https://submeet.net/tools/heartbleed.php>`__.

Rassurez vous, le blog du PGCD s'est mis à jour et a changé ses clés.

 

.. |image0| image:: https://matlink.fr/PGCD/wp-content/uploads/2014/04/Heartbleed.svg_-250x300.png
   :target: https://matlink.fr/PGCD/wp-content/uploads/2014/04/Heartbleed.svg_.png
