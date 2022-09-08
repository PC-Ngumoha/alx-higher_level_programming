-- 1-create_user.sql
-- Creates a user if it doesn't already exist and grants it all privileges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
