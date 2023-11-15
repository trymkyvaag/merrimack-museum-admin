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
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `idArtist` int NOT NULL AUTO_INCREMENT,
  `artist_name` varchar(40) NOT NULL,
  PRIMARY KEY (`idArtist`)
) ENGINE=InnoDB AUTO_INCREMENT=234 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES (1,'Kevin Salemme\r'),(2,'Kevin Salemme\r'),(3,'Kevin Salemme\r'),(4,'Kevin Salemme\r'),(5,'Kevin Salemme\r'),(6,'Kevin Salemme\r'),(7,'Kevin Salemme\r'),(8,'Kevin Salemme\r'),(9,'Kevin Salemme\r'),(10,'Kevin Salemme\r'),(11,'Kevin Salemme\r'),(12,'Kevin Salemme\r'),(13,'Kevin Salemme\r'),(14,'Kevin Salemme\r'),(15,'Kevin Salemme\r'),(16,'Kevin Salemme\r'),(17,'Kevin Salemme\r'),(18,'Kevin Salemme\r'),(19,'Kevin Salemme\r'),(20,'Kevin Salemme\r'),(21,'Kevin Salemme\r'),(22,'Kevin Salemme\r'),(23,'Kevin Salemme\r'),(24,'Kevin Salemme\r'),(25,'Kevin Salemme\r'),(26,'Kevin Salemme\r'),(27,'Kevin Salemme\r'),(28,'Kevin Salemme\r'),(29,'Kevin Salemme\r'),(30,'Kevin Salemme\r'),(31,'Kevin Salemme\r'),(32,'Kevin Salemme\r'),(33,'Kevin Salemme\r'),(34,'Ralph Claflin\r'),(35,'Ralph Claflin\r'),(36,'Ralph Claflin\r'),(37,'Ralph Claflin\r'),(38,'Ralph Claflin\r'),(39,'Ralph Claflin\r'),(40,'Ralph Claflin\r'),(41,'Ralph Claflin\r'),(42,'Ralph Claflin\r'),(43,'Ralph Claflin\r'),(44,'Ralph Claflin\r'),(45,'Ralph Claflin\r'),(46,'Ralph Claflin\r'),(47,'Ralph Claflin\r'),(48,'Ralph Claflin\r'),(49,'Ralph Claflin\r'),(50,'Ralph Claflin\r'),(51,'Ralph Claflin\r'),(52,'Ralph Claflin\r'),(53,'Ralph Claflin\r'),(54,'Ralph Claflin\r'),(55,'Ralph Claflin\r'),(56,'Ralph Claflin\r'),(57,'Ralph Claflin\r'),(58,'Ralph Claflin\r'),(59,'Ralph Claflin\r'),(60,'Ralph Claflin\r'),(61,'Ralph Claflin\r'),(62,'Ralph Claflin\r'),(63,'David Raymond\r'),(64,'David Raymond\r'),(65,'David Raymond\r'),(66,'D. Raymond\r'),(67,'D. Raymond\r'),(68,'Brigitte Keller\r'),(69,'Brigitte Keller\r'),(70,'Brigitte Keller\r'),(71,'D. Goldman\r'),(72,'D. Goldman\r'),(73,'Steve Gilden\r'),(74,'Steve Gilden\r'),(75,'James Fortune\r'),(76,'James Fortune\r'),(77,'Hari Kidd\r'),(78,'Hari Kidd\r'),(79,'Hari Kidd\r'),(80,'Hari Kidd\r'),(81,'Martha Groome\r'),(82,'Martha Groome\r'),(83,'Christian M. Alexander\r'),(84,'Christian M. Alexander\r'),(85,'Syrbick\r'),(86,'Syrbick\r'),(87,'Syrbick\r'),(88,'Syrbick\r'),(89,'N/A\r'),(90,'David Dias\r'),(91,'Curlee Raven Holten\r'),(92,'Jan Hodges Baer\r'),(93,'N/A\r'),(94,'John Latham Knapp\r'),(95,'Steven Careau\r'),(96,'Jo Sandman\r'),(97,'Jan Hodges Baer\r'),(98,'?\r'),(99,'Tom Nee\r'),(100,'N/A\r'),(101,'N/A\r'),(102,'Marlene-Luce Tremblay\r'),(103,'N/A\r'),(104,'N/A\r'),(105,'N/A\r'),(106,'Anne Minich\r'),(107,'N/A\r'),(108,'Neil Serven\r'),(109,'Tara Rachels\r'),(110,'Becky Berner\r'),(111,'N/A\r'),(112,'Emily P. Haley\r'),(113,'N/A\r'),(114,'N/A\r'),(115,'Tisha Tutoh Tuton\r'),(116,'Bonnie Alexander\r'),(117,'N/A\r'),(118,'Milligan Ilz\r'),(119,'Emma Leaden\r'),(120,'N/A\r'),(121,'N/A\r'),(122,'N/A\r'),(123,'Cliffton Peacock\r'),(124,'T. Wiley Carr\r'),(125,'L. Platian\r'),(126,'Katy Jomich\r'),(127,'Paul Shalyer\r'),(128,'Christine Deans; Heather S.\r'),(129,'Charlie Day\r'),(130,'Sara?\r'),(131,'N/A\r'),(132,'Andrew McIntyre\r'),(133,'Rich (Rick?) Bowlant?\r'),(134,'Sarah Hevey\r'),(135,'Gabor Peterdi\r'),(136,'Steve Gilden\r'),(137,'Lou Kohl Morgan\r'),(138,'Emily Wegener\r'),(139,'Bicas?\r'),(140,'?\r'),(141,'N/A\r'),(142,'Jay A. Leccese\r'),(143,'n/a\r'),(144,'?\r'),(145,'n/a\r'),(146,'Michael Silver\r'),(147,'Michael Silver\r'),(148,'Willy Meyer\r'),(149,'Martin Mugar\r'),(150,'Gustaf Miller\r'),(151,'Becky Berner\r'),(152,'Emily Corbato\r'),(153,'n/a\r'),(154,'Carey Wells-Jowers\r'),(155,'?\r'),(156,'?\r'),(157,'Ann McCrea\r'),(158,'Eimear\r'),(159,'n/a\r'),(160,'David Patterson\r'),(161,'n/a\r'),(162,'Dia Stolnitz\r'),(163,'Jaclyn Caruso\r'),(164,'?\r'),(165,'?\r'),(166,'?\r'),(167,'?\r'),(168,'Jaclyn Caruso\r'),(169,'Brooke E. Bolduc\r'),(170,'?\r'),(171,'n/a\r'),(172,'Roger Kenoulo/R.G. Commuli?\r'),(173,'Roger Kenoulo/R.G. Commuli?\r'),(174,'Roger Kenoulo/R.G. Commuli?\r'),(175,'Roger Kenoulo/R.G. Commuli?\r'),(176,'Roger Kenoulo/R.G. Commuli?\r'),(177,'Roger Kenoulo/R.G. Commuli?\r'),(178,'Roger Kenoulo/R.G. Commuli?\r'),(179,'Yacine Brahami\r'),(180,'Arthur DiMambro\r'),(181,'Name is illegible\r'),(182,'n/a\r'),(183,'n/a\r'),(184,'Doreen Raby\r'),(185,'J.A. Fraser\r'),(186,'Colleen Naughton Connaighton\r'),(187,'n/a\r'),(188,'n/a\r'),(189,'Bachrach?\r'),(190,'Cyril Satovsky\r'),(191,'Raymond Parker\r'),(192,'n/a\r'),(193,'n/a\r'),(194,'n/a\r'),(195,'Edy Legrand\r'),(196,'Victor Vasarely\r'),(197,'Lee Reynolds\r'),(198,'n/a\r'),(199,'Larry Slezak\r'),(200,'n/a\r'),(201,'n/a\r'),(202,'Maurice de Vlaminck\r'),(203,'n/a\r'),(204,'Alberto Giacometti\r'),(205,'n/a\r'),(206,'David Raymond');
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
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
