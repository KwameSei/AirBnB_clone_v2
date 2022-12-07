-- setting up MySQL enviroment
-- creating database name
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating new user named, hbnb_dev with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting the new user created all privileges
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting the select privilege to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
