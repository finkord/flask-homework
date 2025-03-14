-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS links;
DROP TABLE IF EXISTS groups;

CREATE TABLE groups (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  group_name TEXT NOT NULL,
  icon TEXT
);

CREATE TABLE links (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  'name' TEXT NOT NULL,
  link TEXT NOT NULL,
  logo TEXT,
  group_id INTEGER,
  FOREIGN KEY (group_id) REFERENCES groups (id)
);