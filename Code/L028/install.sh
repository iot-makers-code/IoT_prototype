#!/bin/bash
sudo apt-get update
sudo apt-get -y install apache2
sudo sed -i \
     's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www/' \
      /etc/apache2/sites-enabled/000-default.conf
sudo usermod -a -G www-data pi
sudo usermod -a -G pi www-data
sudo apt-get -y install php libapache2-mod-php php-mcrypt
