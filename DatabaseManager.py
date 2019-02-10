class Databasemanager():
# /usr/bin/env python3
import pymysql

def get_input_num():
    num = int(input("Enter a number: "))
    return num

def update_oxygen(mycursor):
  data = input("Enter a data to update: ")
  date= input("Enter a time to update: ")
  mycursor.execute("INSERT INTO oxygen(time, num) "
                   "VALUES (%s, %s)"%(repr(date),repr(data)))
  conn.commit()
  #close database
  conn.close()

def update_pressure(mycursor):
  data = input("Enter a data to update: ")
  date= input("Enter a time to update: ")
  mycursor.execute("INSERT INTO pressure(time, num) "
                   "VALUES (%s, %s)"%(repr(date),repr(data)))
  conn.commit()
  #close database
  conn.close()

def update_pulse(mycursor):
  data = input("Enter a data to update: ")
  date= input("Enter a time to update: ")
  mycursor.execute("INSERT INTO pulse(time, num) "
                   "VALUES (%s, %s)"%(repr(date),repr(data)))
  conn.commit()
  #close database
  conn.close()

def query_oxygen(mycursor):
  date = input("Enter a date to query: ")
  mycursor.execute("select*from oxygen where time=(%s)" %repr(date))
  results = mycursor.fetchall()
  for row in results:
      date = row[1]
      num = row[2]
      print ("date=%s,num=%s" % \
             (date, num ))
  conn.commit()
  return
  #close database
  conn.close()

def query_pressure(mycursor):
  date = input("Enter a date to query: ")
  mycursor.execute("select*from pressure where time=(%s)" %repr(date))
  results = mycursor.fetchall()
  for row in results:
      date = row[1]
      num = row[2]
      print ("date=%s,num=%s" % \
             (date, num ))
  conn.commit()
  return
  #close database
  conn.close()

def query_pulse(mycursor):
  date = input("Enter a date to query: ")
  mycursor.execute("select*from pulse where time=(%s)" %repr(date))
  results = mycursor.fetchall()
  for row in results:
      date = row[1]
      num = row[2]
      print ("date=%s,num=%s" % \
             (date, num ))
  conn.commit()
  return
  #close database
  conn.close()

# connect to the local database and users need to change the password to their own ones.
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Gary", charset="utf8")
mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE if not exists  EC500")
mycursor.execute("USE EC500")
mycursor.execute("CREATE TABLE IF NOT EXISTS oxygen(`id` INT UNSIGNED AUTO_INCREMENT, `time` DATE, `num` VARCHAR(255) NOT NULL, PRIMARY KEY (`id`))")
mycursor.execute("CREATE TABLE IF NOT EXISTS pressure(`id` INT UNSIGNED AUTO_INCREMENT, `time` DATE, `num` VARCHAR(255) NOT NULL, PRIMARY KEY (`id`))")
mycursor.execute("CREATE TABLE IF NOT EXISTS pulse(`id` INT UNSIGNED AUTO_INCREMENT, `time` DATE, `num` VARCHAR(255) NOT NULL, PRIMARY KEY (`id`))")
print("Menu:\n1.update_oxygen\n2.update_pressure\n3.update_pulse \n4.query_oxygen\n5.query_pressure\n6.query_pulse")
data=get_input_num();
if (data==1):
    update_oxygen(mycursor)
elif (data==2):
    update_pressure(mycursor)
elif (data==3):
    update_pulse(mycursor)
elif (data==4):
    query_oxygen(mycursor)
elif (data==5):
    query_pressure(mycursor)
elif (data==6):
    query_pulse(mycursor)
