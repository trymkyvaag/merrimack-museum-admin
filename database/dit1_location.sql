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
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `idLocation` int NOT NULL AUTO_INCREMENT,
  `Location` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idLocation`)
) ENGINE=InnoDB AUTO_INCREMENT=272 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Provost\'s Office'),(28,'Austin Hall closet\r'),(29,'Austin Hall closet\r'),(30,'Austin Hall closet\r'),(31,'Austin Hall closet\r'),(32,'Austin Hall closet\r'),(33,'Austin Hall closet\r'),(34,'Storage or McCoy\r'),(35,'Austin Hall 1st Floor\r'),(36,'Storage or McCoy\r'),(37,'Austin Hall 1st Floor\r'),(38,'Storage or McCoy\r'),(39,'Austin Hall 1st Floor\r'),(40,'Storage or McCoy\r'),(41,'Storage or McCoy\r'),(42,'Storage or McCoy\r'),(43,'Storage or McCoy\r'),(44,'Storage or McCoy\r'),(45,'Storage or McCoy\r'),(46,'Storage or McCoy\r'),(47,'Austin Hall 2nd Floor\r'),(48,'Austin Hall 1st Floor\r'),(49,'Storage or McCoy\r'),(50,'Storage or McCoy\r'),(51,'Storage or McCoy\r'),(52,'Storage or McCoy\r'),(53,'Storage or McCoy\r'),(54,'Storage or McCoy\r'),(55,'Storage or McCoy\r'),(56,'Storage or McCoy\r'),(57,'Storage or McCoy\r'),(58,'Storage or McCoy\r'),(59,'Austin Hall 1st Floor\r'),(60,'Austin Hall 1st Floor\r'),(61,'Austin Hall One Stop\r'),(62,'Austin Hall 2nd Floor\r'),(63,'Storage or McCoy\r'),(64,'Storage or McCoy\r'),(65,'McQuade basement\r'),(66,'Storage or McCoy\r'),(67,'Storage or McCoy\r'),(68,'Austin Hall 1st Floor\r'),(69,'Austin Hall 1st Floor\r'),(70,'Austin Hall 1st Floor\r'),(71,'Storage or McCoy\r'),(72,'Storage or McCoy\r'),(73,'Storage or McCoy\r'),(74,'Austin Hall closet\r'),(75,'Storage or McCoy\r'),(76,'Storage or McCoy\r'),(77,'Austin Hall 2nd Floor\r'),(78,'Austin Hall 2nd Floor\r'),(79,'Austin Hall 2nd Floor\r'),(80,'Austin Hall 2nd Floor\r'),(81,'Storage or McCoy\r'),(82,'Storage or McCoy\r'),(83,'Storage or McCoy\r'),(84,'Storage or McCoy\r'),(85,'Austin Hall One-Stop\r'),(86,'Austin Hall One-Stop\r'),(87,'Austin Hall One-Stop\r'),(88,'Austin Hall closet\r'),(89,'Storage or McCoy\r'),(90,'Storage or McCoy\r'),(91,'Storage or McCoy\r'),(92,'Storage or McCoy\r'),(93,'Storage or McCoy\r'),(94,'Storage or McCoy\r'),(95,'Austin Hall closet?\r'),(96,'Storage or McCoy\r'),(97,'Storage or McCoy\r'),(98,'N/A\r'),(99,'N/A\r'),(100,'Thrown out?\r'),(101,'N/A\r'),(102,'N/A\r'),(103,'N/A\r'),(104,'N/A\r'),(105,'N/A\r'),(106,'N/A\r'),(107,'N/A\r'),(108,'N/A\r'),(109,'N/A\r'),(110,'N/A\r'),(111,'N/A\r'),(112,'N/A\r'),(113,'N/A\r'),(114,'N/A\r'),(115,'N/A\r'),(116,'N/A\r'),(117,'N/A\r'),(118,'N/A\r'),(119,'N/A\r'),(120,'N/A\r'),(121,'N/A\r'),(122,'N/A\r'),(123,'N/A\r'),(124,'N/A\r'),(125,'N/A\r'),(126,'N/A\r'),(127,'N/A\r'),(128,'N/A\r'),(129,'N/A\r'),(130,'N/A\r'),(131,'N/A\r'),(132,'N/A\r'),(133,'N/A\r'),(134,'N/A\r'),(135,'N/A\r'),(136,'N/A\r'),(137,'N/A\r'),(138,'N/A\r'),(139,'N/A\r'),(140,'N/A\r'),(141,'N/A\r'),(142,'N/A\r'),(143,'N/A\r'),(144,'N/A\r'),(145,'N/A\r'),(146,'Storage or McCoy\r'),(147,'Storage or McCoy\r'),(148,'Austin Hall closet\r'),(149,'Storage or McCoy\r'),(150,'Storage or McCoy\r'),(151,'Storage or McCoy\r'),(152,'Storage or McCoy\r'),(153,'Storage or McCoy\r'),(154,'Storage or McCoy\r'),(155,'Storage or McCoy\r'),(156,'Storage or McCoy\r'),(157,'Storage or McCoy\r'),(158,'Storage or McCoy\r'),(159,'Storage or McCoy\r'),(160,'Storage or McCoy\r'),(161,'Storage or McCoy\r'),(162,'Storage or McCoy\r'),(163,'Storage or McCoy\r'),(164,'Storage or McCoy\r'),(165,'Storage or McCoy\r'),(166,'Storage or McCoy\r'),(167,'Storage or McCoy\r'),(168,'Storage or McCoy\r'),(169,'Storage or McCoy\r'),(170,'Storage or McCoy\r'),(171,'Lisa Jebali\'s Office\r'),(172,'Lisa Jebali\'s Office\r'),(173,'Lisa Jebali\'s Office\r'),(174,'Lisa Jebali\'s Office\r'),(175,'Lisa Jebali\'s Office\r'),(176,'Lisa Jebali\'s Office\r'),(177,'Lisa Jebali\'s Office\r'),(178,'Lisa Jebali\'s Office\r'),(179,'Austin Hall President\'s Hall\r'),(180,'Austin Hall President\'s Hall\r'),(181,'Austin Hall President\'s Hall\r'),(182,'Austin Hall 1st Floor\r'),(183,'McQuade Basement\r'),(184,'McQuade Basement\r'),(185,'McQuade Basement\r'),(186,'McQuade Basement\r'),(187,'McQuade Basement\r'),(188,'McQuade Basement\r'),(189,'McQuade Basement\r'),(190,'McQuade Basement\r'),(191,'McQuade Basement\r'),(192,'McQuade Basement\r'),(193,'McQuade Basement\r'),(194,'McQuade Basement\r'),(195,'McQuade Basement\r'),(196,'McQuade Basement\r'),(197,'McQuade Basement\r'),(198,'McQuade Basement\r'),(199,'McQuade Basement\r'),(200,'McQuade Basement\r'),(201,'McQuade Basement\r'),(202,'McQuade Basement\r'),(203,'McQuade Basement\r'),(204,'McQuade Basement\r'),(205,'McQuade Basement\r'),(206,'Outside by McQuade'),(232,'England'),(233,'Art Gallery'),(234,'test'),(235,'Storage or McCoy'),(236,'N/A'),(237,'Lisa Jebali\'s Office'),(238,'Austin Hall 1st Floor'),(239,'Austin Hall closet'),(240,'m'),(241,'Home'),(242,'new'),(243,'2'),(244,'Homeeeee'),(245,'here'),(246,'there'),(247,'yeet'),(248,'retest'),(249,'retest again'),(250,'retest a'),(251,'retest again 2'),(252,'retest again 3'),(253,'retest again 4'),(254,'Italia'),(255,'t'),(256,'England, U.K.'),(257,'KBED'),(258,'x'),(259,'e'),(260,'Berlin'),(261,''),(262,'sefesZFs'),(263,'h'),(264,'r'),(265,'y'),(266,'Austin Hall 2nd Floor'),(267,'Austin Hall One Stop'),(268,'McQuade basement'),(269,'Outside near McQuade'),(270,'Austin Hall One-Stop'),(271,'Austin Hall President\'s Hall');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-28 20:29:51
