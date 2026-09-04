import pandas as pd
from tabulate import tabulate
job_list = []
priority_list = []

print("Welcome to the Task Manager")
print("Enter task you want to add:")

try:
    Jobs = str(input("Enter Tasks:"))
    print("Enter Level of Priority: 1 for High, 2 for Medium, 3 for Low :")
    Priority = int(input())
except:
    print("Invalid input.")
    exit()

job_list.append(Jobs)
priority_list.append(Priority)
try:
    exit = str(input("Do you want to add more tasks? if yes just write yes OR type 'done' to exit:"))
except:
    print("Invalid input.")
    exit()

if Jobs == 'done':
    print("thank you for using the Task Manager")
else:
    while exit == 'yes':
        Jobs = str(input("Enter Tasks:"))
        job_list.append(Jobs)
        print ("Enter Level of Priority: 1 for High, 2 for Medium, 3 for Low")
        Priority = int(input())
        priority_list.append(Priority)
        print("Do you want to add more tasks? if yes just write yes OR type 'done' to exit")
        exit = str(input())

if Priority in [1, 2, 3]:
    data = {'Jobs': job_list, 'Priority': priority_list}
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by='Priority', ascending = True)

print(tabulate(sorted_df, headers='keys', tablefmt='grid', showindex = False))
