# Project Plan Template -- Comparing Data Collection & Storage Systems

## Team Name & Members
### Redwood Analytics
- Tech Lead: Dean Callahan - dpc43@humboldt.edu
- Project Manager: Zachary Griffiths - 
- Domain Expert: Evan Blem -
- Quality Assurance: Jaiden Roe - 

## Project Title - Database for Zero Waste

## 1. Purpose & Context
- **Purpose:** Currently, Cal Poly Humboldt has an unrealiable waste audit data collection and storage system. The waste audit data is currently collected by various volunteers who record a few data points by hand about the waste. After it is collected, someone then creates a new waste audit each time, effectively meaning after the audit is presented, the data is not stored for future use. This not only is wasteful from a time perspective but also from any insights that could be gained by seeing larger campus-wide waste trends. While the data does provide many insights currently, having a more reliable and streamlined process that reduces subjectivity about data points, better visualizes the data, and stores this data properly will not only improve the insights gained from each audit but also the efficiency of each audit and their long term impact. 

- **Context:** From our meetings with Morgan King, we learned about various goals and challenges he has with the waste audits. King's main goals with the audits are to identify potential issues with the waste process, raise awareness about ways to reduce waste, and to ultimately reduce the amount of waste on campus. King's main challenges with the waste audits are he uses volunteers so the data collection needs to be simple so they can be easily trained to conduct the audits and the fact that waste practices change frequently in the county.

## 2. Systems to be Compared
 - **System A:** An Excel Spreadsheet data storage system
 - **System B:** An Oracle SQL relational database storage system 

## 3. Evalation Criteria & Methods
1. Ease of Setup: We will evalute this be recording how long it takes, how many steps it takes, and the overall difficulty of the setup. This will be evaluated by our tech lead and quality assurance.  
2. Ease of Use for Auditors (new and experienced): We will evaluate this metric by having a technical and non-technical person attempt to conduct an audit (likely mock test just to test system) and document any issues or suggestions they have. This will be handled by the quality assurance and the tech lead if they need to make changes to the system.  
3. Error Prevention / Data Quality: We will test what happens when we enter incorrect data types, illogical data or poor data, and test values that we expect to cause errors. This will primarily be evaluated by the quality assurance who will work with the tech lead to ensure any issues are addressed. 
4. Ability to Handle Relationships: We will test what happens to data integrity of the systems when neccessary data is purposely missing from entries. This will primarily be evaluated by the quality assurance who will work with the tech lead to ensure any issues are addressed. 
5. Scalability & Performance: We will test how easy it is to make changes to each system and how they perform doing tasks. This will be evaluated by the tech lead and quality assurance. 
6. Reporting & Analysis: We will record observations about the two systems and use these to evaluate which system is better. This will be handled mainly by the domain expert in collobaration with the project manager.
7. Integration with Campus IT: We will evaluate if our recommended system is able to be integrated with any current storage systems the Campus IT uses and the difficulty of giving them control of the system. This will be handled by the domain expert. 
8. Cost (Total Cost of Ownership): We will evaluate cost by recording any costs of the software neccessary for the systems and the potential time and cost for maintenance or upgrades to the systems. This will be handled by the domain expert. 
9. Maintenance After Setup: We will evaluate how taxing these systems are to maintain and if they need to be maintained by someone. Our domain expert will handle this criterion.

## 4. Sample Implementations to be Built
- **Spreadsheet Prototype:** Data will be entered into a Google Form and will then be exported to a Excel spreadsheet. 
- **Database Prototype:** Data will be entered into a website using various web applications and then entered into an Oracle SQL database schema. 

## 5. Data to be Collected for the Trial
- What sample data will you enter? We will use our recorded data from our audit we conducted on 9/11. If we need more data or we decide we want to collect other data points, we may conduct another audit. 
- How will you deliberately try bad data to test error prevention? We will test data that we know may cause errors like wrong input types, illogical values, and more to test for possible errors with our system.

## 6. Roles & Responsibilities
- **Tech Lead:** The tech lead will be responsible for setting up the two data storage systems, troubleshooting both systems, improving user experience with data input,  and ensuring the system is simple for others to modify and maintain. 
- **Project Manager:**
- **Domain Expert:**
- **Quality Assurance:**

## 7. Timeline
| Date | Tech Lead | Project Manager | Domain Expert | Quality Assurance|
|---|---|---|---|---|
|9/8 | Attend meeting with Morgan King; take notes on system requirements| Attend meeting; record action items| Attend meeting; ask questions about audit practices| Attend meeting; note data quality concerns|
|9/10| Help design system trial plan| Draft plan document and assign tasks for 9/11| Review plan for domain accuracy| Review plan for clairty and completeness|
|9/11| Record Data| | Record Observations| Record Data (double check with tech lead's afterward)|
|9/15| Work on and finish project plan| Work on and finish project plan| Work on and finish project plan| 
