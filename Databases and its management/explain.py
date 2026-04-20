'''
The typical process of using an SQLite database can be summarized with the following 
pseudocode:
• Connect to the database: An SQLite database is stored in a file on the system’s disk. 
  This step establishes a connection between the program and a specific database file. 
  If the database file does not exist, it will be created.
• Get a cursor for the database: A cursor is an object that is able to access and manipulate the data in a database.
• Perform operations on the database: Once you have a cursor, you can access and 
  modify the data in the database as needed. You can use the cursor to retrieve data, 
  insert new data, update existing data, and delete data.
• Commit changes to the database: When you make changes to a database, those 
  changes aren’t actually saved in the database until you commit them. After performing any operations that modify the
  contents of a table, be sure to commit those 
  changes to the database.
• Close the connection to the database: When you are finished using the database, you 
  should close the connection.
'''
#LET'S CODE!...
import sqlite3
dbobj=sqlite3.connect('MyDataBase.db')
#by the previous two lines, we CREATED a databases(as it was not existed),
#and connect it with the object called 'dbobj'.
curobj=dbobj.cursor()
#you made an object thst has access to the database and can modify it.
#and also you can do the opperations in your database
'''
THE OPERATIONS ON THE DATABASE GOES HERE!
NOTE: the changes must been occured by the cursor object
'''
#once you finish modifying, you need to commit the changes made
dbobj.commit()
#if you decided to undo (ctrl + Z) for the changes, you can use:
dbobj.rollback()
dbobj.commit()#IMPORTANT; so you save the undo proccess you did
#so, shall we do a commit for each single change we made?
#You can the following method to (automaticize) the commit: 
dbobj.autocommit
#NOTE: we called the connection object, not the cursor one
dbobj.close()
#DONE!

#Another NOTE: if you want to connect (or create) a database in another path,
#then you need to attach the path with the connection sunction, like:
another_database=sqlite3.connect(r'C:\Users\M.ouda\OneDrive - Save the Children International\Desktop\IOW\python\learning stuff\another database.db')
another_database.close()
#=======================================================

#       --{CREATING TABLES}--
#In this time, we will create a table in our database:
conobj=sqlite3.connect('MyDataBase.db')
cursor_obj=conobj.cursor()
#THERE IS A MISSED SQL CODE MUST BE HERE. MOVE TO LINE 389 TO GET IT!
cursor_obj.execute('''
create table family(
                   MemmberID real primary key not null,
                   MemmberName text
                   )
''')
'''
let's have a deeper look on the SQL statement:
  /-->to create a table called "family"
 /--{ create table family( {here we add the data of the coulmns of the table}
                       MemmberID  real    primary key         not null,
                         NAME    DATATYPE   IS A PK?  ALLOWED FOR NULL VALUES?
                       MemmberName text
                       )
'''
conobj.commit()
#as we want to explain more, we will not close the current database
#=======================================================

#       --{ADDING DATA}--
#simply,that can be happened by using the following:
cursor_obj.execute('''
insert into family (MemmberID,MemmberName)
                   values(409669470,"islam")
''')
#to insert many values:
cursor_obj.execute('''
insert into family (MemmberID,MemmberName)
                   values(900621871,"mahmoud"),
                         (909085706,"sooma")
''')
#if all the data were not available at the current time,
#you can use the null value:
cursor_obj.execute('''
insert into family (MemmberID,MemmberName)
                   values(900621871,null),
''')

#PLEASE PAY ATTENTION HERE:
#when you want not to give the data directly or you want
#to recive data from the user and store it in variavbles
#and then pass those variables to the SQL statement, you 
#need to do the following:
MemmberID=int('enter the member ID: ')
MemmberName=int('enter the member name: ')
cursor_obj.execute('''
insert into family (MemmberID,MemmberName)
                   values( ? , ? ),'''
                #          |   |
                #          V   V         
                 , (MemmberID,MemmberName))
#the code is tested and executed previously, you acnt run here
#because of the explaining proccess

