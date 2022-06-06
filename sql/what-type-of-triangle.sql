--https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true

SELECT (CASE
	    -- I know a triangle of zero aea is not a triangle, but the exercise is malformed.
            WHEN a+b+c <= 2*GREATEST(a,b,c) THEN 'Not A Triangle'
            WHEN a = b AND b = c THEN 'Equilateral'
            WHEN a = b OR a = c OR a = b THEN 'Isosceles'
            WHEN a <> b AND a <> c AND b <> c THEN 'Scalene'
        END)
FROM triangles;
