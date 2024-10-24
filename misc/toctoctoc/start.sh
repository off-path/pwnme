#!/bin/bash

# Variables
PCAP_FILE="/root/port_knocking_capture.pcap"
INTERFACE="eth0"  # Remplace par l'interface réseau appropriée, "eth0" dans Docker
DURATION=20  # Temps (en secondes) pour capturer le trafic réseau

# Démarrage des services SSH et Knockd
echo "[+] Démarrage du service SSH..."
service ssh start

echo "[+] Démarrage du service Knockd..."
service knockd start

# Configuration iptables pour bloquer le port SSH initialement
echo "[+] Configuration de iptables pour bloquer l'accès SSH au départ..."
iptables -A INPUT -p tcp --dport 22 -j DROP

# Démarrage de la capture réseau avec tcpdump en arrière-plan
echo "[+] Capture du trafic réseau avec tcpdump pendant $DURATION secondes..."
tcpdump -i "$INTERFACE" -w "$PCAP_FILE" &
TCPDUMP_PID=$!

# Attendre pendant la capture (durée configurable avec $DURATION)
sleep "$DURATION"

# Arrêter tcpdump après la durée spécifiée
echo "[+] Arrêt de la capture réseau..."
kill $TCPDUMP_PID
wait $TCPDUMP_PID 2>/dev/null

echo "[+] Capture terminée. Fichier PCAP généré : $PCAP_FILE"

# Garder le conteneur en fonctionnement avec une boucle infinie
echo "[+] Le conteneur reste actif. Utilisez Ctrl+C pour quitter."
while true; do
  sleep 1000
done