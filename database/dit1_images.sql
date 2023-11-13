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
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `idimages` int NOT NULL AUTO_INCREMENT,
  `image_path` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idimages`)
) ENGINE=InnoDB AUTO_INCREMENT=2267 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'images/a1/a1.png'),(2,'images/a2/a1.png'),(3,'images/a3/a1.png'),(4,'images/a4/a1.png'),(5,'images/a5/a1.png'),(6,'images/a6/a1.png'),(7,'images/a7/a1.png'),(8,'images/a8/a1.png'),(9,'images/a9/a1.png'),(10,'images/a10/a1.png'),(11,'images/a11/a1.png'),(12,'images/a12/a1.png'),(13,'images/a13/a1.png'),(14,'images/a14/a1.png'),(15,'images/a15/a1.png'),(16,'images/a16/a1.png'),(17,'images/a17/a1.png'),(18,'images/a18/a1.png'),(19,'images/a19/a1.png'),(20,'images/a20/a1.png'),(21,'images/a21/a1.png'),(22,'images/a22/a1.png'),(23,'images/a23/a1.png'),(24,'images/a24/a1.png'),(25,'images/a25/a1.png'),(26,'images/a26/a1.png'),(27,'images/a27/a1.png'),(28,'images/a28/a1.png'),(29,'images/a29/a1.png'),(30,'images/a30/a1.png'),(31,'images/a31/a1.png'),(32,'images/a32/a1.png'),(33,'images/a33/a1.png'),(34,'images/a34/a1.png'),(35,'images/a35/a1.png'),(36,'images/a36/a1.png'),(37,'images/a37/a1.png'),(38,'images/a38/a1.png'),(39,'images/a39/a1.png'),(40,'images/a40/a1.png'),(41,'images/a41/a1.png'),(42,'images/a42/a1.png'),(43,'images/a43/a1.png'),(44,'images/a44/a1.png'),(45,'images/a45/a1.png'),(46,'images/a46/a1.png'),(47,'images/a47/a1.png'),(48,'images/a48/a1.png'),(49,'images/a49/a1.png'),(50,'images/a50/a1.png'),(51,'images/a51/a1.png'),(52,'images/a52/a1.png'),(53,'images/a53/a1.png'),(54,'images/a54/a1.png'),(55,'images/a55/a1.png'),(56,'images/a56/a1.png'),(57,'images/a57/a1.png'),(58,'images/a58/a1.png'),(59,'images/a59/a1.png'),(60,'images/a60/a1.png'),(61,'images/a61/a1.png'),(62,'images/a62/a1.png'),(63,'images/a63/a1.png'),(64,'images/a64/a1.png'),(65,'images/a65/a1.png'),(66,'images/a66/a1.png'),(67,'images/a67/a1.png'),(68,'images/a68/a1.png'),(69,'images/a69/a1.png'),(70,'images/a70/a1.png'),(71,'images/a71/a1.png'),(72,'images/a72/a1.png'),(73,'images/a73/a1.png'),(74,'images/a74/a1.png'),(75,'images/a75/a1.png'),(76,'images/a76/a1.png'),(77,'images/a77/a1.png'),(78,'images/a78/a1.png'),(79,'images/a79/a1.png'),(80,'images/a80/a1.png'),(81,'images/a81/a1.png'),(82,'images/a82/a1.png'),(83,'images/a83/a1.png'),(84,'images/a84/a1.png'),(85,'images/a85/a1.png'),(86,'images/a86/a1.png'),(87,'images/a87/a1.png'),(88,'images/a88/a1.png'),(89,'images/a89/a1.png'),(90,'images/a90/a1.png'),(91,'images/a91/a1.png'),(92,'images/a92/a1.png'),(93,'images/a93/a1.png'),(94,'images/a94/a1.png'),(95,'images/a95/a1.png'),(96,'images/a96/a1.png'),(97,'images/a97/a1.png'),(98,'images/a98/a1.png'),(99,'images/a99/a1.png'),(100,'images/a100/a1.png'),(101,'images/a101/a1.png'),(102,'images/a102/a1.png'),(103,'images/a103/a1.png'),(104,'images/a104/a1.png'),(105,'images/a105/a1.png'),(106,'images/a106/a1.png'),(107,'images/a107/a1.png'),(108,'images/a108/a1.png'),(109,'images/a109/a1.png'),(110,'images/a110/a1.png'),(111,'images/a111/a1.png'),(112,'images/a112/a1.png'),(113,'images/a113/a1.png'),(114,'images/a114/a1.png'),(115,'images/a115/a1.png'),(116,'images/a116/a1.png'),(117,'images/a117/a1.png'),(118,'images/a118/a1.png'),(119,'images/a119/a1.png'),(120,'images/a120/a1.png'),(121,'images/a121/a1.png'),(122,'images/a122/a1.png'),(123,'images/a123/a1.png'),(124,'images/a124/a1.png'),(125,'images/a125/a1.png'),(126,'images/a126/a1.png'),(127,'images/a127/a1.png'),(128,'images/a128/a1.png'),(129,'images/a129/a1.png'),(130,'images/a130/a1.png'),(131,'images/a131/a1.png'),(132,'images/a132/a1.png'),(133,'images/a133/a1.png'),(134,'images/a134/a1.png'),(135,'images/a135/a1.png'),(136,'images/a136/a1.png'),(137,'images/a137/a1.png'),(138,'images/a138/a1.png'),(139,'images/a139/a1.png'),(140,'images/a140/a1.png'),(141,'images/a141/a1.png'),(142,'images/a142/a1.png'),(143,'images/a143/a1.png'),(144,'images/a144/a1.png'),(145,'images/a145/a1.png'),(146,'images/a146/a1.png'),(147,'images/a147/a1.png'),(148,'images/a148/a1.png'),(149,'images/a149/a1.png'),(150,'images/a150/a1.png'),(151,'images/a151/a1.png'),(152,'images/a152/a1.png'),(153,'images/a153/a1.png'),(154,'images/a154/a1.png'),(155,'images/a155/a1.png'),(156,'images/a156/a1.png'),(157,'images/a157/a1.png'),(158,'images/a158/a1.png'),(159,'images/a159/a1.png'),(160,'images/a160/a1.png'),(161,'images/a161/a1.png'),(162,'images/a162/a1.png'),(163,'images/a163/a1.png'),(164,'images/a164/a1.png'),(165,'images/a165/a1.png'),(166,'images/a166/a1.png'),(167,'images/a167/a1.png'),(168,'images/a168/a1.png'),(169,'images/a169/a1.png'),(170,'images/a170/a1.png'),(171,'images/a171/a1.png'),(172,'images/a172/a1.png'),(173,'images/a173/a1.png'),(174,'images/a174/a1.png'),(175,'images/a175/a1.png'),(176,'images/a176/a1.png'),(177,'images/a177/a1.png'),(178,'images/a178/a1.png'),(179,'images/a179/a1.png'),(180,'images/a180/a1.png'),(181,'images/a181/a1.png'),(182,'images/a182/a1.png'),(183,'images/a183/a1.png'),(184,'images/a184/a1.png'),(185,'images/a185/a1.png'),(186,'images/a186/a1.png'),(187,'images/a187/a1.png'),(188,'images/a188/a1.png'),(189,'images/a189/a1.png'),(190,'images/a190/a1.png'),(191,'images/a191/a1.png'),(192,'images/a192/a1.png'),(193,'images/a193/a1.png'),(194,'images/a194/a1.png'),(195,'images/a195/a1.png'),(196,'images/a196/a1.png'),(197,'images/a197/a1.png'),(198,'images/a198/a1.png'),(199,'images/a199/a1.png'),(200,'images/a200/a1.png'),(201,'images/a201/a1.png'),(202,'images/a202/a1.png'),(203,'images/a203/a1.png'),(204,'images/a204/a1.png'),(205,'images/a205/a1.png'),(206,'images/a206/a1.png');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-13 18:48:02
