-- SQL script that creates an index
-- idx_name_first on the table names and the first letter of name
CREATE INDEX idx_name_first
ON names (SELECT LEFT(name, 1) AS `name` FROM `names`.`name`);
