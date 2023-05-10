BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
CREATE TABLE IF NOT EXISTS "answer" (
	"id"	INTEGER NOT NULL,
	"diary_id"	INTEGER,
	"content"	TEXT NOT NULL,
	"create_date"	DATETIME NOT NULL,
	"user_id"	INTEGER NOT NULL DEFAULT '1',
	"modify_date"	DATETIME,
	CONSTRAINT "fk_answer_question_id_diary" FOREIGN KEY("diary_id") REFERENCES "diary"("id") ON DELETE CASCADE,
	CONSTRAINT "fk_answer_user_id_user" FOREIGN KEY("user_id") REFERENCES "user"("id") ON DELETE CASCADE,
	CONSTRAINT "pk_answer" PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "diary_voter" (
	"user_id"	INTEGER NOT NULL,
	"diary_id"	INTEGER NOT NULL,
	CONSTRAINT "fk_question_voter_user_id_user" FOREIGN KEY("user_id") REFERENCES "user"("id") ON DELETE CASCADE,
	CONSTRAINT "fk_question_voter_question_id_question" FOREIGN KEY("diary_id") REFERENCES "diary"("id") ON DELETE CASCADE,
	CONSTRAINT "pk_question_voter" PRIMARY KEY("user_id","diary_id")
);
CREATE TABLE IF NOT EXISTS "answer_voter" (
	"user_id"	INTEGER NOT NULL,
	"answer_id"	INTEGER NOT NULL,
	CONSTRAINT "fk_answer_voter_user_id_user" FOREIGN KEY("user_id") REFERENCES "user"("id") ON DELETE CASCADE,
	CONSTRAINT "fk_answer_voter_answer_id_answer" FOREIGN KEY("answer_id") REFERENCES "answer"("id") ON DELETE CASCADE,
	CONSTRAINT "pk_answer_voter" PRIMARY KEY("user_id","answer_id")
);
CREATE TABLE IF NOT EXISTS "diary" (
	"id"	INTEGER NOT NULL,
	"subject"	VARCHAR(100) NOT NULL,
	"content"	TEXT NOT NULL,
	"create_date"	DATETIME NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"modify_date"	DATETIME,
	"tags"	VARCHAR(400),
	CONSTRAINT "fk_question_user_id_user" FOREIGN KEY("user_id") REFERENCES "user"("id") ON DELETE CASCADE,
	CONSTRAINT "pk_diary" PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "notice" (
	"id"	INTEGER NOT NULL,
	"subject"	VARCHAR(100) NOT NULL,
	"content"	TEXT NOT NULL,
	CONSTRAINT "pk_notice" PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(10) NOT NULL,
	"password"	VARCHAR(12) NOT NULL,
	"email"	VARCHAR(120) NOT NULL,
	"nickname"	VARCHAR(20),
	"name"	VARCHAR(20) NOT NULL,
	"dayofbirth"	VARCHAR(8) NOT NULL,
	CONSTRAINT "uq_user_email" UNIQUE("email"),
	CONSTRAINT "uq_user_username" UNIQUE("username"),
	CONSTRAINT "pk_user" PRIMARY KEY("id")
);
INSERT INTO "alembic_version" VALUES ('677a4e9b4ee6');
INSERT INTO "answer" VALUES (1,3,'태그 저장 : Keine,None','2023-04-17 21:28:38.890332',1,NULL);
INSERT INTO "answer" VALUES (2,21,'ㅎㅇ','2023-04-18 15:27:45.606089',1,NULL);
INSERT INTO "answer" VALUES (3,22,'aa','2023-04-18 16:51:40.448036',1,NULL);
INSERT INTO "answer" VALUES (4,14,'안녕','2023-04-18 17:43:26.485016',1,NULL);
INSERT INTO "diary_voter" VALUES (1,22);
INSERT INTO "answer_voter" VALUES (1,3);
INSERT INTO "answer_voter" VALUES (1,4);
INSERT INTO "diary" VALUES (1,'test에요','Install pip3 install oauth2client.','2023-04-17 21:05:18.204920',1,NULL,'Neighbourhood,None,Keine');
INSERT INTO "diary" VALUES (2,'제발!! 저장!!!!','db.Column(''user_id'', db.Integer, db.ForeignKey(''user.id'', ondelete=''CASCADE''), primary_key=True), db.Column(''diary_id'', db.Integer, db.ForeignKey(''diary.id'', ondelete=''CASCADE''),','2023-04-17 21:12:08.421756',1,NULL,'Keine,None,Necessary');
INSERT INTO "diary" VALUES (3,'제발 저장!!! 플리즈','304 - 127.0.0.1 - - [17/Apr/2023 21:22:04] "GET /static/assets/img/logo.png HTTP/1.1" 304 - 127.0.0.1 - - [17/Apr/2023 21:22:04] "GET /static/assets/vendor/bootstrap-icons/fonts/bootstrap-icons.woff2?24e3','2023-04-17 21:27:19.083325',1,NULL,'Keine,None');
INSERT INTO "diary" VALUES (4,'저장 제발!!! 정확하게!!!','ence = request.form.get(''sentence'') sentence = str(sentence) tags = generate_tags(sentence) diary = diary(subject=form.subject.data, content=form.content.data, crea = crea = crea = crea = crea = crea = crea = crea = crea = crea = crea = crea = crea = create.content.data, ence = request.form.get(''sentence'') sentence = str(sentence) tags = generate_tags(sentence','2023-04-17 21:54:01.209585',1,NULL,'Keine,Nominees,None');
INSERT INTO "diary" VALUES (5,'test','All Rights Reserved.','2023-04-17 22:03:04.574940',1,NULL,'None');
INSERT INTO "diary" VALUES (6,'fl','Your ma little flower.','2023-04-17 22:04:11.830958',1,NULL,'None');
INSERT INTO "diary" VALUES (7,'test','Hello from the Python community. https://www.pygame.org/contribute.html [nltk_data] Downloading package punkt.','2023-04-18 09:15:59.251760',1,NULL,'Nominees,Keine,Nomine');
INSERT INTO "diary" VALUES (8,'제발 저장','304 - 127.0.0.1 - - [18/Apr/2023 09:32:19] "GET /static/style.css HTTP/1.1" 304 - 127.0.0.1 - - [18/Apr/2023 09:32:19] "GET /static/assets/vendor/remixicon/remixicon.css HTTP/1.1" 304 - 127.0.0.1 - - [18/','2023-04-18 09:39:15.210269',1,NULL,'                
                Coding
                Online
                Engineering
                Code
                Developer
                Technology
                Science
                Digital
                Website
                Programming
                Computer Science
                Software
                Software Engineering
                Web Development
                Internet
                Software Development
                Web
                Website Development
                Tech');
INSERT INTO "diary" VALUES (9,'제발 저장 태그!','The Debugger is active! * Detected change in ''C:myprojecthelloflaskmyprojectpyboviewsgrammar.py''.','2023-04-18 09:54:02.528300',1,NULL,'
Digital
ComputerScience
Science
Developer
PythonProgramming
Tech
Engineering
Software
Python
Technology
ProgrammingLanguages');
INSERT INTO "diary" VALUES (10,'저장 제발','# Define the function to handle the form submission @grammar.route(''/correct_grammar'', methods=[''POST'', ''GET''])','2023-04-18 10:04:02.942375',1,NULL,',Engineering,Technology,ProgrammingLanguages,Developer,Programming,Software,ComputerScience,Digital,Tech,Coding,SoftwareEngineering,SoftwareDevelopment,Code,Science');
INSERT INTO "diary" VALUES (11,'저장','# Define the function to handle the form submission @grammar.route(''/correct_grammar'', methods=[''POST'', ''GET''])','2023-04-18 10:05:33.951663',1,NULL,'
Programming
Technology
Software
Engineering
ComputerScience
SoftwareDevelopment
Developer
Coding
ProgrammingLanguages
SoftwareEngineering
Digital
Code
Tech
Science');
INSERT INTO "diary" VALUES (12,'저장','# Define the function to handle the form submission @grammar.route(''/correct_grammar'', methods=[''POST'', ''GET''])','2023-04-18 10:10:20.002887',1,NULL,'SoftwareDevelopment
Technology
Developer
Engineering
SoftwareEngineering
Digital
ProgrammingLanguages
Science
Software
Programming
Code
ComputerScience
Coding
Tech');
INSERT INTO "diary" VALUES (13,'태그','# Define the function to handle the form submission @grammar.route(''/correct_grammar'', methods=[''POST'', ''GET''])','2023-04-18 10:16:38.747278',1,NULL,'Software,SoftwareEngineering,Technology,Science,Coding,Developer,Code,Tech,ProgrammingLanguages,ComputerScience,Digital,Engineering,SoftwareDevelopment,Programming');
INSERT INTO "diary" VALUES (14,'태그 저장','Don''t remind me I''m minding my own business Don''t try to find me I''m better left alone than in this It doesn''t surprise me Do you really think that I could care? If you really don''t like me, find somebody else It could be anyone else out there.','2023-04-18 10:32:24.154942',1,NULL,'EmotionalIntelligence,Love,Emotions');
INSERT INTO "diary" VALUES (15,'Metalica - Master of puppets','End of passion play, crumbling away I''m your source of self-destruction Veins that pump with fear, sucking darkest clear Leading on your death''s construction Taste me, you will see More is all you need Dedicated to How I''m killing you Come crawl faster (faster) Obey your master (master) Your life burns faster (faster) Obey your master, master Master of puppets, I''m pulling your strings Twisting your mind and smashing your dreams Blinded by','2023-04-18 10:41:47.661363',1,NULL,'Creative,Storytelling,Death');
INSERT INTO "diary" VALUES (16,'test','As I walk through the valley of the shadow of death I take a look at my life and realize there''s nothin'' left ''Cause I''ve been blastin'' and laughing so long, that even my mama thinks that my mind is gone.''''','2023-04-18 10:51:26.363568',1,NULL,'Death,Emotions');
INSERT INTO "diary" VALUES (17,'help','Please explain how I can improve my English.','2023-04-18 10:57:35.373758',1,NULL,'EnglishLanguage,HelpmeimprovemyEnglish,HelpMe');
INSERT INTO "diary" VALUES (18,'emotion','She said to me that she liked you.','2023-04-18 10:59:34.417690',1,NULL,'EmotionalIntelligence,Ai,Self');
INSERT INTO "diary" VALUES (21,'test','Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.','2023-04-18 12:27:24.937209',1,NULL,'Python''Software''Developer');
INSERT INTO "diary" VALUES (22,'python','Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected.','2023-04-18 12:30:34.547850',1,NULL,'Developer,Software,Computer Science');
INSERT INTO "diary" VALUES (23,'good','Hello everyone, great night.','2023-04-19 09:34:21.919108',1,NULL,'I hope you have a great night.,Hello Everyone,great night');
INSERT INTO "notice" VALUES (1,'2023.04.17 공지사항','영어일기 1.0 ver
프로젝트 영어일기를 위한 웹사이트가 새롭게 오픈했습니다. 
찾아주신 여러분들 환영합니다. 
아울러 여러분의 무단 복제와 공유는 금지하며, 위반할 시 "엉덩이 맴매형"에 처하게 될 것입니다.

- 1.1 ver 모바일 화면 추가 예정
');
INSERT INTO "user" VALUES (1,'admin','pbkdf2:sha256:260000$n7ZH0P2s2NS2Ul4z$ca8231dfb10523cf7f907ef2dbeb86725fa8c2b4559a0285c9bc095c09d7fd44','admin@naver.com','어드민','어드민','2023.04.17');
COMMIT;
