Nous avions un accès SSH root à cette machine : 172.31.101.12
Malheureusement, l'administrateur système, avant de se faire renvoyer il y a quelques jours, a ajouté une couche de sécurité sur le port SSH, rendant l'accès impossible. 

Il semble qu'il ait mis en place un mécanisme de protection non documenté, que nous n'arrivons pas à contourner pour l'instant. 
Cependant, nous avons conservé les credentials d'accès d'un user.
Jo, un collègue a réussi à intercepter un extrait de trafic réseau provenant des dernières interactions de cet administrateur avec le serveur. 
Bein joué Jo

Peut-être que cela vous aidera à comprendre ce qu'il a mis en place.

Votre objectif : Accédez en SSH à la machine en utilisant les informations à votre disposition et récupérez un accès root.

User: jonathan
Password: P@ssw0rd_Jo




# Lancer le docker:

    docker build -t port-knocking-challenge .

    docker run -d --cap-add=NET_ADMIN -p 2222:22 --name ctf_knock port-knocking-challenge

# Rentrer dans le docker:

    docker exec -it ctf_knock /bin/bash

    # Afficher les logs:
        cat /var/log/knockd.log
    
    # Afficher les rules:
        iptables -L --line-numbers
    
    # Delete une rules:
        iptables -D INPUT 1

# Récupérer l'ip du docker:

    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ctf_knock


# Vérouiller le ssh:

    knock 172.17.0.2 9012:tcp 5678:tcp 1234:tcp


# Dévérouiller le ssh:

    knock 172.17.0.2 1234:tcp 5678:tcp 9012:tcp