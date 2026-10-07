# Write your MySQL query statement below
DELETE p2
FROM person p1 JOIN person p2
ON p1.Email = p2.Email
AND p1.Id < p2.Id
