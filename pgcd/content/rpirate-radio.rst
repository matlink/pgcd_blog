Pirate Radio : transformez votre Raspberry Pi en émetteur radio
###############################################################
:date: 2014-11-16 17:05
:category: PGCD
:author: Matlink
:slug: rpirate-radio

Depuis que j'ai ce joujou de `raspberry
pi <https://en.wikipedia.org/wiki/Raspberry_Pi>`__, je ne cesse de
chercher à le bidouiller pour donner des choses marrantes.

Et je suis tombé sur un article décrivant comment bidouiller son RPI
pour en faire une radio.
<http://makezine.com/projects/make-38-cameras-and-av/raspberry-pirate-radio/>`__

Il faut savoir que le RPI (modèle A et B) possède 26 pins GPIO
permettant de contrôler un module externe ou de recevoir des
informations. Avec un petit bout de code (en Python ou autre), il est
alors possible par exemple d'allumer une LED, faire tourner un moteur,
recevoir un signal quand on appuie sur un bouton, ... Les usages sont
multiples et infinis.

Dans cet article, je vais vous montrer comment j'ai moi-même fait pour
faire fonctionner mon RPI en mode radio, car j'ai certaines choses à
rajouter concernant l'installation de base.

Tout d'abord on se connecte en SSH sur la raspberry, et une fois dessus,
on va récupérer le script Python qui permet de lancer la radio :

-  on installe git si c'est pas déjà fait : 
   ``sudo apt-get install git``
-  ensuite, ffmpeg pour lire les fichiers de musique :
   ``sudo apt-get install ffmpeg``
-  config-parser pour lire les fichiers de configuration :
   ``sudo apt-get install python-pip && sudo pip install configparser``
-  on créer un dossier pour la radio :
   ``sudo mkdir ∕pirateradio/ && cd /pirateradio/``
-  on récupère les scripts python de la radio :
   ``git clone https://github.com/Make-Magazine/PirateRadio ./``
-  on modifie le fichier Python pour renseigner notre dossier :
   ``sudo sed -i 's@/root/pifm@/pirateradio/pifm@g' /pirateradio/PirateRadio.py``
-  on ouvre le fichier de configuration et on y met nos paramètres :
   ``sudo nano pirateradio.conf``

   -  frequency : la fréquence sur laquelle émettre la musique
   -  shuffle : True pour activer la lecture aléatoire, False sinon
   -  repeat\_all : True si vous voulez jouer en boucle les musiques
   -  stereo\_playback : pour activer ou non le stéréo
   -  music\_dir : le répertoire où se trouvent vos musiques

Vous copiez ensuite vos musiques dans le répertoire que vous avez
indiqué dans le fichier de configuration. Après ça, il vous faut trouver
un fil métallique afin de faire antenne. Pour ma part, j'ai récupéré le
câble d'un appareil qui ne fonctionnait plus. Vous devez le brancher sur
votre RPI sur le GPIO 4 (le pin 7) comme sur la photo ci dessus :

[caption id="attachment\_147" align="aligncenter"
width="300"]\  Cliquez pour agrandir[/caption]

Il vous reste ensuite plus qu'à lancer la radio avec la commande 
`` python /pirateradio/PirateRadio.py``

J'ai créé un script shell pour installer tout ça automatiquement,
disponible ici :https://github.com/matlink/rpi-radio

`source <http://makezine.com/projects/make-38-cameras-and-av/raspberry-pirate-radio/>`__

.. |antenne\_gpio\_pin7\_400| image:: https://matlink.fr/PGCD/wp-content/uploads/2014/11/antenne_gpio_pin7_400-300x224.jpg
   :target: https://matlink.fr/PGCD/wp-content/uploads/2014/11/antenne_gpio_pin7_400.jpg
