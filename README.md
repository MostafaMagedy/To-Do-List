# To-Do-List

This ToDoList for MIA Task 3.2

features:-
* adding tasks
* remove tasks
* edit tasks
* clear all tasks
* mark done or not done

using Pandas library to save task in csv file Tasks.csv
creating the file if not exist 

handling errors with clear explanation

some challenges I had during coding:-
* first I build the whole script to work with Lists ( on ram ) so I had to rebuild it to work with csv file
* sometimes csv file was creating the columns name again and again so I had to make the dataframe (df) global and created clearTasks function to clear the csv file except first row ( it contains the columns name ) and I saved it as a feature
