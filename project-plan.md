# Project One - Comparing Data Collection & Storage Systems Plan - V2.0

## Team Name & Members
### Redwood Analytics
- Tech Lead: Dean Callahan - dpc43@humboldt.edu
- Project Manager: Zachary Griffiths - zkg3@humboldt.edu
- Domain Expert: Evan Blem - eb335@humboldt.edu
- Quality Assurance: Jaiden Roe - jr650@humboldt.edu

## Project Title - Database for Zero Waste

## 1. Purpose & Context
- **Purpose:** Cal Poly Humboldt was recently recognized with a bronze Zero Waste Certification by the Post-Landfill Action Network. As one of a few universities to earn this certification, it is important to understand how it has achieved this and how it can improve further. One way it can show this information is with campus waste audits, making the need for an efficient and reliable data collection and storage system for these audits necessary. The waste audit data is currently collected by volunteers who manually record a limited set of data points. After it is collected, someone then creates a new waste audit each time, meaning no waste data is stored for future use, except by informal methods. Having a more reliable and streamlined process that reduces subjectivity about data points, better visualizes the data, and stores this data properly will not only improve the insights gained from each audit but also the long term impact and efficiency of each audit.

- **Context:** From our meetings with Morgan King, the Office of Sustainabilities' Climate Action Analyst, we learned about various goals and challenges he has with the current waste audits. Mr. King's main goal with the audits is to identify issues with the campus waste systems in order to reduce total waste on campus. These audits can then be used to raise awareness in the community about proper waste practices and communicate information to University Administration and other groups. Mr. King's main challenge with the waste audits is a general lack of consistency between audits. Additionally, the audits are conducted by volunteers with varying skill sets meaning the data collection needs to be simple to use and also easy to modify as new waste practices are common at the county and university level. 


## 2. Systems to be Compared
- **Spreadsheet Prototype:** Data will be entered into a Google Form and will then be exported to a Google Sheets spreadsheet. The data will be collected from a Google Form asking the user various questions that will give insight about the waste audit, such as the location, weight of each bag, and the weight of each individual category of waste in each bag. Within our spreadsheet, we will also collect timestamp data for each response as well. 

- **Database Prototype:** Data will be entered into a website form which prompts the users for various questions using html and javascript to collect data which then feeds into an Oracle SQL database. The questions that are prompted will collect the same information as the google form. The database will be built off our ERD/design schema which will include relationships between attributes and tables.

## 3. Evaluation Criteria & Methods
1. Ease of Setup: The ease of setup for each setup is an important consideration for each system as having a quick and easy system setup improves efficiency. To evaluate the ease of setup, we will document if any software needs to be installed, how easy it is to install, and how long it takes to install. This criterion will be evaluated by the Project Manager and Tech Lead.  

2. Ease of Use for Auditors: To represent actual auditors, we will conduct tests of our systems to ensure they are easy to use for all skill levels. To do this we will gather volunteers, including those with different skill levels, to conduct an audit using our data collections systems. We will document any suggestions or issues with the system, record how long the audit took, and if there were any errors with data. This criterion will be evaluated by the Quality Assurance and Domain Expert.  

3. Error Prevention/Data Quality: Having a system that can automatically deal with poor data quality or errors is important for having an efficient storage system. To test our systems ability to handle this, we will create various system and data tests which we will have as a final deliverable. Specific tests we will carry out include what happens when you enter incorrect data types, illogical data (ex. compost data in landfill), edge cases, duplicates, and when you don’t enter necessary data. This will be evaluated by the Quality Assurance, Domain Expert, and Tech Lead. 

4. Ability to Handle Relationships: Relationships between data points is extremely important for gathering insights about waste practices and visualizing trends over time. Ensuring our data storage systems have relationships between data that can be modified as needed is a necessity for a proper database. We will test that these relationships are functioning as expected based on our ERD/design schema. Specific tests we may do include testing what happens to data integrity when important data points are missing from entries and what happens when you create improper relationships. This will be evaluated by the Domain Expert and Tech Lead.

5. Scalability & Performance: Our goal with our system is to make a lasting audit 
format and data storage system that will be used for years to come. As such, our system must be able to handle large amounts of audit data and scale appropriately. We will evaluate scalability by testing how our systems perform with large-scale mock data sets. For the performance aspect, we will also be conducting real or test audits to see how our system performs with the data collection and then additional basic data analysis. This will be evaluated by the Quality Assurance and Tech Lead. 

6. Reporting & Analysis: We will write a systems analysis report which will summarize each data collection and storage system and ultimately recommend which to use. This report will evaluate each system based on other criteria/factors we record including system costs, system maintenance, user experience, and scalability and performance tests. Additionally, this report will show examples of analysis that's possible with the new systems such as automated basic data visualizations like in data over time and by location. This criteria will be worked on by all roles. 

7. Integration with Campus IT: We will set up meetings with IT to integrate our final data collection and storage system. In our meetings we will discuss how our storage system will be hosted, how current databases are already used, and how the audit data will be backed up. This will be done by the Project Manager and Tech Lead. 

8. Total Cost of Ownership: We will evaluate the cost of the systems by recording or estimating any costs of the software or hardware necessary for the systems. Additionally, we will estimate the labor hours and the costs associated with having employees that are responsible for maintenance or upgrades to the systems. This will be done by the Project Manager and Tech Lead.

9. Maintenance After Setup: System maintenance is an important factor that will influence which system we recommend for use. To evaluate which system is better, we will look at how much maintenance each system will need and the difficulty of maintaining them. To gauge the difficulty, we will estimate or test each system for factors like system updates, modifications to the system’s design schema, and how data is backed up. This criterion will be tested by the Project Manager and Tech Lead.

