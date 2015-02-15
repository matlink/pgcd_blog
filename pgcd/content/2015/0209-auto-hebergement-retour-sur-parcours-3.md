Title: Auto-hébergement : le retour sur mon parcours (troisième partie)
Date: 2015-02-09
Category: Auto-hébergement
Author: Matlink
Tags: auto hébergement, expérience, yunohost
Slug: auto-hebergement-le-retour-sur-mon-parcours-3
Image: 2014/logo_ynh.png

Avant tout, voici [la première partie]({filename}/2014/1115-auto-hebergement-le-retour-sur-mon-parcours-1.md) ainsi que [la deuxième partie]({filename}/2014/1120-auto-hebergement-le-retour-sur-mon-parcours-2.md) pour ceux qui n'en auraient pas encore pris connaissance.

Je voudrais d'abord m'excuser auprès de ceux qui attendaient cette troisième partie que je vous avais promis dans la partie 2. Les choses ont faites qu'elle a due être retardée. 

Cela fait un an cette semaine que je m'auto-héberge (et que j'ai totalement quitté Windows par la même occasion, ainsi que Gmail). Au début ce n'était que partiellement, mais aujourd'hui cela a pris une grosse part dans mon utilisation d'Internet. J'ai beaucoup appris en m’intéressant aux sujets : configuration de [Postfix](https://en.wikipedia.org/wiki/Postfix_(software)), de [DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail), de [BIND](https://fr.wikipedia.org/wiki/BIND), de [Nginx](https://fr.wikipedia.org/wiki/Nginx) ... Nous ne pouvons apprendre ce genre de choses qu'en pratiquant. 

Il y a un an tout juste, j'achetais le nom de domaine matlink.fr, car je venais d'acquérir mon petit raspberry pi et j'avais envie d'y héberger un petit blog : le PGCD, né sur Facebook (que j'ai quitté il y a un an aussi) par une bande de potes partant d'un délire autour de centres d’intérêts : les sciences, la technologie, les "geekeries", les jeux vidéos, ... 

Je voulais vous présenter [Yunohost](https://yunohost.org) : un projet qui a pour but de rendre plus facile l'auto-hébergement pour des personnes initiées, qui n'ont pas de très grandes connaissances en la matière. Yunohost est basé sur Debian : ce n'est qu'une surcouche avant tout. Ce qui est pratique avec Yunohost, c'est que ça fonctionne sur le champ : on l'installe, on lance la procédure de post-installation et ça roule. Yunohost propose même de vous fournir un nom de domaine en .nohost.me ou en .noho.st. C'est pratique quand vous avez la flemme de créer un nom de domaine, ou quand vous voulez simplement tester la solution (cependant si vous souhaitez vous auto-héberger de façon plus importante il est fortement préférable d'acheter votre nom de domaine).
<table style="text-align:center;">
<tr>
	<td>![Jappix]({filename}/images/20150209/jappix.png)</td>
	<td>![Roundcube]({filename}/images/20150209/roundcube.png)</td>
	<td>![Transmission]({filename}/images/20150209/transmission.png)</td>
	<td>![TinyTinyRSS]({filename}/images/20150209/ttrss.png)</td>
</tr>
<tr>
	<td>Jappix</td>
	<td>Roundcube</td>
	<td>Transmission</td>
	<td>TinyTinyRSS</td>
</tr>
</table>
Par défaut, l'installation Yunohost dispose d'un serveur mail, d'un serveur web, et il est possible d'ajouter des applications facilement (les applications les plus utilisées en générale sont disponibles). Aussi, vous avez une jolie interface web faite en JavaScript qui permet d'éviter de passer par la ligne de commande pour faire des choses simples comme ajouter un utilisateur, ajouter une application, ajouter un nom de domaine, faire les mises à jour, ...

De plus, Yunohost est disponible pour raspberry pi et se trouve sous forme d'une [image raspbian](https://yunohost.org/#/install_on_raspberry_fr) à déployer sur la carte SD (comme une raspbian classique). 

Yunohost fonctionne ensuite avec ce qui appellent des "[applications packagées](https://yunohost.org/#/apps_en)" : c'est à dire que les applications sont empaquetées avec des scripts qui permettent d'automatiser l'installation, la mise à jour, la suppression et la sauvegarde de celles-ci. C'est très pratique lorsque l'on veut installer une application très rapidement, telle que OwnCloud. La communauté peut aussi créer ses propres packages et les ajouter à la liste de ceux disponibles, cependant ils devront être vérifiés par la "packaging team" avant d'être officiellement supportées.
Je vais pas en dire plus, la [documentation](https://yunohost.org/#/docs_fr) est relativement bien fournie (surtout celle en anglais). 

Il faut cependant bien garder à l'esprit qu'une fois que vous utilisez ce genre de solution certes très pratiques au début, vous en êtes dépendant. Si les mainteneurs des applications ne les mettent pas à jour, vous devez le faire vous même (comme si vous n'utilisiez pas Yunohost en fait). Yunohost peut vous restreindre sur certains points, lorsque vous avez une idée qui est incompatible avec la manière dont fonctionne Yunohost. Cela peut devenir frustrant, donc à long terme se séparer de Yunohost me paraît être une bonne idée. 

Il est clair que je ne me suis jamais autant épanoui dans le domaine de l'informatique que depuis que je m'auto-héberge et que j'utilise GNU/Linux tous les jours. C'est un pas à franchir pour s'affranchir. 