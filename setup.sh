#!/bin/bash

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
rm get-docker.sh

# Install pigpio
apt install pigpio
pip3 install pigpio

# Automate running pigpio daemon
systemctl enable pigpiod.service
echo "Reboot after 30 seconds."
sleep 30
reboot

