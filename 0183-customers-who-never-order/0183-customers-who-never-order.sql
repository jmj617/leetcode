# Write your MySQL query statement below
select
    c.name as Customers
from
    Orders as o
right join Customers as c
    on o.customerId = c.id
where
    o.customerId is NULL;