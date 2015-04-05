Title: Comment je m'évade de Google Play Store sur Android
Date: 2015-04-05
Category: Auto-hébergement
Author: Matlink
Tags: android,google,tuto
Slug: comment-je-mevade-google-store-android
Image: 20150405/antrollid.jpeg


S'évader, c'est le bon mot selon moi car Google est une prison.

Je vous parlais dans un [récent billet]({filename}/2015/0326-recherche-dev-android.md) d'une application pour télécharger les Apks du Play Store depuis un PC. Sauf que bien évidement c'est galère pour les mises à jour, les installation de nouvelles apps, ...

<span class="figure float-left">
![logo F-Droid]({filename}/images/20150405/fdroid.png)
<span class="caption">F-Droid</span>
</span>
Si vous ne connaissez pas [F-Droid](https://f-droid.org/), il s'agit en fait d'un store alternatif ne regroupant que des applications pour Androïd sous licence libre. On peut y retrouver Mozilla Firefox, [K-9 Mail](https://en.wikipedia.org/wiki/K-9_Mail), [VLC](https://www.videolan.org/vlc/download-android.html) et bien d'autres. C'est très utile car cela évite de passer par le market de Google. Une bonne pratique, c'est de d'abord consulter F-Droid afin de savoir si l'app que l'on cherche n'y est pas avant de regarder ailleurs. Ainsi, on [privilégie le logiciel libre](https://www.april.org/campagne/).

Il faut savoir qu'il est possible de monter son propre dépôt F-Droid afin de servir ses propres applications. On peut retrouver les dépôts de différents acteurs de la lutte pour le logiciel libre tel que [The Guardian Project](https://guardianproject.info/)(qui d'ailleurs est inclut par défaut dans F-Droid mais pas activé). C'est sympa, et ça permet d'avoir un choix (qui est mieux que 0 quand on utilise le Google Play Store) qui favorise la décentralisation. Pour monter son propre dépôt, il suffit de suivre [ce tuto](https://f-droid.org/wiki/page/Installing_the_Server/Repo_Tools) utilisant un outil écrit en Python qui permet de le gérer facilement : mises à jour, archives, description des applications ... 

Du coup je me suis dit : "J'ai une app PC qui télécharge mes apks du Play Store. Et j'ai possibilité de monter un dépot F-Droid. Pourquoi ne pas lier les deux ?". [Google Play Downloader de Tuxicoman](https://codingteam.net/project/googleplaydownloader) n'est qu'en interface graphique, j'ai donc concocté [un petit script Python](https://github.com/matlink/gplay-cli) qui reprends largement le code d'origine pour en faire un en ligne de commande uniquement. À partir de ça, on peut faire les mises à jour d'Apks facilement et régulièrement via des cronjobs, et envoyer les apks mis à jour dans le dépôt F-Droid. C'est là qu'est né mon [dépot qui se met à jour tout seul](https://matlink.fr/fdroid/).

Plus de Google sur mon téléphone Android (Cyanogenmod sans les Google Apps) mais je peux quand même profiter des applications du Play Store sans que [The Evil Big Brother](https://fr.wikipedia.org/wiki/Don't_be_evil) soit dans mon téléphone. Je trouve ça cool, et chacun peut monter son petit dépôt perso et en faire profiter la communauté. Les trolls diront que Cyanogenmod est maintenant une entreprise et que c'est mal d'installer Cyanogenmod. En attendant, c'est l'alternative qui je trouve possède le plus de fonctionnalités, est la moins boguée, et qui possède le bouclier "protection des données" bloquant tous les accès à vos données personnelles (contacts, SMS, journal d'appels) par défaut. Il faut ensuite accepter si besoin l'autorisation demandée par l'application à accéder à une partie de vos données. 

Il me manque plus qu'une [connexion](https://yunohost.org/#/isp_fr) d'entreprise [SDSL](https://fr.wikipedia.org/wiki/Symmetric_Digital_Subscriber_Line) et faire mon auto-hébergement tranquillou ...