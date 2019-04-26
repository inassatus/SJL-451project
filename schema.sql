CREATE TABLE businessTable(
	business_id varchar(50) primary key,
	name varchar(256),
	address varchar(256),
	city varchar(50),
	state varchar(50),
	zipcode int,
	latitude real,
	longitude real,
	stars float(5),
	reviewrating real,
	reviewcount int,
	numCheckins int,
	openStatus boolean
);

CREATE TABLE category(
	business_id varchar(50) not null,
	name varchar(50),
	primary key(business_id, name),
	foreign key(business_id) REFERENCES businessTable(business_id)
);
CREATE TABLE attribute(
	business_id varchar(50) not null,
	name varchar(50),
	value text,
	primary key(business_id, name),
	foreign key(business_id) REFERENCES businessTable(business_id)
);
CREATE TABLE hours(
	business_id varchar(50) not null,
	day varchar(10),
	open varchar(5),
	close varchar(5),
	foreign key(business_id) REFERENCES businessTable(business_id)
);
CREATE TABLE checkins(
	business_id varchar(50) not null,
	day varchar(10),
	count int,
	time varchar(5),
	foreign key(business_id) REFERENCES businessTable(business_id)
);

CREATE TABLE userTable(
	user_id varchar(50) primary key,
	name varchar(50),
	stars float(5),
	cool int,
	funny int,
	useful int,
	fans int,
	reviewcount int,
	since varchar(32)
);

CREATE TABLE favorite(
	user_id varchar(50) primary key,
	business_id varchar(50),
	foreign key(user_id) REFERENCES userTable(user_id),
	foreign key(business_id) REFERENCES businessTable(business_id)
);

CREATE TABLE friend(
	user_id varchar(50) not null,
	friend_id varchar(50) not null,
	primary key(user_id, friend_id),
	foreign key(user_id) REFERENCES userTable(user_id)
);

CREATE TABLE review(
	review_id varchar(50) not null,
	user_id varchar(50) not null,
	business_id varchar(50),
	stars float(5),
	date varchar(32),
	text text,
	useful int,
	funny int,
	cool int,
		foreign key(business_id) REFERENCES businessTable(business_id),
		foreign key(user_id) REFERENCES userTable(user_id)
);