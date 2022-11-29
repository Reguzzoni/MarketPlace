// create database python
create database python;

// create schema marketplace
create schema marketplace;

// create table market_data into schema marketplace
create table "marketplace".market_data (
	mkt_data_id serial,
	value int
);
