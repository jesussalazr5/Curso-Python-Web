--SQLite
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
id integer primary key autoincrement,
titulo string not null,
texto string not null,
data_criacao timestamp null default current_timestamp



);