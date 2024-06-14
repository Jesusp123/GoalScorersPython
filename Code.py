#Takes File and Extracts data of GoalScorers throughout Europe
import pandas as pd
DA=pd.read_csv('GoalScorers.csv')
print("Original Unaltered DataSet")
print(DA.head(5).to_string(),'\n')
#Filters out unimportant Data and returns dataframe
DS=pd.read_csv('GoalScorers.csv',usecols=["Country","Player Names","Matches_Played","Mins","Goals","Year"])
df=pd.DataFrame(DS)
print("Filtered and Turned into DataFrame")
print(df.head(5).to_string(),'\n')
#Creates Column for Avg minutes it takes a player to score a goal
df["Goals Every_Minutes"]=df["Mins"]/df["Goals"]
print("Add Nevv Column by dividing data in Other Columns")
print(df.head(5).to_string(),'\n')
#Takes a group of Countries and uses them to filter data
GE=["England","Spain","Germany","Italy"]
mi=df[df["Country"].isin(GE)]
print("Filtered out Data Based on Specific Countries:England,Germany,Italy,Spain")
print(mi,'\n')
#Sorts Filtered data by goals and total mins played
mi1=mi.sort_values(by=["Goals","Mins"],ascending=False)
print("Sorts data by Goals and Then by Mins")
print(mi1.head(10).to_string(),'\n')
#Returns players VVith more than 20 goals
mi2=mi1[mi1["Goals"]>20]
print("Players VVith over 20 Goals")
print(mi2.head(10).to_string(),'\n')
#Resets index to 0
mi2.reset_index(inplace=True,drop=True)
print("Resets index to 0")
print(mi2.head(10).to_string(),'\n')
#Prints all players vvho play in France
lig=df[df["Country"]=="France"]
print("Prints Data from French League Players")
print(lig.head(10).to_string(),'\n')
#Prints all leagues
lea=df["Country"]
er=lea.unique()
print("Prints all Countries in altered Dataset")
print(er,'\n')
#Sorts by Goal Every _ Minutes
pd=df.sort_values(by=['Goals Every_Minutes'])
print("Sorted Data based on Goals Every_Minutes")
print(pd.head(10).to_string())
#Filter Bundesliga and sort by Goals
bun=df[df["Country"]=="Germany"]
bun1=bun.sort_values(by=["Goals"],ascending=False)
print("Returns bundesliga Data Sorted by Goals")
print(bun1.head(10).to_string(),'\n')
#Filter Premier League and sort by Goals
prem=df[df["Country"]=="England"]
prem1=prem.sort_values(by=["Goals"],ascending=False)
print("Returns Premier League Data Sorted by Goals")
print(prem1.head(10).to_string())

