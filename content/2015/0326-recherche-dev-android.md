Title: Recherche développeur Androïd
Date: 2015-03-26
Category: Annonces
Author: Matlink
Tags: dev, android, java, protobuff
Slug: recherche-dev-android
Image: 20150326/Android_robot.png

J'ai découvert y'a un petit moment déjà une application en Python permettant de [télécharger des Apks sur le Play Store](https://codingteam.net/project/googleplaydownloader). C'est très pratique, et ça gère même les mises à jour. 

Le seul problème, c'est qu'on devient dépendant d'un ordinateur et que cela n'est pas si simple que l'application Play Store de Google. Les mises à jour qui ne requièrent pas d'autorisation supplémentaire ne sont pas faites automatiquement, on n'est pas notifié quand y'a des mises à jour, on doit copier chaque apk sur l'appareil pour faire l'installation à la main ... C'est terriblement chouette comme application, cependant j'aimerai l'avoir sur mon téléphone.

GooglePlayDownloader de [Tuxicoman](https://twitter.com/tuxicoman) utilise une API en Python permettant d’interagir avec le Play Store directement (il embarque un ID d'appareil Androïd, un compte google etc ...). Il existe une version [JAVA de cette API](https://github.com/Akdeniz/google-play-crawler), cependant elle n'est plus maintenue depuis plus d'un an, et utilise des librairies dépréciées. 

J'ai donc envie de reprendre cette API JAVA pour l'adapter à Androïd, seulement j'ai que très peu de connaissance en application pour mobile, et même en passant cette lacune, j'ai quelques problèmes à utiliser des librairies non dépréciées (car celles utilisées dans la version de Akdeniz ne sont plus dans les API Androïd 19+).

Si des personnes pensent être suffisamment renseignées sur la chose, et sont intéressées pour m'aider à développer cette application, qui je le rappelle, permet de télécharger des applications du Google Play Store sans devoir passer par l'application de Google elle-même, alors contactez moi (matlink[at]matlink[point]fr). Les avantages d'une telle application sont les suivants : 

- application libre, code source disponible et modifiable etc... permettant de savoir ce que fait l'application. Ce qui n'est pas le cas de Play Store de Google
- possibilité d'utiliser un compte Google totalement aléatoire, par exemple un compte n'étant relié à rien (de base sur Androïd on ne peut avoir qu'un seul compte Google), ou bien un compte servant à plusieurs personnes (afin de réduire la profilage des utilisateurs)
- d'autres que j'oublie sûrement

Et bien sûr cette application sera totalement libre, et disponible sur [F-Droid](https://f-droid.org/) si je trouve un moyen de la déposer (après avoir compris comment tout fonctionne sur [leur système de dépôt](https://f-droid.org/wiki/page/Inclusion_Policy) ).

Merci de votre lecture, et pensez à partager, à commenter, à faire tourner sans modération ! Je vous en remercie, et peut-être que cela vous profitera aussi un jour (quand vous aurez sûrement décidé de virer Google de vos téléphones !).