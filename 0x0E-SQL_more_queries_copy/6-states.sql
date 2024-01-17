-- Creates the database 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Creates the table 'states' within the 'hbtn_0d_usa' database.
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);
