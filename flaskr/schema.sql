DROP TABLE IF EXISTS activity;

CREATE TABLE activity (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  type INTEGER NOT NULL,
  duration INTEGER NOT NULL,
  distance FLOAT,
  calories INTEGER,
  averageHR INTEGER,
  averagePower INTEGER
);

insert into activity (name, type, duration, distance, calories, averageHR) values ("Slow Long", 1, 3159, 6.26, 594, 171);