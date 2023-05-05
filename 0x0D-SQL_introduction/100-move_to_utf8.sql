-- 100-move_to_utf8.sql
-- Converts the database `hbtn_0c_0`, table `first_table` and column `name`
-- to use the UTF-8 character set
ALTER DATABASE 
	`hbtn_0c_0` 
	CHARACTER SET utf8mb4 
	COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0;

ALTER TABLE 
	`first_table` 
	CONVERT TO CHARACTER SET utf8mb4 
	COLLATE utf8mb4_unicode_ci;

ALTER TABLE 
	`first_table`
	CHANGE `name` `name`
	VARCHAR(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
