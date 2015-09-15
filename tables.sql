create table if not exists post(
    id int primary key auto_increment,
    title varchar(40),
    title_pic varchar(100) default '',
    datetime datetime,
    body text,
    published tinyint default 0
) engine=innodb default charset=utf8;

