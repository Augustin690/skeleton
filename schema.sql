PRAGMA foreign_keys = ON;

CREATE TABLE People(id INTEGER PRIMARY KEY,first_name VARCHAR,last_name VARCHAR, address VARCHAR, phone_nb VARCHAR);

CREATE TABLE Course(id INTEGER PRIMARY KEY, name VARCHAR, teacher VARCHAR);

CREATE TABLE Room(id INTEGER PRIMARY KEY, name Varchar, capacity INT);

CREATE TABLE Curriculum(id INTEGER PRIMARY KEY, name VARCHAR, secretary VARCHAR, director VARCHAR);

CREATE TABLE Reservation(course INT,room INT,start_date DATE, start_time TIME, end_date DATE, end_time TIME);

CREATE TABLE Registration(people INT, curriculum INT);

CREATE TABLE Credit(curriculum INT,course INT, ECTS INT);
