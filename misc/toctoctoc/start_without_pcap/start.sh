#!/bin/bash

# Démarrage des services SSH et Knockd
echo "[+] Démarrage du service SSH..."
service ssh start

echo "[+] Démarrage du service Knockd..."
service knockd start

# Configuration iptables pour bloquer le port SSH initialement
echo "[+] Configuration de iptables pour bloquer l'accès SSH au départ..."
iptables -A INPUT -p tcp --dport 22 -j DROP

# Garder le conteneur en fonctionnement avec une boucle infinie
echo "[+] Le conteneur reste actif. Utilisez Ctrl+C pour quitter."
while true; do
  sleep 1000
done