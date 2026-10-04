# Write your MySQL query statement below
select p.firstname,p.lastName,s.city,s.state
from person p
LEFT JOIN address s
on p.personId = s.personId;