-- https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true

WITH dots AS (
SELECT MAX(LAT_N) AS b, MIN(LAT_N) AS a, MAX(LONG_W) AS d, MIN(LONG_W) AS c
FROM station
)
SELECT ROUND(SQRT((a-b)*(a-b) + (c-d)*(c-d)),4)
FROM dots
