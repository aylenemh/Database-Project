use database-project;
drop table if exists songs;
create table songs(id int NOT NULL AUTO_INCREMENT primary key,  title varchar(50), artist varchar(50), genre varchar(20));
insert into songs (title, artist, genre) values ("Five Hundred Miles", "The Kingston Trio", "Folk"), ("Yesterday Once More", "The Carpenters", "pop"), ("A Whole New World ", "Alan Menken", "R&B, Soul");