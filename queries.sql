--queries.sql
/*
This file shows some useful sample queries you can run on the database. This was mainly used to compare our two data storage and collection systems but does offer basic audit analysis. 
Redwood Analytics: Dean Callahan, Zachary Griffiths, Evan Blem, Jaiden Roe
Date Last Modified: 10/12/25
*/

--These statements will display all the tables and their contents;
set linesize 170;
set pagesize 20;

select *
from waste_audit;

select *
from auditors;

select * 
from building;

select *
from categories;

select * 
from comments;

select *
from comments_toxic_material;

select * 
from comments_collection_methods;

select * 
from comments_other;

--Select Information For Directly Comparing Audits (Compares Audit with ID 100001 and 100002)
--The two lines below will improve the format of the outputs
set linesize 170;
set pagesize 20;

prompt 
prompt Creating query to compare audits 100001 and 100002
select w.audit_id, b.building_id, b.building_name, date_conducted, category_name, category_weight, percent_by_weight, percent_by_volume
from waste_audit w, categories c, building b
where b.building_id = w.building_id and w.audit_id=c.audit_id and w.audit_id in (100001, 100002);

set linesize 80;
set pagesize 14;


