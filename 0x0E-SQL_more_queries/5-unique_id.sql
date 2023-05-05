-- 5-unique_id.sql
-- Creates a table with an ID field that always has 1 as it's default value.
-- and is always unique
CREATE TABLE IF NOT EXISTS unique_id(
id INT UNIQUE DEFAULT 1,
name VARCHAR(256)
);
