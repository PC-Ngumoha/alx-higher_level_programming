-- 6-states.sql
-- Creates a DB 'hbtn_0d_usa' and TABLE 'states'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
id INT NOT NULL UNIQUE AUTO_INCREMENT,
name VARCHAR(256),
PRIMARY KEY (`id`)
);
