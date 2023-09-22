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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `idCategory` int NOT NULL AUTO_INCREMENT,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idCategory`)
) ENGINE=InnoDB AUTO_INCREMENT=207 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Photography\r'),(2,'Photography\r'),(3,'Photography\r'),(4,'Photography\r'),(5,'Photography\r'),(6,'Photography\r'),(7,'Photography\r'),(8,'Photography\r'),(9,'Photography\r'),(10,'Photography\r'),(11,'Photography\r'),(12,'Photography\r'),(13,'Photography\r'),(14,'Photography\r'),(15,'Photography\r'),(16,'Photography\r'),(17,'Photography\r'),(18,'Photography\r'),(19,'Photography\r'),(20,'Photography\r'),(21,'Photography\r'),(22,'Photography\r'),(23,'Photography\r'),(24,'Photography\r'),(25,'Photography\r'),(26,'Photography\r'),(27,'Photography\r'),(28,'Photography\r'),(29,'Photography\r'),(30,'Photography\r'),(31,'Photography\r'),(32,'Photography\r'),(33,'Photography\r'),(34,'Painting\r'),(35,'Painting\r'),(36,'Painting\r'),(37,'Painting\r'),(38,'Painting\r'),(39,'Painting\r'),(40,'Painting\r'),(41,'Painting\r'),(42,'Painting\r'),(43,'Painting\r'),(44,'Painting\r'),(45,'Painting\r'),(46,'Oil on linen\r'),(47,'Painting\r'),(48,'Painting\r'),(49,'Oil on linen\r'),(50,'Painting\r'),(51,'Painting\r'),(52,'Painting\r'),(53,'Painting\r'),(54,'Painting\r'),(55,'Painting\r'),(56,'Painting\r'),(57,'Painting\r'),(58,'Painting\r'),(59,'Painting\r'),(60,'Oil and ink on linen\r'),(61,'Oil on linen\r'),(62,'Painting\r'),(63,'painting\r'),(64,'painting\r'),(65,'painting\r'),(66,'N/A\r'),(67,'N/A\r'),(68,'painting\r'),(69,'painting\r'),(70,'painting\r'),(71,'painting\r'),(72,'painting\r'),(73,'print\r'),(74,'painting\r'),(75,'Pencil on kraft paper\r'),(76,'Handcast Paper\r'),(77,'painting\r'),(78,'Watercolor painting\r'),(79,'Watercolor painting\r'),(80,'Oil on canvas\r'),(81,'Acrylic on canvas\r'),(82,'Acrylic on canvas\r'),(83,'Graphite on paper\r'),(84,'Graphite on paper\r'),(85,'N/A\r'),(86,'N/A\r'),(87,'N/A\r'),(88,'N/A\r'),(89,'Charcoal on paper\r'),(90,'Painting\r'),(91,'Etching\r'),(92,'Mixed Media on paper\r'),(93,'N/A\r'),(94,'Mixed Media on panel\r'),(95,'Ink lime on paper\r'),(96,'Tar on 100% rag paper\r'),(97,'Mixed Media on paper\r'),(98,'N/A\r'),(99,'N/A\r'),(100,'N/A\r'),(101,'N/A\r'),(102,'N/A\r'),(103,'N/A\r'),(104,'N/A\r'),(105,'N/A\r'),(106,'N/A\r'),(107,'N/A\r'),(108,'painting\r'),(109,'painting\r'),(110,'painting\r'),(111,'N/A\r'),(112,'painting\r'),(113,'painting\r'),(114,'painting\r'),(115,'N/A\r'),(116,'N/A\r'),(117,'N/A\r'),(118,'N/A\r'),(119,'N/A\r'),(120,'N/A\r'),(121,'N/A\r'),(122,'N/A\r'),(123,'painting\r'),(124,'Oil on canvas\r'),(125,'N/A\r'),(126,'N/A\r'),(127,'N/A\r'),(128,'N/A\r'),(129,'N/A\r'),(130,'N/A\r'),(131,'N/A\r'),(132,'N/A\r'),(133,'N/A\r'),(134,'Drawing\r'),(135,'Intaglio\r'),(136,'print\r'),(137,'N/A\r'),(138,'Ink on paper\r'),(139,'N/A\r'),(140,'N/A\r'),(141,'N/A\r'),(142,'painting\r'),(143,'print\r'),(144,'painting\r'),(145,'no info\r'),(146,'Platinum photograph on gampi paper\r'),(147,'Platinum photograph on gampi paper\r'),(148,'Linocut\r'),(149,'M/M on board\r'),(150,'Mixed Media collage construction\r'),(151,'N/A\r'),(152,'N/A\r'),(153,'N/A\r'),(154,'painting\r'),(155,'N/A\r'),(156,'N/A\r'),(157,'Bisqued raku\r'),(158,'Sculpture\r'),(159,'N/A\r'),(160,'N/A\r'),(161,'N/A\r'),(162,'Color photograph\r'),(163,'N/A\r'),(164,'N/A\r'),(165,'N/A\r'),(166,'N/A\r'),(167,'N/A\r'),(168,'N/A\r'),(169,'N/A\r'),(170,'N/A\r'),(171,'N/A\r'),(172,'N/A\r'),(173,'N/A\r'),(174,'N/A\r'),(175,'N/A\r'),(176,'N/A\r'),(177,'N/A\r'),(178,'N/A\r'),(179,'Acrylic on canvas\r'),(180,'Oil on panel\r'),(181,'Oil painting\r'),(182,'N/A\r'),(183,'N/A\r'),(184,'N/A\r'),(185,'N/A\r'),(186,'N/A\r'),(187,'N/A\r'),(188,'N/A\r'),(189,'N/A\r'),(190,'Etching\r'),(191,'Silk screen\r'),(192,'N/A\r'),(193,'N/A\r'),(194,'N/A\r'),(195,'Oil painting\r'),(196,'Silk screen\r'),(197,'N/A\r'),(198,'N/A\r'),(199,'Woodcut\r'),(200,'N/A\r'),(201,'N/A\r'),(202,'Color lithograph\r'),(203,'N/A\r'),(204,'Lithograph\r'),(205,'N/A\r'),(206,'Sculpture');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-21 21:12:30
