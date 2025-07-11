CREATE DATABASE  IF NOT EXISTS `psbb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `psbb`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: psbb
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `anecdote`
--

DROP TABLE IF EXISTS `anecdote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anecdote` (
  `idanecdote` int NOT NULL AUTO_INCREMENT,
  `idstudclass` int DEFAULT NULL,
  `anecdate` date DEFAULT NULL,
  `idteacher` int DEFAULT NULL,
  `anectype` varchar(10) DEFAULT NULL,
  `anecdesc` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`idanecdote`),
  KEY `idstudclass` (`idstudclass`),
  CONSTRAINT `anecdote_ibfk_1` FOREIGN KEY (`idstudclass`) REFERENCES `studentclass` (`idstudclass`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anecdote`
--

LOCK TABLES `anecdote` WRITE;
/*!40000 ALTER TABLE `anecdote` DISABLE KEYS */;
INSERT INTO `anecdote` VALUES (14,1,'2022-11-23',1,'Positive','Bakthaswaraa Bhajan competition - won first price\n');
/*!40000 ALTER TABLE `anecdote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `idattendance` int NOT NULL AUTO_INCREMENT,
  `idstudclass` int DEFAULT NULL,
  `dateabsent` date DEFAULT NULL,
  `absentreason` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idattendance`),
  KEY `idstudclass` (`idstudclass`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`idstudclass`) REFERENCES `studentclass` (`idstudclass`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (25,1,'2022-11-23',''),(26,2,'2022-11-23',''),(27,8,'2022-11-23',''),(28,9,'2022-11-23','');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classconfig`
--

DROP TABLE IF EXISTS `classconfig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classconfig` (
  `idclass` varchar(15) NOT NULL,
  `standard` int DEFAULT NULL,
  `division` varchar(3) DEFAULT NULL,
  `acadyr` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idclass`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Details of all classes and divisions along with academic year';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classconfig`
--

LOCK TABLES `classconfig` WRITE;
/*!40000 ALTER TABLE `classconfig` DISABLE KEYS */;
INSERT INTO `classconfig` VALUES ('12E1202223',12,'E1','2022-2023'),('12F2202223',12,'F2','2022-2023');
/*!40000 ALTER TABLE `classconfig` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classsubject`
--

DROP TABLE IF EXISTS `classsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classsubject` (
  `idclasssubject` int NOT NULL,
  `idclass` varchar(15) DEFAULT NULL,
  `idsubject` int DEFAULT NULL,
  PRIMARY KEY (`idclasssubject`),
  KEY `idsubject` (`idsubject`),
  KEY `idclass` (`idclass`),
  CONSTRAINT `classsubject_ibfk_1` FOREIGN KEY (`idsubject`) REFERENCES `subject` (`idsubject`),
  CONSTRAINT `classsubject_ibfk_2` FOREIGN KEY (`idclass`) REFERENCES `classconfig` (`idclass`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classsubject`
--

LOCK TABLES `classsubject` WRITE;
/*!40000 ALTER TABLE `classsubject` DISABLE KEYS */;
INSERT INTO `classsubject` VALUES (1,'12F2202223',1),(2,'12F2202223',2),(3,'12F2202223',3),(4,'12F2202223',4),(5,'12F2202223',5),(6,'12E1202223',1),(7,'12E1202223',2),(8,'12E1202223',3),(9,'12E1202223',4),(10,'12E1202223',7);
/*!40000 ALTER TABLE `classsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessionlog`
--

DROP TABLE IF EXISTS `sessionlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sessionlog` (
  `idsessionlog` int NOT NULL AUTO_INCREMENT,
  `idclass` varchar(45) DEFAULT NULL,
  `idsubject` int DEFAULT NULL,
  `datelog` datetime DEFAULT NULL,
  `sessionnum` int DEFAULT NULL,
  `logcontent` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`idsessionlog`),
  KEY `idclass` (`idclass`),
  KEY `idsubject` (`idsubject`),
  CONSTRAINT `sessionlog_ibfk_1` FOREIGN KEY (`idclass`) REFERENCES `classconfig` (`idclass`),
  CONSTRAINT `sessionlog_ibfk_2` FOREIGN KEY (`idsubject`) REFERENCES `subject` (`idsubject`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table to store details of every session conducted in the class.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessionlog`
--

LOCK TABLES `sessionlog` WRITE;
/*!40000 ALTER TABLE `sessionlog` DISABLE KEYS */;
INSERT INTO `sessionlog` VALUES (25,'12E1202223',1,'2022-11-23 00:00:00',1,'Chapter 7 completed. Homework given.'),(26,'12E1202223',2,'2022-11-23 00:00:00',2,'Integration chapture completed. Bookback excercise HW given.'),(27,'12E1202223',3,'2022-11-23 00:00:00',3,'Optics chapter started. Assignment given on Optics.'),(28,'12E1202223',4,'2022-11-23 00:00:00',4,'Organic chapter 1 completed. Class test scheduled for 25-Nov.'),(29,'12E1202223',7,'2022-11-23 00:00:00',5,'Half yearly portions completed. Daily revision to start Friday 25-Nov'),(30,'12F2202223',5,'2022-11-23 00:00:00',1,'SQL chapter completed. Bookback excercise to be completed on 25th Nov'),(31,'12F2202223',2,'2022-11-23 00:00:00',2,'Integration chapter completed.');
/*!40000 ALTER TABLE `sessionlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `idstudent` varchar(10) NOT NULL,
  `studfname` varchar(45) DEFAULT NULL,
  `studlname` varchar(45) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `studdob` date DEFAULT NULL,
  `studadmissiondate` date DEFAULT NULL,
  `studexitdate` date DEFAULT NULL,
  PRIMARY KEY (`idstudent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('K123456','Abishek','S','Male','2005-01-01','2010-01-01',NULL),('K123458','Karthik','M','Male','2005-01-01','2010-01-01',NULL),('K123459','Pranav','T','Male','2005-01-01','2010-01-01',NULL),('K123460','Dharshini','S','Female','2005-01-01','2005-01-01',NULL),('K123461','Harini','M','Female','2005-01-01','2005-01-01',NULL),('K123462','Praneeth','B','Male','2005-01-01','2005-01-01',NULL),('K123463','Harish','S','Male','2005-01-01','2005-01-01',NULL),('K123464','Harsha','G','Male','2005-01-01','2005-01-01',NULL),('K123465','Abirami','S','Female','2005-01-01','2005-01-01',NULL),('S123457','Raam','M','Male','2005-01-01','2010-01-01',NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentclass`
--

DROP TABLE IF EXISTS `studentclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studentclass` (
  `idstudclass` int NOT NULL AUTO_INCREMENT,
  `idstudent` varchar(10) DEFAULT NULL,
  `idclass` varchar(15) DEFAULT NULL,
  `rollnumber` int DEFAULT NULL,
  PRIMARY KEY (`idstudclass`),
  KEY `idstudent` (`idstudent`),
  KEY `idclass` (`idclass`),
  CONSTRAINT `studentclass_ibfk_1` FOREIGN KEY (`idstudent`) REFERENCES `student` (`idstudent`),
  CONSTRAINT `studentclass_ibfk_2` FOREIGN KEY (`idclass`) REFERENCES `classconfig` (`idclass`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentclass`
--

LOCK TABLES `studentclass` WRITE;
/*!40000 ALTER TABLE `studentclass` DISABLE KEYS */;
INSERT INTO `studentclass` VALUES (1,'S123457','12F2202223',1),(2,'K123456','12F2202223',2),(3,'K123458','12F2202223',3),(4,'K123459','12F2202223',4),(5,'K123460','12F2202223',5),(6,'K123461','12E1202223',1),(7,'K123462','12E1202223',2),(8,'K123463','12E1202223',3),(9,'K123464','12E1202223',4),(10,'K123465','12E1202223',5);
/*!40000 ALTER TABLE `studentclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `idsubject` int NOT NULL,
  `subjectname` varchar(45) DEFAULT NULL,
  `acadyr` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idsubject`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='All the subjects taught across all classes and divisions';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1,'English','2022-2023'),(2,'Mathematics','2022-2023'),(3,'Physics','2022-2023'),(4,'Chemistry','2022-2023'),(5,'Computer Science','2022-2023'),(6,'Informatics','2022-2023'),(7,'Biology','2022-2023'),(8,'Economics','2022-2023'),(9,'Commerce','2022-2023'),(10,'Basic Mathematics','2022-2023');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `idteacher` int NOT NULL AUTO_INCREMENT,
  `teacherfname` varchar(45) DEFAULT NULL,
  `teacherlname` varchar(45) DEFAULT NULL,
  `teacherinitials` varchar(5) DEFAULT NULL,
  `teachergender` varchar(10) DEFAULT NULL,
  `teacherdoj` date DEFAULT NULL,
  `teacherlwd` date DEFAULT NULL,
  PRIMARY KEY (`idteacher`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='This is the master table with details of all the teachers';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'Abcd','Efgh','AE','Female','2022-01-01',NULL);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vw_anecdote`
--

DROP TABLE IF EXISTS `vw_anecdote`;
/*!50001 DROP VIEW IF EXISTS `vw_anecdote`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_anecdote` AS SELECT 
 1 AS `idanecdote`,
 1 AS `idstudclass`,
 1 AS `anecdate`,
 1 AS `idteacher`,
 1 AS `anectype`,
 1 AS `anecdesc`,
 1 AS `idstudent`,
 1 AS `studfname`,
 1 AS `studlname`,
 1 AS `gender`,
 1 AS `idclass`,
 1 AS `rollnumber`,
 1 AS `standard`,
 1 AS `division`,
 1 AS `acadyr`,
 1 AS `teacherfname`,
 1 AS `teacherlname`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_attendstudclass`
--

DROP TABLE IF EXISTS `vw_attendstudclass`;
/*!50001 DROP VIEW IF EXISTS `vw_attendstudclass`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_attendstudclass` AS SELECT 
 1 AS `idstudent`,
 1 AS `studfname`,
 1 AS `studlname`,
 1 AS `gender`,
 1 AS `studdob`,
 1 AS `studadmissiondate`,
 1 AS `studexitdate`,
 1 AS `idstudclass`,
 1 AS `idclass`,
 1 AS `rollnumber`,
 1 AS `standard`,
 1 AS `division`,
 1 AS `acadyr`,
 1 AS `idattendance`,
 1 AS `dateabsent`,
 1 AS `absentreason`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_classsubject`
--

DROP TABLE IF EXISTS `vw_classsubject`;
/*!50001 DROP VIEW IF EXISTS `vw_classsubject`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_classsubject` AS SELECT 
 1 AS `idclasssubject`,
 1 AS `idclass`,
 1 AS `idsubject`,
 1 AS `subjectname`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_sesslogsubject`
--

DROP TABLE IF EXISTS `vw_sesslogsubject`;
/*!50001 DROP VIEW IF EXISTS `vw_sesslogsubject`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_sesslogsubject` AS SELECT 
 1 AS `idsessionlog`,
 1 AS `idclass`,
 1 AS `idsubject`,
 1 AS `datelog`,
 1 AS `sessionnum`,
 1 AS `logcontent`,
 1 AS `subjectname`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_studentclass`
--

DROP TABLE IF EXISTS `vw_studentclass`;
/*!50001 DROP VIEW IF EXISTS `vw_studentclass`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_studentclass` AS SELECT 
 1 AS `idstudent`,
 1 AS `studfname`,
 1 AS `studlname`,
 1 AS `gender`,
 1 AS `studdob`,
 1 AS `studadmissiondate`,
 1 AS `studexitdate`,
 1 AS `idstudclass`,
 1 AS `idclass`,
 1 AS `rollnumber`,
 1 AS `standard`,
 1 AS `division`,
 1 AS `acadyr`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vw_anecdote`
--

/*!50001 DROP VIEW IF EXISTS `vw_anecdote`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_anecdote` AS select `anecdote`.`idanecdote` AS `idanecdote`,`anecdote`.`idstudclass` AS `idstudclass`,`anecdote`.`anecdate` AS `anecdate`,`anecdote`.`idteacher` AS `idteacher`,`anecdote`.`anectype` AS `anectype`,`anecdote`.`anecdesc` AS `anecdesc`,`vw_studentclass`.`idstudent` AS `idstudent`,`vw_studentclass`.`studfname` AS `studfname`,`vw_studentclass`.`studlname` AS `studlname`,`vw_studentclass`.`gender` AS `gender`,`vw_studentclass`.`idclass` AS `idclass`,`vw_studentclass`.`rollnumber` AS `rollnumber`,`vw_studentclass`.`standard` AS `standard`,`vw_studentclass`.`division` AS `division`,`vw_studentclass`.`acadyr` AS `acadyr`,`teacher`.`teacherfname` AS `teacherfname`,`teacher`.`teacherlname` AS `teacherlname` from ((`anecdote` join `teacher`) join `vw_studentclass`) where ((`anecdote`.`idstudclass` = `vw_studentclass`.`idstudclass`) and (`anecdote`.`idteacher` = `teacher`.`idteacher`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_attendstudclass`
--

/*!50001 DROP VIEW IF EXISTS `vw_attendstudclass`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_attendstudclass` AS select `vw_studentclass`.`idstudent` AS `idstudent`,`vw_studentclass`.`studfname` AS `studfname`,`vw_studentclass`.`studlname` AS `studlname`,`vw_studentclass`.`gender` AS `gender`,`vw_studentclass`.`studdob` AS `studdob`,`vw_studentclass`.`studadmissiondate` AS `studadmissiondate`,`vw_studentclass`.`studexitdate` AS `studexitdate`,`vw_studentclass`.`idstudclass` AS `idstudclass`,`vw_studentclass`.`idclass` AS `idclass`,`vw_studentclass`.`rollnumber` AS `rollnumber`,`vw_studentclass`.`standard` AS `standard`,`vw_studentclass`.`division` AS `division`,`vw_studentclass`.`acadyr` AS `acadyr`,`attendance`.`idattendance` AS `idattendance`,`attendance`.`dateabsent` AS `dateabsent`,`attendance`.`absentreason` AS `absentreason` from (`vw_studentclass` join `attendance`) where (`vw_studentclass`.`idstudclass` = `attendance`.`idstudclass`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_classsubject`
--

/*!50001 DROP VIEW IF EXISTS `vw_classsubject`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_classsubject` AS select `classsubject`.`idclasssubject` AS `idclasssubject`,`classsubject`.`idclass` AS `idclass`,`classsubject`.`idsubject` AS `idsubject`,`subject`.`subjectname` AS `subjectname` from (`classsubject` join `subject`) where (`classsubject`.`idsubject` = `subject`.`idsubject`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_sesslogsubject`
--

/*!50001 DROP VIEW IF EXISTS `vw_sesslogsubject`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_sesslogsubject` AS select `sessionlog`.`idsessionlog` AS `idsessionlog`,`sessionlog`.`idclass` AS `idclass`,`sessionlog`.`idsubject` AS `idsubject`,`sessionlog`.`datelog` AS `datelog`,`sessionlog`.`sessionnum` AS `sessionnum`,`sessionlog`.`logcontent` AS `logcontent`,`subject`.`subjectname` AS `subjectname` from (`sessionlog` join `subject`) where (`subject`.`idsubject` = `sessionlog`.`idsubject`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_studentclass`
--

/*!50001 DROP VIEW IF EXISTS `vw_studentclass`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_studentclass` AS select `student`.`idstudent` AS `idstudent`,`student`.`studfname` AS `studfname`,`student`.`studlname` AS `studlname`,`student`.`gender` AS `gender`,`student`.`studdob` AS `studdob`,`student`.`studadmissiondate` AS `studadmissiondate`,`student`.`studexitdate` AS `studexitdate`,`studentclass`.`idstudclass` AS `idstudclass`,`studentclass`.`idclass` AS `idclass`,`studentclass`.`rollnumber` AS `rollnumber`,`classconfig`.`standard` AS `standard`,`classconfig`.`division` AS `division`,`classconfig`.`acadyr` AS `acadyr` from ((`student` join `studentclass`) join `classconfig`) where ((`student`.`idstudent` = `studentclass`.`idstudent`) and (`studentclass`.`idclass` = `classconfig`.`idclass`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 19:40:20
