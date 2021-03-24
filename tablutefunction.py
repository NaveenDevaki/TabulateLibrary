##  hi.... everyone i am gona show you how tables can be created by using tabulate function


##step1: install the tabulate in your local python machine
## for that go to your cmd simply type pip install tabulate
## after open idle or your jupyter note book


##start with the Tabulate


from tabulate import tabulate
# your importing the tabulate

table=[["Name","Bob","Alice"],["age",21,23],["gender","Male","Male"]]

#i created a variable table and i created a list inside a list


print(tabulate(table))

#output:

#------  ----  -----
#Name    Bob   Alice
#age     21    23
#gender  Male  Male
#------  ----  -----


##second optional argument named headers defines the list of column headers to be used

table=[['Rajan',23],['Jhon',32]]
# created a table with parameters for my columns

headers=["Name","age"]
# created headers variable to store my data to the pointers

print(tabulate(table,headers))

#output:

#Name      age
#------  -----
#Rajan      23
#Jhon       32


#work with dict


print(tabulate({"Name":["alice","bob"],
                "age":[23,13]},headers="keys"))



#output
#Name      age
#------  -----
#alice      23
#bob        13


##Row indices


print(tabulate([["F",23],["M",34]],showindex='always'))


#-  -  --
#0  F  23
#1  M  34
#-  -  --



#we can give any formate to our tables

table=[['Bob',23],['Roy',24],['jhon',25],['Richard',27]]
headers=['Names','Age']
print(table,headers,tablefmt="grid")


##there are different formats avilable
##Thank you








