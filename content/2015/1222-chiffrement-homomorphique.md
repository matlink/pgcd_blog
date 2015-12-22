Title: Le chiffrement homomorphique
Date: 2015-12-22 23:00
Category: Sécurité 
Author: Matlink
Tags: chiffrement, mode, recherche
Slug: chiffrement-homomorphique
Image: 20151222/chiffrement.jpg

Aussi appellé chiffrement homomorphe, le chiffrement homomorphique (ou Homomorphic Encryption, HE, en anglais) est un mode de chiffrement qui s'oppose au chiffrement dit "classique". Il propose des avantages, mais également des inconvénients face au modèles que nous connaissons depuis quasiment un centenaire.

La cryptographie "classique"
---------------------------
RSA, AES, DES, GOST, One-Time-Pad, ... La liste est longue. Ce sont des crypto-systèmes bien connus qui servent plusieurs buts (tous n'assouvissent pas tous les besoins) : confidentialité, intégrité, non-répudiation, authenticité, ... Il existe deux types de cryptographie : symétrique et asymétrique. Dans un premier temps, les deux parties se sont accordées sur un secret commun qui sert à chiffrer et déchiffrer les messages. Dans le deuxième temps, chaque entité possède une paire de clé Publique/Privée dont l'une sert pour chiffer (la clé publique) et l'autre pour déchiffrer (clé privée).

Dans ces crypto-systèmes dits "classiques", nous en connaissons des bons et des mauvais, mais tous possèdent une propriété : un message chiffré par l'un de ces systèmes doit être préalablement déchiffré pour y effectuer des opérations. Qui dit déchiffrement dit accès à la clé symétrique ou privée, et dans certains cas cela nous embête. Nous aimerons qu'une entité dans laquelle nous avons peu confiance, puisse effectuer des opérations sur les messages chiffrés sans connaître la clé privée/symétrique. C'est ce qu'on appelle le chiffrement homomorphique.

Quelques applications possibles
-------------------------------
Ce type de chiffrement est revenu à la mode après la [thèse](https://crypto.stanford.edu/craig/craig-thesis.pdf) de [Craig Gentry](https://en.wikipedia.org/wiki/Craig_Gentry_(computer_scientist)), qui d'ailleurs propose un crypto-système totalement homomorphe. Nous allons revenir sur ce que veut dire totalement ou partiellement homomorphe.

<center>
	<span class="figure">
		![craig_gentry]({filename}/images/20151222/gentry.jpg)
		<span class="caption">Craig Gentry - by Christopher Lane; John D. and Catherine T. MacArthur Foundation </span>
	</span>
</center>

Dans sa thèse, Gentry propose deux applications au chiffrement homomorphe : 

- au sein d'un moteur de recherche, l'utilisateur envoie une requête chiffrée à ce moteur de recherche, sans que ce dernier n'ai connaissance de la requête reçue. Il applique son opération classique de recherche de pages correspondantes et renvoie la réponse à l'utilisateur de façon chiffrée. Ainsi, le moteur de recherche a pu faire son travail sans jamais connaître la requête que nous lui avons passé.

- vous avez des fichiers chiffrés sur un serveur distant et vous souhaitez faire une recherche parmis ces fichiers : par exemple récupérer les fichiers qui contiennent le mot "PGCD". Vous envoyez votre recherche de façon chiffrée à votre serveur distant, il applique la recherche sans connaître ce qu'il cherche et vous retourne le résultat. Cela évite que le serveur distant ne connaisse la clé utilisée pour chiffrer les fichiers (en cas de compromission, c'est pratique) et cela vous évite aussi d'avoir à transférer les fichiers en local pour les déchiffrer et ainsi faire votre recherche.

J'ajoute à ça une troisième application, qui me vient de mon prof de cours de biométrie : vous avez une base d'empreintes digitales des personnes autorisées à entrer dans votre laboratoire de recherche, mais ces empreintes sont naturellement chiffrées (la CNIL l'oblige, car ce sont des données personnelles non révocables). Pour entrer dans votre laboratoire, les personnes scannent leurs empreintes digitales et ces empreintes sont comparées à celles dans la base de données. Il est clair que la vérification ne peut pas se faire tel un mot de passe : deux empreintes digitales d'une même personne prises à deux moments différents ne sont JAMAIS identiques (ce sont des données biométriques) donc par conséquent il n'est pas possible de faire une simple comparaison des empreintes chiffrées (deux chiffrés de deux empreintes différentes sont évidement différents). Grâce au chiffrement homomorphique, il serait possible de comparer les empreintes digitales chiffrées sans jamais les déchiffrer.

Le Chiffrement homomorphique
----------------------------
Nous allons pas ré-expliquer en entière la thèse de Gentry, car cela ne serai que répéter ce qui ne peut pas être mieux dit qu'il ne l'a fait. Mais juste un petit exemple simple. Je vous ai menti quand j'ai dis que la cryptographie classique ne permettant pas l'homomorphie : RSA est un contre exemple.

Lorsque l'on prend le chiffrement asymétrique RSA de façon brute, telle que définie au tout début (sans padding), nous obtenons un système de chiffrement partiellement homomorphe pour la loi multiplication. Un bref rappel de RSA pour se remettre dans le contexte (Wikipédia) : 

- on choisis deux nombres premiers `p` et `q` différents et très grands (de l'ordre de 2048 bits voire plus)
- on calcule `N=pq` le module et `φ(N)=(p-1)(q-1)` la fonction indicatrice d'Euler pour `N`
- on choisis `e` premier avec `φ(N)` et `d` l'inverse de `e` dans `ℤ/φ(N)ℤ`
- le couple `(N,e)` est la clé publique et `d` est la clé privée
- le chiffré `C` d'un message `M` est défini tel que `C=M`<sup>`e`</sup>`  modulo N`

Soit `M`<sub>1</sub> et `M`<sub>2</sub> deux messages et `C`<sub>1</sub> et `C`<sub>2</sub> leurs chiffrés respectifs. De façon évidente, nous avons (`M`<sub>1</sub>`M`<sub>2</sub>)<sup>e</sup>=`M`<sub>1</sub><sup>e</sup>`M`<sub>2</sub><sup>e</sup>=`C`<sub>1</sub>`C`<sub>2</sub>  `mod N`. Ce qui signifie que le chiffré du produit des messages est égal au produit des chiffrés des messages. On dit que RSA est homomorphique pour la loi multiplication.

Nous pouvons voir la propriété homomorphique comme bénéfique ou pas, selon le contexte. C'est une des raisons pour lesquelles RSA n'est pas utilisé tel quel, cela donne un avantage à un attaquant : connaissant deux couples chiffré/clair pour une paire de clés donnée, on peut en déduire de façon certaine un troisième couple chiffré/clair qui soit valide pour la paire de clés fixée.

L'outils mathématique utilisé par Gentry pour son crypto-système sont les réseaux euclidiens. Un réseau est généré par ce qu'on appelle des bases : certaines sont de "bonnes bases" et d'autres sont de "mauvaises bases", mais toutes peuvent représenter le même réseau (sous certaines conditions, non co-linéarité des vecteurs de la base). Ainsi, les "mauvaises" bases servent à effectuer des opérations sur les messages chiffrés, et les "bonnes" bases servent à déchiffrer les messages. Nous pouvons donc confier les "mauvaises" bases à notre serveur distant, à Google, en toute confiance (modulo le fait qu'ils puissent altérer les données à leur guise, mais ça c'est possible même s'ils n'ont rien du tout).

Partiel ou total
----------------
Un système de chiffrement homomorphe est dit partiel lorsqu'il permet d'effectuer des opérations sur les chiffrés pour une ou quelques opérations. Il est totallement homomorphe lorsqu'il permet de faire toutes les opérations possibles sur des messages clairs, sur les chiffrés. RSA est partiellement homomorphe pour la loi multiplication. Le crypto-système de Gentry est totallement homomorphe.

Inconvénients
-------------
Un des désavantages est que la taille des clés et le coût des opérations sont largement plus grands. À priori, l'ordre de grandeur serait de 1 pour 1000 comparé au chiffrement classique (sans confirmation).

Tout ce pan de la cryptographie est ouvert depuis un moment : juste après avoir inventé RSA, Rivest et Shamir en 1978 se sont demandés s'il ne pouvait pas exister de crypto-système totalement homomorphe. Gentry leur a répondu en 2009 : OUI.
