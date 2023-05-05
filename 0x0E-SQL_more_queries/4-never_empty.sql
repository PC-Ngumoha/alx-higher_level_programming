-- 4-never_empty.sql
-- Creates a table with an ID field that always has 1 as it's default value.
CREATE TABLE IF NOT EXISTS id_not_null(
id INT DEFAULT 1,
name VARCHAR(256)
);
