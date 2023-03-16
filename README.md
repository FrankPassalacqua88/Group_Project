# Group_Project

## Overview

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

The process of cleansing data for utilization has now been completed.  

Datasets in original and cleansed format may be found within the [Resources folder](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/tree/main/Resources).  

A list of references from where the original data was sourced is available via the [Resource Hyperlinks](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/4bf8de5c99385051b0ad16081716bf3c53ba59b7/Resources/Hyperlinks/Resource_Hyperlinks.docx).

**Questions to be Answered**
1. Is there a correlation between a country's economic factors (GDP), demographics (population) and medal count?
2. Can we predict, based on an athlete's physical attributes and team (country), whether they'll place a medal?
3. Can the model determine if a hypothetical althlete would win?

**Description of Data Exploration**

The data exploration phase required that each member of the team roll up their sleeves and become acquainted with the data.  As we became familiar with our different sources, it became clear that certain files would be more beneficial than others to each of our individual tasks.  Although it had been cleansed, as we began to work with the data individually we also realized the data may have required additional modification, data merge or additional calculation to achieve those tasks.

**Description of the Analyis Phase**

During the analyis phase of the project the team began by discussing the ideas we had for the questions we wanted to answer.  We then attempted to mock up what tools, data and outputs we'd be seeking to achieve.  Thru trial and error on code, correction and modification to code, and by listening to the feedback of the fellow team members we continued to see progress daily. 

**Google Slides**

A draft version of the presentation is available in Google Slides: [Presentation](https://1drv.ms/p/s!AsgKvHxaT8bpmC03mzbFumuZ0agN?e=F3RH36)

### GitHub

The team has created a Github to house the project as we complete each milestone that includes the following:
- [x] A README.md to track progress status and final deliverable
- [x] A Resources folder to house all data (draft and cleansed)
- [x] An Admin folder to house meeting notes and agenda topics
- [x] An Images folder for the ERD and future graphics
- [x] Individual member folders for draft code
- [x] Folder for Final Dashboard and Presentation
- [ ] WIP - Additional files/folders to be discussed as needed

Additionally, the team has a rolling cycle of determining if/when meetings are needed and are actively utilizing slack and dedicated class time to communicate. Recap of the meeting schedule (to date) is below.
- [x] 2/23 - Initial meeting to discuss potential topics (Olympic data, Lottery, Food Stores) 
- [x] 2/27 - Finalize topic (Olympic data)
- [x] 2/28 - Class; enhance topic to include athlete bio data
- [x] 3/01 - Class; discuss Random Forest as machine learning model and assign team tasks
- [x] 3/05 - Check-in to review progress of each task
- [x] 3/06 - Subset meeting to discuss data intro
- [x] 3/07 - Class; round table to discuss status and address any issues
- [x] 3/09 - Class; round table to review chart status and initial RandomForest modeling results
- [x] 3/14 - Class; issue resolution and Panel dashboard discussion
- [x] 3/16 - Class; continue issue resolution and Panel dashboard to do's


A list of team tasks has been documented and can be viewed here: [Team Notes](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/4bf8de5c99385051b0ad16081716bf3c53ba59b7/Admin/Team_Notes.docx)

### Machine Learning Model

An initial provisional machine learning model, Random Forest, was explored by several team members to test for viability.  This utilizes draft data and returns an initial accuracy rating of between 30-40%.  The team discussed opportunities to improve this rating by merging and focusing on different data.  The team is hoping the feedback will move the model from a minimum viable product into a semi-final model, requiring only small tweaks thereafter.

Over the course of weeks 2 and 3, significant progress was achieved.  The model is now considered functional and includes a confusion matrix and accuracy score the team is satisfied with.  With additional data cleansing and modification, as well as adjustments to code, the accuracy is now sitting at +90%.   

A link to the model can be found here: [Provisional Machine Learning Model](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/d011f619eddb42940fc4c106471e63a7da366733/fp/RandomForest-MedalPredictor.ipynb)

### Database 

The final machine learning model and dashboard will primarily pull data in from cleansed CSV files.  After the datasets were located and exported, the team evaluated how each of the components of data related to one another via an [ERD](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/097e394fb11aaeb831c7b5a3930cc990cdd31402/images/ERD.png) and suggestions to cleanse and improve the data was discussed.  The cleansing was accomplished via Jupyter Notebook and Pandas and examples of how the data has been cleansed can be viewed via the below links:

1. [Cleaning Data File 1](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/42d9fbe2bd781425c091011fd1685999287671fa/wpf/Cleaning.ipynb)
2. [Cleaning Data File 2](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/42d9fbe2bd781425c091011fd1685999287671fa/wpf/Cleaning2.ipynb)
3. [Cleaning Data File 3](https://github.com/FrankPassalacqua88/Olympic_Data_Analysis/blob/b93ee9b55bb98d825a0c2eb33b12fb89544c7920/wpf/Cleaning3.ipynb)

Now that the files are ready for utlization they will be connected to the provisional machine learning model.

### Dashboard

After preliminary discussion, we believed we would utilize an html website to deliver the final presentation.  After additional discussion and research, we are now segwaying to test code using Panel as the dashboard.  We do have preliminary working models, however, in each instance we have hurdles to overcome to achieve full functionality.  For example, the widgets are not properly interactiving with the charts, or the team is unsatisfied with the dashboard layout.  There is much more to learn and achieve here prior to completion. To date we have achieved the following DRAFTS: 

- [x] Created a visual dashboard storyboard, available on Google Slides:  [Dashboard](https://1drv.ms/p/s!AsgKvHxaT8bpmChrwYOLs8rwNU-l?e=STcr98)
- [x] Can describe the tools that will be used to create the final dashboard, as seen on the storyboard and achieved via usage of the following: 
    1. Jupiter Notebook to house code
    2. Libraries including: Pandas, Hvplot, RandomForest, etc.
    3. Panel to be used for the dashboard
- [x] Final location of interactive elements are a work in progress but the goal is to include dropdown menus and animation frames that provide time lapses over portions of the data
