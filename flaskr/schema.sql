DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS step_count;

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

CREATE TABLE step_count (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date_col DATE,
  steps INTEGER,
  week_number INTEGER
);

insert into activity (name, type, duration, distance, calories, averageHR) values ("Slow Long", 1, 3159, 6.26, 594, 171);