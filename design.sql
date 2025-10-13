--design.sql
/*
Redwood Analytics: Dean Callahan, Zachary Griffiths, Evan Blem, Jaiden Roe
Date Last Modified: 10/12/25
*/

DROP TABLE Building CASCADE CONSTRAINTS;
CREATE TABLE Building
(BUILDING_ID    VARCHAR2(11),
building_name   VARCHAR2(40) NOT NULL,
building_type   VARCHAR2(40),
PRIMARY KEY (BUILDING_ID)
);



DROP TABLE Waste_Audit CASCADE CONSTRAINTS;
CREATE TABLE Waste_Audit
(AUDIT_ID    INTEGER,
building_id  VARCHAR2(11) NOT NULL,
number_bags  INTEGER,
total_weight DECIMAL(5,2),
weight_error INTEGER,
volume_error INTEGER,
date_conducted DATE NOT NULL,
PRIMARY KEY (AUDIT_ID),
FOREIGN KEY (building_id) REFERENCES Building(building_id)
);


DROP SEQUENCE waste_audit_seq;
CREATE SEQUENCE waste_audit_seq START WITH 100003 INCREMENT BY 1 MAXVALUE 199999;

CREATE OR REPLACE TRIGGER audit_id
BEFORE INSERT ON waste_audit
FOR EACH ROW
BEGIN
     IF :NEW.audit_id IS NULL THEN
       SELECT waste_audit_seq.NEXTVAL
       INTO :NEW.audit_id
       FROM dual;
     END IF;
END;
/



DROP TABLE Auditors CASCADE CONSTRAINTS;
CREATE TABLE Auditors
(AUDITOR_ID int,
email_address    VARCHAR2(40),
auditor_fname    VARCHAR2(40),
auditor_lname    VARCHAR2(40),
PRIMARY KEY (AUDITOR_ID)
);


DROP SEQUENCE auditor_seq;
CREATE SEQUENCE auditor_seq START WITH 200005 INCREMENT BY 1 MAXVALUE 299999;

CREATE OR REPLACE TRIGGER auditor_id
BEFORE INSERT ON auditors
FOR EACH ROW
BEGIN
     IF :NEW.auditor_id IS NULL THEN
       SELECT auditor_seq.NEXTVAL
       INTO :NEW.auditor_id
       FROM dual;
     END IF;
END;
/



DROP TABLE Categories CASCADE CONSTRAINTS;
CREATE TABLE Categories
(CATEGORY_NAME    VARCHAR2(40),
audit_id          INTEGER,
category_weight   DECIMAL(5,2) NOT NULL,
percent_by_weight DECIMAL(5,2),
percent_by_volume DECIMAL(5,2) NOT NULL,
PRIMARY KEY (CATEGORY_NAME,AUDIT_ID),
FOREIGN KEY (audit_id) REFERENCES Waste_Audit(audit_id)
);


CREATE OR REPLACE TRIGGER update_weight_error
AFTER INSERT OR UPDATE ON Categories
DECLARE 
	sum_weight    DECIMAL(5,2);
	total_weight  DECIMAL(5,2);
BEGIN
	
   FOR r IN (SELECT DISTINCT audit_id FROM Categories) LOOP
	SELECT NVL(SUM(category_weight), 0)
	    INTO sum_weight
	    FROM Categories
	 WHERE audit_id = r.audit_id;

         BEGIN
             SELECT total_weight
             INTO total_weight
             FROM Waste_Audit
            WHERE audit_id = r.audit_id;
         EXCEPTION
            WHEN NO_DATA_FOUND THEN
               CONTINUE;
         END;
    IF total_weight IS NULL THEN
        UPDATE Waste_Audit SET weight_error = 0
         WHERE audit_id = r.audit_id;
    ELSIF ABS(total_weight - sum_weight) > 0.01 THEN
        UPDATE Waste_Audit SET weight_error = 1
         WHERE audit_id = r.audit_id;
    ELSE
        UPDATE Waste_Audit SET weight_error = 0
         WHERE audit_id = r.audit_id;
    END IF;
   END LOOP;
END;
/

CREATE OR REPLACE TRIGGER update_volume_error
AFTER INSERT OR UPDATE OR DELETE ON Categories
DECLARE
    sum_volume    DECIMAL(5,2);
BEGIN

 FOR r in (SELECT DISTINCT audit_id FROM Categories) LOOP
    SELECT NVL(SUM(percent_by_volume), 0)
      INTO sum_volume
      FROM Categories
     WHERE audit_id = r.audit_id;
     
 IF ABS(sum_volume-100) > 0.01 THEN
        UPDATE Waste_Audit
           SET volume_error = 1
         WHERE audit_id = r.audit_id;
    ELSE
        UPDATE Waste_Audit
           SET volume_error = 0
         WHERE audit_id = r.audit_id;
    END IF;
  END LOOP;
END;
/



DROP TABLE Comments CASCADE CONSTRAINTS;
CREATE TABLE Comments
(COMMENT_ID    INTEGER,
comment_type   VARCHAR2(40),
audit_id       INTEGER,
PRIMARY KEY (COMMENT_ID),
FOREIGN KEY (audit_id) REFERENCES Waste_Audit(audit_id)
);


DROP SEQUENCE comment_seq;
CREATE SEQUENCE comment_seq START WITH 400007 INCREMENT BY 1 MAXVALUE 499999;

CREATE OR REPLACE TRIGGER comment_id
BEFORE INSERT ON Comments
FOR EACH ROW
BEGIN
  IF :NEW.comment_id IS NULL THEN
    SELECT comment_seq.NEXTVAL INTO :NEW.comment_id FROM dual;
  END IF;
END;
/


DROP TABLE Comments_Toxic_Material CASCADE CONSTRAINTS;
CREATE TABLE Comments_Toxic_Material
(COMMENT_ID    INTEGER,
toxic_items    VARCHAR2(40),
PRIMARY KEY (COMMENT_ID),
FOREIGN KEY (comment_id) REFERENCES Comments(COMMENT_ID)
);


DROP TABLE Comments_Collection_Methods CASCADE CONSTRAINTS;
CREATE TABLE Comments_Collection_Methods
(COMMENT_ID        INTEGER,
collection_methods VARCHAR2(40),
PRIMARY KEY (COMMENT_ID),
FOREIGN KEY (comment_id) REFERENCES Comments(COMMENT_ID)
);


DROP TABLE Comments_Other CASCADE CONSTRAINTS;
CREATE TABLE Comments_Other
(COMMENT_ID   INTEGER,
other_comment VARCHAR2(40),
PRIMARY KEY(COMMENT_ID),
FOREIGN KEY (comment_id) REFERENCES Comments(COMMENT_ID)
);
