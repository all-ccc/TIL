CREATE TABLE songs (
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  Title VARCHAR(50),
  Artist VARCHAR(50),
  Album VARCHAR(50),
  Genre VARCHAR(50),
  Duration INTEGER
);

INSERT INTO songs(title, artist, album, genre, duration)
VALUES
  ('New Title', 'Artist 1', 'Album 1', 'Pop', 200),
  ('Song 2', 'Artist 2', 'Album 2', 'Rock', 300),
  ('Song 3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
  ('Song 4', 'Artist 4', 'Album 4', 'Electronic', 180),
  ('Song 5', 'Artist 5', 'Album 5', 'R&B', 320);


UPDATE
  songs
SET
  title = 'Updated Title'
WHERE
  title = 'New Title';