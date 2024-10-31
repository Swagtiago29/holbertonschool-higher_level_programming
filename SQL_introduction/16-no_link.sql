-- list all records of the table second_table only if they have name
SELECT score, name FROM second_table WHERE name EXISTS ORDER BY score DESC