Title: Intégration de Piwik, un suivi des visites libre
Date: 2015-01-29
Category: Annonces
Tags: Piwik, suivi
Slug: integration-piwik-visites
Author: Matlink
Image: Piwik_2.0_logo.svg.png

Lorsque le blog [était encore sur Wordpress]({filename}refonte-pgcd.md), nous utilisions un plugin afin d'observer le nombre de visites que nous avions environs par jour et par semaine. Sachez que les adresses IP étaient masquées et que nous connaissions seulement le navigateur utilisé lors de la visite. 
Je viens donc d'ajouter à l'instant le suivi grâce à un petit script JavaScript du nom de [Piwik](http://piwik.org). C'est un bout de code intégré dans chaque page qui se connecte au blog lorsque vous le visitez. 

Et ma vie privée, t'y pense ?
-----------------------------
Évidement ! Il faut savoir qu'à l'installation, Piwik m'a demandé si je voulais respecter la vie privée des personnes visitant ce blog. Bon vous vous en doutez, j'ai dit oui. Comment ça marche ? Piwik prend en compte le paramètre "Indiquer aux sites web que je ne souhaite pas être pisté". Ainsi, si ce paramètre est actif, le script n'enverra aucune information vers le blog. Aussi, sachez que si cette option est désactivée dans votre navigateur, Piwik ne conserve pas les adresses IP entièrement, mais seulement le début (par exemple pour l'IP 137.137.1.1, il ne garde que 137.137). Plus respectueux de la vie privée en effet. 

Tu voulais rendre ceci public ...
-----------------------------------
Ouais, c'est vrai ! Si vous vous connectez sur [l'interface de façon anonyme ](https://fr.matlink.fr/piwik), vous aurez accès à la partie publique des statistiques. Beaucoup d'informations vous serons cachées, mais vous pourrez voir le principal : le nombre de visites :)

Après tout ce discours, si vous ne souhaitez pas que ce blog fasse des statistiques sur vos visites, c'est tout à votre honneur. Signalez le moi à l'adresse pgcd[at]matlink[point]fr ou bien commentez dans la section ci-dessous. Et puis vous savez, ce n'est pas comme si [y'avait un bouton "like"](https://www.abine.com/blog/2012/how-facebook-buttons-track-you/) sur la page :)