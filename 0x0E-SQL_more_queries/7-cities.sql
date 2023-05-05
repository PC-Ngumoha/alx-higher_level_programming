-- 7-cities.sql
-- Creates a DB 'hbtn_0d_usa' and TABLE 'cities'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
id INT NOT NULL UNIQUE AUTO_INCREMENT,
name VARCHAR(256),
state_id INT NOT NULL,
PRIMARY KEY (`id`),
FOREIGN KEY (`state_id`) REFERENCES states(`id`)
);
