Title: Refonte du blog du PGCD avec Pelican
Date: 2015-01-27
Category: Annonces
Tags: annonces, auto-hébergement, CMS, pelican

<span class="float-left">
	![pelican_logo]({filename}/images/pelican_logo.png)
</span>

Si vous lisez cet article, vous avez probablement remarqué un gros changement au niveau du rendu du blog. En effet, je viens tout juste de terminer la migration du blog vers un nouveau [CMS](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_de_contenu) au joli nom de [Pelican](http://blog.getpelican.com).

Pourquoi quitter Wordpress ?
----------------------------
C'est une bonne question, et heureusement j'ai quelques réponses. 
Wordpress est un CMS développé en [PHP](https://en.wikipedia.org/wiki/PHP). Wordpress, c'est cool car ça fonctionne bien, c'est joli et y'a pas besoin de se casser la tête pour écrire des articles. Cependant, Wordpress est connu pour être un emmental avec plein de trous. [On en découvre souvent](https://wpvulndb.com/). À ça rajoutons les [plugins](https://wordpress.org/plugins/), développés par la communauté. Ces plugins rajoutent des failles de sécurité également, et ils sont parfois codés avec les pieds (et quand on a des pieds de Hobbits, ça fait mal ! ).

Aussi, le problème d'avoir du PHP pour son blog, c'est qu'à chaque visite, le serveur exécute le fichier demandé, et cela augmente forcément la charge du serveur et le temps de réponse également. Pour un petit blog comme le PGCD c'est évidement une "pain in the arse" (une douleur dans l'cul ahah) comme diraient les Anglais.
Et puis Wordpress est lourd (on a un facteur 75 environ) : 

	::bash

		$ du -h -d0 wordpress 
		158M	wordpress ### Dossier d'installation de Wordpress
		$ du -h -d0 pelican 
		2,2M	pelican ### Version statique du PGCD

Pourquoi utiliser Pelican ?
---------------------------
Tout d'abord je voulais quelque chose de static. Rien de plus sécurisé que du [HTML](https://en.wikipedia.org/wiki/HTML) complètement statique (sans JavaScript dans l'idéal). Et niveau temps de réponse, y'a pas photo ça fuse comme un suppo dans les fesses (le serveur n'a aucun traitement à faire : simplement récupérer le fichier et l'envoyer) ! 
Il n'y avait pas que Pelican qui se proposait à moi pour être utilisé, d'autres choses comme [Middleman](https://middlemanapp.com/), [Jekyll](http://jekyllrb.com/), ... Mais [Aeris](https://twitter.com/aeris22) utilise Pelican depuis un moment et cela à l'air de bien fonctionner. Donc dans le cas où j'aurai un problème Aeris sera là pour m'aider :)

Aussi, le fait de pouvoir écrire ses articles en local sans avoir à contacter le serveur ne fait qu'améliorer l'expérience utilisateur : pas besoin d'uploader les fichiers à chaque changement, visualisation rapide, ... De plus, Python est multi-plate-forme donc il est possible aussi de générer les articles depuis Windows (je n'ai pas essayé mais je ne vois rien qui ne puisse géner cela).

Comment ça fonctionne ?
-----------------------
Pelican est développé en [Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29). D'après la [documentation en ligne](http://docs.getpelican.com/en/3.5.0/) il supporte le langage [Markdown](https://en.wikipedia.org/wiki/Markdown), [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) et [AsciiDoc](http://www.methods.co.nz/asciidoc/). Il prend les fichiers dans un dossier prédéfini, il les interprète et les converti au format HTML. Il est donc possible de générer les fichiers HTML depuis une machine locale et ne déposer sur le serveur que ces fichiers. Le serveur n'a donc pas besoin d'avoir des processus supplémentaires à faire tourner (donc c'est l'idéal pour les machines à faibles ressources tel un Raspberry Pi). 

Markdown me semble le plus simple à apprivoiser, c'est donc avec ce langage que j'écris les articles. 

Mais est-ce aussi vraiment customisable ?
-----------------------------------------
Oui. Voire encore plus customisable que Wordpress. Il faut juste mettre les mains dans le code des [thèmes](http://docs.getpelican.com/en/3.5.0/themes.html) et donc d'avoir fait un peu de HTML/CSS (mais ceci est accessible à tout le monde :)). Beaucoup de thèmes sont [disponibles](https://github.com/getpelican/pelican-themes) pour ceux qui ne souhaitent pas mettre la main dans le cambouis. 

Où sont passés les commentaires ?
---------------------------------
Je suis encore en phase d'apprivoisement avec ce nouvel outil et j'ai encore pas mal de choses à améliorer. Maintenant que j'ai réécris tous les articles un-à-un, je vais pouvoir me consacrer disons aux méta-fonctions du blog : commentaires, statistiques (qu'il pourrait être intéressant de rendre publics), publication automatique sur Facebook/Twitter, ...


Si vous avez des remarques, des questions, ou si vous voulez plus de précisions concernant ce dont je viens de parler, ne postez pas un commentaire (car il ne sont pas encore disponibles), mais envoyez un mail à pgcd[at]matlink[point]fr .