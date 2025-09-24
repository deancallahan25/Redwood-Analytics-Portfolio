# Project One - Comparing Data Collection & Storage Systems Plan V2.0


## Team Name & Members
### Redwood Analytics
- Tech Lead: Dean Callahan - dpc43@humboldt.edu
- Project Manager: Zachary Griffiths - zkg3@humboldt.edu
- Domain Expert: Evan Blem - eb335@humboldt.edu
- Quality Assurance: Jaiden Roe - jr650@humboldt.edu


## Project Title - Database for Zero Waste


## 1. Purpose & Context
- **Purpose:** Cal Poly Humboldt was recently recognized with a bronze Zero Waste Certification by the Post-Landfill Action Network. As one of a few universities to earn this certification, it is important to understand how it has achieved this and how it can improve further. One way it can show this information is with campus waste audits, making the need for an efficient and reliable data collection and storage system for these audits necessary. The waste audit data is currently collected by volunteers who manually record a limited set of data points. After it is collected, someone then creates a new waste audit each time, meaning no waste data is stored for future use except by informal methods. This not only is wasteful from a time perspective but also from any insights that could be gained by seeing larger campus-wide waste trends with differences between audits. Having a more reliable and streamlined process that reduces subjectivity about data points, better visualizes the data, and stores this data properly will not only improve the insights gained from each audit but also the efficiency of each audit and their long term impact.


- **Context:** 


From our meetings with Morgan King, the Office of Sustainabilities' Climate Action Analyst, we learned about various goals and challenges he has with the current waste audits. Mr. King's main goal with the audits is to identify issues with the campus waste systems in order to reduce total waste on campus. These audits can then be used to raise awareness in the community about proper waste practices and communicate information to University Administration and other groups. Mr. King's main challenge with the waste audits is a general lack of consistency between audits. Additionally, the audits are conducted by volunteers with varying skill sets meaning the data collection needs to be simple to use and also easy to modify as new waste practices are common at the county and university level. 


## 2. Systems to be Compared
- **System A:** An Excel Spreadsheet data storage system
- **System B:** An Oracle SQL relational database storage system