#NOTE that the string MUST be surrounded by double quotes
#as the SQL statement is surrounded by single quotes. got it?
conobj.commit()

#=======================================================

#       --{SQL INJECTION}--
#Have you ever asked yourself that why we cannot use any other 
#string formula else than the triple quotes one? for example the
#f'string' one or the concatination one? that refers to SQL injection.
#In SQL injection, the user can sometimes pass an SQL code insted of data
#which enables them to exit from the quotes and edit on the execution code
#and in short:HACKS YOU!. then what to do? the following:
#1. Make sure to use the triple quotes string (and don't phelosiphize and 
# use the f'string' methods, OK?)
#2. instead of asking the user for data and passing it directly to the SQL 
#statement, you can create a function that makes sure that it's valid and safe
#
#In general, this is a whole science called "Cyber Security", and we won't go
#deeper as the purpose of this chapter is to deliver an introduction into databases

#=======================================================

#       --{ QUERYING DATA WITH THE SQL SELECT STATEMENT}--
#Let's make a big table to make the selecting statement works well:
connect=sqlite3.connect('test.accdb')
cursor=connect.cursor()
cursor.execute('''
create table data1(ID real primary key not null,
                   name text, phoneNumber real)
''')
cursor.execute('''
insert into table data1(ID, name, phoneNumber)
               values(111,"asd",1111),
                    (222,"qwe",2222),
                    (333,"zxc",3333),
                    (444,"qwe",4444),
                    (555,"qaz",5555),
                    (666,"wsx",2222),
''')
connect.commit()

cursor.execute('''
select ID from data1 
''')
#===>returns the whole ID column
cursor.execute('''
select ID,name from data1 
''')
#===>returns the whole ID and name columns
cursor.execute('''
select * from data1 
''')
#===>returns the whole columns of the table whatever they are
cursor.execute('''
select ID from data1 where phoneNumber==1111
''')
#===>returns the ID columns which has the phoneNumber value of 1111
#NOTE: you can select a column basing on a condition in another different column
#NOTE: the relational (boolean) operators of python are the same for SQL also 
#(on addition to <> which means: "not equal to")

#   --{FETCHING THE RESULTS}--
#imagine that you are trying to buy tomatos, then SELECTING the wanted ones
#does NOT mean that they became yours till you pay and leave. so for programming...
#the SELECT statement determines the data and do NOT display them. to do so, we use 
#the FETCH three methods: 
cursor.fetchall()#display all the data
cursor.fetchone()#display one piece (line) of the data
cursor.fetchmany(3)# display a specific number of data 

#   --{SQL LOGICAL OPERATORS: AND & OR & NOT}--
#you can add those logical operators into the selection statement
#(or anyone in the CRUD system) IN THE "WHERE" SECTION. examples:
cursor.execute('''
select * from data1 where NOT ID == 111
''')
#===>returns all the data from table data1 which has an ID value else than 111
cursor.execute('''
select name from data1 where ID == 111 OR NOT phoneNumber == 3333
''')
#===>returns the names which has an ID of 111 or has a phoneNumber else than 3333

# --{prioreties of logical operators}--
#1. NOT >> 2. AND >> 3. OR >> 4. relational operators (> / < / >= / <= / == / != or <>)

#    --{STRING COMPARISON}--
#it's easy as you deploy the same cod eyou used before
cursor.execute('''
select ID from data1 where name=='qaz'
''')  
#now if you asked me that this method searches for the whole string, works as the following:
#name1= abcdef, name2= ABCDEF, name3= bcd
#select * from tabl 1 where name=='bcd' ===> only te value of name 3 will be shown
#so, ow to search for strings whose CONTAINS a specific string? we use the LIKE method
cursor.execute('''
select name from data1 where name like "%a%"
''')
#===>returns all the names which contain "a"

# --{SORTING RESULTS OF THE SELECT STATEMENT}--
#you can use the term "order by coulmn1" to arrange data basing in coulmn1
cursor.execute('''
select name from data1 order by ID
''')
#===> return the names arranged by their ID 

