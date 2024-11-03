-- create user and give privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' INDENTIFIED BY 'user_0d_1_pwd';
-- grants privileges to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';