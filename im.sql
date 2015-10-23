CREATE TABLE Countries 
(

	id SMALLINT UNSIGNED,
	alpha2 VARCHAR(2),
	alpha3 VARCHAR(3),
	name VARCHAR(64),
	targetable TINYINT(1),
	CONSTRAINT pk_country PRIMARY KEY (id)

);

CREATE TABLE Regions
(

	id SMALLINT UNSIGNED,
	country_id SMALLINT UNSIGNED,
	name VARCHAR(64),
	iso_code VARCHAR(4),
	CONSTRAINT pk_region PRIMARY KEY (id),
	CONSTRAINT fk_region_country_id FOREIGN KEY (country_id) REFERENCES Countries (id)

);

CREATE TABLE Cities
(
	
	id SMALLINT UNSIGNED,
	country_id SMALLINT UNSIGNED NULL,
	region_id SMALLINT UNSIGNED NULL,
	name VARCHAR(64),
	iso_code VARCHAR(4),
	CONSTRAINT pk_city PRIMARY KEY (id),
	CONSTRAINT fk_city_country_id FOREIGN KEY (country_id) REFERENCES Countries (id)

);

LOAD DATA LOCAL INFILE "/Users/aaron/projects/IM/data/countries"
INTO TABLE Countries
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE "/Users/aaron/projects/IM/data/regions.csv"
INTO TABLE Regions
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA LOCAL INFILE "/Users/aaron/projects/IM/data/cities.csv"
INTO TABLE Cities
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

create user guest identified by *********;

grant select on IM.* to guest;