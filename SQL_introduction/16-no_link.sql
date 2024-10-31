-- list all records of the table second_table only if they have name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;