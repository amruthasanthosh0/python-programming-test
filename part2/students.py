import csv
def sortlist(key,marklist):
  sort=sorted(marklist,key=lambda x:int(x[key]),reverse=True)
  return sort

def displaytopper(marklist,subjects):
  for i in subjects:
    mark=sortlist(i,marklist)    
    print(f"""Topper in {i} is: {mark[0]['Name']}""")

def total(marklist,subjects):
  totalmark=[]
  for row in marklist:
    total=0
    for i in subjects:
       total+=int(row[i])
    d=dict(Name=row['Name'],Mark=total)
    totalmark.append(d)
  sort=sorted(totalmark,key=lambda x:int(x['Mark']),reverse=True)
  return totalmark
  
filename=input("Enter the csv filename")
with open(filename+'.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  studentlist=[]  
  for row in reader:
    studentlist.append(row)
subjects=['Maths','Biology','English','Physics','Chemistry','Hindi']
displaytopper(studentlist,subjects)
totalmark=total(studentlist,subjects)
print(f"""Best students in the class are :1. {totalmark[0]['Name']},  2. {totalmark[1]['Name']},  3. {totalmark[2]['Name']}""")


