/*
scalability_test.sql
Redwood Analytics: Dean Callahan, Zachary Griffiths, Evan Blem, Jaiden Roe
Date Last Modified: 10/12/25

This file will insert 5000 rows into our database to test performance and scalablity of this data storage system.
*/

--Create and time the amount it takes to insert 5000 mock rows in the waste_audit table
SET SERVEROUTPUT ON
DECLARE
   v_start TIMESTAMP;
   v_end TIMESTAMP;
BEGIN
	v_start:=SYSTIMESTAMP;
INSERT INTO Waste_Audit(audit_id, building_id, number_bags, total_weight, date_conducted)
SELECT waste_audit_seq.NEXTVAL, 
      ((SELECT building_id FROM (SELECT building_id FROM building ORDER BY DBMS_RANDOM.VALUE) WHERE ROWNUM = 1)),
	round(DBMS_RANDOM.value(1,10)),
	round(DBMS_RANDOM.value(5,200),2),
	trunc(SYSDATE-DBMS_RANDOM.VALUE(1,365))
FROM DUAL
CONNECT BY LEVEL<=5000;

v_end := SYSTIMESTAMP;
DBMS_OUTPUT.PUT_LINE('Elasped time: ' ||TO_CHAR(v_end-v_start));
END;
/

prompt Inserted the mock data

select count(*) from waste_audit;

