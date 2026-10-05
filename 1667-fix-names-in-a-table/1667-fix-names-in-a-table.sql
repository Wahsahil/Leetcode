select user_id, concat(UPPER (left(name,1)), LOWER(substring(name,2))) as name
from Users
order by user_id