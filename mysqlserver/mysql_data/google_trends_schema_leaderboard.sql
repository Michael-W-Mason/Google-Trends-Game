-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: google_trends_schema
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `leaderboard`
--

DROP TABLE IF EXISTS `leaderboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leaderboard` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `score` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leaderboard`
--

LOCK TABLES `leaderboard` WRITE;
/*!40000 ALTER TABLE `leaderboard` DISABLE KEYS */;
INSERT INTO `leaderboard` VALUES (1,'Michael',5,'2022-04-27 12:52:07','2022-04-27 12:52:07'),(2,'Michael',0,'2022-04-27 14:53:24','2022-04-27 14:53:24'),(3,'Tom',0,'2022-04-27 14:53:42','2022-04-27 14:53:42'),(4,'Bill',0,'2022-04-27 15:19:34','2022-04-27 15:19:34'),(5,'Bill',0,'2022-04-27 15:23:46','2022-04-27 15:23:46'),(6,'Joe',0,'2022-04-27 15:27:08','2022-04-27 15:27:08'),(7,'John',0,'2022-04-27 15:31:08','2022-04-27 15:31:08'),(8,'Alex',4,'2022-04-27 15:37:43','2022-04-27 15:37:43'),(9,'Bill',0,'2022-04-27 15:37:52','2022-04-27 15:37:52'),(10,'Jonny',5,'2022-04-27 15:38:02','2022-04-27 15:38:02'),(11,'Ted',4,'2022-04-27 15:38:11','2022-04-27 15:38:11'),(12,'Jim',9,'2022-04-27 15:38:27','2022-04-27 15:38:27'),(13,'; 1=1;',7,'2022-04-27 15:51:32','2022-04-27 15:51:32'),(14,'; 1=1;',3,'2022-04-27 15:52:05','2022-04-27 15:52:05'),(15,'asdfasdf',0,'2022-04-27 15:57:22','2022-04-27 15:57:22'),(16,'Alex',0,'2022-04-27 16:05:56','2022-04-27 16:05:56'),(17,'Logan',2,'2022-04-27 16:13:43','2022-04-27 16:13:43'),(18,'testing',3,'2022-04-27 18:45:20','2022-04-27 18:45:20'),(19,'Random',10,'2022-04-27 18:57:07','2022-04-27 18:57:07'),(20,'Michael',3,'2022-04-27 19:52:58','2022-04-27 19:52:58'),(21,'askljdhfgopasuidygv',2,'2022-04-28 11:41:20','2022-04-28 11:41:20'),(22,'Jimmy John',6,'2022-04-28 14:47:12','2022-04-28 14:47:12'),(23,'Zoom',8,'2022-04-29 14:24:42','2022-04-29 14:24:42');
/*!40000 ALTER TABLE `leaderboard` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-02 10:03:39
