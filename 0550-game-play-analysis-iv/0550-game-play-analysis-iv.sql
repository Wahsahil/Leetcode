with x as (
    select player_id, event_date,
        MIN(event_date) Over( partition by player_id) as first_login,
        LEAD(event_date, 1) over(partition by player_id order by event_date) as next_login
    from Activity
)
Select ROUND(COUNT(DISTINCT CASE WHEN DATEDIFF(next_login,event_date) = 1 and event_date = first_login THEN player_id END) / COUNT(DISTINCT player_id), 2) as fraction
FROM x;