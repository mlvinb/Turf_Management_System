-- 1. View all available turfs

SELECT turf_id, turf_name, location, price_per_hour
FROM turf
WHERE availability = 'Available';


-- 2. Find bookings for a specific date

SELECT b.booking_id, u.name, t.turf_name, b.start_time, b.end_time
FROM booking b
JOIN users u ON b.user_id = u.user_id
JOIN turf t ON b.turf_id = t.turf_id
WHERE b.date = '2025-01-10';


-- 3. Check if a turf is already booked for a time slot

SELECT *
FROM booking
WHERE turf_id = 1
  AND date = '2025-01-10'
  AND (
      start_time < '18:00:00'
      AND end_time > '16:00:00'
  );


-- 4. Count total bookings per turf

SELECT t.turf_name, COUNT(b.booking_id) AS total_bookings
FROM turf t
LEFT JOIN booking b ON t.turf_id = b.turf_id
GROUP BY t.turf_name;


-- 5. Find the most booked turf

SELECT t.turf_name, COUNT(b.booking_id) AS bookings
FROM turf t
JOIN booking b ON t.turf_id = b.turf_id
GROUP BY t.turf_name
ORDER BY bookings DESC
LIMIT 1;


-- 6. List users who have made more than one booking

SELECT u.name, COUNT(b.booking_id) AS booking_count
FROM users u
JOIN booking b ON u.user_id = b.user_id
GROUP BY u.user_id
HAVING booking_count > 1;


-- 7. Calculate total revenue per turf

SELECT t.turf_name,
       SUM(
           TIMESTAMPDIFF(HOUR, b.start_time, b.end_time) * t.price_per_hour
       ) AS total_revenue
FROM booking b
JOIN turf t ON b.turf_id = t.turf_id
GROUP BY t.turf_name;


-- 8. View all bookings with status "Booked”

SELECT booking_id, user_id, turf_id, date, start_time, end_time
FROM booking
WHERE status = 'Booked';


-- 9. Find users who never made a booking

SELECT u.name, u.email
FROM users u
LEFT JOIN booking b ON u.user_id = b.user_id
WHERE b.booking_id IS NULL;


-- 10. Daily booking count

SELECT date, COUNT(*) AS total_bookings
FROM booking
GROUP BY date
ORDER BY date;
