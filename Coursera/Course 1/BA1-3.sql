--Trying to get the total supplies of some 
--candy during 2019 year grouped by name:

SELECT candy_name, SUM(q_ty) FROM supply
GROUP BY candy_name
HAVING date between 01.01.2019 AND 01.01.2020

--Trying to get the summary sales (candy quantity) 
--for each candy shop grouped by date:

SELECT location, date, SUM(q_ty)
FROM slaes AS SL LEFT JOIN candy_shop AS CS
ON SL.candy_shop_ID=CS.candy_shop_ID
GROUP BY location, date
ORDER BY location DESC