## 3. Evaluation Criteria & Methods
1. Ease of Setup: We will evaluate this by recording how long it takes, how many steps it takes, and the overall difficulty of the setup. This will be evaluated by our tech lead and quality assurance. (describe importance, it is vague what metrics are you evaluating by
2. Ease of Use for Auditors (new and experienced): We will evaluate this metric by having a technical and non-technical person attempt to conduct an audit (likely a mock test just to test the system) and document any issues or suggestions they have. This will be handled by the quality assurance and the tech lead if they need to make changes to the system. 
3. Error Prevention / Data Quality: We will test what happens when we enter incorrect data types, illogical data or poor data, and test values that we expect to cause errors. This will primarily be evaluated by the quality assurance who will work with the tech lead to ensure any issues are addressed.
4. Ability to Handle Relationships: We will test what happens to data integrity of the systems when necessary data is purposely missing from entries. This will primarily be evaluated by the quality assurance who will work with the tech lead to ensure any issues are addressed. 
5. Scalability & Performance: We will test how easy it is to make changes to each system and how they perform tasks. This will be evaluated by the tech lead and quality assurance. 
6. Reporting & Analysis: We will record observations about the two systems and use these to evaluate which system is better. This will be handled mainly by the domain expert in collaboration with the project manager. 
7. Integration with Campus IT: We will evaluate if our recommended system is able to be integrated with any current storage systems the Campus IT uses and the difficulty of giving them control of the system. This will be handled by the project manager and tech lead.
8. Cost (Total Cost of Ownership): We will evaluate the cost of the systems by recording or estimating any costs of the software or hardware necessary for the systems. Additionally, we will estimate the labor hours and the costs associated with having employees that are responsible for maintenance or upgrades to the systems. This will be done by the project manager in addition to the tech lead.
9. Maintenance After Setup: We will evaluate how taxing these systems are to maintain and if they need to be maintained by someone. Our domain expert will handle this criterion.


## 4. Sample Implementations to be Built
- **Spreadsheet Prototype:** Data will be entered into a Google Form and will then be exported to an Excel spreadsheet. The data will be structured with the columns being the names or descriptions of our data and the rows as the values of the data.
- **Database Prototype:** Data will be entered into a frontend website form (or google sheet if this proves too difficult) and then entered into an Oracle SQL database schema. The tables will be made of groups of related data points like weight and category and will have appropriate relations between tables.


## 5. Data to be Collected for the Trial
- What sample data will you enter? We will use our recorded data from our audit we conducted on 9/11. If we need more data or we decide we want to collect other data points, we may conduct another audit.
- How will you deliberately try bad data to test error prevention? We will test data that we know may cause errors like wrong input types, illogical values, and more to test for possible errors with our system.


## 6. Roles & Responsibilities
- **Tech Lead:** The tech lead is the main role responsible for the coding and technical aspects of the project. The tech lead will be responsible for setting up the two data storage systems based on an ERD/design schema, troubleshooting both systems, improving user experience with data input, and ensuring the system is simple for others to modify and maintain. The main deliverables the Tech Lead will be responsible for are the the ERD/design schema, the two data collection/database systems, and the report comparing the two systems. 
- **Project Manager:** The project manager will oversee and manage everyone's tasks, address problems the team encounters, and ensure the project is on schedule. The project manager will be responsible for communicating with stakeholders, coordinating waste audits or tests, and interacting with departments such as IT for handling the systems handoff. Costs of system analysis
- **Domain Expert:**  The domain expert is the main role concerned with the data quality and its logical relevance to waste audits. The domain expert will be responsible for creating. They will consider the main goals of the project, make sure the data collected is logical, decide what needs to be collected, and how the data can be visualized and summarized for it to have the most impact.
- **Quality Assurance:** The quality assurance will test the two prototypes, both personally and with a new user, review all work for clarity and mistakes, will need to recruit users for tests.


## 7. Final Deliverables
ERD/Design Schema (Domain Expert, Tech Lead)
Two Data Collection and Storage Systems (Tech Lead)
Simple visualizations of data for each system (Tech Lead, Domain Expert)
System/Data Tests (Quality Assurance, Tech Lead??) 
Information about Data Collection and Quality (Domain Expert, Quality Assurance)
Systems Analysis Report (Project Manager, Quality Assurance)
Comparing and recommending the best system for future use (Tech Lead)
System maintenance and system summaries (Project Manager, Tech Lead)
Includes information about cost


## 8. Timeline
| Date | Tech Lead | Project Manager | Domain Expert | Quality Assurance|
|---|---|---|---|---|
|9/8 | Attend meeting with Morgan King; take notes on system requirements| Attend meeting; record action items| Attend meeting; ask questions about audit practices| Attend meeting; note data quality concerns|
|9/10| Help design system trial plan| Draft plan document and assign tasks for 9/11| Review plan for domain accuracy| Review plan for clarity and completeness|
|9/11| Record Data| | Record Observations| Record Data (double check with tech leads afterward)|
|9/15| Work on and finish project plan| Work on and finish project plan| Work on and finish project plan|
|9/24| Finish revised project plan| Finish revised project plan | Finish revised project plan |Finish revised project plan|
|9/25| Design ERD/Design Schema & input form drafts| Conduct Second Audit | Conduct Second Audit| Conduct Second Audit|
|9/26| Finish ERD/Design Schema| Start outlining the project report| Finalize what data should be collected | Draft basic test cases|
|9/29| Have fully working forms| Have finished project report outline| Modify data fields of forms as necessary| Run basic test cases on form|
|10/1| Work on prototypes| Conduct check in with team, revise plan/timeline if necessary| | |
|10/2| Have working storage prototypes|contact IT to schedule meeting about system maintenance | | |
|10/3| Make improvements to prototypes| | | |
|10/6| Storage systems and forms finalized  | | | |
|10/8| Create sample uses of the system (show basic visualizations with the data)| Ideally meet with IT | | |
|10/9| Evaluate systems for report, automate basic data visualizations| | | |
|10/10| Draft report | Draft report | Have draft for all deliverables done | Have draft for all deliverables done |
|10/11| Have all systems fully operational, ready to give access/ownership to IT or Office of Sustainability| | |  |
|10/13| Revise report| handoff system to IT| |
|10/15| Final report changes due| Final report changes due| | |
|10/16| Final **minor** changes to deliverables| Final **minor** changes to deliverable | | |
|10/17| Final deliverables are due| Final deliverables are due| Final deliverables are due| Final deliverables are due|



