from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app import DATABASE_SCHEMA
from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import model_seed

@app.route('/seed_db')
def seed_db():
    query = """
    CREATE DATABASE  IF NOT EXISTS `hfrvkh6wwv1igdt6` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hfrvkh6wwv1igdt6`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: hfrvkh6wwv1igdt6
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `albums`
--

DROP TABLE IF EXISTS `albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albums` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `name` varchar(45) DEFAULT NULL,
  `cover_image_url` text,
  PRIMARY KEY (`id`),
  KEY `fk_albums_users1_idx` (`user_id`),
  CONSTRAINT `fk_albums_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albums`
--

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;
INSERT INTO `albums` VALUES (2,2,'2022-06-09 21:33:18','2022-06-09 22:05:57','Equipment','https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/273034001_111311818127691_5009079324458558081_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=vuAqODfGwooAX_W_euE&_nc_ht=scontent-sea1-1.xx&oh=00_AT-qJ4nBsUkTSuBKqDyyOwxOhcc-nRH8OIyuWRx4uqLKfw&oe=62A86E60'),(3,2,'2022-06-09 22:08:04','2022-06-09 22:08:20','Trenching Jobs','https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/275154976_125306990061507_8597431314394412864_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=0debeb&_nc_ohc=Lnah7KnH1b0AX-YIWD-&tn=s_ruLKfnu2D1wMFH&_nc_ht=scontent-sea1-1.xx&oh=00_AT_2DPEzNw39r_Y_oqlmvQwiN-GQ8qBPEoK16vX-VyajRA&oe=62A80125');
/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albums_has_images`
--

DROP TABLE IF EXISTS `albums_has_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albums_has_images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `image_id` int NOT NULL,
  `album_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`image_id`,`album_id`),
  KEY `fk_images_has_albums_albums1_idx` (`album_id`),
  KEY `fk_images_has_albums_images1_idx` (`image_id`),
  CONSTRAINT `fk_images_has_albums_albums1` FOREIGN KEY (`album_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `fk_images_has_albums_images1` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albums_has_images`
--

LOCK TABLES `albums_has_images` WRITE;
/*!40000 ALTER TABLE `albums_has_images` DISABLE KEYS */;
INSERT INTO `albums_has_images` VALUES (3,1,2,'2022-06-09 22:04:46','2022-06-09 22:04:46'),(4,2,2,'2022-06-09 22:06:36','2022-06-09 22:06:36'),(5,3,2,'2022-06-09 22:07:03','2022-06-09 22:07:03'),(6,4,3,'2022-06-09 22:08:31','2022-06-09 22:08:31'),(7,5,3,'2022-06-09 22:08:40','2022-06-09 22:08:40'),(8,6,3,'2022-06-09 22:08:51','2022-06-09 22:08:51');
/*!40000 ALTER TABLE `albums_has_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `business_info`
--

DROP TABLE IF EXISTS `business_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `business_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `about_us` text,
  `about_us_img` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `company_logo` varchar(255) DEFAULT NULL,
  `front_page_img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_info`
--

LOCK TABLES `business_info` WRITE;
/*!40000 ALTER TABLE `business_info` DISABLE KEYS */;
INSERT INTO `business_info` VALUES (2,'6940 Mormon Creek Rd, Lolo, MT 59847','(406) 546-9948','brandon@lolocreekexcavating.com','2022-06-09 21:16:36','2022-06-09 21:19:55','<p style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 1em; font-family: Cinzel; font-size: medium;\">Lolo Creek Excavating, LLC was started by Brandon Williams in the small town of Lolo, Montana. Brandon has worked in the excavation industry for over 5 years and has experience in a wide variety of construction and excavation applications.</p><p style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 1em; font-family: Cinzel; font-size: medium;\">Always ready to take on a challenge, we are looking to target both the residential and commercial markets in the Missoula/Bitterroot Valleys and surrounding areas. We know there is a lack of available excavation companies to work on and complete even the smallest projects. That\'s why our goal at Lolo Creek Excavating is to alleviate those issues by providing prompt and excellent service to our local area home and business owners.</p><p style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 1em; font-family: Cinzel; font-size: medium;\">As a new company in the area, we are looking to show the industry that we can\'t be beat when it comes to customer service, willingness to go above and beyond, and dedication to making your current and future projects a success.</p><p style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; margin-bottom: 1em; font-family: Cinzel; font-size: medium;\">Give Brandon a call anytime to chat about your excavation or snow removal needs, and receive a free quote. (406) 546-9948</p>','http://res.cloudinary.com/lolocreekexcavating1/image/upload/v1654834823/business_info/about_us_img.png','Lolo Creek Excavating, LLC','http://res.cloudinary.com/lolocreekexcavating1/image/upload/v1654812501/business_info/company_logo.png','http://res.cloudinary.com/lolocreekexcavating1/image/upload/v1654812508/business_info/front_page_img.jpg');
/*!40000 ALTER TABLE `business_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bio` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_employees_users1_idx` (`user_id`),
  CONSTRAINT `fk_employees_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `url` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_images_users1_idx` (`user_id`),
  CONSTRAINT `fk_images_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/273034001_111311818127691_5009079324458558081_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=vuAqODfGwooAX_W_euE&_nc_ht=scontent-sea1-1.xx&oh=00_AT-qJ4nBsUkTSuBKqDyyOwxOhcc-nRH8OIyuWRx4uqLKfw&oe=62A86E60','2022-06-09 22:04:46','2022-06-09 22:04:46',2,'','dozer'),(2,'https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/273022630_111311854794354_8068786147503849611_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=ioGlfxnVPX8AX9lrHFy&_nc_ht=scontent-sea1-1.xx&oh=00_AT9zHlHePm0gRiNNjYt-8bDQ1LQigA-nMUGluh4ws1C7Bg&oe=62A749FC','2022-06-09 22:06:36','2022-06-09 22:06:36',2,'','skidster'),(3,'https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/274990469_125307490061457_8184601650044320453_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=qUQLJPljArAAX8H9pdV&_nc_ht=scontent-sea1-1.xx&oh=00_AT_dwozUF1lSqVRpiolfT9_d1tc5q5XYMr5brQpE-rUNtA&oe=62A8636A','2022-06-09 22:07:03','2022-06-09 22:07:03',2,'','Truck'),(4,'https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/275154976_125306990061507_8597431314394412864_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=0debeb&_nc_ohc=Lnah7KnH1b0AX-YIWD-&tn=s_ruLKfnu2D1wMFH&_nc_ht=scontent-sea1-1.xx&oh=00_AT_2DPEzNw39r_Y_oqlmvQwiN-GQ8qBPEoK16vX-VyajRA&oe=62A80125','2022-06-09 22:08:31','2022-06-09 22:08:31',2,'','Dig 1'),(5,'https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/275057396_125306983394841_5959909917603892701_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=0debeb&_nc_ohc=qu22drbl3rAAX9-Lqc8&_nc_ht=scontent-sea1-1.xx&oh=00_AT9Mp_a0-6FSWTQhNOP04BTK1QnTKrhib6yOmuNXuI-ovA&oe=62A84651','2022-06-09 22:08:40','2022-06-09 22:08:40',2,'','Dig 2'),(6,'https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/275210040_125306976728175_4030516457741705221_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=0debeb&_nc_ohc=K_6vQV28ib8AX_mYuxx&_nc_ht=scontent-sea1-1.xx&oh=00_AT9yuEqLjAdjLY0DHNfOVV11uwshKsP3OK_M2PcA7YW02g&oe=62A87364','2022-06-09 22:08:50','2022-06-09 22:08:50',2,'','Dig 3');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` text,
  `sender` varchar(255) DEFAULT NULL,
  `receiver` varchar(255) DEFAULT NULL,
  `ip` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `level` tinyint DEFAULT NULL,
  `is_completed` tinyint DEFAULT '0',
  `in_process` tinyint DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (10,'Site Work','<ul class=\"list-disc ml-3\" style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: medium;\"><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Grading</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Leveling</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Clearing land for development</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Roads – repair and/or maintenance</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Materials – delivery, placement, spreading, and/or haul-off</li></ul>','2022-06-09 21:20:32','2022-06-09 21:20:32'),(11,'Excavation','<ul class=\"list-disc ml-3\" style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: medium;\"><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Footings</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Septic tanks</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Drain/leach fields</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Ditches</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">French drains</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Backfilling</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Driveways – constructing and/or resurfacing</li><li style=\"border-image: initial; --tw-translate-x:0; --tw-translate-y:0; --tw-rotate:0; --tw-skew-x:0; --tw-skew-y:0; --tw-scale-x:1; --tw-scale-y:1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:proximity; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:0px; --tw-ring-offset-color:#fff; --tw-ring-color:rgb(59 130 246/0.5); --tw-ring-offset-shadow:0 0 #0000; --tw-ring-shadow:0 0 #0000; --tw-shadow:0 0 #0000; --tw-shadow-colored:0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ;\">Building sites – creating and/or leveling</li></ul>','2022-06-09 21:20:44','2022-06-09 21:20:44'),(12,'Snow Removal','<p><span style=\"font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: medium;\">We have equipment to plow and clear both large or small projects. With our rubber track skid steer, we can clear a lot, road or driveway with ease while being gentle on whatever the surface is. If you have large piles that need to be moved on site or hauled off, we got you.</span><br></p>','2022-06-09 21:20:55','2022-06-09 21:20:55'),(13,'Helical Pier Installation','<p>Helical Piers for new construction, sinking foundation mitigation, jacking up houses, post and pier...<br></p>','2022-06-09 21:28:03','2022-06-09 21:28:03'),(14,'Grading','<p>We are equipped to complete grading projects of all kinds: leveling, repairing of surfaces, (roads, driveways)<br></p>','2022-06-09 21:28:45','2022-06-09 21:28:45');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `level` tinyint DEFAULT '1',
  `pw` char(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Brandom','Williams','brandon@lolocreekexcavating.com','2022-06-09 21:17:37','2022-06-09 21:17:37',5,'$2b$12$qzInUYNg5xqZGxGcMLaTi.rA64JZm6zmYjdBN2pSFFm6hS88UzPcu'),(3,'Tyler','Thibault','tyler.thibault@protonmail.com','2022-06-09 23:15:09','2022-06-09 23:15:22',9,'$2b$12$eppCCP0CLIbm.om.oxaDx.cqDbpBO.EFP2XOM89MaxA9H0ET6dUty');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-10 14:11:40
    """
    connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
    return redirect('/')