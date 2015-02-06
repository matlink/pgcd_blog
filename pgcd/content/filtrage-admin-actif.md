Title: Filtrage administratif actif, comment le contourner ?
Date: 2015-02-06
Category: Réseaux
Tags: filtrage, censure, thepiratebay, neutralité du net, tutoriel
Author: Matlink
Image: 543px-The_Pirate_Bay_logo.svg.png


Je vous disais il y a quelque temps que [The Pirate Bay avait fait l'oeuvre de censure administrative]({filename}/faites-serveur-proxy-the-pirate-bay.md).

Aujourd'hui, les [FAI](https://fr.wikipedia.org/wiki/Fournisseur_d'accès_à_internet) sont [passés à l'acte et appliquent la loi](http://www.numerama.com/magazine/32134-le-decret-sur-le-blocage-des-sites-sans-juge-est-publie.html). Les plus habitués d'entre vous auront constaté que [The Pirate Bay](https://thepiratebay.se) affiche une page blanche si vous tentez de vous y connecter (pas pour tout les FAI à priori). 

Comment ce filtrage fonctionne ?
--------------------------------
De façon étonnante et tout à fait utile, ce filtrage est un filtrage au niveau des [DNS](https://fr.wikipedia.org/wiki/Domain_Name_System). Lorsque vous demandez le nom de domaine thepiratebay.se, on vous retourne un truc bidon (du genre 127.0.0.1 qui en fait est une adresse IP qui désigne votre machine).

		$ dig @212.27.40.240 thepiratebay.se +short
		127.0.0.1

Ici, je demande via DIG l'adresse de la machine désignée par thepiratebay.se au DNS d'IP 212.27.40.240. Ce DNS est celui donné par ma freebox lorsque je lui demande un DNS. On constate que ce DNS ment, car 127.0.0.1 n'est pas l'adresse de thepirate.se (ou sinon je m'appelle The Pirate Bay).

Que se passe-t-il si je demande à quelqu'un d'autre ?
-----------------------------------------------------
Prenons au hasard, un DNS fournit par [FDN](http://blog.fdn.fr/?post/2014/12/07/Filtrer-The-Pirate-Bay-Ubu-roi-des-Internets) : 

		$ dig @80.67.169.12 thepiratebay.se +short
		104.28.4.42
		104.28.5.42

Ce DNS n'a pas l'air de me mentir. Pour vérifier il faudrait entrer l'une des IP manuellement dans le navigateur. Malheureusement, le protection DDoS de Cloudflare empêche la connexion directe via l'IP. 
Je vous invite à tester en changeant les DNS utilisés par votre système d'exploitation, il y a des tonnes de tutos là dessus sur le web.
Je vous donne quelques DNS qui pour l'instant ont l'air de tenir la route : 

		#######FDN nameservers###############
		nameserver 80.67.169.12
		nameserver 2001:910:800::12
		nameserver 80.67.169.40
		nameserver 2001:910:800::40
		#######LDN###########################
		nameserver 80.67.188.188
		nameserver 2001:913::8
		#######ARN###########################
		nameserver 89.234.141.66
		nameserver 2a00:5881:8100:1000::3

Je pense que ces DNS sont de confiance, car ils appartiennent à des associations qui défendent les libertés sur Internet (FDN entre autres) et n'ont pas de raison d'user de leurs pouvoirs. Malheureusement, tout fournisseur de DNS en France doit se soumettre à la loi Française, et peut-être que FDN devra filtrer ce qu'on lui demande.

Il est toujours aussi exaspérant de voir que les [mesures prises par le gouvernement ](https://www.laquadrature.net/fr/pjl-terrorisme) pour faire appliquer la loi sur l'Internet en France, ne sont ni adaptées ni efficaces, du moins contre les personnes un peu renseignées. 

En gros, seules les personnes qui n'utilisent pas The Pirate Bay, se verront privées de The Pirate Bay.