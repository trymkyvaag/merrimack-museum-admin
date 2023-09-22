LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/artwork.csv'
INTO TABLE artwork
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(title, date_created, width, comments, height);

select * from artwork