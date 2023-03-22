DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS chain_data;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE chain_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    quantity INTEGER,
    seller_name TEXT NOT NULL,
    price INTEGER
);