'''
Write a program to generate a series of marks of 10 students. Give grace marks up to 3 marks of
those who are having marks between 30 to 33 marks and print the new list of the marks.
'''
import pandas as pd
std_marks = []
for i in range(1,11):
  m = int(input("Enter the marks:"))
  std_marks.append(m)
  s = pd.Series(index=range(1201,1211),data=std_marks)
  s[s==32]=s+1
  s[s==31]=s+2
  s[s==30]=s+3
  print("New List is:")
  print(s[s>=33])


##########################################
'''
Create a dataframe using lists.                                                                                           1
Display books for class XII.                                                                                                         1
Display the books whose price is more than 250.                                                                         1
Plot these data on line chart.
'''
import pandas as pd
import matplotlib.pyplot as mpp
#Answer 1
data={'BookID':['B0001','B0002','B0003','B0004','B0005','B0006'],\
      'Subject':['Computer Science','Computer Science','Computer Appllications',\
      'Informatics Practices','Artificial Intelligence','Informatics Practices'],\
      'Class':['XII','XII','X','XII','IX','XII'],\
      'Publisher':['NCERT','Dhanpat Rai','BPB','NCERT','KIPS','Oswal books'],\
      'Price':[270,340,120,270,340,299]}
books=pd.DataFrame(data)
#Asnwer 2
print("Class XII Books:")
print(books[books['Class']=='XII'].to_string(header=False,index=False))
print("***********************************************************")
#Asnwer 3
print("Books having price more than 250")
print(books[books['Price']>250].to_string(header=False,index=False))
#Answer 4
books.plot(x='Subject',y='Price',kind='bar')
mpp.show()


##########################################
'''
Create above table in MySQL.
Insert records.
To display the detail of class XII students in descending order of their marks.
Display all the details of students in ascending order of name.
Find the maximum marks of the student for each class.
Count the students class wise is display only those number who is more than 2.
Display unique cities from the table.
'''
create table students
(rollno int(4) primary key,
name varchar(20) not null,
class varchar(4),
dob date,
gender char(1),
city varchar(20),
marks float);
insert into students values (1, 'Naman', 'XII','1995/05/09','M','Anand',453)
select * from students order by marks desc;
select * from students order by name asc
select class,max(marks) from students group by class
select class,count(*) from students group by class having count(*)>2
select distinct city from students;


##########################################
'''
Considering the above dataframe answer the following queries by writing appropriate command in python pandas.
i. Add a new column named discount which is 10% of their bill amount.
ii. Add a row with row index 1008 as Rohan,Bharuch,6000,2011-04-01.
iii. Now plot a bar chart depicting the customer name on x-axis and their corresponding
bill amount on y-axis, with appropriate Graph title, x-axis title, y-axis title, gridlines
and color etc.
'''
import pandas as pd
import matplotlib.pyplot as plt
d={'cname':['Shruti','Tushar','Jay','Sameer','Mayank','Meena','Dhairya'],
   'city':['Ahmedabad','Baroda','Surat','Ahmedabad','Surat','Baroda','Ahmedabad'],
   'billamt':[9500,5300,4550,4000,8500,4300,3000],
   'tran_date':['2010-10-01','2010-01-04','2009-03-01','2009-04-01','2008-08-05','2008-08-06','2009-10-10']}
customer=pd.DataFrame(d)
#Answer 1
customer['discount']=customer['billamt']*0.10
print(customer)
#Answer 2
customer.loc[1008]=['Rohan','Bharuch',6000,'2011-04-01',600]
print(customer)
#Answer 3
plt.bar(customer['cname'],customer['billamt'],color=['r','g','b','c','m','y','k'])
plt.title("Report",color='Red')
plt.xlabel("Customer Names",color='Blue')
plt.ylabel("Bill Amount",color='Magenta')
plt.show()


##########################################
'''
Create below table “staff” and insert all records.
i. Display the difference of maximum and minimum salary of each section.
ii. Display the staff name, designation and date of joining who joins in the month of July and April.
iii. Display the records of staff in their descending order of salary.
iv. Show first 3 character of staff name.
v. Display the records of staff who is working since last 12 years
vi. Display power of length of staff name
'''
select max(salary)-min(salary) from staff group by section;
select sname,designation,dojoin from staff where monthname(dojoin) in ('April','July');
select * from staff order by salary desc;
select left(sname,3) from staff;
select * from staff where year(now())-year(dojoin)=12;
select power(length(sname),2) from staff;


##########################################
'''
 Write a program in python to create the following
 dataframe named “country” storing the following details:
 #Considering the above dataframe answer the following question by
 writing appropriatecommand in python pandas:
Display complete data for China and India.
Display Country, Population and BirthRate of Brazil and Pakistan.
Create a CSV File from the above data frame.
Now plot a bar chart depicting the Country on x-axis and their
corresponding Population on y-axis, with appropriate Graph title, x-axis title, y-axis title,
gridlines an color etc.
'''
import pandas as pd
import matplotlib.pyplot as plt
d={'country':['China','India','US','Indonasia','Brazil','Pakistan'],
   'population':[1379750000,1330780000,324882000,260581000,206918000,194754000],
   'birthrate':[12.00,21.76,13.21,18.84,18.43,27.62],
   'updatedate':['2010-10-01','2010-01-04','2009-03-01','2009-04-01','2008-08-05','2010-04-05']}