## 4 Implementations/Final Deliverables
-ERD/Design Schema (Domain Expert, Tech Lead)
-Two Data Collection and Storage Systems (Tech Lead)
-Simple visualizations of data for each system (Tech Lead, Domain Expert)
-System/Data Tests (Quality Assurance) 
-Information about Data Collection, Data Definitions, and Quality (Domain Expert, Quality Assurance)
-Systems Analysis Report (All)
    -Comparing and recommending the best system for future use (Project Manager, Domain Expert)
    -System Cost Analysis (Project Manager, Tech Lead)
    -System Maintenance and System Summaries (Project Manager, Tech Lead)


## 5. Data to be Collected for the Trial
- What sample data will you enter?: We will use our recorded data from our audit we conducted on 9/11 and 9/25, as well as large mock datasets created based on observations from buildings on campus. If we need more data or we decide we want to collect other data points, we may conduct a third audit. For our attributes we will collect building location, time, date, audit id, columns for the weight and percent volume for each category (landfill, mixed recycling, compost, etc.), and what (if any) hazardous materials were present. Additionally, we may collect information about the site waste process itself like what type of bins they use and if they have separate bins for paper towels. The exact definitions will be defined by the Domain Expert.   
- How will you deliberately try bad data to test error prevention?: We will create various test cases that we will document which includes deliberately bad data to test error prevention. Specific tests we will carry out include what happens when you enter incorrect data types, illogical data (ex. compost data in landfill), edge cases, duplicates, and when you don’t enter necessary data. 

## 6. Roles & Responsibilities
- **Tech Lead:** The tech lead role will be responsible for creating the two data collection and storage systems based on an ERD/design schema, ensuring the system is simple for others to modify and maintain, analyzing these systems, and creating data visualizations. The main deliverables they will be responsible for are the ERD/design schema, the two data collection/database systems, and the report comparing the two systems. 

- **Project Manager:** The project manager role will oversee and manage everyone's tasks, address problems the team encounters, and ensure the project is on schedule. They will also be responsible for communicating with stakeholders, coordinating waste audits, and interacting with departments such as IT for handling the systems handoff. The main deliverables they will be responsible for are the report comparing the two systems. 

- **Domain Expert:**  The domain expert role is the main role concerned with the data quality and its logical relevance to waste audits. They will consider the main goals of the project, make sure the data collected is logical, provide data definitions, decide what needs to be collected, and how the data can be visualized and summarized for it to have the most impact. The main deliverables they will be responsible for are the ERD/design schema, data collection and data definition information.

- **Quality Assurance:** The quality assurance role will be responsible for evaluating the functionality and reliability of our two data collection and storage systems. This will include creating error/validation tests, testing system performance, and real system tests with users. Additionally, they will review all deliverables for clarity,  logical, and consistency issues, with particular attention to the final report. The main deliverables they will be responsible for are tests, the report comparing the two systems, and data collection and quality information. 


## 7. Timeline
| Date | Tech Lead | Project Manager | Domain Expert | Quality Assurance|
|---|---|---|---|---|
|9/8 | Attend meeting with Morgan King; take notes on system requirements| Attend meeting; record action items| Attend meeting; ask questions about audit practices| Attend meeting; note data quality concerns|
|9/10| Help design system trial plan| Draft plan document and assign tasks for 9/11| Review plan for domain accuracy| Review plan for clarity and completeness|
|9/11| Record Data| Record Data| Record Observations| Record Data (double check with tech leads afterward)|
|9/15| Work on and finish project plan| Work on and finish project plan| Work on and finish project plan|
|9/24| Finish revised project plan| Finish revised project plan | Finish revised project plan |Finish revised project plan|
|9/25| Design ERD/Design Schema & input form drafts or Conduct Second Audit| Conduct Second Audit at Campus Marketplace| Conduct Second Audit| Conduct Second Audit|
|9/26| Finish ERD/Design Schema| Start outlining the project report| Finalize what data should be collected | Draft basic test cases|
|9/29| Have fully working forms| Have finished project report outline| Modify data fields of forms as necessary| Run basic test cases on form|
|10/1| Work on prototypes| Conduct team check in| Start drafting what insights we should show with data| Continue with testing database systems, recruit system testers|
|10/2| Have working storage prototypes (fully functional)|contact IT to schedule meeting about system maintenance |Ensure prototypes fit domain |Help with finalizing storage prototypes and error testing them |
|10/3| Make improvements to prototypes| Go through system with Morgan King and potential third waste audit| Test systems in practice either mock or real audit to ensure fits domain| Continue testing prototypes|
|10/6| Storage systems and forms finalized | Finalizing storage systems | Finalizing storage systems | Finalizing storage systems |
|10/8| Create sample uses of the system (show basic visualizations with the data)| Ideally meet with IT here|Work on data visualizations with a focus on ensuring they fit domain and goals| |
|10/9| Evaluate systems for report, automate basic data visualizations| | Work on data visualizations with a focus on ensuring they fit domain and goals| |
|10/10| Draft report | Draft report | Have draft for all deliverables done | Have draft for all deliverables done |
|10/11| Have all systems fully operational| Revise report| Revise deliverables |  Edit and revise report|
|10/13| Revise report| Conduct system handoff| Revise deliverables |Edit and revise report|
|10/15| Final report changes due| Final report changes due| Final report changes due |Final report changes due|
|10/17| Final deliverables are due| Final deliverables are due| Final deliverables are due| Final deliverables are due|



