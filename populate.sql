--populate.sql
/*
Redwood Analytics: Dean Callahan, Zachary Griffiths, Evan Blem, Jaiden Ro
Date Last Modified: 10/12/25
*/

--Delete Statements
/*
DELETE FROM Comments_Other;
DELETE FROM Comments_Collection_Methods;
DELETE FROM Comments_Toxic_Material;
DELETE FROM Comments;
DELETE FROM Categories;
DELETE FROM Auditors;
DELETE FROM Building;
DELETE FROM Waste_Audit;
*/
prompt Inserting into Building table
/*
INSERT INTO Building VALUES(BUILDING_ID, building_name, building_type);
*/

INSERT INTO Building VALUES ('ALDER', 'Alder Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('AMH', 'Alistar McCrone Hall', 'Hall');
INSERT INTO Building VALUES ('ARTA', 'Art A', 'Academic');
INSERT INTO Building VALUES ('ARTB', 'Art B', 'Academic');
INSERT INTO Building VALUES ('BH', 'Baiocchi House', 'House');
INSERT INTO Building VALUES ('BALH', 'Balabanis House (MCC)', 'House');
INSERT INTO Building VALUES ('BSS', 'Behavioral and Social Sciences', 'Academic');
INSERT INTO Building VALUES ('BOAT', 'Boat Facility', 'Facility');
INSERT INTO Building VALUES ('BRH', 'Brero House (ITEPP)', 'House');
INSERT INTO Building VALUES ('BHH', 'Bret Harte House', 'House');
INSERT INTO Building VALUES ('BROH', 'Brookins House', 'House');
INSERT INTO Building VALUES ('BUCH', 'Buck House (CCAT)', 'House');
INSERT INTO Building VALUES ('CA', 'Campus Apartments','Housing');
INSERT INTO Building VALUES ('CEF', 'Campus Events Field', 'Field');
INSERT INTO Building VALUES ('CEDAR', 'Cedar Residence Hall','Residence Hall');
INSERT INTO Building VALUES ('CERAM', 'Ceramics Lab', 'Lab');
INSERT INTO Building VALUES ('CHINQ', 'Chinquapin Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('CCF', 'College Creek Field', 'Field');
INSERT INTO Building VALUES ('CCFLR', 'College Creek Field Locker Rooms', 'Facility');
INSERT INTO Building VALUES ('CCCTR', 'Community Center', 'Center');
INSERT INTO Building VALUES ('CREEK', 'Creekside Lounge', 'Lounge');
INSERT INTO Building VALUES ('CYPRS', 'Cypress Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('DELNO', 'Del Norte Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('SCIE', 'Dennis K. Walker Greenhouse', 'Greenhouse');
INSERT INTO Building VALUES ('GRNH', 'Experimental Greenhouse', 'Greenhouse');
INSERT INTO Building VALUES ('FM', 'Facilities Management','Administration');
INSERT INTO Building VALUES ('FERN', 'Fern Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('FWH', 'Feuerwerker House', 'House');
INSERT INTO Building VALUES ('FSH', 'Fish Hatchery','Facility');
INSERT INTO Building VALUES ('FGYM', 'Forbes Gym', 'Gym');
INSERT INTO Building VALUES ('FR', 'Forestry', 'Academic');
INSERT INTO Building VALUES ('FH', 'Founders Hall', 'Hall');
INSERT INTO Building VALUES ('GH', 'Gist Hall', 'Hall');
INSERT INTO Building VALUES ('GSAC', 'Gutswurrak Student Activities Center', 'Center');
INSERT INTO Building VALUES ('HH', 'Hadley House', 'House');
INSERT INTO Building VALUES ('HAH', 'Hagopian House', 'House');
INSERT INTO Building VALUES ('HGH', 'Harry Griffith Hall', 'Hall');
INSERT INTO Building VALUES ('HEMLC', 'Hemlock Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('JH', 'Jenkins Hall', 'Hall');
INSERT INTO Building VALUES ('JGC', 'Jolly Giant Commons', 'Commons');
INSERT INTO Building VALUES ('JUNIP', 'Juniper Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('KA', 'Kinesiology and Athletics', 'Academic');
INSERT INTO Building VALUES ('LAURE', 'Laurel Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('LIB', 'Library', 'Library');
INSERT INTO Building VALUES ('LAPT', 'Little Apartments', 'Housing');
INSERT INTO Building VALUES ('MADRN', 'Madrone Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('MAPLE', 'Maple Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('MWCC', 'Marine Wildlife Care Center', 'Center');
INSERT INTO Building VALUES ('MCOM', 'Marketing and Communications', 'Administration');
INSERT INTO Building VALUES ('MWH', 'Mary Warren House', 'House');
INSERT INTO Building VALUES ('MENDO', 'Mendocino Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('MUSA', 'Music A', 'Academic');
INSERT INTO Building VALUES ('MUSB', 'Music B', 'Academic');
INSERT INTO Building VALUES ('NR', 'Natural Resources', 'Academic');
INSERT INTO Building VALUES ('NHE', 'Nelson Hall East', 'Hall');
INSERT INTO Building VALUES ('NHW', 'Nelson Hall West', 'Hall');
INSERT INTO Building VALUES ('PARK', 'Parking Kiosk', 'Facility');
INSERT INTO Building VALUES ('PEPR', 'Pepperwood Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('RWC', 'Recreation and Wellness Center', 'Center');
INSERT INTO Building VALUES ('RB', 'Redwood Bowl', 'Athletics');
INSERT INTO Building VALUES ('REDWO', 'Redwood Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('SERC', 'Schatz Energy Research Center', 'Center');
INSERT INTO Building VALUES ('SCIA', 'Science A', 'Academic');
INSERT INTO Building VALUES ('SCIB', 'Science B', 'Academic');
INSERT INTO Building VALUES ('SCIC', 'Science C', 'Academic');
INSERT INTO Building VALUES ('SCLPT', 'Sculpture Lab', 'Lab');
INSERT INTO Building VALUES ('SHAST', 'Shasta Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('SR', 'Shipping and Receiving', 'Facility');
INSERT INTO Building VALUES ('SH', 'Siemens Hall', 'Hall');
INSERT INTO Building VALUES ('SBS', 'Student and Business Services', 'Administration');
INSERT INTO Building VALUES ('HC', 'Student Health and Counseling', 'Health');
INSERT INTO Building VALUES ('SRC', 'Student Recreation Center', 'Center');
INSERT INTO Building VALUES ('SUNST', 'Sunset Residence Hall',  'Residence Hall');
INSERT INTO Building VALUES ('SWET', 'Swetman', 'Academic');
INSERT INTO Building VALUES ('TANOK', 'Tan Oak Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('TH', 'Telonicher House', 'House');
INSERT INTO Building VALUES ('TA', 'Theatre Arts', 'Academic');
INSERT INTO Building VALUES ('TELC', 'Trinity Early Learning Center', 'Center');
INSERT INTO Building VALUES ('TRIN', 'Trinity Residence Hall', 'Residence Hall');
INSERT INTO Building VALUES ('UPF', 'Upper Playing Field', 'Field');
INSERT INTO Building VALUES ('VMH', 'Van Matre Hall', 'Hall');
INSERT INTO Building VALUES ('WAGH', 'Anderson Wagner House', 'House');
INSERT INTO Building VALUES ('WWH', 'Walter Warren House (INRSEP)', 'House');
INSERT INTO Building VALUES ('WH', 'Warren House', 'House');
INSERT INTO Building VALUES ('WDFS', 'Wildlife and Fisheries', 'Academic');
INSERT INTO Building VALUES ('WGP', 'Wildlife Game Pens', 'Facility');
INSERT INTO Building VALUES ('WILLO', 'Willow Residence Hall', 'Residence Hall');

/* No codes for these locations, currently making up codes for them now */
INSERT INTO Building VALUES ('BAQ', 'Balabanis Art Quad', 'Quad');
INSERT INTO Building VALUES ('CYN', 'The Canyon', 'Complex');
INSERT INTO Building VALUES ('CCC', 'College Creek Complex', 'Residence Complex');
INSERT INTO Building VALUES ('CVC', 'Creekview Complex', 'Residence Complex');
INSERT INTO Building VALUES ('HILL', 'The Hill', 'Complex');
INSERT INTO Building VALUES ('LBC', 'Library Circle', 'Circle');
INSERT INTO Building VALUES ('RPL', 'Redwood Plaza', 'Plaza');
INSERT INTO Building VALUES ('RSL', 'Redwood Sciences Lab', 'Lab');
INSERT INTO Building VALUES ('UQ', 'University Quad', 'Quad');
INSERT INTO Building VALUES ('MARKET', 'Marketplace Dining', 'Dining');

prompt Inserting into Waste_Audit table
/*
Format 
INSERT INTO Waste_Audit VALUES (AUDIT_ID, building_id, number_bags, total_weight, weight_error, volume_error, date_conducted);
*/
INSERT INTO Waste_Audit VALUES (100001,'SBS', NULL, 40.17,0,0,TO_DATE('09-11-2025','MM-DD-YYYY'));
INSERT INTO Waste_Audit VALUES (100002, 'MARKET',11, 51.5,0,0,TO_DATE('09-25-2025','MM-DD-YYYY'));


prompt Inserting into Auditors table
/*
INSERT INTO Auditors VALUES(AUDITOR_ID, email_address, auditor_fname, auditor_lname);
*/
INSERT INTO Auditors VALUES (200001, 'dpc43@humboldt.edu','Dean', 'Callahan');
INSERT INTO Auditors VALUES (200002, 'zkg3@humboldt.edu','Zachary', 'Griffiths');
INSERT INTO Auditors VALUES (200003, 'eb335@humboldt.edu','Evan', 'Blem');
INSERT INTO Auditors VALUES (200004, 'jr650@humboldt.edu','Jaiden', 'Roe');


prompt Inserting into Categories table
/*
INSERT INTO Categories VALUES(CATEGORY_NAME, audit_id, category_weight, percent_by_weight, percent_by_volume);
*/
INSERT INTO Categories VALUES ('Landfill', 100001, 10.91, 25.9, 30);
INSERT INTO Categories VALUES ('Mixed Recycling', 100001, 5.26, 13.1, 18);
INSERT INTO Categories VALUES ('Compost', 100001, 22, 54.8, 50);
INSERT INTO Categories VALUES ('Universal Waste Recycling', 100001, 0, 0, 0);
INSERT INTO Categories VALUES ('Hazardous Waste', 100001, 0, 0, 0);
INSERT INTO Categories VALUES ('Other', 100001, 2.5, 6.2, 2);

INSERT INTO Categories VALUES ('Landfill', 100002, 22.59, 43.86, 65);
INSERT INTO Categories VALUES ('Mixed Recycling', 100002, 8.33, 13.1, 15);
INSERT INTO Categories VALUES ('Compost', 100002, 24.36, 47.37, 20);
INSERT INTO Categories VALUES ('Universal Waste Recycling', 100002, 0, 0, 0);
INSERT INTO Categories VALUES ('Hazardous Waste', 100002, 0, 0, 0);
INSERT INTO Categories VALUES ('Other', 100002, 2.5, 6.2, 2);


prompt Inserting into Comments table
/*
INSERT INTO Comments VALUES(COMMENT_ID,comment_type,audit_id);
*/
INSERT INTO Comments VALUES (400001, 'Toxic Material', 100001);
INSERT INTO Comments VALUES (400002, 'Collection Methods', 100001);
INSERT INTO Comments VALUES (400003, 'Other', 100001);

INSERT INTO Comments VALUES (400004, 'Toxic Material', 100002);
INSERT INTO Comments VALUES (400005, 'Collection Methods', 100002);
INSERT INTO Comments VALUES (400006, 'Other', 100002);

prompt Inserting into Comments_Toxic_Material table
/*
INSERT INTO Comments_Toxic_Material VALUES(COMMENT_ID,toxic_items);
*/
INSERT INTO Comments_Toxic_Material VALUES (400001, 'Pen');
INSERT INTO Comments_Toxic_Material VALUES (400004, 'None');


prompt Inserting into Comments_Collection_Methods table
/*
INSERT INTO Comments_Collection_Methods VALUES(COMMENT_ID,collection_methods);
*/
INSERT INTO Comments_Collection_Methods VALUES (400002, 'None');
INSERT INTO Comments_Collection_Methods VALUES (400005, 'None');

prompt Inserting into Comments_Other table
/*
INSERT INTO Comments_Other VALUES(COMMENT_ID,collection_methods);
*/
INSERT INTO Comments_Other VALUES (400003, 'None');
INSERT INTO Comments_Other VALUES (400006, 'None');





