-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

SELECT
  FirstName AS '이름'
FROM
  employees;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;


-- 02. Sorting data
SELECT
  FirstName
FROM
   employees
ORDER BY
  FirstName;

SELECT
  FirstName
FROM
   employees
ORDER BY
  FirstName DESC; -- 내림차순

SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City ASC;

SELECT
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;


-- NULL 정렬 예시
SELECT
  ReportsTo
From
  employees
ORDER BY
  ReportsTo DESC;


-- 03. Filtering data
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  Name, Bytes
FROM 
  tracks
WHERE
  -- Bytes >= 100000
  -- AND Bytes <= 500000;
  Bytes BETWEEN 100000 AND 500000;

SELECT
  Name, Bytes
FROM 
  tracks
WHERE   -- WHERE절 이후 정렬 !!
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son'; -- 끝이 son으로 끝나는 데이터

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a'; -- 끝이 a로 끝나는 4자리 데이터


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY    -- 정렬 후 LIMIT !!
  Bytes DESC
LIMIT
  7;    -- 7개만 조회

SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY    -- 정렬 후 LIMIT !!
  Bytes DESC
-- LIMIT 3, 4;
LIMIT 4 OFFSET 3;   -- 4 ~ 7번째(총 4개) 조회
-- OFFSET에 3을 지정한 경우 처음부터 3번째까지의 데이터를 제외하고 4번째 데이터부터 조회

SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  Country;

SELECT
  Composer,
  AVG(Bytes) AS avgOfBytes
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  avgOfBytes DESC;

SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;

-- 04. Grouping data


