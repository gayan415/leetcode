-- https://leetcode.com/problems/combine-two-tables/

SELECT
	Person.FirstName,
	Person.LastName,
	Address.City,
	Address.State
FROM Person
LEFT JOIN Address ON Address.PersonId = Person.PersonId
