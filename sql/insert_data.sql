INSERT INTO admin (username, password)
VALUES
('admin', 'admin123'),
('manager', 'manager123');


INSERT INTO users (name, email, password)
VALUES
('Arjun Nair', 'arjun@gmail.com', 'arjun123'),
('Rahul Menon', 'rahul@gmail.com', 'rahul123'),
('Anjali Thomas', 'anjali@gmail.com', 'anjali123');


INSERT INTO turf (turf_name, location, price_per_hour, turf_type, availability)
VALUES
('Green Arena', 'Kochi', 1200.00, 'Football', 'Available'),
('Sky Sports Turf', 'Trivandrum', 1000.00, 'Cricket', 'Available'),
('PlayZone Arena', 'Calicut', 1500.00, 'Football', 'Available'),
('Urban Sports Hub', 'Thrissur', 900.00, 'Badminton', 'Available');

INSERT INTO booking (user_id, turf_id, date, start_time, end_time, status)
VALUES
(1, 1, '2025-01-10', '17:00:00', '18:00:00', 'Booked'),
(2, 2, '2025-01-10', '18:00:00', '20:00:00', 'Booked'),
(3, 3, '2025-01-11', '16:00:00', '17:00:00', 'Booked');