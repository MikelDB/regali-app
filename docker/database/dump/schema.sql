CREATE DATABASE testDB;

use testDB;

CREATE TABLE IF NOT EXISTS `person` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `google_id` varchar(36) NOT NULL UNIQUE,
  `name` varchar(16) NOT NULL,
  `email` varchar(36) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `is_authenticated` tinyint(1) NOT NULL DEFAULT 1,
  `profile_pic` TEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `event` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(36) NOT NULL,
  `created_at` date NOT NULL,
  `person_id` int(10) unsigned NOT NULL,
  `reference` varchar(36) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

GRANT ALL PRIVILEGES ON testDB.* TO testuser;


