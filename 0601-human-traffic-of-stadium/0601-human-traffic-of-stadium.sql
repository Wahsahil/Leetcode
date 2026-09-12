SELECT id, visit_date, people
FROM Stadium
WHERE id IN (
    SELECT id
    FROM (
        SELECT
            id,
            people,
            LAG(people, 1) OVER (ORDER BY id) AS prev1,
            LAG(people, 2) OVER (ORDER BY id) AS prev2,
            LEAD(people, 1) OVER (ORDER BY id) AS next1,
            LEAD(people, 2) OVER (ORDER BY id) AS next2
        FROM Stadium
    ) x
    WHERE people >= 100
      AND (
          (prev1 >= 100 AND prev2 >= 100)
          OR
          (prev1 >= 100 AND next1 >= 100)
          OR
          (next1 >= 100 AND next2 >= 100)
      )
)
ORDER BY visit_date;