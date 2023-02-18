import csv

#writing a csv file
# f = open("./example.csv",'w', newline='') #create an example file object
# wtr = csv.writer(f) #writer object allows you to write a csv file

# wtr.writerow(['name', 'age', 'language'])

# name_list = ['Alice', 'Bob', 'Carol']
# age_list = [10,20,30]
# lang_list = ['Python', 'C', "Java"]

# for i in range(3):
#     name = name_list[i]
#     age = age_list[i]
#     language = lang_list[i]
#     wtr.writerow([name, age, language])

# f.close()

#read a csv file
# f = open('./example.csv', 'r')
# rdr = csv.reader(f)

# next(rdr)

# for row in rdr:
#     print(row)

# f.close()

#append a csv file
f = open('./example.csv', 'a', newline="")
wtr = csv.writer(f)
wtr.writerow(["Dan", 40, "C#"])
wtr.writerow(['Erin', 50, "C++"])

f.close()