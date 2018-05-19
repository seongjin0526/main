
use main;

create table main.video_store(
	id int primary key auto_increment,
	subject varchar(100),
	content varchar(1000),
	sumnail_id int,
	regist_id int,
	create_date DATETIME DEFAULT NOW(),
	modify_date datetime DEFAULT null
);

ALTER TABLE main.video_store convert to charset utf8;

create table main.file_store(
	id int primary key auto_increment,
    file_dir varchar(100),
    file_name varchar(100),
    file_size varchar(100),
    file_ext varchar(100),
    del_yn varchar(10),
    create_date DATETIME DEFAULT NOW(),
	modify_date datetime
);

ALTER TABLE main.file_store convert to charset utf8;

insert into video_store(subject, content, sumnail_id, regist_id)
values('프로그래밍 기초','안녕! 내용입니다', '1', '1');

insert into video_store(subject, content, sumnail_id, regist_id)
values('프로그래밍 응용','안녕! 내용입니다', '1', '1');

insert into video_store(subject, content, sumnail_id, regist_id)
values('프로그래밍 초급','안녕! 내용입니다', '1', '1');

insert into video_store(subject, content, sumnail_id, regist_id)
values('프로그래밍 중급','안녕! 내용입니다', '1', '1');

insert into video_store(subject, content, sumnail_id, regist_id)
values('프로그래밍 고급','안녕! 내용입니다', '1', '1');

insert into video_store(subject, content, sumnail_id, regist_id)
values('프로그래밍 특급','안녕! 내용입니다', '1', '1');
