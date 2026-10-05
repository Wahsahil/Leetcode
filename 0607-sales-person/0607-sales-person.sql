select s.name
from SalesPerson s
where s.sales_id not in ( 
    select o.sales_id from Orders o join company c
    ON o.com_id = c.com_id
    WHERE c.name = 'RED'    
)
