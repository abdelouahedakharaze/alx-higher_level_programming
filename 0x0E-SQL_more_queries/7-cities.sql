-- Creates the database 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Creates the table 'cities' within the 'hbtn_0d_usa' database.
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    PRIMARY KEY(`id`),
    `id`       INT          NOT NULL AUTO_INCREMENT,
    `state_id` INT          NOT NULL,
    `name`     VARCHAR(256) NOT NULL,
    FOREIGN KEY(`state_id`)
    REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
