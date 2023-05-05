-- 3-force_name.sql
-- Creates a table with a field that cannot be NULL
CREATE TABLE IF NOT EXISTS force_name(
id INT,
name VARCHAR(256) NOT NULL
);
