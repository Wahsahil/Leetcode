# Write your MySQL query statement below
select t.request_at as 'Day',
round(SUM(
    CASE
        WHEN status IN ('cancelled_by_driver', 'cancelled_by_client')
        THEN 1
        ELSE 0
    END
)/count(*) ,2) as 'Cancellation Rate'
from Trips t
join Users u
on t.client_id = u.users_id 
join Users u1
on t.driver_id = u1.users_id
where u.banned = 'No'
and u1.banned = 'No'
and t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at