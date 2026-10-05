select id , (case 
when p_id is null then 'Root'  
WHEN id IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Inner'
else 'Leaf' 
end
) as type
from Tree