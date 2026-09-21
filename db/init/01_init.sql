create database if not exists shopping_db character set utf8mb4 collate utf8mb4_general_ci;

create user if not exists 'lee'@'localhost' identified by 'q1w2e3';
create user if not exists 'lee'@'%' identified by 'q1w2e3';

grant select, insert, update, delete on shopping_db.* to 'lee'@'%';
grant select, insert, update, delete on shopping_db.* to 'lee'@'localhost';
flush privileges;

create database if not exists shopping_db character set utf8mb4 collate utf8mb4_general_ci;

create user if not exists 'lee'@'localhost' identified by 'q1w2e3';
create user if not exists 'lee'@'%' identified by 'q1w2e3';

grant select, insert, update, delete on shopping_db.* to 'lee'@'%';
grant select, insert, update, delete on shopping_db.* to 'lee'@'localhost';


-- study 데이터베이스 생성
create database if not exists study character set utf8mb4 collate utf8mb4_general_ci;

-- lee가 study도 사용할 수 있도록 권한 부여
grant select, insert, update, delete on study.* to 'lee'@'%';
grant select, insert, update, delete on study.* to 'lee'@'localhost';

use study;

-- numcount 테이블 생성
create table if not exists numcount (
    id int auto_increment primary key,
    num int not null,
    insert_at datetime default current_timestamp
);

flush privileges;
