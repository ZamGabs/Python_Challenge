# importing all dependencies
import os
import csv
# defining path - i am using it this way because it was not working for me 
PyBank=os.path.join('/Users/gabrielazamora/Python Challenge/Python_Challenge/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv')

# reading the csv file
with open(PyBank,'r') as csv_file:
    budget=csv.reader(csv_file)
    header=next(budget)
    print(header)
# defining variables
    total_months=0
    net_total=0
    profit_and_losses=[]
    average_changes=[]
    date=[]
    
    for columns in budget:
        total_months=total_months+1
        net_total=net_total+int(columns[1])
        profit_and_losses.append(columns[1])
        date.append(columns[0])
    for x in range(1,len(profit_and_losses)):
        change=int(profit_and_losses[x])-int(profit_and_losses[x-1])
        average_changes.append(change)
    print(total_months,average_changes,date)
    #profit_loss_change=sum(average_changes)/len(average_changes)
    #print(profit_loss_change)
    #greatest_increase=max(profit_loss_change)
    #greatest_decrease=min(profit_loss_change)
    #greatest_increase_date=date[average_changes.index(greatest_increase)+1]
    #greatest_decrease_date=date[average_changes.index(greatest_decrease)+1]
    #print(greatest_decrease,greatest_increase,greatest_decrease_date)