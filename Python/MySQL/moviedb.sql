-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema moviesdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema moviesdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `moviesdb` DEFAULT CHARACTER SET utf8 ;
USE `moviesdb` ;

-- -----------------------------------------------------
-- Table `moviesdb`.`actors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `moviesdb`.`actors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `bio` LONGTEXT NULL,
  `imdb` VARCHAR(255) NULL,
  `birthdate` DATE NULL,
  `awards` VARCHAR(255) NULL,
  `movies` LONGTEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `moviesdb`.`movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `moviesdb`.`movies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(100) NULL,
  `release_year` DATE NULL,
  `genre` VARCHAR(45) NULL,
  `rating` VARCHAR(5) NULL,
  `actors` LONGTEXT NULL,
  `producers` LONGTEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
