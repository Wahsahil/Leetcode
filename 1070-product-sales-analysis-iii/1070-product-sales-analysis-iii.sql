with x as (select *, rank() over(partition by product_id order by year) as rnk from Sales)
select product_id , year as first_year, quantity,price from x
where rnk = 1
