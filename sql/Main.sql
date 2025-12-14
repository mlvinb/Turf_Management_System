CREATE DATABASE turf_management;
USE turf_management;

CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(50)
);

CREATE TABLE turf (
    turf_id INT AUTO_INCREMENT PRIMARY KEY,
    turf_name VARCHAR(50),
    location VARCHAR(100),
    price_per_hour DECIMAL(10,2),
    turf_type VARCHAR(30),
    availability VARCHAR(20)
);

CREATE TABLE booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    turf_id INT,
    date DATE,
    start_time TIME,
    end_time TIME,
    status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (turf_id) REFERENCES turf(turf_id)
);
