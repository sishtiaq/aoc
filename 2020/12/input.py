
t0 = [('F',10),
      ('N',3),
      ('F',7),
      ('R',90),
      ('F',11),]
# Run
#     sed "s/\([A-Z]*\)\([0-9]*\)/('\1',\2),/g"
# on input
# L,R instructions are only 90,180,270
t1 = [('W',1),
      ('L',90),
      ('F',26),
      ('S',3),
      ('W',2),
      ('N',5),
      ('L',180),
      ('S',4),
      ('F',41),
      ('W',1),
      ('F',48),
      ('W',3),
      ('F',44),
      ('F',63),
      ('W',5),
      ('N',3),
      ('E',5),
      ('F',7),
      ('R',180),
      ('W',1),
      ('N',3),
      ('W',3),
      ('R',180),
      ('F',38),
      ('N',1),
      ('E',3),
      ('L',90),
      ('F',49),
      ('S',5),
      ('F',11),
      ('E',1),
      ('R',90),
      ('W',3),
      ('N',4),
      ('E',3),
      ('R',180),
      ('W',5),
      ('F',93),
      ('S',1),
      ('F',67),
      ('L',180),
      ('W',3),
      ('S',5),
      ('N',3),
      ('L',180),
      ('E',1),
      ('N',2),
      ('F',90),
      ('S',3),
      ('W',3),
      ('N',3),
      ('E',1),
      ('F',77),
      ('W',3),
      ('N',3),
      ('L',180),
      ('E',2),
      ('F',25),
      ('N',1),
      ('W',1),
      ('S',1),
      ('E',5),
      ('S',4),
      ('R',180),
      ('W',1),
      ('F',13),
      ('L',90),
      ('W',4),
      ('S',5),
      ('F',13),
      ('N',2),
      ('R',90),
      ('F',89),
      ('R',90),
      ('W',3),
      ('L',90),
      ('W',5),
      ('N',5),
      ('E',4),
      ('S',4),
      ('F',26),
      ('N',1),
      ('R',270),
      ('N',5),
      ('E',5),
      ('L',180),
      ('R',180),
      ('W',4),
      ('R',90),
      ('W',5),
      ('F',49),
      ('S',2),
      ('F',53),
      ('W',5),
      ('L',180),
      ('F',54),
      ('L',90),
      ('N',3),
      ('F',3),
      ('W',5),
      ('R',180),
      ('S',4),
      ('L',90),
      ('F',49),
      ('W',4),
      ('S',5),
      ('F',73),
      ('L',270),
      ('W',1),
      ('S',4),
      ('F',46),
      ('S',4),
      ('W',2),
      ('S',5),
      ('E',4),
      ('N',4),
      ('F',6),
      ('E',4),
      ('S',4),
      ('F',38),
      ('F',4),
      ('E',4),
      ('R',90),
      ('N',1),
      ('W',2),
      ('F',20),
      ('N',3),
      ('F',64),
      ('R',90),
      ('S',3),
      ('W',5),
      ('N',1),
      ('W',4),
      ('N',3),
      ('F',17),
      ('R',90),
      ('F',62),
      ('E',4),
      ('E',2),
      ('F',47),
      ('R',90),
      ('W',1),
      ('N',3),
      ('R',90),
      ('N',2),
      ('R',90),
      ('F',57),
      ('L',270),
      ('N',2),
      ('W',3),
      ('S',5),
      ('W',4),
      ('E',2),
      ('S',5),
      ('F',93),
      ('F',57),
      ('S',1),
      ('L',90),
      ('F',50),
      ('N',2),
      ('F',4),
      ('N',1),
      ('L',90),
      ('F',34),
      ('N',2),
      ('L',90),
      ('N',4),
      ('W',3),
      ('N',5),
      ('R',180),
      ('S',3),
      ('L',90),
      ('W',3),
      ('S',3),
      ('L',90),
      ('F',70),
      ('L',90),
      ('E',1),
      ('F',92),
      ('N',1),
      ('F',96),
      ('F',85),
      ('S',5),
      ('L',90),
      ('W',1),
      ('L',90),
      ('W',1),
      ('F',23),
      ('L',90),
      ('S',1),
      ('R',90),
      ('W',5),
      ('S',5),
      ('F',66),
      ('W',3),
      ('L',180),
      ('W',2),
      ('L',90),
      ('N',2),
      ('E',3),
      ('R',270),
      ('R',270),
      ('N',3),
      ('W',5),
      ('R',90),
      ('S',3),
      ('E',1),
      ('R',90),
      ('F',78),
      ('E',1),
      ('S',1),
      ('R',90),
      ('S',3),
      ('F',52),
      ('S',4),
      ('F',9),
      ('L',90),
      ('W',1),
      ('N',2),
      ('F',8),
      ('R',90),
      ('N',1),
      ('F',63),
      ('E',5),
      ('F',18),
      ('E',3),
      ('F',43),
      ('E',2),
      ('F',10),
      ('R',90),
      ('F',96),
      ('S',5),
      ('F',22),
      ('W',2),
      ('S',5),
      ('F',39),
      ('R',90),
      ('F',38),
      ('S',5),
      ('R',90),
      ('E',3),
      ('L',90),
      ('W',3),
      ('N',2),
      ('F',14),
      ('L',270),
      ('S',4),
      ('F',78),
      ('F',85),
      ('L',90),
      ('N',3),
      ('E',3),
      ('S',3),
      ('F',98),
      ('E',2),
      ('S',2),
      ('F',100),
      ('S',3),
      ('S',3),
      ('W',5),
      ('W',3),
      ('S',5),
      ('F',67),
      ('L',180),
      ('S',2),
      ('E',5),
      ('S',1),
      ('L',90),
      ('N',5),
      ('E',2),
      ('W',2),
      ('R',90),
      ('E',1),
      ('N',2),
      ('L',90),
      ('F',77),
      ('W',1),
      ('F',84),
      ('L',90),
      ('S',2),
      ('E',4),
      ('R',90),
      ('E',1),
      ('R',90),
      ('S',3),
      ('S',4),
      ('F',89),
      ('R',90),
      ('N',1),
      ('E',4),
      ('R',90),
      ('N',1),
      ('F',97),
      ('L',90),
      ('S',1),
      ('W',3),
      ('R',180),
      ('F',70),
      ('S',5),
      ('E',1),
      ('L',180),
      ('W',5),
      ('F',86),
      ('S',3),
      ('F',20),
      ('R',90),
      ('S',1),
      ('W',4),
      ('R',90),
      ('W',1),
      ('F',3),
      ('S',3),
      ('R',90),
      ('F',43),
      ('L',180),
      ('F',81),
      ('E',2),
      ('N',3),
      ('F',16),
      ('L',90),
      ('S',2),
      ('F',17),
      ('E',3),
      ('F',1),
      ('E',4),
      ('F',17),
      ('W',3),
      ('N',3),
      ('W',5),
      ('S',3),
      ('W',4),
      ('F',60),
      ('E',3),
      ('E',1),
      ('S',5),
      ('L',90),
      ('E',2),
      ('S',5),
      ('F',19),
      ('E',2),
      ('R',90),
      ('F',20),
      ('R',180),
      ('S',4),
      ('F',9),
      ('R',90),
      ('N',5),
      ('W',5),
      ('F',56),
      ('N',2),
      ('L',180),
      ('N',1),
      ('E',5),
      ('L',90),
      ('F',15),
      ('W',4),
      ('F',26),
      ('R',90),
      ('W',2),
      ('F',19),
      ('S',3),
      ('W',1),
      ('R',90),
      ('W',5),
      ('R',180),
      ('W',4),
      ('N',2),
      ('F',86),
      ('N',5),
      ('E',3),
      ('W',3),
      ('N',3),
      ('L',270),
      ('W',3),
      ('F',42),
      ('N',5),
      ('W',2),
      ('R',180),
      ('W',2),
      ('R',180),
      ('S',4),
      ('R',90),
      ('F',55),
      ('S',3),
      ('R',90),
      ('S',3),
      ('E',3),
      ('R',90),
      ('F',11),
      ('S',4),
      ('F',38),
      ('W',1),
      ('L',90),
      ('F',8),
      ('R',90),
      ('E',5),
      ('R',90),
      ('W',1),
      ('W',5),
      ('S',2),
      ('F',2),
      ('F',92),
      ('S',3),
      ('F',77),
      ('S',5),
      ('R',90),
      ('F',24),
      ('E',3),
      ('R',90),
      ('N',3),
      ('F',16),
      ('L',270),
      ('W',3),
      ('F',83),
      ('L',270),
      ('E',2),
      ('F',98),
      ('L',180),
      ('F',89),
      ('E',5),
      ('F',98),
      ('S',4),
      ('E',2),
      ('L',90),
      ('N',4),
      ('L',180),
      ('F',57),
      ('S',5),
      ('R',90),
      ('L',90),
      ('S',4),
      ('W',4),
      ('S',5),
      ('S',4),
      ('W',4),
      ('F',43),
      ('N',2),
      ('F',29),
      ('W',3),
      ('R',90),
      ('F',41),
      ('R',90),
      ('N',2),
      ('F',78),
      ('R',90),
      ('E',5),
      ('N',1),
      ('W',2),
      ('F',6),
      ('L',270),
      ('W',5),
      ('F',91),
      ('W',5),
      ('N',1),
      ('S',4),
      ('F',41),
      ('W',4),
      ('F',74),
      ('E',1),
      ('R',90),
      ('N',4),
      ('F',76),
      ('W',4),
      ('S',2),
      ('L',180),
      ('N',2),
      ('R',180),
      ('W',4),
      ('F',79),
      ('R',270),
      ('W',1),
      ('F',92),
      ('W',1),
      ('L',90),
      ('F',71),
      ('N',4),
      ('L',180),
      ('W',4),
      ('F',16),
      ('W',5),
      ('F',84),
      ('S',5),
      ('F',35),
      ('W',4),
      ('R',90),
      ('F',25),
      ('L',180),
      ('N',1),
      ('E',3),
      ('F',15),
      ('S',4),
      ('R',180),
      ('F',46),
      ('S',1),
      ('W',1),
      ('R',180),
      ('E',4),
      ('N',5),
      ('R',90),
      ('S',1),
      ('W',3),
      ('S',3),
      ('L',270),
      ('F',94),
      ('R',180),
      ('N',1),
      ('W',4),
      ('N',5),
      ('W',2),
      ('S',2),
      ('W',3),
      ('F',53),
      ('L',180),
      ('S',3),
      ('F',19),
      ('N',3),
      ('F',54),
      ('L',180),
      ('S',5),
      ('F',8),
      ('S',1),
      ('N',5),
      ('L',90),
      ('E',4),
      ('N',3),
      ('F',28),
      ('R',180),
      ('F',23),
      ('E',1),
      ('L',90),
      ('E',3),
      ('F',6),
      ('W',4),
      ('R',90),
      ('N',1),
      ('F',89),
      ('S',1),
      ('W',2),
      ('S',5),
      ('F',8),
      ('N',3),
      ('F',23),
      ('N',4),
      ('F',5),
      ('L',90),
      ('N',3),
      ('R',90),
      ('W',4),
      ('L',180),
      ('S',3),
      ('F',7),
      ('N',2),
      ('W',3),
      ('R',180),
      ('E',1),
      ('L',180),
      ('S',4),
      ('R',90),
      ('S',1),
      ('F',99),
      ('N',3),
      ('F',96),
      ('W',3),
      ('R',90),
      ('F',73),
      ('W',5),
      ('F',71),
      ('R',180),
      ('S',2),
      ('F',84),
      ('N',4),
      ('F',4),
      ('W',4),
      ('R',90),
      ('F',34),
      ('E',2),
      ('W',2),
      ('F',53),
      ('N',4),
      ('R',90),
      ('N',5),
      ('E',5),
      ('R',90),
      ('F',60),
      ('N',4),
      ('F',28),
      ('S',2),
      ('W',1),
      ('N',4),
      ('F',54),
      ('R',270),
      ('F',45),
      ('S',5),
      ('F',93),
      ('L',90),
      ('F',66),
      ('R',180),
      ('F',92),
      ('N',4),
      ('F',97),
      ('R',90),
      ('W',5),
      ('S',1),
      ('W',5),
      ('F',68),
      ('S',3),
      ('L',90),
      ('E',3),
      ('F',94),
      ('S',4),
      ('F',64),
      ('R',180),
      ('F',18),
      ('N',1),
      ('S',4),
      ('E',5),
      ('E',2),
      ('F',81),
      ('N',1),
      ('L',90),
      ('F',3),
      ('R',90),
      ('F',81),
      ('W',4),
      ('S',4),
      ('E',5),
      ('N',5),
      ('R',270),
      ('E',3),
      ('S',2),
      ('W',1),
      ('L',180),
      ('S',1),
      ('F',84),
      ('W',2),
      ('L',270),
      ('F',6),
      ('N',1),
      ('R',180),
      ('E',5),
      ('F',7),
      ('E',2),
      ('L',180),
      ('E',2),
      ('F',80),
      ('N',1),
      ('L',90),
      ('F',88),
      ('R',90),
      ('W',5),
      ('N',1),
      ('F',71),
      ('R',180),
      ('N',2),
      ('E',2),
      ('R',90),
      ('N',1),
      ('W',1),
      ('L',90),
      ('E',4),
      ('S',4),
      ('L',180),
      ('F',27),
      ('L',90),
      ('F',57),
      ('F',38),
      ('W',5),
      ('L',180),
      ('S',5),
      ('R',90),
      ('S',4),
      ('W',1),
      ('S',3),
      ('L',90),
      ('F',36),
      ('S',1),
      ('W',5),
      ('R',90),
      ('F',65),
      ('R',90),
      ('E',1),
      ('N',4),
      ('E',1),
      ('F',14),
      ('L',90),
      ('F',44),
      ('R',90),
      ('F',34),
      ('S',2),
      ('L',90),
      ('R',180),
      ('F',87),
      ('W',3),
      ('L',90),
      ('F',9),
      ('R',90),
      ('W',3),
      ('L',90),
      ('S',5),
      ('F',69),
      ('S',3),
      ('W',4),
      ('N',4),
      ('F',30),
      ('W',5),
      ('F',15),
      ('R',90),
      ('L',180),
      ('W',4),
      ('F',5),
      ('R',180),
      ('E',1),
      ('F',6),
      ('R',180),
      ('S',1),
      ('F',20),
      ('E',1),
      ('S',2),
      ('E',5),
      ('F',13),
      ('N',5),
      ('F',83),
      ('W',2),
      ('L',270),
      ('E',2),
      ('R',90),
      ('S',5),
      ('F',62),
      ('R',270),
      ('N',4),
      ('R',90),
      ('F',20),
      ('L',90),
      ('N',2),
      ('E',3),
      ('L',90),
      ('F',37),
      ('N',2),
      ('N',2),
      ('F',82),
      ('L',90),
      ('F',23),
      ('E',3),
      ('F',63),
      ('R',180),
      ('F',1),
      ('N',2),
      ('R',90),
      ('F',68),
      ('E',5),
      ('F',75),
      ('R',90),
      ('W',3),
      ('R',180),
      ('E',4),
      ('E',1),
      ('N',3),
      ('R',90),
      ('N',3),
      ('L',180),
      ('F',92),
      ('R',90),
      ('S',4),
      ('F',27),
      ('R',180),
      ('S',4),
      ('L',180),
      ('W',5),
      ('F',70),
      ('S',5),
      ('L',180),
      ('F',89),
      ('R',90),
      ('W',2),
      ('N',3),
      ('F',64),
      ('L',90),
      ('E',1),
      ('L',90),
      ('F',77),
      ('E',4),
      ('F',55),
      ('E',2),
      ('L',90),
      ('W',2),
      ('F',46),
      ('N',2),
      ('R',90),
      ('F',94),
      ('S',5),
      ('R',180),
      ('F',9),
      ('L',180),
      ('S',4),
      ('L',90),
      ('F',25), ] 
