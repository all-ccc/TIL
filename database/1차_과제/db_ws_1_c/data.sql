-- SELECT *
-- FROM songs;

SELECT DISTINCT
  genre, COUNT(*) AS count, AVG(duration) AS average_duration
FROM
  songs
GROUP BY
  genre;