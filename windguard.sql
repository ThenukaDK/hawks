-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 26, 2016 at 04:29 PM
-- Server version: 5.1.36
-- PHP Version: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `windguard`
--

-- --------------------------------------------------------

--
-- Table structure for table `anamolies`
--

CREATE TABLE IF NOT EXISTS `anamolies` (
  `anomalyId` varchar(255) NOT NULL,
  `imageMapId` varchar(255) NOT NULL,
  `noOfAnamolies` int(255) NOT NULL,
  `noOfLogs` int(255) NOT NULL,
  `noOfCuts` int(255) NOT NULL,
  `noOfMarijuana` int(255) NOT NULL,
  `alertSend` tinyint(1) NOT NULL,
  `imageUrl` varchar(255) NOT NULL,
  `dateTime` datetime NOT NULL,
  PRIMARY KEY (`anomalyId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `anamolies`
--

INSERT INTO `anamolies` (`anomalyId`, `imageMapId`, `noOfAnamolies`, `noOfLogs`, `noOfCuts`, `noOfMarijuana`, `alertSend`, `imageUrl`, `dateTime`) VALUES
('7b0d0790-d2ba-492b-8e9b-f176bc00fdd1', '123', 48, 42, 6, 0, 1, '../img/detected_images/20160826-1540317b0d0790-d2ba-492b-8e9b-f176bc00fdd1.jpg', '2016-08-26 15:40:31'),
('2d0046a0-df97-4b04-a7b8-4b226aa96e11', '123', 86, 82, 4, 0, 1, '../img/detected_images/20160826-1540312d0046a0-df97-4b04-a7b8-4b226aa96e11.jpg', '2016-08-26 15:40:31'),
('89a2c094-b947-4fb2-9ded-8b40ac0e59d1', '123', 16, 13, 3, 0, 1, '../img/detected_images/20160726-23274789a2c094-b947-4fb2-9ded-8b40ac0e59d1.jpg', '2016-07-26 23:27:47'),
('cd92ef12-bcc6-4ce6-a2bf-9e805ea8c708', '123', 16, 13, 3, 0, 1, '../img/detected_images/20160826-154030cd92ef12-bcc6-4ce6-a2bf-9e805ea8c708.jpg', '2016-08-26 15:40:30'),
('888ec5d8-66c0-4e8c-a143-454916f281dd', '123', 390, 363, 27, 0, 1, '../img/detected_images/20160826-154030888ec5d8-66c0-4e8c-a143-454916f281dd.jpg', '2016-08-26 15:40:30'),
('457ae8d2-793a-4121-ab4b-3912a74f04f7', '123', 86, 82, 4, 0, 1, '../img/detected_images/20160726-232748457ae8d2-793a-4121-ab4b-3912a74f04f7.jpg', '2016-07-26 23:27:48'),
('90192a60-554e-4d9d-9e77-8dff9d6e3eb7', '123', 48, 42, 6, 0, 1, '../img/detected_images/20160726-23274890192a60-554e-4d9d-9e77-8dff9d6e3eb7.jpg', '2016-07-26 23:27:48'),
('2ceb7a6c-afaa-4e6d-ac52-bdc67a42e9a9', '123', 390, 363, 27, 0, 1, '../img/detected_images/20160726-2327472ceb7a6c-afaa-4e6d-ac52-bdc67a42e9a9.jpg', '2016-07-26 23:27:47');

-- --------------------------------------------------------

--
-- Table structure for table `chargingpole`
--

CREATE TABLE IF NOT EXISTS `chargingpole` (
  `poleId` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL,
  `latitude` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chargingpole`
--


-- --------------------------------------------------------

--
-- Table structure for table `copters`
--

CREATE TABLE IF NOT EXISTS `copters` (
  `copterId` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `longtitude` varchar(255) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  PRIMARY KEY (`copterId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `copters`
--


-- --------------------------------------------------------

--
-- Table structure for table `copters_on_pole`
--

CREATE TABLE IF NOT EXISTS `copters_on_pole` (
  `copterId` varchar(255) NOT NULL,
  `poleId` varchar(255) NOT NULL,
  `landTime` datetime NOT NULL,
  `leaveTime` datetime NOT NULL,
  `noOfImagesStored` int(255) NOT NULL,
  PRIMARY KEY (`poleId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `copters_on_pole`
--


-- --------------------------------------------------------

--
-- Table structure for table `image_map`
--

CREATE TABLE IF NOT EXISTS `image_map` (
  `imageMapId` varchar(255) NOT NULL,
  `poleId` varchar(255) NOT NULL,
  `copterId` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  `imageUrl` varchar(255) NOT NULL,
  `dateTime` datetime NOT NULL,
  PRIMARY KEY (`imageMapId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `image_map`
--

INSERT INTO `image_map` (`imageMapId`, `poleId`, `copterId`, `longitude`, `latitude`, `imageUrl`, `dateTime`) VALUES
('20160726-2024289edb61de-6a31-42c1-bb1e-43f23ceff7m5', 'aaaa', '321', '88.659', '87.65', '../img/imagemap/20160726-2024289edb61de-6a31-42c1-bb1e-43f23ceff7m5.jpg', '2016-07-18 23:19:53'),
('20160726-2024289edb61de-6a31-42c1-bb1e-43f23ceff7n6', 'bbbb', '435', '85.36', '84.26', '../img/imagemap/20160726-2024289edb61de-6a31-42c1-bb1e-43f23ceff7n6.jpg', '2016-07-19 23:19:46');

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE IF NOT EXISTS `notifications` (
  `notificationId` varchar(255) NOT NULL,
  `imageMapId` varchar(255) NOT NULL,
  `anomalyId` varchar(255) NOT NULL,
  `notification` varchar(255) NOT NULL,
  `notificationSend` tinyint(1) NOT NULL,
  `notificationType` int(11) NOT NULL,
  `dateTime` datetime NOT NULL,
  PRIMARY KEY (`notificationId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`notificationId`, `imageMapId`, `anomalyId`, `notification`, `notificationSend`, `notificationType`, `dateTime`) VALUES
('5796fc2847d9e', '.123.', '5893ad39-6975-4cb2-a2de-60509fa4bce1', 'Some Anomalies Detected!', 1, 2, '2016-07-25 22:59:02'),
('5796fc2847a76', '.123.', '7f22715a-a6b3-4518-ab4f-b6d0e5b7aa78', 'Heavy Damage Detected!', 1, 1, '2016-07-25 22:59:01'),
('5796fc2847c15', '.123.', '7052d1e9-7b9d-45a9-a636-4b467406b885', 'Some Anomalies Detected!', 1, 2, '2016-07-25 22:59:01'),
('5796fc2847838', '.123.', 'b9d9da12-f366-4d4a-a154-259b89653b54', 'Heavy Damage Detected!', 1, 1, '2016-07-25 22:59:03'),
('57977034974f6', '.123.', 'a82bedd7-b3f2-462e-951e-699b5bb49a21', 'Heavy Damage Detected!', 1, 1, '2016-07-26 19:44:12'),
('579770349e0d0', '.123.', '32675905-9d30-4ed6-81ee-f516be964e89', 'Some Anomalies Detected!', 1, 2, '2016-07-26 19:44:12'),
('579777423e49c', '.123.', '3d622023-9054-4aa3-bd9d-dd08f0ed73e4', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:09:30'),
('579777423e65b', '.123.', '2ce3bf57-54d7-4e48-9f23-520ac3f1920c', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:09:30'),
('579777423e727', '.123.', '6d5357f7-0a3e-4d60-bda6-4e34c6a9b384', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:09:30'),
('579777423e8ab', '.123.', '9f69512d-73dd-49d7-b5fd-2d3654c0092b', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:09:31'),
('579777eedeb9d', '.123.', '6f743760-6f1e-4641-a8ca-a7131cd69f5f', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:15:21'),
('579778c5910d8', '.123.', '0cbb35e5-243d-4751-9363-dea42bd01e0e', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:20:45'),
('579778c591237', '.123.', 'fb21e037-e874-4b3b-a313-55d2e77012eb', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:20:45'),
('579778c591352', '.123.', '0f29d9a7-9ce0-4f27-bbbb-1f65f4598ae1', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:20:44'),
('579778c591447', '.123.', 'bffebc54-01af-4262-9766-ca015878b8d7', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:20:44'),
('579778ffd9c8e', '.123.', '83feeff2-4e52-46d8-8279-b718dc3523c9', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:21:43'),
('579778ffd9e15', '.123.', '45abcca2-fe44-414e-aacc-2bf3039ad8ab', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:21:43'),
('579778ffd9f5d', '.123.', 'b7844eea-a8a4-4cad-868d-d9b4fa7361a5', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:21:42'),
('579778ffda136', '.123.', '3b1e8303-44a4-45ad-8f59-6e400586428e', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:21:43'),
('579779a56ce00', '.123.', '39e8146b-5980-43b4-867b-f5cf18471d1a', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:24:29'),
('579779a56cf91', '.123.', '9edb61de-6a31-42c1-bb1e-43f23ceff7d2', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:24:28'),
('579779a56d0ca', '.123.', '85ff84ba-f6a4-4fb5-8ece-ff737a2ab41b', 'Some Anomalies Detected!', 1, 2, '2016-07-26 20:24:28'),
('579779a56d1fb', '.123.', '2085ed42-5cfe-48a1-b8b9-2ea4838a1caf', 'Heavy Damage Detected!', 1, 1, '2016-07-26 20:24:28'),
('5797a49c7ba2d', '.123.', '89a2c094-b947-4fb2-9ded-8b40ac0e59d1', 'Some Anomalies Detected!', 1, 2, '2016-07-26 23:27:47'),
('5797a49c7bbdb', '.123.', '457ae8d2-793a-4121-ab4b-3912a74f04f7', 'Heavy Damage Detected!', 1, 1, '2016-07-26 23:27:48'),
('5797a49c7bcd6', '.123.', '90192a60-554e-4d9d-9e77-8dff9d6e3eb7', 'Some Anomalies Detected!', 1, 2, '2016-07-26 23:27:48'),
('5797a49c7bde8', '.123.', '2ceb7a6c-afaa-4e6d-ac52-bdc67a42e9a9', 'Heavy Damage Detected!', 1, 1, '2016-07-26 23:27:47'),
('57c015fe9be80', '.123.', '7b0d0790-d2ba-492b-8e9b-f176bc00fdd1', 'Some Anomalies Detected!', 1, 2, '2016-08-26 15:40:31'),
('57c015fea5897', '.123.', '2d0046a0-df97-4b04-a7b8-4b226aa96e11', 'Heavy Damage Detected!', 1, 1, '2016-08-26 15:40:31'),
('57c015fea5c2f', '.123.', 'cd92ef12-bcc6-4ce6-a2bf-9e805ea8c708', 'Some Anomalies Detected!', 1, 2, '2016-08-26 15:40:30'),
('57c015fea5eed', '.123.', '888ec5d8-66c0-4e8c-a143-454916f281dd', 'Heavy Damage Detected!', 1, 1, '2016-08-26 15:40:30');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `userId` varchar(255) NOT NULL,
  `userType` varchar(50) NOT NULL,
  `userName` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `title` varchar(100) NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userId`, `userType`, `userName`, `password`, `title`) VALUES
('thenukaa@gmail.com', 'Admin', 'Thenuka', 'underground1992', 'Department head'),
('dinidust@yahoo.com', 'User', 'Dinidu', 'dinidu123', 'police officer'),
('uygunihu@hnuih.com', 'User', 'nhuihnihn', '123', 'root');
