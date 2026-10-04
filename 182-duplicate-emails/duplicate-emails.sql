# Write your MySQL query statement below
select email Email
from person
group by email having count(email)>1;