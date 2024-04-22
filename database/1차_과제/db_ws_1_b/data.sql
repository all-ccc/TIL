-- 데이터 조회
SELECT *
FROM
  songs;


-- 데이터 정렬
SELECT *
FROM
  songs
ORDER BY
  title DESC;


-- 데이터 필터링
SELECT *
FROM
  songs
WHERE
  genre = 'Pop';


-- 조건부 조회
SELECT *
FROM
  songs
WHERE
  (duration / 60) >= 3;