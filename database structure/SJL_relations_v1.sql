Create Table user(
	uid int primary key
	uname varchar(255) not null
	location varchar(255) not null
	uvote int
	nfan int
	joined date
	ave float
	friendlist text
	friend int foreign key references user(friend)
);

Create Table business(
	bname varchar(255) primary key
	rating float
	baddress varchar(255) not null
	checkin int
	nreview int
	bcategory varchar(255)
);

Create Table review(
	rid int primary key
	uname varchar(255)
	bname varchar(255)
	rtext text not null
	created date not null
	nstar int
	rating float
);

Create Table checkindata(
	selected_time date primary key
	selected_business varchar(255) not null 
	count int
);