Title: Textsecure : les SMS et MMS chiffrés, c'est fini
Date: 2015-03-06
Category: Sécurité
Author: Matlink
Tags: textsecure, android, vie privée
Slug: textsecure-sms-mms-chiffres-finis
Image: 20150306/TextSecure_Blue_Icon.png

C'est une mauvaise nouvelle qui vient à nous ce soir concernant [TextSecure](https://whispersystems.org/#encrypted_texts), l'application Android permettant d'échanger des SMS et MMS de façon chiffrée. Il faut savoir que TextSecure permet trois choses : envoyer des SMS/MMS non chiffrés comme le ferait une autre application classique, envoyer des SMS/MMS chiffrés en passant par le réseau mobile et envoyer des messages chiffrés en passant par le réseau Internet. 

<center>
![text_secure]({filename}/images/20150306/TextSecure_conversation_list.png)
</center>

Aujourd'hui, les développeurs annoncent qu'ils arrêtent le support de la partie SMS/MMS chiffrés à partir de la prochaine version (2.7.0) .

Pourquoi ?
----------
Les [raisons évoquées](https://whispersystems.org/blog/goodbye-encrypted-sms/) sont les suivantes (traduction quasi-directe) : 

- l'envoi des SMS/MMS chiffrés ne peut se faire de façon transparente : les utilisateurs doivent manuellement créer un premier échange de clés. Le problème est que les gens ne savent pas tous ce que représente réellement "une clé", ce qui rend moins efficace ce genre de solution. 
- l'arrivée de la compatibilité iOS : avec Signal, iOS se voit disposer d'une solution compatible avec TextSecure. Cependant, iOS ne possède pas d'[API](https://fr.wikipedia.org/wiki/Interface_de_programmation) qui permet à Signal d'envoyer/recevoir des SMS programmés rendant impossible la lecture des SMS chiffrés. Cela peut donc perturber les utilisateurs.
- SMS et MMS sont un désastre concernant la sécurité : aucune métadonnée ne peut passer autrement qu'en clair sur le réseau mobile. Ainsi, tous les réseaux télécoms sont capables d'intercepter les SMS et d'en examiner les métadonnées, révélant beaucoup trop d'informations même si le contenu est indéchiffrable. Les développeurs ne veulent pas avoir mauvaise conscience en sachant que des gouvernements peuvent oppresser des dissidents qui utilisent ce genre de solution.
- paranoïa sécuritaire : en voulant se focaliser sur la sécurité des SMS et MMS, les développeurs n'ont plus de temps à accorder au développement de TextSecure afin de la rendre meilleure.

<span class="figure float-left">
[![Open WhisperSystems]({filename}/images/20150306/whisper.png)](https://whispersystems.org)
<span class="caption">Logo de <br/>[Open WhisperSystems](https://whispersystems.org/)</span>
</span>


C'est l'ensemble de ces su-citées raisons qui poussent [Open WhisperSystems](https://whispersystems.org) à abandonner le support des SMS/MMS chiffrés (via le réseau mobile). 
Il est vrai que la façon dont sont conçus les SMS/MMS ne permet pas de conserver un minimum de vie privée et de sécurité : les métadonnées des SMS/MMS peuvent très souvent suffire à en savoir beaucoup sur le contenu du message qui transite, ce qui reste gênant.

Du coup, que puis-je faire ? Je trouvais ça cool, TextSecure !
--------------------------------------------------------------
Oui, moi aussi. Mais il est vrai que vouloir sécuriser (et conserver sa vie privée avec) les SMS/MMS est peine perdue. 
Cependant, TextSecure permet l'envoi de messages via le transport TextSecure, qui lui protège les métadonnées. Bon, c'est pas aussi pratique que les SMS/MMS car il faut avoir une connexion internet active (Wifi ou bien Data), mais ce n'est pas ce qui manque de nos jours ([enfin dans certains pays c'est plus compliqué](https://twitter.com/TAbugharsa/status/573945270699950080)).

En espérant que TextSecure continuera de fournir les SMS/MMS chiffrés sans accorder de support, ou qu'un fork naisse. En tous cas, merci aux devs d'avoir donné de leur temps, en cette ère [post-Snowden](https://en.wikipedia.org/wiki/Edward_Snowden) !

[source](https://whispersystems.org/blog/goodbye-encrypted-sms/)