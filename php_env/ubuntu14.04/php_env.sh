#! /bin/bash

apt-get update
apt-get upgrade
# 安装apache2
apt-get install apache2  apache2-doc
# 安装php5
apt-get install php5 libapache2-mod-php5 php5-curl
# 安装mysql
apt-get install mysql-server mysql-client
# 安装phpmyadmin
apt-get install phpmyadmin
ln -s /usr/share/phpmyadmin /var/www/html/mysqladmin
# 启用mcrypt
php5enmod mcrypt
service apache2 restart
