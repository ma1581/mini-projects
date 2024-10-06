-- Create the database
CREATE DATABASE IF NOT EXISTS pollapp;

-- Switch to the created database
USE pollapp;

-- Create the user 'ma1581' with the password '1581'
CREATE USER IF NOT EXISTS 'ma1581'@'%' IDENTIFIED BY '1581';

-- Grant all privileges to the user 'ma1581' on the 'pollapp' database
GRANT ALL PRIVILEGES ON pollapp.* TO 'ma1581'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
