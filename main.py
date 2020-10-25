import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()
maxsalery = 1000.00

def adduser(name, surname, salary):
    c.execute("insert into users (name, surname, salary) values ('%s', '%s', '%s')" %(name, surname, salary))
    conn.commit()


c.execute("create table if not exists users (id integer primary key not null, name varchar(255), surname varchar(255), salary float)")
conn.commit()
name = input("Enter user name: ")
surname = input("Enter user surname: ")
salary = input("Enter user salary: ")
while float(salary) > maxsalery:
    salary = input("Enter user salary more litle: ")

adduser(name, surname, salary)

print("Users list: \n")
c.execute('select * from users')
ulist = c.fetchone()

while ulist is not None:
    print("id: "+str(ulist[0]) + " Name: "+str(ulist[1]) + " Surname: "+str(ulist[2])+ " Salary: "+str(ulist[3]))
    ulist = c.fetchone()

c.close()
conn.close()