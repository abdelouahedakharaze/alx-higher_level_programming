-- Creates the user 'user_0d_1' with full privileges and sets a password.
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on all databases and tables to 'user_0d_1'.
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost'
   IDENTIFIED BY 'user_0d_1_pwd';

-- Refreshes the privilege tables to apply the changes.
FLUSH PRIVILEGES;
