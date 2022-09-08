-- 2-create_read_user.sql
-- Creates user 'user_0d_2' and database 'hbtn_0d_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
