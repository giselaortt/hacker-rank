--https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
WITH mysalary AS (
    SELECT name, students.id, pkg.salary AS salary, friend_id, p.salary AS bff_salary
    FROM students
    JOIN packages AS pkg ON students.id = pkg.id
    LEFT JOIN friends ON friends.id = students.id
    LEFT JOIN packages AS p ON p.id = friends.friend_id
)
SELECT name
FROM mysalary
WHERE bff_salary > salary
ORDER BY bff_salary;
