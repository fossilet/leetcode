SELECT
  p.FirstName AS FirstName,
  p.LastName  AS LastName,
  a.City      AS City,
  a.State     AS State
FROM Person AS p LEFT JOIN Address AS a ON p.PersonId = a.PersonId
