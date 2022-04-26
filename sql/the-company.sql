--https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
WITH numbers AS (
    SELECT Company.company_code, COUNT(DISTINCT Lead_Manager.lead_manager_code) AS lm, COUNT(DISTINCT Senior_Manager.senior_manager_code) AS sm, COUNT(DISTINCT Manager.manager_code) AS m, COUNT(DISTINCT Employee.employee_code) AS e
    FROM Company, Lead_Manager, Senior_Manager, Manager, Employee
    WHERE Company.company_code = Lead_Manager.company_code AND Lead_Manager.company_code = Senior_Manager.company_code AND Company.company_code = Manager.company_code AND Company.company_code = Employee.company_code
    GROUP BY Company.company_code
)
SELECT Company.company_code, Company.founder, numbers.lm, numbers.sm, numbers.m, numbers.e
from numbers
JOIN Company ON numbers.company_code = Company.company_code
ORDER BY Company.company_code ASC;
