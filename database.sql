CREATE DATABASE RESTAURANT;
USE RESTAURANT;

CREATE TABLE STARTERS
(
SLNO INT(4) PRIMARY KEY,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4) NOT NULL
);
INSERT INTO STARTERS VALUES(1,'GREEN SALAD','50');
INSERT INTO STARTERS VALUES(2,'SWEET CORN SOUP','85');
INSERT INTO STARTERS VALUES(3,'MUSHROOM SOUP','85');
INSERT INTO STARTERS VALUES(4,'HOT AND SOUR SOUP','85');
INSERT INTO STARTERS VALUES(5,'MIXED VEG SOUP','85');
INSERT INTO STARTERS VALUES(6,'MUSHROOM CORN SOUP','85');
INSERT INTO STARTERS VALUES(7,'VEG MANCHOW','90');
INSERT INTO STARTERS VALUES(8,'GOBI MANCHURIAN','135');
INSERT INTO STARTERS VALUES(9,'BABYCORN MANCHURIAN','135');
INSERT INTO STARTERS VALUES(10,'PANEER TIKKA','150');
INSERT INTO STARTERS VALUES(11,'VEG SPRINGROLL','135');

CREATE TABLE MAINCOURSE_NONVEG
(
SLNO INT(4) PRIMARY KEY,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4)  NOT NULL
);
INSERT INTO MAINCOURSE_NONVEG VALUES(1,'CHICKEN BIRYANI','170');
INSERT INTO MAINCOURSE_NONVEG VALUES(2,'CHICKEN FRIEDRICE','150');
INSERT INTO MAINCOURSE_NONVEG VALUES(3,'SCHEZWAN FRIEDRICE NON','150');
INSERT INTO MAINCOURSE_NONVEG VALUES(4,'MUTTON BIRYANI','160');
INSERT INTO MAINCOURSE_NONVEG VALUES(5,'EGG BIRYANI','130');
INSERT INTO MAINCOURSE_NONVEG VALUES(6,'PRAWNS FRY','135');
INSERT INTO MAINCOURSE_NONVEG VALUES(7,'CHICKEN TKKSML ','175');
INSERT INTO MAINCOURSE_NONVEG VALUES(8,'CHICKEN SINGAPURI','175');
INSERT INTO MAINCOURSE_NONVEG VALUES(9,'CHICKEN PPPRMSL','175');
INSERT INTO MAINCOURSE_NONVEG VALUES(10,'CHICKEN CHETINADU','140');
INSERT INTO MAINCOURSE_NONVEG VALUES(11,'CHICKEN SCHEZWAN NDLS','140');
INSERT INTO MAINCOURSE_NONVEG VALUES(12,'CHICKEN CHOWMEIN','130');

CREATE TABLE MAINCOURSE_VEG
(
SLNO INT(4)PRIMARY KEY,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4)  NOT NULL
);
INSERT INTO MAINCOURSE_VEG VALUES(1,'SCHEZWAN FRIED RICE','130');
INSERT INTO MAINCOURSE_VEG VALUES(2,'MIXEDVEG FRIED RICE','120');
INSERT INTO MAINCOURSE_VEG VALUES(3,'CURD RICE','65');
INSERT INTO MAINCOURSE_VEG VALUES(4,'VEG BIRYANI','130');
INSERT INTO MAINCOURSE_VEG VALUES(5,'VEG PULAV','125');
INSERT INTO MAINCOURSE_VEG VALUES(6,'ROTI','27');
INSERT INTO MAINCOURSE_VEG VALUES(7,'NAAN','32');
INSERT INTO MAINCOURSE_VEG VALUES(8,'KULCHA','32');
INSERT INTO MAINCOURSE_VEG VALUES(9,'BUTTER NAAN','32');
INSERT INTO MAINCOURSE_VEG VALUES(10,'RUMALI ROTI','37');
INSERT INTO MAINCOURSE_VEG VALUES(11,'PANEER BUTTER MSL','130');
INSERT INTO MAINCOURSE_VEG VALUES(12,'PANEER MUTTER MSL','130');
INSERT INTO MAINCOURSE_VEG VALUES(13,'MIX VEG CURRY','145');
INSERT INTO MAINCOURSE_VEG VALUES(14,'DAL FRY','110');
INSERT INTO MAINCOURSE_VEG VALUES(15,'BABYCORN MASALA','150');
INSERT INTO MAINCOURSE_VEG VALUES(16,'MALAI KOFTA','145');
INSERT INTO MAINCOURSE_VEG VALUES(17,'ALLU MUTTER MSL','130');
INSERT INTO MAINCOURSE_VEG VALUES(18,'VEG KOLHAPURI','145');
INSERT INTO MAINCOURSE_VEG VALUES(19,'SCHEZWAN NDLS','140');
INSERT INTO MAINCOURSE_VEG VALUES(20,'VEG CHOWMEIN','130');
INSERT INTO MAINCOURSE_VEG VALUES(21,'FRIED NDLS','130');

