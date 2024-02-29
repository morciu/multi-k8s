CREATE DATABASE IF NOT EXISTS mysql_db;

CREATE USER 'mysql_user'@'%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON mysql_db TO 'mysql_user'@'%';
FLUSH PRIVILEGES;

USE mysql_db;