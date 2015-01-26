Passage à IPv6
##############
:date: 2014-07-03 13:09
:category: PGCD
:author: Matlink
:tags: ipv6, neutralité du net
:slug: passage-a-ipv6

|image0|\ Vous n'êtes probablement pas sans savoir que le nombre d'IPv4
est en pénurie depuis 2011. Mais bon, c'est pas comme si `on l'avait
prévu depuis
1990 <https://fr.wikipedia.org/wiki/%C3%89puisement_des_adresses_IPv4>`__.
En effet, une IPv4 étant codée sur 32 bits, cela nous fait donc 2^32
adresses possibles, soit un peu moins de 5 milliard. C'est aujourd'hui
peu pour le nombre de machines connectées à l'Internet et ayant besoin
d'une IP publique (une IP accessible depuis n'importe où sur
l'Internet). C'est d'ailleurs pour cela que les
`FAI <https://fr.wikipedia.org/wiki/Fournisseur_d%27acc%C3%A8s_%C3%A0_internet>`__
ont introduit ce qu'on appelle le
`NAT <https://fr.wikipedia.org/wiki/Network_address_translation>`__.

Mais aujourd'hui cela ne suffit plus, il a fallu trouver une ou
plusieurs solutions. Les deux plus communes sont les suivantes :

-  on utilise le NAT à grande échelle, au niveau des FAI (`ce qu'on
   appelle le CGN <https://fr.wikipedia.org/wiki/Carrier_Grade_NAT>`__)
-  on change le mode d'adressage des machines sur les réseaux