CREATE TABLE DESSERTS
(
SLNO INT(4) PRIMARY KEY,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4)  NOT NULL
);
INSERT INTO DESSERTS VALUES(1,'COOKIECREAM','125');
INSERT INTO DESSERTS VALUES(2,'ROYALCRUNCH','125');
INSERT INTO DESSERTS VALUES(3,'FRUIT FUSION','250');
INSERT INTO DESSERTS VALUES(4,'HOT FUDGE','250');
INSERT INTO DESSERTS VALUES(5,'SOFT SERVE','105');
INSERT INTO DESSERTS VALUES(6,'BROWNIE SUNDAE','250');
INSERT INTO DESSERTS VALUES(7,'TRIPLE SUNDAE','250');
INSERT INTO DESSERTS VALUES(8,'POPSICLES','200');
INSERT INTO DESSERTS VALUES(9,'CHOCODIP','125');
INSERT INTO DESSERTS VALUES(10,'BERRYBLAST','120');

CREATE TABLE DRINKS
(
SLNO INT(4) PRIMARY KEY,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4)  NOT NULL
);
INSERT INTO DRINKS VALUES(1,'COLD BADAM MILK','50');
INSERT INTO DRINKS VALUES(2,'HOT BADAM MILK','55');
INSERT INTO DRINKS VALUES(3,'MILKSHAKES V,S,P','65');
INSERT INTO DRINKS VALUES(4,'CARAMEL SHAKE','70');
INSERT INTO DRINKS VALUES(5,'DRYFRUIT SHAKE','100');
INSERT INTO DRINKS VALUES(6,'SOFT DRINKS','75');
INSERT INTO DRINKS VALUES(7,'WATER','66');
INSERT INTO DRINKS VALUES(8,'ICE TEA','70');
INSERT INTO DRINKS VALUES(9,'COFFEE','60');
INSERT INTO DRINKS VALUES(10,'TEA','50');
INSERT INTO DRINKS VALUES(11,'LASSI','55');

CREATE TABLE CHAATS
(
SLNO INT(4) PRIMARY KEY ,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4)  NOT NULL
);
INSERT INTO CHAATS VALUES(1,'SAMOSA CHAT','30');
INSERT INTO CHAATS VALUES(2,'SAMOSA DAHI CHAT','35');
INSERT INTO CHAATS VALUES(3,'PLAIN KACHORI','20');
INSERT INTO CHAATS VALUES(4,'KACHORI MASALA','30');
INSERT INTO CHAATS VALUES(5,'DAHI KACHORI','30');
INSERT INTO CHAATS VALUES(6,'PANI PURI','25');
INSERT INTO CHAATS VALUES(7,'DAHI PURI','30');
INSERT INTO CHAATS VALUES(8,'BHEL PURI','25');
INSERT INTO CHAATS VALUES(9,'ALOO PURI','25');
INSERT INTO CHAATS VALUES(10,'DAHI PAPDI CHAT','25');
INSERT INTO CHAATS VALUES(11,'PEANUT CHAT','30');
INSERT INTO CHAATS VALUES(12,'TOMATO CHAT','25');

CREATE TABLE MEALS
(
SLNO INT(4) PRIMARY KEY ,
VARIETY VARCHAR(40) NOT NULL ,
PRICE INT(4)  NOT NULL
);
INSERT INTO MEALS VALUES(1,'SOUTH INDIAN MEALS','150');
INSERT INTO MEALS VALUES(2,'NORTH INDIAN MEALS','150');
INSERT INTO MEALS VALUES(3,'ANDHRA MEALS','160');
INSERT INTO MEALS VALUES(4,'FULL MEALS','200');
INSERT INTO MEALS VALUES(5,'FAMILY PACK MEALS','250');