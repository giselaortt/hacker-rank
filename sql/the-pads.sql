--https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true
SELECT CONCAT(name,'(',SUBSTRING(Occupation,1,1),')')
FROM occupations
ORDER BY name;
SELECT CONCAT('There are a total of ',COUNT(1),' ',lower(occupation),'s.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(1) ASC, Occupation ASC;
