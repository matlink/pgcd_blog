Title: Mon script Python pour récupérer des Apks du Play Store
Date: 2015-04-10 17:00
Category: Logiciels Libres
Author: Matlink
Tags: android,tuto,google play store
Slug: script-python-récupérer-apks-play-store
Image: 20150405/antrollid.jpeg

Comme évoqué dans mon billet sur [comment je m'évade du Play Store]({filename}/2015/0405-comment-je-mevade-google-android.md), j'ai fait de [GooglePlayDownloader](https://codingteam.net/project/googleplaydownloader) (qui n'est disponible qu'en interface graphique) une version en ligne de commande simplement. Le script est disponible via cette adresse, sur github : [https://github.com/matlink/gplay-cli](https://github.com/matlink/gplay-cli).

Donc maintenant, je vais vous montrer comment vous en servir. 

Pré-requis
----------
Cela fonctionne sur GNU/Linux mais aussi sous Windows, `pip` est installé par défaut avec Python 2.9+.
Le script utilise quelques librairies, qu'il vous faudra installer avec `pip` : 

- python-protobuf (>=2.4) pour le dialogue avec le Google PlayStore -> `pip install protobuf`
- python-requests (>=0.12) -> `pip install requests`
- python-ndg-httpsclient pour les connections SSL -> `pip install ndg-httpsclient`
- python (>=2.5)

À l'aide !
----------
Premièrement pour avoir de l'aide, tapez `./gplay-cli.py -h` : 

		usage: gplay-cli.py [-h] [-y] [-s SEARCH] [-n NUMBER] [-d AppID [AppID ...]]
                    [-u FOLDER] [-f FOLDER] [-v] [-c CONF_FILE] [-p]

		A Google Play Store Apk downloader and manager for command line

		optional arguments:
		  -h, --help            show this help message and exit
		  -y, --yes             Say yes to all prompted questions
		  -s SEARCH, --search SEARCH
		                        Search the given string in Google Play Store
		  -n NUMBER, --number NUMBER
		                        For the search option, returns the given number of
		                        matching applications
		  -d AppID [AppID ...], --download AppID [AppID ...]
		                        Download the Apps that map given AppIDs
		  -u FOLDER, --update FOLDER
		                        Update all APKs in a given folder
		  -f FOLDER, --folder FOLDER
		                        Where to put the downloaded Apks, only for -d command
		  -v, --verbose         Be verbose
		  -c CONF_FILE, --config CONF_FILE
		                        Use a different config file than credentials.conf
		  -p, --progress        Prompt a progress bar while downloading packages


On va détailler chaque option une à une. La première, `--yes` qui permet de répondre oui à toutes les questions posées par le script. Pour le moment, la seule question qui est posée est "Do you agree? y/n ?" lors des mises à jour des applications, quand elles sont disponibles.

Recherche
---------
La deuxième est `--search` suivie d'une chaîne à rechercher. Elle permet de lancer une recherche sur le Play Store concernant la chaîne donnée. Le résultat est affiché sous forme de tableau avec les différentes valeurs de l'application. Voyons sur un exemple : `./gplay-cli.py --search firefox`

	Title                          Creator             Size     Downloads     Last Update    AppID                            Version     Rating  
	Firefox pour Android           Mozilla             33.5MB   100 000 000+  3 avr. 2015    org.mozilla.firefox              2015040230  4.35    
	Firefox Beta                   Mozilla             34.2MB   5 000 000+    7 avr. 2015    org.mozilla.firefox_beta         2015040628  4.35    
	Opera Mini - navigateur web    Opera Software ASA  1.2MB    100 000 000+  22 janv. 2015  com.opera.mini.android           34          4.40    
	Navigateur Google Chrome       Google Inc.         30.4MB   500 000 000+  20 mars 2015   com.android.chrome               2272096     4.24    
	Navigateur Web                 Litter Penguin      774.1KB  1 000 000+    25 nov. 2014   com.explore.web.browser          210         4.02    
	FlashFox - Flash Browser       Mobius Networks     32.6MB   1 000 000+    8 avr. 2015    mobi.browser.flashfox            2015040724  3.75    
	Dolphin Browser                Dolphin Browser     14.5MB   50 000 000+   2 avr. 2015    mobi.mgeek.TunnyBrowser          445         4.56    
	Navigateur Opera pour Android  Opera Software ASA  18.6MB   50 000 000+   19 mars 2015   com.opera.browser                1600590386  4.33    
	XMLViewer for Firefox          Metaphyze           226.2KB  100 000+      1 juin 2013    com.flashmatch.xmlviewerfirefox  4           4.20    
	UC Browser pour Android        UCWeb Inc.          15.2MB   100 000 000+  18 mars 2015   com.UCMobile.intl                171         4.51

Le tableau n'est pas bien arrangé ici, j'ai simplement copié-collé la sortie de la commande et la taille des espaces n'est pas la même sur navigateur. On peut y voir, pour chaque application, son titre, son créateur, sa taille, son nombre de téléchargements, la date de sa dernière mise à jour, son `AppID` qui va nous intéresser par la suite, son numéro de version qui permet au script de vérifier des mises à jour, et enfin son score sur 5 selon les utilisateurs.
Par défaut, il ne récupère que les 10 premiers résultats. Si l'option `--number` est spécifiée, le nombre qui suit définira le nombre de résultats à afficher.

Téléchargement
--------------
Maintenant, l'option `--download` suivie d'un `AppID`. C'est là qu'intervient l'`AppID` récupéré pour la recherche. Cette option télécharge l'application correspondante à l'`AppID` dans le dossier courant, et la nomme AppID.apk. Par défaut, la commande n'affiche rien, mais avec l'option `--verbose` elle montrera l'application en cours de téléchargement : 

	$ ./gplay-cli.py --download org.mozilla.firefox --verbose
	1/1 org.mozilla.firefox 

Rien de bien magique. Par la suite, pour que ce soit un peu plus agréable à l'utilisation, j'espère pouvoir intégrer une barre de progression. Sachez qu'il est possible de spécifier plusieurs `AppID` à la suite pour télécharger plusieurs Apks : 

	$ ./gplay-cli.py --download org.mozilla.firefox org.mozilla.firefox_beta --verbose
	1/2 org.mozilla.firefox
	2/2 org.mozilla.firefox_beta 

Mises à jour 
------------
L'option `--update` suivie d'un chemin contenant des fichiers .apks va scanner tous les fichiers d'application pour vérifier s'il n'y a pas des mises à jour de disponibles. Si c'est le cas, le script vous propose de les mettre à jour en vous demandant votre accord avec "Do you agree? y/n ?" sauf si l'option `--yes` est spécifiée, auquel cas il les mettra à jour sans demander. Un exemple avec firefox : 

	$ ./gplay-cli.py --update ./mes_apks/
	The following applications will be updated :
	org.mozilla.firefox.apk Version : 2015032020 -> 2015040230

	Do you agree?
	y/n ?y

Spécifier un dossier de destination pour `--download`
----------------------------------------------------
C'est avec `--folder` suivi du dossier dans lequel vous voulez télécharger l'apk. Par exemple, téléchargeons firefox dans le dossier "mes_apks" (si le dossier n'existe pas alors il sera créé) : 

	$ ./gplay-cli.py --download org.mozilla.firefox --folder ./mes_apks/

Cette option n'est valable que pour l'option `--download`. Si cette dernière n'est pas renseignée, alors l'option `--folder` sera ignorée !

Parle, petit script !
---------------------
Vous l'aurez compris, l'option `--verbose` permet de rendre le script plus verbeux

Progression
-----------
L'option `--progress` affichera une barre de progression pendant le téléchargements des applications.

Des raccourcis pour les options
-------------------------------
Car taper `--download` est trop long, voici la liste des raccourcis pour les options : 

- `--help` -> `-h`
- `--yes` -> `-y`
- `--search` -> `-s`
- `--number` -> `-n`
- `--download` -> `-d`
- `--update` -> `-u`
- `--folder` -> `-f`
- `--verbose` -> `-v`
- `--progress` -> `-p`

Ainsi, taper `-d` revient à écrire `--download`.

Compte Google
-------------
Ce script nécessite 3 choses pour fonctionner : une adresse gmail, son mot de passe et un `android_ID`. Ceux par défaut sont fournis par Tuxicoman et sont fonctionnels en l'état. Cependant vous voudriez probablement changer ces informations, pour un compte à vous, qu'il soit nouveau ou pas. Pour cela, et ce n'est pas très pratique pour le moment je vous l'accorde, il faut ouvrir le fichier `gplay-cli.py` et changer les informations à la ligne `self.config`.

Si vous souhaitez générer un `android_ID`, voyez [https://github.com/nviennot/android-checkin](https://github.com/nviennot/android-checkin) sinon vous pouvez utiliser celui d'un de vos appareils. Cela peut-être utile par exemple, lorsque l'application voulue n'est pas disponible pour l'appareil possédant cet `android_ID`.

Ce qu'il reste à faire
----------------------
C'est pas fini, et je compte ajouter les fonctionnalités suivantes : 

- <strike> gérer les erreurs quand l'`AppID` ne correspond à aucune application existante sur le Play Store </strike> : l'erreur "this package does not exist, try to search it via `--search` before" est affichée au cas où le nom donné n'existe pas
- <strike> spécifier le nombre de résultats pour la recherche </strike> :  c'est fait, avec l'option `--number` suivie du nombre de résultats à conserver
- <strike> pouvoir gérer la conf du compte Google et de l'`android_ID` dans un fichier extérieur au script </strike> : les identifiants sont à mettre dans `credentials.conf` désormais
- <strike>avoir une barre de progression, ou un taux d'avancement pour les téléchargements des applications</strike>: disponible avec l'option `--progress`

Si vous y trouvez des bugs, avez de quelconques remarques concernant ce script, voulez m'aider, ou pas, je serai ravi d'en parler dans les commentaires ou par mail !