country=pd.DataFrame(d)
#Answer 1
print("Answer 1")
print(country[country['country']=='China'].to_string(header=False,index=False))
print(country[country['country']=='India'].to_string(header=False,index=False))
#Answer 2
print("Answer 2")
c=country.loc[:,['country','population','birthrate']]
print(c[c['country']=='Brazil'].to_string(header=False,index=False))
print(c[c['country']=='Pakistan'].to_string(header=False,index=False))
#Answer 3
plt.bar(country['country'],country['population'],color=['r','g','b','c','m','y','k'])
plt.title("Population Report")
plt.xlabel("Country")
plt.ylabel("Population")
plt.grid()
plt.show()
country.to_csv('country.csv')


##########################################
'''
Consider the table “Charity” and write SQL queries for the tasks that follow:
i) Display the name of week day when socks purchased.
ii) Display remainder after dividing price by qty
iii) Display the discount amount by 10% in two decimal places.
iv) Display the records of items purchased in the month 11.
v) Display maximum qty purchased from the table.
vi) Display itemname, price and qty in the descending order of price
vii) Display item_id, itemname and position of s in each itemname.
'''
select dayname(pdate) from charity;
select mod(price,qty) from charity;
select round(price*0.10,2) from charity;
select * from charity where month(pdate)=11;
select max(qty) from charity;
select itemname, price, qty from charity order by price desc;
select item_id,itemname, instr(itemname,'s') from charity;


##########################################                   Set 4
'''
Write a program in python to create the following dataframe named “employee” storing
the following details:
i. Display Name, Post and Salary for all employees earning more than 60000 .
ii. Add a new row of your choice data.
iii. Transfer these data from dataframe to csv named employees.csv.
iv. Now plot a multi-line chart depicting the Employee Name on x-axis and their corresponding Salary on
y-axis, with appropriate Graph title, x-axis title, y-axis title, legends and color etc.
'''
import pandas as pd
import matplotlib.pyplot as plt
d={'Ename':['Anil','Akshay','Ajay','Varun','Siddharth','Rajesh'],
   'Post':['Manager','Clerk','Manager','Analyst','Developer','Clerk'],
   'Salary':[65000,33000,75000,66000,60000,35000],
   'Dt_join':['2018-03-02','2018-05-01','2018-09-15','2018-04-11','2018-10-12','2018-06-12']}
employee=pd.DataFrame(d,index=[101,102,103,104,105,106])
#Answer 1
print("Answer 1")
em=employee.loc[:,['Ename','Post','Salary']]
print(em[em.Salary>60000].to_string(header=False,index=False))
#Answer 2
print("Answer 2")
employee.loc[employee.index[-1]+1]=['Ranveer','Analyst',65000,'2020-01-06']
print(employee.iloc[-1])
#Answer 3
employee.to_csv('employees.csv')
#Answer 4
plt.plot(employee['Ename'],employee['Salary'],color='r')
plt.title("Employee Analysis",color='blue')
plt.xlabel("Employee Names",color='red')
plt.ylabel("Salary",color='magenta')
plt.legend(['Salary'])
plt.show()


##########################################
'''
Create the table “employee” and write sql queries for the following:
a) Count and display employees post wise.
b) Display 3 characters from 2nd place from the column ename.
c) Display last 2 characters of post column.
d) Display ename in lower letters
e) Display most senior employee
'''
select post,count(*) from employee group by post;
select mid(ename,2,3) from employee;
select right(post,2) from employee;
select lower(ename) from employee;
select min(Dt_join) from employee;


##########################################    Set 5
'''
Write a Python code for following questions:
a) create above Data Frame “ved_medicines”
b) Display medicines and its price.
c) Display last 4 medicines
d) Display records of medicines whose price is more 20
e) Draw a bar chart which represent medicine name on x-axis and its price on y-axis.
'''
import pandas as pd
import matplotlib.pyplot as plt
d={'medicineid':[5147,5274,4296,4175,4385],
   'medicinename':['Paracetamol','D-Cold','Vicks Vaporub','Vicks Action 500','Soframycin'],
   'price':[15,20,45,15,85],
   'manufacturer':['Dwarkesh Pharma','Apollo Pharmacy','Procter & Gamble','Procter & Gamble','Sanofi']}
ved_medicines=pd.DataFrame(d)
#Answer 1
print("Answer 1")
print(ved_medicines.loc[:,['medicinename','price']].to_string(header=False,index=False))
#Answer 2
print("Answer 2")
print(ved_medicines.tail(4))
#Answer 3
print(ved_medicines[ved_medicines.price>20])
#Answer 4
plt.bar(ved_medicines['medicinename'],ved_medicines['price'],color=['r','g','b','c','y'])
plt.title("Medicine Report",color='blue')
plt.xlabel("Medicine Names",color='red')
plt.ylabel("Price",color='magenta')
plt.legend(['Price'])
plt.show


##########################################
'''
Observe the above medicine table and write queries for following:
a) Display the unique manufacturer from medicine
b) Display manufacturer and total price for each manufacturer
c) Display manufacturer and price in the ascending order of price
d) Display first 4 characters of medicinename which medicine id contains 5 as last digit
e) Display all medicine names in Capital letter
'''
select distinct(manufacturer) from medicines;
select manufacturer,sum(price) from medicines group by manufacturer;
select manufacturer,price from medicines order by price;
select left(medicinename,4) from medines where medicineid like '%5';
select upper(mdeicinename) from manufacturer;

