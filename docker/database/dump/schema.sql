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

CREATE TABLE IF NOT EXISTS `list` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `reference` varchar(64) NOT NULL UNIQUE,
  `user_id` int(10) unsigned NOT NULL,
  `name` varchar(36) NOT NULL,
  `public` tinyint(1) NOT NULL DEFAULT 1,
  `active` tinyint(1) NOT NULL DEFAULT 1,
  `updated_at` TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `created_at` TIMESTAMP DEFAULT current_timestamp,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `list_element` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `reference` varchar(64) NOT NULL UNIQUE,
  `list_id` int(10) unsigned NOT NULL,
  `name` varchar(36) NOT NULL,
  `url` Text NOT NULL,
  `updated_at` TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `created_at` TIMESTAMP DEFAULT current_timestamp,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

GRANT ALL PRIVILEGES ON testDB.* TO testuser;


