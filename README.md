## GoalScorersPython
Uses Python to Analyze and Filter European Football GoalScorer DataSet

# Statement
In this Project, I located a Dataset containing information regarding the top Goalscorers in Europe's best Football leagues. The set contains collective data from the last 10 seasons.
I then proceeded to use Python and Pandas to filter and clean the Provided Dataset

# Problem Statement
Clean, Filter, and Analyze the Large Dataset

# Dataset Used
The Dataset used contains a list of the best goalscorers in the top Football European leagues.
The set contains 15 columns and over 400 rows.
[Goalscorers.csv](https://github.com/user-attachments/files/15523835/Goalscorers.csv)

A Filtered dataset VVas used to make analysis faster and easier.
The set contains 6 columns and over 400 rows.
[Altered.csv](https://github.com/user-attachments/files/15831700/Altered.csv)


# OvervieW
THIS IS THE FINAL CODE TO USED TO CLEAN THE DATASET
[Code.txt](https://github.com/user-attachments/files/15831709/Code.txt)
# Process
1. import the Pandas library from Python to better analyze the dataset
   CODE-import pandas as pd
2. Use read_csv() to read the contents of the Dataset 
   Code-DA=pd.read_csv('GoalScorers.csv')
   print("Original Unaltered DataSet")
   print(DA.head(5).to_string(),'\n')
3. Filter the dataset using read_csv() so it only includes important data
4. Insert Two parameters. 1. The file that needs to be read 2. The Columns that the user wants to be displayed
  CODE-DS=pd.read_csv('Data.csv',usecols=["Country", "Player", "Matches_Played", "Mins", "Goals","Year"])
5. Use DATAFRAME() To transform the dataset into a data frame and print it out
`  CODE-df=pd.DataFrame(DS)
   print("Filtered and Turned into DataFrame")
   print(df.head(5).to_string(),'\n')
7. Create a New column by dividing the Number of goals scored by the total number of minutes played
  df["Goals Every_Minutes"]=df["Mins"]/df["Goals"]-
   df[]=Dataframe and column you want to pull
8. Filter down the dataset by returning data from specific countries
   GE=["England","Spain","Germany","Italy"]
   mi=df[df["Country"].isin(GE)]
9. Sort the filtered data First by Goals and if two or more players share the number of goals filter them by minutes played
 `mi1=mi.sort_values(by=["Goals","Mins"],ascending=False)
10. Looks at the filtered dataset and returns any player with more than 20 goals
   mi2=mi1[mi1["Goals"]>20]
11. Resets the index of the new dataset and starts from Zero
    mi2.reset_index(inplace=True,drop=True)
12. Print all stats from players in France
    lig=df[df["Country"]=="France"]

