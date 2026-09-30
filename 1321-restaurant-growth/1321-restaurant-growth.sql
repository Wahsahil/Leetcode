select c.visited_on , sum(c2.daily_amount) as amount,  round(avg(c2.daily_amount),2) as average_amount
from (select visited_on,sum(amount) as daily_amount from Customer group by visited_on)  c  
join 
(
    select visited_on,sum(amount) as daily_amount
    from Customer
    group by visited_on
)  c2
on
c2.visited_on between date_sub(c.visited_on,Interval 6 day) and c.visited_on                  
group by c.visited_on
having count(*)=7
order by c.visited_on      