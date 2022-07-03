/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - online_game_center_booking_system
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`z` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_game_center_booking_system`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `timeslot_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`customer_id`,`timeslot_id`,`amount`,`date`,`status`) values (1,1,2,'1000','2022-02-25','paid');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint`,`reply`,`date`) values (1,1,'hhhh','asd','2022-02-09 22:57:16');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`first_name`,`last_name`,`place`,`phone`,`email`) values (1,'anna@gmail.com','anna','rose','kochii','9999999999','anna@gmail.comm');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`user_type`) values ('admin','admin','admin'),('anna@gmail.com','anna','customer'),('rio@gmail.com','rio','staff');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `booking_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount`,`date`) values (1,1,'1000','2022-02-25');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `fstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`first_name`,`last_name`,`house_name`,`place`,`phone`,`email`,`fstatus`) values (1,'rio@gmail.com','rio','pp','ggggggg','vypin','9999999999','rio@gmail.com','active');

/*Table structure for table `timeslot` */

DROP TABLE IF EXISTS `timeslot`;

CREATE TABLE `timeslot` (
  `timeslot_id` int(11) NOT NULL AUTO_INCREMENT,
  `venue_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `mstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`timeslot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `timeslot` */

insert  into `timeslot`(`timeslot_id`,`venue_id`,`date`,`time`,`mstatus`) values (1,1,'2022-02-24','8.00AM-9.00AM','active'),(2,1,'2022-02-24','9.00AM-10.00AM','active'),(3,1,'2022-02-24','5.00PM-6.00PM','active'),(4,1,'2022-02-18','5.00PM-6.00PM','active'),(5,2,'2022-02-18','5.00PM-6.00PM','active'),(6,4,'2022-02-18','10.00AM-11.00AM','active'),(7,4,'2022-02-25','10.00AM-11.00AM','active'),(8,4,'2022-02-25','10.00AM-11.00AM','active'),(9,5,'2022-02-25','5.00PM-6.00PM','active');

/*Table structure for table `venue` */

DROP TABLE IF EXISTS `venue`;

CREATE TABLE `venue` (
  `venue_id` int(11) NOT NULL AUTO_INCREMENT,
  `venue` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  `vstatus` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`venue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `venue` */

insert  into `venue`(`venue_id`,`venue`,`place`,`amount`,`details`,`vstatus`) values (1,'5S FO0OTBALLL TRUF','ernakulam','1000','cchhgcghcg','active'),(2,'9S FO0OTBALLL TRUF','kochi','2000','dfsdf','active'),(3,'11S FO0OTBALLL TRUF','kochi','3000','adfsf','active'),(4,'Basket  ball Court indoor','kochi','1000','gjkgjhgyjfguyf','active'),(5,'Indoor Tennis Court','ernakulam','2000','bbbbbbbbbb','active'),(6,'Indoor Badminton Court','kochi','2000','gjkgjhgyjfguyf','active'),(7,'Indoor Criket Court','ernakulam','2000','kkkkkkk','active'),(8,'Indoor Volleyball Court','kochi','2000','bbbbbbbbbb','active'),(11,'5s Futsal grount indoor','kochi','2000','gjkgjhgyjfguyf','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
