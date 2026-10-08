# Write your MySQL query statement below
select b.book_id ,b.title,b.author,b.genre,b.publication_year , sum(case when bo.return_date is null then 1 else 0 end) as current_borrowers
from library_books b
join borrowing_records bo
 on b.book_id = bo.book_id
group by b.book_id,b.title,b.author,b.genre, b.publication_year,b.total_copies
HAVING sum(case when bo.return_date is null then 1 else 0 end) = b.total_copies
order by current_borrowers DESC, b.title ASC;