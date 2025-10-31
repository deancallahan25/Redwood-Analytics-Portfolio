
--Testing all the triggers from the design sql statements


-- Building

INSERT INTO Building (BUILDING_ID, building_name, building_type)
VALUES ('B001', 'Science Hall', 'Academic');

INSERT INTO Building (BUILDING_ID, building_name, building_type)
VALUES ('B002', 'Main Library', 'Academic');

-- waste audits

INSERT INTO Waste_Audit (building_id, number_bags, total_weight, weight_error, volume_error, date_conducted)
VALUES ('B001', 10, 25.00, NULL, NULL, TO_DATE('2025-10-10', 'YYYY-MM-DD'));

INSERT INTO Waste_Audit (building_id, number_bags, total_weight, weight_error, volume_error, date_conducted)
VALUES ('B002', 5, 12.50, NULL, NULL, TO_DATE('2025-10-11', 'YYYY-MM-DD'));

-- auditors

INSERT INTO Auditors (email_address, auditor_fname, auditor_lname)
VALUES ('dcallahan@redwood.edu', 'Dean', 'Callahan');

INSERT INTO Auditors (email_address, auditor_fname, auditor_lname)
VALUES ('zgriffiths@redwood.edu', 'Zachary', 'Griffiths');

-- categories

INSERT INTO Categories (category_name, audit_id, category_weight, percent_by_weight, percent_by_volume)
VALUES ('Recyclables', 100003, 10.00, 40.00, 40.00);

INSERT INTO Categories (category_name, audit_id, category_weight, percent_by_weight, percent_by_volume)
VALUES ('Compost', 100003, 10.00, 40.00, 40.00);

INSERT INTO Categories (category_name, audit_id, category_weight, percent_by_weight, percent_by_volume)
VALUES ('Landfill', 100003, 5.00, 20.00, 20.00);

-- audits

INSERT INTO Categories (category_name, audit_id, category_weight, percent_by_weight, percent_by_volume)
VALUES ('Recyclables', 100004, 4.00, 32.00, 60.00);

INSERT INTO Categories (category_name, audit_id, category_weight, percent_by_weight, percent_by_volume)
VALUES ('Landfill', 100004, 6.00, 48.00, 30.00);

