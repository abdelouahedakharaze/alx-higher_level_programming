-- Creates the table 'unique_id' with a default value for the 'id' column and sets it as unique.
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id`   INT          DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
