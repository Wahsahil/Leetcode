with x as (
    select id , num,
    lag(num,1) over(order by id) as pre1,
    lag(num,2) over(order by id) as pre2
    from logs
)
select distinct(num) as ConsecutiveNums
from x
where num = pre1 and pre1 = pre2