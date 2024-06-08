## GoalScorersPython
Uses Python to Analyze and Filter European Football GoalScorer DataSet

# Statement
In this Project, I located a Dataset containing information regarding the top Goalscorers in Europe's best Football leagues. The set contains collective data from the last 10 seasons.
I then proceeded to use Python and Pandas to filter and clean the Provided Dataset

# Problem Statement
Clean, Filter, and Analyze the Large Dataset

# Dataset Used
The Dataset used contains a list of the best goalscorers in the top Football European leagues
The set contains 15 columns and over 400 rows
[Goalscorers.csv](https://github.com/user-attachments/files/15523835/Goalscorers.csv)

# OvervieW
THIS IS THE FINAL CODE TO USED TO CLEAN THE DATASET
[Goalscorers.txt](https://github.com/Jesusp123/GoalScorersPython/files/15397099/Goalscorers.txt)

# Process
1. import the Pandas library from Python to better analyze the dataset
   CODE-import pandas as pd
2. Use read_csv() to read the contents of the Dataset
3. Insert Two parameters into 1. The file that needs to be read 2. The Columns that the user wants to be displayed
  CODE-DS=pd.read_csv('Data.csv',usecols=["Country", "Player", "Matches_Played", "Mins", "Goals"])
4. Use DATAFRAME() To transform dataset into data frame
`CODE-df=pd.DataFrame(DS)
5. Create New column by dividing the Number of goals scored by the total number of minutes played
  df["Goals Every_Minutes"]=df["Mins"]/df["Goals"]-df[]=Dataframe and column you want to pull
 

