WITH x AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
y AS (
    SELECT
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM x
)

SELECT id, visit_date, people
FROM y
WHERE cnt >= 3
ORDER BY visit_date;