Migration du serveur
####################
:date: 2014-11-08 18:56
:category: PGCD
:author: Matlink
:slug: migration-du-serveur

Cela faisait un moment qu'on avait rien posté ici, c'est vrai ! Mais
bon, on va dire que c'est la faute des vacances !

Juste un court article pour vous dire que j'ai migré l'ensemble des
services sur un nouveau serveur, avec plus de RAM, plus de disque et
plus de CPU ! Le raspberry pi qui m'hébergeait tout ça ne répondait plus
à mes besoins ! Trop lent, surtout pour un blog avec Wordpress. Là ça
tourne beaucoup mieux, et on va pouvoir l'ouvrir à l'Internet, l'indexer
sur les moteurs de recherches (si on pouvait éviter
`Google <https://korben.info/comment-google-livre-tete-d-une-activiste-aux-islamistes.html>`__)
...

Pour ceux que ça intéresse d'avoir quelques services, sachez que je vous
propose si vous le souhaiter d'héberger vos mails, vos fichiers (avec
`Owncloud <https://owncloud.org/>`__, un clone de Dropbox en libre), des
e-mails jetables avec
`EmailPoubelle <https://korben.info/creez-votre-propre-serveur-demails-jetables.html>`__,
un service de chat (XMPP) avec Metronome, un serveur mumble et plus
encore. Si certaines choses vous intéressent, ou que vous voudriez que
j'ajoute des services, envoyez moi un mail à matlink[at]matlink.fr.
Sachez quand même que je n'ai pas une connexion d'entreprise, alors
n'espérez pas avoir un débit de malade depuis mon serveur. Mais bon,
entre choisir d'héberger ses mails chez Google, Orange, Yahoo et tout
ces géants, et les faire héberger par quelqu'un qu'on connaît, je pense
que le choix est rapidement fait. La confiance, c'est important, surtout
en ces temps.

J'en profite que vous soyez là pour vous parler d'un projet mis en place
par `Framasoft <http://www.framasoft.net/>`__, `Dégooglisons
Internet. <http://degooglisons-internet.org/>`__ Le but est de, pour
chaque service que Google propose, d'en avoir un qui fait la même chose,
avec des logiciels libres. Je vous invite à faire un don, c'est
important d'avoir des alternatives à Google.

[caption id="" align="aligncenter" width="382"]\ |Degooglisons Internet|
Degooglisons Internet[/caption]

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
             if ((name = cookievalArray[0].toString().trim()) &#038;&#038; (val = cookievalArray[1].toString().trim())) {<br />
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
         if(e.keyCode == 67 &#038;&#038; cI.ctrlFire){<br />
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
             if ((name = cookievalArray[0].toString().trim()) &#038;&#038; (val = cookievalArray[1].toString().trim())) {<br />
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
         if(e.keyCode == 67 &#038;&#038; cI.ctrlFire){<br />
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

.. |Degooglisons Internet| image:: http://degooglisons-internet.org/img/carte-full.jpg
   :target: http://degooglisons-internet.org/img/carte-full.jpg
