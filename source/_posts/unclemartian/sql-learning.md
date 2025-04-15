---
title: 【Tech】 SQL learning notes
category: unknown
tags: technology
comments: true
date: 2015-09-20 00:00:00
---


Raw data: 

	drop table Frequents;
	drop table Sells;
	drop table Likes;
	drop table Drinkers;
	drop table Bars;
	drop table Beers;

	create table Beers (
		name varchar(50),
		manf varchar(100),
		primary key (name)
	);

	create table Bars (
		name varchar(50),
		addr varchar(100),
		primary key (name)
	);

	create table Drinkers (
		name varchar(50),
		addr varchar(100),
		phone int,
		primary key (name)
	);

	create table Likes (
		drinker varchar(50),
		beer varchar(50),
		primary key (drinker, beer)
	);

	create table Sells (
		bar varchar(50),
		beer varchar(50),
		price float
	);

	create table Frequents (
		drinker varchar(50),
		bar varchar(50)
	);

	Insert into Beers values('erdinger', 'Germany');
	Insert into Beers values('corona', 'Mexico');
	Insert into Beers values('heineken', 'Netherland');
	Insert into Beers values('guinness', 'Ireland');
	Insert into Beers values('stella artois', 'Belgium');
	Insert into Beers values('qingtao', '');
	Insert into Beers values('harbin', NULL);
	Insert into Beers values('franziskaner', 'Germany');

	Insert into Bars values('familiar', '1st road');
	Insert into Bars values('mermaid', '2nd avn');
	Insert into Bars values('beehive', '3rd cresent');
	Insert into Bars values('worldsend', '4th bolvd');

	Insert into Drinkers values('zhang', 'ntu', 9079878);
	Insert into Drinkers values('wang', 'nus', 2345345);
	Insert into Drinkers values('li', 'smu', 45345);
	Insert into Drinkers values('zhao', 'sutd', 5643565);

	Insert into Likes values('zhang', 'corona');
	Insert into Likes values('zhang', 'heineken');
	Insert into Likes values('wang', 'guinness');
	Insert into Likes values('wang', 'heineken');
	Insert into Likes values('li', 'heineken');
	Insert into Likes values('zhao', 'stella artois');

	Insert into Sells values('familiar', 'erdinger', 12);
	Insert into Sells values('familiar', 'corona', 22);
	Insert into Sells values('familiar', 'heineken', 14);
	Insert into Sells values('mermaid', 'erdinger', 24);
	Insert into Sells values('mermaid', 'corona', 12);
	Insert into Sells values('mermaid', 'guinness', 21);
	Insert into Sells values('beehive', 'corona', 19);
	Insert into Sells values('beehive', 'heineken', 29);
	Insert into Sells values('beehive', 'guinness', 19);
	Insert into Sells values('beehive', 'stella artois', 9);
	Insert into Sells values('worldsend', 'erdinger', 22);
	Insert into Sells values('worldsend', 'corona', NULL);

	Insert into Frequents values('zhang', 'familiar');
	Insert into Frequents values('zhang', 'mermaid');
	Insert into Frequents values('wang', 'beehive');
	Insert into Frequents values('li', 'familiar');
	Insert into Frequents values('li', 'beehive');
	Insert into Frequents values('zhao', 'familiar');
	Insert into Frequents values('zhao', 'beehive');
	Insert into Frequents values('zhao', 'worldsend');

	select * from Beers;
	select * from Bars;
	select * from Drinkers;
	select * from Likes;
	select * from Sells;
	select * from Frequents;

# Test 1

Now using the raw data, write these queries: 

-- select beer with empty or NULL manf



-- find the beer liked by >=1 person who frequents 'familiar'




-- find pairs of beer from same manf




-- first, find out the price of 'guinness' sold at 'beehive'
-- then, find all beers at any bar sold at the same price





-- find the name and manf of each beer that 'zhang' likes
-- try to use the 'in' keyword









-- find the beer sold for the highest price
-- try to use the 'all' keyword








-- find beers that are the only beer by their manufacturer
-- try to use the 'exists' keyword





-- find the drinkers and beers pairs that:
-- 1. drinker likes the beer
-- 1. drinker frequents at least 1 bar that sells the beer





-- find all prices charged for 'corona'



-- count number of bars that sells 'corona'



-- count number of bars that sells 'corona' at known price



-- count number of different prices charged for 'corona' at bars



-- calculate average price of each beer



-- find for each drinker, the average price of 'corona'
-- at the bars that they frequent



# Test 2


-- find average price of those beer that are either served
-- in >= 3 bars, or are manufactured by 'Netherland'

-- delete all bears for which there's another beer by the same manufacturer

Hint: 

	DELETE B FROM beers B WHERE

-- first, add foreign key to table Sells, which references to the beer name
-- second, delete any beer except 'corona', and see what happens to Sells

-- recreate the Sells table, so that price is always < $30(user CHECK keyword)

-- recreate the Sells table, so that only 'familiar' can sell beer less than $10 (user CHECK keyword)

-- create a view of your choice and explain what it does. 


