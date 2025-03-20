-- Create the database and switch to it
CREATE DATABASE IF NOT EXISTS train;
USE train;

-- Create the accounts table
CREATE TABLE IF NOT EXISTS accounts (
    Mobile VARCHAR(15),
    Email VARCHAR(100),
    Username VARCHAR(20),
    Password VARCHAR(20),
    Name VARCHAR(50),
    DOB VARCHAR(20),
    Gender VARCHAR(20),
    Nationality VARCHAR(50),
    Address VARCHAR(100),
    PIN VARCHAR(10)
);

-- Create the trains table
CREATE TABLE IF NOT EXISTS trains (
    No VARCHAR(10),
    Name VARCHAR(100),
    Source VARCHAR(50),
    Destination VARCHAR(50),
    2S VARCHAR(10),
    SL VARCHAR(10),
    AC VARCHAR(10),
    Deparature VARCHAR(20),
    Arrival VARCHAR(20)
);

-- Create the tickets table
CREATE TABLE IF NOT EXISTS tickets (
    Name VARCHAR(100),
    Age VARCHAR(10),
    Gender VARCHAR(50),
    Nationality VARCHAR(50),
    Fare VARCHAR(20),
    TransId VARCHAR(50),
    PNR VARCHAR(50),
    Train VARCHAR(100),
    No VARCHAR(10),
    Date VARCHAR(20),
    Deparature VARCHAR(20),
    Arrival VARCHAR(20),
    Source VARCHAR(50),
    Destination VARCHAR(50),
    Passengers VARCHAR(10),
    Class VARCHAR(10),
    Berth VARCHAR(10),
    Mode VARCHAR(50),
    TransDate VARCHAR(100),
    TransTime VARCHAR(100)
);

-- Create the cancels table
CREATE TABLE IF NOT EXISTS cancels (
    Train VARCHAR(100),
    No VARCHAR(10),
    TransId VARCHAR(50),
    TransDate VARCHAR(100),
    Source VARCHAR(50),
    Destination VARCHAR(50),
    CancelDate VARCHAR(100),
    PNR VARCHAR(50),
    CancelId VARCHAR(50),
    Refund VARCHAR(20),
    Deducted VARCHAR(20)
);