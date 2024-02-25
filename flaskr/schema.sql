DROP TABLE IF EXISTS activity;
DROP TABLE IF EXISTS step;
DROP TABLE IF EXISTS weight;

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

CREATE TABLE step (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date DATE,
  steps INTEGER,
  week_number INTEGER
);

CREATE TABLE weight (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date DATE,
  weight INTEGER,
  week_number INTEGER
);

insert into activity (name, type, duration, distance, calories, averageHR) values ("Slow Long", 1, 3159, 6.26, 594, 171);