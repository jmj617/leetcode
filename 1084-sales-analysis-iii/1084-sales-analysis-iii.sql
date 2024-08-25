# Write your MySQL query statement below
select
    DISTINCT p.product_id,
    p.product_name
from
    Sales as s
left join Product as p
on s.product_id = p.product_id
where
    s.product_id not in (
        select s.product_id 
        from Sales as s 
        where 
            s.sale_date > '2019-03-31' or
            s.sale_date < '2019-01-01')
    