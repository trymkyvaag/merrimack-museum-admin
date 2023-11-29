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
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `move_request`
--

LOCK TABLES `move_request` WRITE;
/*!40000 ALTER TABLE `move_request` DISABLE KEYS */;
INSERT INTO `move_request` VALUES (34,5,'New home',0,0,'Give me pls',1,'2023-11-19 19:22:40'),(35,2,'New home',0,0,'Give me pls',1,'2023-11-19 19:22:47'),(36,1,'et',0,1,'test',1,'2023-11-19 23:32:48'),(37,205,'my office',0,1,'Give me pls',1,'2023-11-20 00:30:21'),(38,304,'here',0,0,'new',1,'2023-11-20 00:47:56'),(39,305,'Nashua',0,1,'Give my pretty pls',1,'2023-11-20 02:36:52'),(40,3,'home',0,1,'I like this a lot',1,'2023-11-20 05:27:07'),(41,1,'new home',0,0,'hi',1,'2023-11-20 05:37:36'),(42,1,'pagani',0,0,'test',1,'2023-11-20 19:38:40'),(43,44,'Home',0,0,'pls',1,'2023-11-20 19:48:33'),(44,1,'home',0,1,'t',1,'2023-11-20 19:58:19'),(45,47,'office 105',0,1,'I really like this, can I have it next week',1,'2023-11-20 21:17:26'),(46,1,'fes',0,0,'gedrg',1,'2023-11-20 21:19:50'),(47,1,'home',0,0,'hi',1,'2023-11-22 00:33:25'),(48,1,'home',0,1,'hi',1,'2023-11-22 21:49:08'),(49,308,'home',0,0,'gsrg',1,'2023-11-26 04:07:03'),(50,1,'tt',0,0,'pwease',1,'2023-11-27 02:13:29'),(51,310,'home',0,0,'hi',1,'2023-11-27 02:15:21'),(52,1,'home',0,0,'',1,'2023-11-27 02:19:14'),(53,311,'KASH',0,0,'Fly it to me',1,'2023-11-27 02:35:11'),(54,1,'home',0,0,'',1,'2023-11-27 02:40:20'),(55,1,'KASH',0,0,'I like this photo a lot!',1,'2023-11-27 03:39:55'),(57,1,'Nashua',0,0,'Please gimme!!!',60,'2023-11-29 01:09:25');
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

-- Dump completed on 2023-11-28 20:29:52
