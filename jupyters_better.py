import os
import csv
import sys

csvpath = os.path.join("budget_data.csv")
print(csvpath)

with open(csvpath) as csvfile:
    budgetdata = csv.reader(csvfile, delimiter=",")
    
    next(budgetdata)
    budgetlist = list(budgetdata)
    
file =open("analysis.txt", "w")
text = "Financial analysis \n"
text += "---------------------------------------\n"

text += "Total Months: " + str(len(budgetlist)) + "\n"
    
totalvalue = sum([int(row[1]) for row in budgetlist])
text += "Total: $" + str(totalvalue)

newlist = [(int(budgetlist[x + 1][1]) - int(budgetlist[x][1])) for x in range(len(budgetlist) -1)]
text += "Average Change: $" + str(round(sum(newlist) / len(newlist),2)) + "\n"

text += "Greatest Increase in Profits: " + budgetlist[newlist.index(max(newlist)) + 1][0] + " $" + str(max(newlist)) + "\n"
text += "Greatest Decrease in Profits: " + budgetlist[newlist.index(min(newlist)) + 1][0] + " $" + str(min(newlist)) + "\n"

file.write(text)
file.close()