Title: La brique internet faite maison
Date: 2015-05-15 23:00
Category: Réseaux
Author: Matlink
Tags: vpn, tutoriel, pjlrenseignement, vie privée, libertés
Slug: brique-internet-faite-maison
Image: 20150515/wifi_router.jpg

En ces temps de surveillance de masse de plus en plus présente, il est d'or de commencer à s'inquiéter à propos de notre vie privée (même si pour certains c'est fait depuis longtemps). Comme bientôt nous n'allons plus pouvoir faire confiance à nos Fournisseurs d'Accès à l'Internet, il faut trouver une solution MAINTENANT pour se prémunir des [fameuses boîtes noires](https://twitter.com/LesBoitesNoires).

Les super copains de chez FFDN ont eu l'idée de génie ([une révolution diront certains](http://www.free.fr/adsl/freebox-revolution.html)) de fabriquer ce qu'ils appellent [la brique internet](https://labriqueinter.net/). Je vous conseille d'aller consulter la vidéo assez courte qui explique parfaitement comment cela fonctionne. De façon rapide, c'est un appareil que vous branchez derrière la box que vous a fournit votre FAI auquel vous connectez tous vos appareils. Ensuite, la brique internet se contente de se connecter à un VPN (qu'il faudra configurer) et fera passer tout le trafic à travers ce tunnel VPN. Ainsi, toutes les connections de tous les appareils branchés à la brique auront l'adresse IP publique du VPN. Cela permet de s'affranchir de la configuration VPN sur chacune des machines de votre maison, en créant un tunnel totalement transparent. 

Comme j'ai déjà deux Raspberry Pi qui traînent à la maison, je me suis dit qu'il fallait que je construise cette brique moi-même. C'est chose faite, je partage maintenant mon expérience en vous expliquant pas à pas comment j'ai fait. Ce tutoriel est bien sûr valable pour d'autres machines que le Raspberry Pi, à condition qu'elle soit allumée 24/24h car elle servira de passerelle pour toute vos machines. 

Prérequis 
---------

- une machine capable d'être allumée 24/24h
- ayant un système d'exploitation GNU/Linux, l'idéal étant Debian (Raspbian pour le RPi), mais cela fonctionnera évidement avec les dérivées de Debian. Pour les autres systèmes, je parie que vous êtes assez experts pour vous adapter :)
- une connexion wifi sur cette machine, dans le cas où vous souhaiteriez faire passer les connexions des appareils wifi également (smartphones, ordinateurs portables, ...)
- un câble Ethernet pour brancher votre brique à votre box
- une connexion SSH en root sur la machine si elle ne possède pas d'écran
- on suppose que votre réseau Ethernet a cette plage d'IP : 192.168.1.0/24, et qu'elle possède l'IP 192.168.1.113
- le réseau wifi de brique aura cette place d'IP : 192.168.2.0/24
- vous avez des accès à un VPN avec OpenVPN (il en existe des gratuits si vous voulez essayer, taper "free openvpn" sur votre moteur de recherche préféré)
______________

C'est parti
-----------
Tout d'abord le tutoriel se base [sur celui-ci, en anglais](http://blog.frd.mn/raspberry-pi-vpn-gateway/).

La partie réseau
----------------

Premièrement, on va mettre à jour le bouzin : 
	
	::bash
	sudo apt-get update && sudo apt-get upgrade -y

On s'assure que les interfaces réseau sont au point : 
	
	::bash
	# ifconfig
	eth0      Link encap:Ethernet  HWaddr b8:27:eb:df:af:23  
	          inet addr:192.168.1.113  Bcast:192.168.0.255  Mask:255.255.255.0 # eth0 a une IP sur le réseau de la box
	          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
	          RX packets:139615 errors:0 dropped:0 overruns:0 frame:0
	          TX packets:114337 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:98383968 (93.8 MiB)  TX bytes:67553219 (64.4 MiB)

	[... on ignore lo ...]

	wlan0     Link encap:Ethernet  HWaddr e8:94:f6:24:ef:25  # Si votre carte wifi s'appelle wlan1, adaptez vous par la suite
	          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1 #wlan0 n'a pas encore d'IP
	          RX packets:10127 errors:0 dropped:59 overruns:0 frame:0
	          TX packets:17222 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:759737 (741.9 KiB)  TX bytes:21601475 (20.6 MiB)

On installe `hostapd` pour créer un point d'accès WIFI : 

	::bash
	sudo apt-get install hostapd

On ajuste sa configuration ainsi, en remplaçant <NOM_DU_RESEAU\> et <MOT_DE_PASS_DU_RESEAU\> : 

	::bash
	sudo nano /etc/hostapd

	interface=wlan0  
	driver=nl80211 # A remplacer par le nom du driver de votre carte wifi, je vous laisse chercher  
	ssid=<NOM_DU_RESEAU> # Le nom que vous voulez donner à votre point d'accès WIFI 
	hw_mode=g  
	channel=6  
	macaddr_acl=0  
	auth_algs=1  
	ignore_broadcast_ssid=0  
	wpa=2  
	wpa_passphrase=<MOT_DE_PASS_DU_RESEAU>  
	wpa_key_mgmt=WPA-PSK  
	wpa_pairwise=TKIP  
	rsn_pairwise=CCMP  

Installons le serveur DHCP, `isc-dhcp-server` : 

	::bash
	sudo apt-get install isc-dhcp-server

Configurons-le :

	::bash
	sudo nano /etc/dhcp/dhcp.conf

Commentez les lignes :
	
	::bash
	#option domain-name "example.org";
	#option domain-name-servers ns1.example.org, ns2.example.org;

Décommentez :
	
	::bash
	authoritative;

Puis ajoutez à la fin : 

	::bash
	subnet 192.168.2.0 netmask 255.255.255.0 {  
	    range 192.168.2.10 192.168.2.254;
	    option broadcast-address 192.168.2.255;
	    option routers 192.168.2.1;
	    default-lease-time 600;
	    max-lease-time 7200;
	    option domain-name "vpn";
	    option domain-name-servers 192.168.2.1;
	} 

Aussi, indiquez le fichier de configuration DHCP : 

	::bash
	sudo nano /etc/default/isc-dhcp-server

	INTERFACES="wlan0" # à adapter si votre carte wifi s'appelle autrement

On va configurer la carte wifi maintenant. Dans le fichier `/etc/network/interfaces`, ajoutez : 

	::bash
	allow-hotplug wlan0  
	iface wlan0 inet static  
		address 192.168.2.1
		netmask 255.255.255.0

Et commentez les autres lignes concernant wlan0 : 

	::bash
	#iface wlan0 inet manual
	#wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	#iface default inet dhcp

On définit l'IP de wlan0 manuellement pour éviter de relancer le service :
	
	::bash
	sudo ifconfig wlan0 192.168.2.1

Configuration d'OpenVPN
-----------------------

On installe OpenVPN : 

	::bash
	sudo apt-get install openvpn unzip

On va créer un dossier spécifique pour accueillir la configuration du service VPN que l'on va utiliser, pour moi pour tester c'est Freevpn : 

	::bash
	sudo mkdir -p /etc/openvpn/freevpn
	cd /etc/openvpn/freevpn
	wget https://freevpn.me/OpenVPN-Certificate-Bundle-Server1.zip
	unzip OpenVPN-Certificate-Bundle-Server1.zip

On va renommer les fichiers `*.ovpn` en `.conf` :

	::bash
	sudo rename 's/ovpn/conf/' *.ovpn 
	sudo rename 's/ /_/g' *.conf

Ajoutons un fichier avec les identifiants dedans : 

	::bash
	sudo echo "<NOM_UTILISATEUR>" >> auth.txt # à remplacer par votre nom d'utilisateur, freevpnme pour freevpn.me
	sudo echo "<MOT_DE_PASSE>" >> auth.txt # le mot de passe, sg7JncTs pour freevpn.me

On indique le fichier `auth.txt` dans chacun des fichiers de conf : 

	::bash
	sed -i 's/auth-user-pass/auth-user-pass \/etc\/openvpn\/freevpn\/auth.txt/g' *.conf

Ensuite, dans le fichier `/etc/default/openvpn`, on va écrire : 

	::bash
	AUTOSTART="FreeVPN.me-TCP443"

Cela va utiliser le fichier de conf `FreeVPN.me-TCP443".conf` lors du démarrage du service d'OpenVPN.
On démarre OpenVPN : 

	::bash
	sudo service openvpn start

On regarde quel interface de tunneling a été créé : 

	::bash
	#ifconfig
	tun1      Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
          inet addr:10.13.0.114  P-t-P:10.13.0.113  Mask:255.255.255.255
          UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
          RX packets:5935 errors:0 dropped:0 overruns:0 frame:0
          TX packets:7085 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:100 
          RX bytes:2791801 (2.6 MiB)  TX bytes:844812 (825.0 KiB)

Chez moi c'est tun1, mais chez vous ça pourrait être tun0. Encore une fois, adaptez vous.

Le NAT pour rediriger tout dans le tunnel, et seulement ça
----------------------------------------------------------

On active l'IP forwarding : 

	::bash
	sudo echo 1 > /proc/sys/net/ipv4/ip_forward 

Ouvrez le fichier `/etc/sysctl.conf` et décommentez la ligne : 
	
	::bash
	net.ipv4.ip_forward = 1  

Ajoutez ensuite ces règles pour iptables : 

	::bash
	sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -m comment --comment "Use VPN IP for eth0"  
	sudo iptables -t nat -A POSTROUTING -o tun1 -j MASQUERADE -m comment --comment "Use VPN IP for tun1"  
	sudo iptables -A FORWARD -s 192.168.2.0/24 -i wlan0 -o eth0 -m conntrack --ctstate NEW -j REJECT -m comment --comment "Block traffic from clients to eth0"  
	sudo iptables -A FORWARD -s 192.168.2.0/24 -i wlan0 -o tun0 -m conntrack --ctstate NEW -j ACCEPT -m comment --comment "Allow only traffic from wlan0 clients to tun1" 
	sudo iptables -A FORWARD -s 192.168.1.0/24 -i eth0 -o tun0 -m conntrack --ctstate NEW -j ACCEPT -m comment --comment "Allow only traffic from eth0 clients to tun1"  

Sauvegardez les pour le prochain redémarrage : 

	::bash
	sudo iptables-save > /etc/iptables.ipv4.nat

Pour les charger à chaque reboot : 

	::bash
	sudo echo "up iptables-restore < /etc/iptables.ipv4.nat" >> /etc/network/interfaces


Tout est prêt
-------------

En toute logique, vous êtes capables de voir un nouveau réseau wi-fi portant le nom que vous avez donné dans la conf. En vous connectant dessus, vous devriez passer par le tunnel VPN. Pour en avoir le cœur net, il vous suffit de vous rendre sur des sites tels que [http://monip.org](http://monip.org) et de constater que votre IP à changé. 

Si vous êtes en filaire plutôt qu'en sans fil, il faut alors forcer le système à utiliser comme passerelle par défaut votre brique, en lui donnant son IP. Voici deux alias permettant d'activer/désactiver le routage par la brique : 

	::bash
	$ alias | grep vpn
	# Pour activer le passage par la brique
	alias vpne='sudo route del -n default gw 192.168.1.1; sudo route add -n default gw 192.168.1.113;'
	# Pour désactiver le passage par la brique
	alias vpnd='sudo route del -n default gw 192.168.1.113; sudo route add -n default gw 192.168.1.1;'

Pour Windows, il faut aller dans les paramètres de la carte réseau et changer la passerelle par défaut. Il doit y avoir des commandes pour le faire, mais je ne les connais pas.


Et surtout, pensez à vérifier régulièrement que le routage fonctionne toujours en consultant [http://monip.org](http://monip.org) pour vous assurer que votre IP n'est pas l'habituelle que votre FAI vous a donné.