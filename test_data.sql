--test inserting data into table to see if the errors will show up or not for the building table 
INSERT INTO Building VALUES(67,100, 'Hi there');
INSERT INTO Building VALUES(67,100, 'Hi there');

-- inserting data into waste audit able to see if errors will show up in the waste audit table
INSERT INTO Waste_Audit VALUES (11, NULL, 'C9 910', '16',12,TO_DATE('23-32-1320','MM-DD-YYYY'));

-- insearting data into the auditor table to show if errors will popped up
INSERT INTO Auditors VALUES (920, 'jr650@humboldt.edu','Jaiden', 21);

--  Categories insert values 
INSERT INTO Categories VALUES (123, 'LandFill', 10.91, 'asdf', 30);
