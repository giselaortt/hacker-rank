--https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
with kids as ( 
    SELECT BST1.N, BST1.P, BST2.N AS SON
    FROM BST AS BST1 LEFT JOIN BST AS BST2 ON BST1.N = BST2.P
)
SELECT DISTINCT N, (
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN SON IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END
    )
FROM kids
ORDER BY N;