#    --{aggregate functions}--
#the agregate functions are some functions used in SQL to operate calculations
#in the data came from the select statement
cursor.execute('''
select sum(phoneNumber) from table1
''')
#===>returns the sum of the phone numbers together (letting the phoneNumber as int)
cursor.execute('''
select avg(phoneNumber) from table1
''')
#===>returns the average of the phone numbers together (letting the phoneNumber as int)
cursor.execute('''
select count(phoneNumber) from table1
''')
#===>returns the number of the phoneNumber columns (letting the phoneNumber as int)
cursor.execute('''
select max(phoneNumber) from table1
''')
#===>returns the highest value of the phoneNumber (letting the phoneNumber as int)
cursor.execute('''
select min(phoneNumber) from table1
''')
#===>returns the lowest value of the phoneNumber columns (letting the phoneNumber as int)

#=======================================================

#       --{UPDATING AND DELETING EXISTING ROWS}--
#the general formula of the updating statement:
'''
update table1
set column = value
where criteria
'''
# WARNING!!!: without esing the where statement, all the coulms will be updated
#example:
cursor.execute('''
update data1
set phoneNumber=1234
where ID == 111
''')
#HINT: it's recommended to use the primary key in the "where criteria" section

#   --{UPDATING MULTIPLE COLUMNS}--
#now, of course you area asking: shall I make a full updatins statement for each single 
#update I want to make? OF COURSE NO. you can vary the changes you want in the set section
#as thr following:
cursor.execute('update data1 set ID=666,name="rfv" where ID==222')

#NOTE that I used the single quotes + printed the SQL statements in one line

#    --{DETRMINING THE NUMBER OF ROWS UPDATED}--
#we can (unfortunetly) do that after commiting and using the following method (in the print statement)
connect.commit()
print(cursor.rowcount)
#=======================================================

#       --{DELETING ROWS WITH THE DELETE STATEMENT}--
#its general fomula is:
#'''delete from table1 where criteria'''
#WARNING!: as menteioned before, without the "where criteria" statement, the whole table will be deleted!
#examples:
cursor.execute('''
delete from table1 where ID==444
''')

#HINT: it's recommended to use the primary key in the "where criteria" section

#we can determine te number of rows deleted using the same method as updating
connect.commit()
print(cursor.rowcount)

#=======================================================

#       --{MORE ABOUT PRIMARY KEYS}--
'''
Here are some general rules to remember about primary keys:
• Primary keys must hold a value. They cannot be NULL.
• Each row's primary key value must be unique. No two rows in a table can have the 
  same primary key.
• A table can have only one primary key. However, multiple columns can be combined 
  create a composite key. We will discuss composite keys momentarily
'''
#    --{The RowID Column in SQLite and primary key types}--
#the RowID is a coulmn that defaultly considered as an INTEGER primary key and its
#name can be changed if you created a column with the same properties:
#"ColumnName INTEGER PRIMARY KEY". It has an autoincrement number, so if you typed:
#'''select * from table1''' it will appear if you applied the condition mentioned before
#and if you typed:'''select RowID from table1''' then and apllied the condition both at 
#once, then it will NOT recognize it! it's just a default name with default properties for
#the primary key

#    --{The composite key}--
#As you were a student in IUG, there is a number and a charachter for each classroom,
#now, imagine that the buildings has names instead of symbols, then neither the number
#of the room nor the building can be a primary key,you can solve it by many methods:
#1. depend on the RowID to get the primary key
#2. make a "composite key"
#Instead of having unique values in 1 coulmn, what about making it in 2 columns?
#like:
"""
1   ==>11     DID
2   ==>12     YOU
3   ==>21     GOT
4   ==>22     IT?
"""
#how to do it? do the following:
'''
create table2(
column1 datatype1,
column2 datatype2,
primary key(column1,column2)
)
'''
#NOTE:try to separate between the brackets of table2, primary key and cursor

#=======================================================

