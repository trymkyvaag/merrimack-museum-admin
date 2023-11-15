-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dit1
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
-- Table structure for table `move_request`
--

DROP TABLE IF EXISTS `move_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `move_request` (
  `idmove_request` int NOT NULL AUTO_INCREMENT,
  `artwork_id` int DEFAULT NULL,
  `to_location` varchar(30) DEFAULT NULL,
  `is_pending` tinyint NOT NULL,
  `is_approved` tinyint NOT NULL,
  `comments` varchar(200) DEFAULT NULL,
  `user_id` int NOT NULL,
  `time_stamp` datetime NOT NULL,
  PRIMARY KEY (`idmove_request`),
  KEY `FK_MoveRequest_Artwork_idx` (`artwork_id`),
  KEY `FK_MoveRequest_User_idx` (`user_id`),
  CONSTRAINT `FK_MoveRequest_Artwork` FOREIGN KEY (`artwork_id`) REFERENCES `artwork` (`idArtwork`),
  CONSTRAINT `FK_MoveRequest_UserAddress` FOREIGN KEY (`user_id`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `move_request`
--

LOCK TABLES `move_request` WRITE;
/*!40000 ALTER TABLE `move_request` DISABLE KEYS */;
INSERT INTO `move_request` VALUES (1,1,'510 Turnpike',0,0,NULL,0,'2023-11-15 15:02:00'),(2,1,'my house',1,0,'I need this asap',1,'1999-10-01 12:07:45'),(3,15,'Palmisano',1,0,'Please give me this, pretty please',56,'2023-11-15 15:02:00'),(4,19,'home',1,0,'hi',1,'2023-11-15 15:02:00'),(5,19,'home',1,0,'hi',1,'0000-00-00 00:00:00'),(6,19,'home',1,0,'hi',1,'0000-00-00 00:00:00'),(7,19,'home',1,0,'hi',1,'0000-00-00 00:00:00'),(8,28,'home',1,0,'comment',1,'0000-00-00 00:00:00'),(9,1,'pagani',1,0,'se bUFbweaufbgvuyedarbvea',1,'0000-00-00 00:00:00'),(10,3,'home',1,0,'wassup',1,'0000-00-00 00:00:00'),(11,16,'home',1,0,'hello',1,'2023-11-15 09:44:00'),(12,1,'hu',0,1,'hu',1,'2002-12-22 16:11:00'),(13,1,'redlamp',1,0,'wassup bruh',1,'2023-11-15 20:40:59'),(14,1,'redlamp',1,0,'wassup bruh 2',1,'2023-11-15 20:41:20');
/*!40000 ALTER TABLE `move_request` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-15 15:52:30
