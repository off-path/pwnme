# 1. Utiliser une base d'image légère comme Ubuntu
FROM ubuntu:20.04

# 2. Mettre à jour les paquets et installer les services nécessaires
RUN apt-get update && apt-get install -y \
    openssh-server \
    iptables \
    knockd \
    sudo \
    vim

# 3. Configuration SSH
RUN mkdir /var/run/sshd
RUN echo 'root:root_password' | chpasswd
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# 4. Configuration de l'utilisateur Jonathan
RUN useradd -m jonathan
RUN echo 'jonathan:P@ssw0rd_Jo' | chpasswd
RUN echo 'jonathan ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# 5. Configuration du port knocking
COPY knockd.conf /etc/knockd.conf
RUN echo 'START_KNOCKD=1' > /etc/default/knockd

# 6. Exposer le port SSH (il ne sera accessible qu'après le port knocking)
EXPOSE 22

# 7. Démarrer les services SSH et Knockd
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