#       --{HANDLING DATABASE EXCEPTIONS}--
#Of course, as SQL is a language, the errors are potential, then the 
#"try except" term is required, this is how they work:
try:
    cursor.execute('''
delete from data2 where ID==888
''')
except sqlite3.OperationalError: 
    print('no table called "data2"')
#as you can see, here is an exeption raised. NOTE that SQLITE3 comes with its
#special exceptions. GOT IT?

#=======================================================

#       --{RELATIONAL DATA}--
#In short, when you have many tables in one database and some of the columns in 2 
#or more tables have te same data, then when you change a value in one table, you 
#will need to change the same value in all the tables, wich requires much time and
#effort.
#Relational data guarantees theintegrity if the database, so when you change the value
#in one table, it will also change in all the tables. theat can be done using something
#called: FOREIGN KEYS. A foreign key is a key whose a primary key in another table. we 
#have the following exmple:
#table teacher(teacherID:integer primary key, name:text, subject:text)
#table student(studentID:integer primary key, name:text, class:text)
#table lecture(lectureID:integer primary key, studentID: foreign key, teacherID:foreign key)
#now we have duplicated(or imported) data, so when we need to change the data, all the data
#will be changed. and the quistion is how to type the foreign key in SQL?
cursor.execute('''
create table nasayeb(nasayebID integer primary key
               ,nasayebName text)
''')
cursor.execute('''
create table zawaaj(zawaajID integer primary key,
               foreign key(El3arees references family (MemmberID)),
               foreign key(El3arosa references nasayeb(nasayebID)))
''')
#Let's explain closely:
"""
cursor.execute('''
create table zawaaj(zawaajID integer primary key,   }-----Everything here is OK and explained
               foreign key  (El3arees   references family (MemmberID)),
               foreign key  (El3arosa   references nasayeb(nasayebID)))
''')           ^^^^^^^^^^^   ^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
               |||||||||||   ||||||||   ||||||||||||||||||||||||||||
               creating a    the name   the source of the foreign key 
               foreign key   of the     (which is a primary key in
                             foreign     another table)
                             key in the
                             current 
                             table
"""
#I hope to understand the explaining! 

#    --{ENABLING FOREIGN KEY ENFORCEMENT IN SQLITE3}-- 

#CAUTION!!!: this topic contains many subtopics, so read the topic carefully.
#In the previous example, you need to add foreign kees and integrate them manually. In SQL, you
#can enforce the SQL integrity using the following code:

#cursor.execute('''pragma foreign_keys=on''') 

#this code doesn't incude a name of a table nor a column nor data, but it's a full SQL code. 
#ALSO, the place of this code MUST be originally after the cursor creation statement directly, or
#accurately in line 52.
#After typing this code, you can naturally complete doing everything you want
#NOTE: Any value added to the foreign key column MUST be available in the primary key column. So 
#when you add values to the table that contains the foreign keys, make sure that the values added 
#to the foreign key columns must be available in the primary key columns.
#So for the updating... look at this wrong example:
"""
cursor.execute('''
update table2
set table1ID=999999999
where table1Name='blah blah blah'
''')
"""
#in the previous example, we changed the value of the foreign key into a one that is not available 
#in the primary key column. To do so, you need to insert a new row with the primary key value you 
#want and go ahead... Got it?
#About deleting, you CANNOT delete a row of primary key that its value is referenced ("mentioned")
#as a foreign key in another table, because this will leave NULL values, to do so, delete the rows 
#with the foreign key value referenced to the primary key value you want to delete ... GOT IT? 

#    --{RERTIVING COLUMNS FROM MULTIPLE TABLES IN A SELECT STATEMENT}-- 
#Imagine that we have 2 columns (from 2 tables) in one databse, how wll we separate betwwn them when 
#we use SQL code (for selection or so what)? the answer is simple: replace "columnName" with 
# "tableName.columnName". here is how to work:
"""
cursor.execute('''
select table2.column1,table1.column1 
from table2,table1
where table2.column1 CRITERIA
''')
"""