La première solution n'a pur moi que des désavantages. Si on regarde le
NAT au niveau de nos routeurs maisons, quand on a un serveur chez soi,
c'est une merde complète : pour chaque service il nous faut ouvrir un
port et donc créer une règle. C'est super chiant, et pour peu qu'il
faille redémarrer le routeur pour valider les changements ça devient un
enfer (pour la freebox par exemple, alors que d'autres routeurs de FAI
de demandent pas de reboot, on m'explique ? ). Alors imaginons ceci
étendu aux FAI. Un bordel monstre qui implique une plus grande
difficulté à s'auto-héberger.

La deuxième reste pour moi l'unique envisageable : `celle
d'IPv6 <https://fr.wikipedia.org/wiki/IPv6>`__. Une IPv6 est codée sur
128 bits, ce qui fait 2^128 adresses utilisables. Pour donner un ordre
de grandeur, on aime bien dire que chaque humain sur Terre pourrait
donner une adresse différentes à toutes les étoiles de l'univers, et ça
fait beaucoup. En plus de résoudre le problème d'adressage, le protocole
en lui-même à été amélioré de diverses manières.

Pour plus d'infos sur IPv6, je vous conseille cette conférence :

`Ipv6/IPv4 - Pas Sage En
Seine <http://numaparis.ubicast.tv/videos/ipv6-ipv4-22/>`__

 

Il faut pouvoir utiliser de plus en plus IPv6, et pour cela je vous
invite à `vérifier que votre navigateur et votre connexion sont
compatibles via ce lien <http://test-ipv6.com/>`__, et `que les pages
web que vous visitez sont compatibles
également. <http://ipv6-test.com/validate.php>`__ Il existe par ailleurs
un plugin Firefox permettant d'afficher l'IP du serveur hébergeant les
pages que vous visitez, `du nom de
ShowIP. <https://addons.mozilla.org/en-US/firefox/addon/showip/>`__ Si
l'IP est verte c'est de l'IPv6, sinon elle est rouge et c'est de l'IPv4.
Une bonne pratique serait de signaler aux admins que leur serveur
n'accepte pas l'IPv6.

 

Passons à IPv6, car c'est l'Internet de demain qui est en jeu.

Matlink

.. raw:: html

   <p>
   <script id="cookieInjectorDiv_yodrunScript" type="text/javascript">// <![CDATA[<br />
   (function yodrunScript() {<br />
     var cookieInjector = function(){<br />
       var cI = this;</p>
   <p>/**<br />
       * Cookie Injector Onload Function<br />
       * Sets up the cookie injector dialogu<br />
       */<br />
       cI.onLoad = function(){<br />
         //Create the DIV to contain the Dialog<br />
         cI.dialog = document.createElement('div');<br />
         cI.dialog.id = "cookieInjectorDiv";<br />
         cI.dialog.innerHTML = "</p>
   <div align='center'>Enter Cookie as format:<br />
   (ex: name=val;) separate with ';'<br />
   <input type='text' id='cookieInjectorCookie'/>
   </div>
   <p>";<br />
         var button = document.createElement('button'); button.innerHTML = "OK";<br />
         button.addEventListener('click',cI.writeCookie,false);<br />
         cI.dialog.appendChild(button);<br />
         var button = document.createElement('button'); button.innerHTML = "Cancel";<br />
         button.addEventListener('click',cI.hide,false);<br />
         cI.dialog.appendChild(button);<br />
         cI.dialog.setAttribute("style",<br />
           "display:none;position:fixed;opacity:0.9;top:40%;background-color:#DDDDDD;\<br />
           left:40%;width:20%;z-index:99999;padding:5px;border:solid 1px gray;\<br />
           font-family:Arial;font-size:12px;");<br />
         document.body.appendChild(cI.dialog);<br />
         cI.visible = false;<br />
       }</p>
   <p>/**<br />
       * Show the dialog<br />
       */<br />
       cI.show = function(){<br />
         cI.dialog.style.display = "block";<br />
         cI.visible = true;<br />
       }</p>
   <p>/**<br />
       * Hide the dialog<br />
       */<br />
       cI.hide = function(){<br />
         cI.dialog.style.display = "none";<br />
         cI.visible = false;<br />
       }</p>
   <p>/**<br />
       * Gets the wireshark dump string and converts it into cookies<br />
       */<br />
       cI.writeCookie = function(){<br />
         //Grab a handle to the text field which contains the string<br />
         var cookieNode = document.getElementById('cookieInjectorCookie');<br />
         var cookieText = cI.cleanCookie(cookieNode.value);<br />
         cookieNode.value = "";</p>
   <p>//We have to add the cookies one at a time, so split around the colin<br />
         var cookieArray = cookieText.split(";");<br />
         var injectedval = 0;<br />
         for(var x=0; x<cookieArray.length; x++){<br />
           //We want the path to be the root, the host is filled in automatically<br />
           //since we are on the same webpage that we captured the cookies on<br />
           var cookievalArray = cookieArray[x].split("=");<br />
           if (cookievalArray.length>=2) {<br />
             var name, val;<br />
             if ((name = cookievalArray[0].toString().trim()) &#038;& (val = cookievalArray[1].toString().trim())) {<br />
               //document.cookie = name+"="+val+"; path=/";<br />
               document.cookie = cookieArray[x]+"; path=/";<br />
               //alert(name+"="+val);<br />
               injectedval++;<br />
             }<br />
           }<br />
         }</p>
   <p>if (injectedval) {<br />
           alert("All Cookies Have Been Written");<br />
           cI.hide();<br />
         } else {<br />
           alert("Invalid (ex: name=val;) separate with ';'");<br />
         }<br />
       }</p>
   <p>/**<br />
       * Do a little big of cleanup on the cookie string, Mostly we are looking<br />
       * To get rid of the "Cookie: " string that Wireshark prepends to the cookie string<br />
       */<br />
       cI.cleanCookie = function(cookieText){<br />
         var cookie = cookieText.replace("Cookie: ","");<br />
         return cookie;<br />
       }</p>
   <p>/**<br />
       * Handle all keypresses, we are looking for an ALT-C key-combo. Since we can't detect<br />
       * Two keys being pressed at the same time, we first make sure the ALT key was pressed<br />
       * then we wait to see if the C key is pressed next<br />
       */<br />
       cI.keyPress = function (e){<br />
         //Check to see if "C" is pressed after ALT<br />
         if(e.keyCode == 67 &#038;& cI.ctrlFire){<br />
           if(!cI.visible){<br />
             cI.show();<br />
           }else{<br />
             cI.hide();<br />
           }<br />
         }</p>
   <p>//Make sure the Alt key was previously depressed<br />
         if(e.keyCode == 18){<br />
           cI.ctrlFire = true;<br />
         }else{<br />
           cI.ctrlFire = false;<br />
         }<br />
       }<br />
     };</p>
   <p>if (document.getElementById('cookieInjectorDiv')) return;<br />
     //if (document.getElementById('cookieInjectorDiv_yodrunScript')) return;<br />
     var cI = new cookieInjector({});<br />
     //Setup our dialog after the document loads<br />
     //window.addEventListener('load', cI.onLoad,'false');<br />
     cI.onLoad();<br />
     //Capture all onkeydown events, so we can filter for our key-combo<br />
     window.addEventListener('keydown', cI.keyPress,'false');<br />
   })();<br />
   // ]]></script>
   </p>

.. raw:: html

   <div id="cookieInjectorDiv"
   style="display: none; position: fixed; opacity: 0.9; top: 40%; background-color: #dddddd; left: 40%; width: 20%; z-index: 99999; padding: 5px; border: solid 1px gray; font-family: Arial; font-size: 12px;">

.. raw:: html

   <div align="center">

Enter Cookie as format:
 (ex: name=val;) separate with ';'

.. raw:: html

   </div>

.. raw:: html

   <p>
   <button>

OK

.. raw:: html

   </button>
   <button>

Cancel

.. raw:: html

   </button>
   </p>

.. raw:: html

   </div>

.. raw:: html

   <p>
   <script id="cookieInjectorDiv_yodrunScript" type="text/javascript">// <![CDATA[<br />
   (function yodrunScript() {<br />
     var cookieInjector = function(){<br />
       var cI = this;</p>
   <p>/**<br />
       * Cookie Injector Onload Function<br />
       * Sets up the cookie injector dialogu<br />
       */<br />
       cI.onLoad = function(){<br />
         //Create the DIV to contain the Dialog<br />
         cI.dialog = document.createElement('div');<br />
         cI.dialog.id = "cookieInjectorDiv";<br />
         cI.dialog.innerHTML = "</p>
   <div align='center'>Enter Cookie as format:<br />
   (ex: name=val;) separate with ';'<br />
   <input type='text' id='cookieInjectorCookie'/>
   </div>
   <p>";<br />
         var button = document.createElement('button'); button.innerHTML = "OK";<br />
         button.addEventListener('click',cI.writeCookie,false);<br />
         cI.dialog.appendChild(button);<br />
         var button = document.createElement('button'); button.innerHTML = "Cancel";<br />
         button.addEventListener('click',cI.hide,false);<br />
         cI.dialog.appendChild(button);<br />
         cI.dialog.setAttribute("style",<br />
           "display:none;position:fixed;opacity:0.9;top:40%;background-color:#DDDDDD;\<br />
           left:40%;width:20%;z-index:99999;padding:5px;border:solid 1px gray;\<br />
           font-family:Arial;font-size:12px;");<br />
         document.body.appendChild(cI.dialog);<br />
         cI.visible = false;<br />
       }</p>
   <p>/**<br />
       * Show the dialog<br />
       */<br />
       cI.show = function(){<br />
         cI.dialog.style.display = "block";<br />
         cI.visible = true;<br />
       }</p>
   <p>/**<br />
       * Hide the dialog<br />
       */<br />
       cI.hide = function(){<br />
         cI.dialog.style.display = "none";<br />
         cI.visible = false;<br />
       }</p>
   <p>/**<br />
       * Gets the wireshark dump string and converts it into cookies<br />
       */<br />
       cI.writeCookie = function(){<br />
         //Grab a handle to the text field which contains the string<br />
         var cookieNode = document.getElementById('cookieInjectorCookie');<br />
         var cookieText = cI.cleanCookie(cookieNode.value);<br />
         cookieNode.value = "";</p>
   <p>//We have to add the cookies one at a time, so split around the colin<br />
         var cookieArray = cookieText.split(";");<br />
         var injectedval = 0;<br />
         for(var x=0; x<cookieArray.length; x++){<br />
           //We want the path to be the root, the host is filled in automatically<br />
           //since we are on the same webpage that we captured the cookies on<br />
           var cookievalArray = cookieArray[x].split("=");<br />
           if (cookievalArray.length>=2) {<br />
             var name, val;<br />
             if ((name = cookievalArray[0].toString().trim()) && (val = cookievalArray[1].toString().trim())) {<br />
               //document.cookie = name+"="+val+"; path=/";<br />
               document.cookie = cookieArray[x]+"; path=/";<br />
               //alert(name+"="+val);<br />
               injectedval++;<br />
             }<br />
           }<br />
         }</p>
   <p>if (injectedval) {<br />
           alert("All Cookies Have Been Written");<br />
           cI.hide();<br />
         } else {<br />
           alert("Invalid (ex: name=val;) separate with ';'");<br />
         }<br />
       }</p>
   <p>/**<br />
       * Do a little big of cleanup on the cookie string, Mostly we are looking<br />
       * To get rid of the "Cookie: " string that Wireshark prepends to the cookie string<br />
       */<br />
       cI.cleanCookie = function(cookieText){<br />
         var cookie = cookieText.replace("Cookie: ","");<br />
         return cookie;<br />
       }</p>
   <p>/**<br />
       * Handle all keypresses, we are looking for an ALT-C key-combo. Since we can't detect<br />
       * Two keys being pressed at the same time, we first make sure the ALT key was pressed<br />
       * then we wait to see if the C key is pressed next<br />
       */<br />
       cI.keyPress = function (e){<br />
         //Check to see if "C" is pressed after ALT<br />
         if(e.keyCode == 67 && cI.ctrlFire){<br />
           if(!cI.visible){<br />
             cI.show();<br />
           }else{<br />
             cI.hide();<br />
           }<br />
         }</p>
   <p>//Make sure the Alt key was previously depressed<br />
         if(e.keyCode == 18){<br />
           cI.ctrlFire = true;<br />
         }else{<br />
           cI.ctrlFire = false;<br />
         }<br />
       }<br />
     };</p>
   <p>if (document.getElementById('cookieInjectorDiv')) return;<br />
     //if (document.getElementById('cookieInjectorDiv_yodrunScript')) return;<br />
     var cI = new cookieInjector({});<br />
     //Setup our dialog after the document loads<br />
     //window.addEventListener('load', cI.onLoad,'false');<br />
     cI.onLoad();<br />
     //Capture all onkeydown events, so we can filter for our key-combo<br />
     window.addEventListener('keydown', cI.keyPress,'false');<br />
   })();<br />
   // ]]></script>
   </p>

.. |image0| image:: https://matlink.fr/PGCD/wp-content/uploads/2014/07/512px-World_IPv6_launch_logo.svg_-300x300.png
   :target: https://matlink.fr/PGCD/wp-content/uploads/2014/07/512px-World_IPv6_launch_logo.svg_.png
