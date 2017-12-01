drop table if exists users;
create table users (
  id integer primary key autoincrement,
  account string not null,
  password string not null,
  email string not null,
  mobile string,
  real_name string,
  nick_name string
);