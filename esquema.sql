--SQLite
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
id integer primary key autoincrement,
titulo string not null,
data_criacao timestamp not null default current_timestamp



);