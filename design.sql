--design.sql
/*
Redwood Analytics: Dean Callahan, Zachary Griffiths, Evan Blem, Jaiden Ro
Date Last Modified: 10/02/25
*/
drop table Building cascade constraints;
create table Building
(BUILDING_ID varchar(20),
building_type varchar(40),
building_name varchar(40),
primary key (BUILDING_ID)
);


drop table Waste_Audit cascade constraints;
create table Waste_Audit
(AUDIT_ID int,
building_id varchar(20),
number_bags integer,
total_weight decimal(5,2),
weight_error integer,
date_conducted date,
primary key (AUDIT_ID),
foreign key (building_id) references Building(building_id)
);


drop table Form_Metadata cascade constraints;
create table Form_Metadata
(FORM_ID int,
time_submitted DATE DEFAULT SYSDATE,
date_submitted DATE DEFAULT SYSDATE,
primary key (FORM_ID)
);

drop table Auditors cascade constraints;
create table Auditors
(AUDITOR_ID int,
email_address varchar(40),
auditor_fname varchar(40),
auditor_lname varchar(40),
primary key (AUDITOR_ID)
);

drop table Categories cascade constraints;
create table Categories
(CATEGORY_NAME varchar(40),
audit_id int,
category_weight decimal(5,2),
percent_by_weight decimal(5,2),
percent_by_volume decimal(5,2),
primary key (CATEGORY_NAME,AUDIT_ID),
foreign key (audit_id) references Waste_Audit(audit_id)
);

drop table Comments cascade constraints;
create table Comments
(COMMENT_ID int,
comment_type varchar(40),
audit_id int,
primary key (COMMENT_ID),
foreign key (audit_id) references Waste_Audit(audit_id)
);

drop table  Comments_Toxic_Material cascade constraints;
create table Comments_Toxic_Material
(COMMENT_ID int,
toxic_items varchar(40),
foreign key (comment_id) references Comments(COMMENT_ID),
primary key (COMMENT_ID)
);

drop table  Comments_Collection_Methods cascade constraints;
create table Comments_Collection_Methods
(COMMENT_ID int,
collection_methods varchar(40),
foreign key (comment_id) references Comments(COMMENT_ID),
primary key (COMMENT_ID)
);

drop table  Comments_Other cascade constraints;
create table Comments_Other
(COMMENT_ID int,
other_comment varchar(40),
foreign key (comment_id) references Comments(COMMENT_ID),
primary key (COMMENT_ID)
);
