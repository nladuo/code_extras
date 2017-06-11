#!/bin/bash

yum update

#创建文件夹
mkdir /apps
mkdir /apps/mysql
mkdir /apps/nginx
mkdir /apps/php

# 安装nginx
yum -y install gcc gcc-c++ autoconf automake make git
yum -y install zlib zlib-devel openssl openssl--devel pcre pcre-devel
wget http://nginx.org/download/nginx-1.8.1.tar.gz
tar zvxf nginx-1.8.1.tar.gz
cd nginx-1.8.1
./configure --prefix=/apps/nginx
make && make install
cd ..
mkdir /var/www
mkdir /var/www/html
mv /apps/nginx/html/* /var/www/html/
wget https://raw.githubusercontent.com/nladuo/linux_scripts/master/php_env/centos/6.6/resource/nginx.conf
mv -f nginx.conf /apps/nginx/conf/
echo "export PATH=/apps/nginx/sbin:\$PATH" >> ~/.bashrc
source ~/.bashrc

# 安装mysql
/usr/sbin/groupadd mysql
/usr/sbin/useradd -g mysql mysql
yum -y install cmake bison ncurses-devel
wget http://dev.mysql.com/get/Downloads/MySQL-5.5/mysql-5.5.15.tar.gz
tar xvf mysql-5.5.15.tar.gz
cd mysql-5.5.15/

cmake -DCMAKE_INSTALL_PREFIX=/apps/mysql \
    -DMYSQL_UNIX_ADDR=/tmp/mysql.sock \
    -DDEFAULT_CHARSET=utf8 \
    -DDEFAULT_COLLATION=utf8_general_ci \
    -DWITH_EXTRA_CHARSETS=all \
    -DWITH_MYISAM_STORAGE_ENGINE=1 \
    -DWITH_INNOBASE_STORAGE_ENGINE=1 \
    -DWITH_MEMORY_STORAGE_ENGINE=1 \
    -DWITH_READLINE=1 \
    -DENABLED_LOCAL_INFILE=1 \
    -DMYSQL_DATADIR=/apps/mysql/data \
    -DMYSQL_USER=mysql

make && make install
cd ..
if [ $(getconf WORD_BIT) = '32' ] && [ $(getconf LONG_BIT) = '64' ] ; then
 ln -s /apps/mysql/lib/libmysqlclient.so.18 /usr/lib64/libmysqlclient.so.18
else
 ln -s /apps/mysql/lib/libmysqlclient.so.18 /usr/lib/libmysqlclient.so.18
fi

cp /apps/mysql/support-files/my-large.cnf /etc/my.cnf

/apps/mysql/scripts/mysql_install_db \
--defaults-file=/etc/my.cnf \
--basedir=/apps/mysql \
--datadir=/apps/mysql/data \
--user=mysql

cp /apps/mysql/support-files/mysql.server /etc/init.d/
service mysql.server start
echo "export PATH=/apps/mysql/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc

# 安装php
yum -y install libmcrypt-devel mhash-devel libxslt-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel libidn libidn-devel openssl openssl-devel
wget http://cn2.php.net/distributions/php-5.5.22.tar.gz
tar -zvxf php-5.5.22.tar.gz
cd php-5.5.22
./configure --prefix=/apps/php  --enable-fpm --with-mcrypt --enable-mbstring --enable-pdo --with-pdo-mysql=/apps/mysql --with-curl --disable-debug  --disable-rpath --enable-inline-optimization --with-bz2  --with-zlib --enable-sockets --enable-sysvsem --enable-sysvshm --enable-pcntl --enable-mbregex --with-mhash --enable-zip --with-pcre-regex --with-mysql --with-mysqli --with-gd --with-jpeg-dir --without-pear 
make && make install
cd ..
/usr/sbin/groupadd www-data
/usr/sbin/useradd -g www-data www-data
wget https://raw.githubusercontent.com/nladuo/linux_scripts/master/php_env/centos/6.6/resource/php-fpm.conf
mv php-fpm.conf /apps/php/etc/
cp php-5.5.22/sapi/fpm/init.d.php-fpm  /etc/init.d/php-fpm
chmod +x /etc/init.d/php-fpm
chkconfig --add php-fpm
service php-fpm start
echo "export PATH=/apps/php/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc

# 安装phpmyadmin
cd /var/www/html
wget https://files.phpmyadmin.net/phpMyAdmin/4.6.3/phpMyAdmin-4.6.3-english.tar.gz
tar -zvxf phpMyAdmin-4.6.3-english.tar.gz
mv phpMyAdmin-4.6.3-english mysqladmin
wget https://raw.githubusercontent.com/nladuo/linux_scripts/master/php_env/centos/6.6/resource/config.inc.php
mv config.inc.php mysqladmin/
