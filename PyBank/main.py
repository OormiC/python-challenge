import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data_list = [row for row in csvreader]
    data_list.pop(0)
    total_months = len(data_list)#Q1
    monthly_amount = [int(i[1]) for i in data_list]
    total = sum(monthly_amount)#Q2

    change_list = []
    for index in range(len(monthly_amount)-1):
        change = monthly_amount[index+1] - monthly_amount[index]
        change_list.append(change)
    average_change = round(sum(change_list)/len(change_list),2) #Q3(need to round to 2dp)
    
    max_increase = change_list[0]
    for num in change_list:
        if num > max_increase:
            max_increase = num #Q4 val

    max_decrease = change_list[0]
    for num in change_list:
        if num < max_decrease:
            max_decrease = num #Q5 val

    monthly_change = [[i[0]] for i in data_list]
    monthly_change.pop(0)
    for i in range(len(monthly_change)):
        monthly_change[i].append(change_list[i])
        
    for i in monthly_change:
        if i[1] == max_increase:
            max_increase_date = i[0]
        elif i[1] == max_decrease:
            max_decrease_date = i[0]
    
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total))
print("Average Change: $" + str(average_change))
print(f"Greatest Increase in Profits: {max_increase_date} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${str(max_decrease)})")

output_path = os.path.join("analysis", "analysis.csv")
with open(output_path, 'w') as csvfile:
    
    csvfile.write("Financial Analysis" + '\n')
    csvfile.write("----------------------------" + '\n')
    csvfile.write("Total Months: " + str(total_months)+ '\n')
    csvfile.write("Total: $" + str(total) + '\n')
    csvfile.write("Average Change: $" + str(average_change) + '\n')
    csvfile.write(f"Greatest Increase in Profits: {max_increase_date} (${str(max_increase)})" + '\n')
    csvfile.write(f"Greatest Decrease in Profits: {max_decrease_date} (${str(max_decrease)})" + '\n')
    
    

    
    

    
    
    
    


    

        


    
