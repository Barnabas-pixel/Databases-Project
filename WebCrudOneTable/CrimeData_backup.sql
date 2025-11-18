-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: CrimeData
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CaseFile`
--

DROP TABLE IF EXISTS `CaseFile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CaseFile` (
  `caseNumber` bigint NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  `officerFirstName` varchar(20) NOT NULL,
  `officerLastName` varchar(20) NOT NULL,
  PRIMARY KEY (`caseNumber`),
  KEY `CaseFile_fk_officer` (`officerFirstName`,`officerLastName`),
  CONSTRAINT `CaseFile_fk_officer` FOREIGN KEY (`officerFirstName`, `officerLastName`) REFERENCES `PrimaryOfficer` (`firstName`, `lastName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CaseFile`
--

LOCK TABLES `CaseFile` WRITE;
/*!40000 ALTER TABLE `CaseFile` DISABLE KEYS */;
INSERT INTO `CaseFile` VALUES (25681550541255,'Closed','Alex','Johnson'),(75652255265242,'Under-Investigation','Paige','Williams');
/*!40000 ALTER TABLE `CaseFile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CaseSuspect`
--

DROP TABLE IF EXISTS `CaseSuspect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CaseSuspect` (
  `caseNumber` bigint NOT NULL,
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  PRIMARY KEY (`caseNumber`,`firstName`,`lastName`),
  KEY `CaseSuspect_suspect_fk` (`firstName`,`lastName`),
  CONSTRAINT `CaseSuspect_case_fk` FOREIGN KEY (`caseNumber`) REFERENCES `CaseFile` (`caseNumber`),
  CONSTRAINT `CaseSuspect_suspect_fk` FOREIGN KEY (`firstName`, `lastName`) REFERENCES `Suspect` (`firstName`, `lastName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CaseSuspect`
--

LOCK TABLES `CaseSuspect` WRITE;
/*!40000 ALTER TABLE `CaseSuspect` DISABLE KEYS */;
INSERT INTO `CaseSuspect` VALUES (75652255265242,'Isabella','Smith'),(25681550541255,'John','Roger');
/*!40000 ALTER TABLE `CaseSuspect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CrimeIncident`
--

DROP TABLE IF EXISTS `CrimeIncident`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CrimeIncident` (
  `incidentID` bigint NOT NULL AUTO_INCREMENT,
  `incidentDate` date NOT NULL,
  `location` varchar(100) NOT NULL,
  `typeOfCrime` varchar(50) NOT NULL,
  `caseNumber` bigint NOT NULL,
  PRIMARY KEY (`incidentID`),
  KEY `CrimeIncident_fk_case` (`caseNumber`),
  CONSTRAINT `CrimeIncident_fk_case` FOREIGN KEY (`caseNumber`) REFERENCES `CaseFile` (`caseNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CrimeIncident`
--

LOCK TABLES `CrimeIncident` WRITE;
/*!40000 ALTER TABLE `CrimeIncident` DISABLE KEYS */;
INSERT INTO `CrimeIncident` VALUES (1,'2024-03-27','1229 Reserve Avenue, Silver City, 25050','Homicide',25681550541255),(2,'2024-11-05','Citizen Park, Silver City, 25050','Assault',75652255265242);
/*!40000 ALTER TABLE `CrimeIncident` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Person`
--

DROP TABLE IF EXISTS `Person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Person` (
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  PRIMARY KEY (`firstName`,`lastName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Person`
--

LOCK TABLES `Person` WRITE;
/*!40000 ALTER TABLE `Person` DISABLE KEYS */;
INSERT INTO `Person` VALUES ('Alex','Johnson'),('Isabella','Smith'),('John','Roger'),('Paige','Williams');
/*!40000 ALTER TABLE `Person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PrimaryOfficer`
--

DROP TABLE IF EXISTS `PrimaryOfficer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PrimaryOfficer` (
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `badgeNumber` varchar(10) NOT NULL,
  `officerRank` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`firstName`,`lastName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PrimaryOfficer`
--

LOCK TABLES `PrimaryOfficer` WRITE;
/*!40000 ALTER TABLE `PrimaryOfficer` DISABLE KEYS */;
INSERT INTO `PrimaryOfficer` VALUES ('Alex','Johnson','CF-021','Detective'),('Paige','Williams','CF-035','Sergeant');
/*!40000 ALTER TABLE `PrimaryOfficer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Suspect`
--

DROP TABLE IF EXISTS `Suspect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Suspect` (
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`firstName`,`lastName`),
  CONSTRAINT `Suspect_firstName_lastName_fk` FOREIGN KEY (`firstName`, `lastName`) REFERENCES `Person` (`firstName`, `lastName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Suspect`
--

LOCK TABLES `Suspect` WRITE;
/*!40000 ALTER TABLE `Suspect` DISABLE KEYS */;
INSERT INTO `Suspect` VALUES ('Isabella','Smith',29),('John','Roger',41);
/*!40000 ALTER TABLE `Suspect` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-18  0:42:17
