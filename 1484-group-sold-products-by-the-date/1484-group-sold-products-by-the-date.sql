select sell_date, count(distinct(product)) as num_sold, Group_concat(Distinct product order by product asc) as products
from Activities
group by sell_date
order by sell_date;