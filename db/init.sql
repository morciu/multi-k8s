CREATE DATABASE IF NOT EXISTS appdb;

USE appdb;

CREATE USER 'mysql_user'@'%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON appdb TO 'mysql_user'@'%';
FLUSH PRIVILEGES;

USE appdb;
