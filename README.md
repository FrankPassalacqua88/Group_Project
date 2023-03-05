# Group_Project

## Segment 1

### Presentation

**Topic**

Data Science & Analytics Capstone Project Topic: Olympic Medaling

**Reason for Selection**

The team reviewed and discussed 3 potential topics.  After exploring multiple datasets and considering the pros and cons of each, we decided to pursue Olympic Medaling. Collectively, we believed this dataset offered the most opportunity to demonstrate existing skills and expand our knowledge to test each theory.  After further conversation with our instructor, we decided to push ourselves beyond the economic factors and demographics and have incorporated analytics that will also focus on Olympic athlete data.

**Description of Data Source**

To date, we have found numerous sources to collect the following information:
- Olympic game data
- Country economic factors (GDP) and demographics (population)
- Olympic athletes bio and physical attributes

We are in the process of cleansing data for utilization.

A list of resources is available here: [Resource Hyperlinks](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/4bf8de5c99385051b0ad16081716bf3c53ba59b7/Resources/Hyperlinks/Resource_Hyperlinks.docx)

**Questions to be Answered**
1. Is there a correlation between a country's economic factors (GDP), demographics (population) and medal count?
2. Can we predict, based on an athlete's physical attributes and team (country), whether they'll place a medal?
3. Can we predict what % of medals a country might win when using economic factors and demographics?

### GitHub

The team has created a Github to house the project as we complete each milestone that includes the following:
- [x] A README.md to track progress status and final deliverable
- [x] A Resources folder to house all data (draft and cleansed)
- [x] An Admin folder to house meeting notes and agenda topics
- [x] Individual member folders for draft code
- [ ] WIP - Folder for Final Dashboard and Presentation
- [ ] WIP - Additional files/folders to be discussed as needed

Additionally, the team has a rolling cycle of determining if/when meetings are needed and are actively utilizing slack and dedicated class time to communicate. Recap of the meeting schedule (to date) is below.
- [x] 2/23 - Initial meeting to discuss potential topics (Olympic data, Lottery, Food Stores) 
- [x] 2/27 - Finalize topic (Olympic data)
- [x] 2/28 - Class; enhance topic to include athlete bio data
- [x] 3/01 - Class; discuss Random Forest as machine learning module and assign team tasks
- [x] 3/05 - Check-in to review progress of each task
- [ ] 3/06 - Subset meeting to discuss data intro
- [ ] 3/07 - Class; round table to discuss status and address any issues

A list of team tasks has been documented and can be viewed here: [Team Notes](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/4bf8de5c99385051b0ad16081716bf3c53ba59b7/Admin/Team_Notes.docx)

### Machine Learning Model

An initial provisional machine learning model, Random Forest, was explored by several team members to test for viability.  This utilizes draft data and returns an initial accuracy rating of between 30-40%.  The team discussed opportunities to improve this rating by merging and focusing on different data.  Results of the improvements will be forthcoming as we progress.

A link to the initial model can be found here: **ENTER LINK TO PROVISIONAL MACHINE LEARNING MODEL**

### Database 

The final machine learning model and dashboard will primarily pull data in from cleansed CSV files.  After the datasets were located and exported, the team evaluated how each of the components of data related to one another via an [ERD](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/097e394fb11aaeb831c7b5a3930cc990cdd31402/images/ERD.png) and suggestions to cleanse and improve the data was discussed.  The cleansing was accomplished via Jupyter Notebook and Pandas and examples of how the data has been cleansed can be viewed via the below links:

1. [Cleaning Data File 1](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/42d9fbe2bd781425c091011fd1685999287671fa/wpf/Cleaning.ipynb)
2. [Cleaning Data File 2](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/42d9fbe2bd781425c091011fd1685999287671fa/wpf/Cleaning2.ipynb)
3. [Cleaning Data File 3](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/b93ee9b55bb98d825a0c2eb33b12fb89544c7920/wpf/Cleaning3.ipynb)

Now that the files are ready for utlization they will be connected to the provisional machine learning model.

### Dashboard

After preliminary discussion, we believe we will utilize an html website to deliver the final presentation.  This is currently being tested for viability and will be determined shortly.
