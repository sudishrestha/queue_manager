import RPi.GPIO as GPIO
import time
import os
from fpdf import FPDF
import datetime
import subprocess
from time import gmtime, strftime
import MySQLdb
import serial
import requests
from multiprocessing import Process


try:
    ser = serial.Serial("/dev/ttyACM0",9600);
except:
    try:
        ser = serial.Serial("/dev/ttyACM1",9600);
    except:
        print("Diplay Controller not found");
copss = "C00xx,C00xx,C00xx,C00xx,C00xx,C00xx,C00xx,C00xx,C00xx,C00xx"
coupon = "xx"
ramp1="xx"
ramp2 = "xx"
ramp3 ="xx"
ramp4 ="xx"
ramp5="xx"
ramp6 = "xx"
ramp7 ="xx"
ramp8 ="xx"
ramp9="xx"
ramp10 = "xx"
shortcut = "xx"

def getMech(ramp):
    
    global shortcut
    shortcut="xx"
    db= MySQLdb.connect("localhost", "sudish", "shrestha", "qms")
    cursor = db.cursor()
    sql = "SELECT * FROM mechanic_data where ramp="+str(ramp)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          id = row[0]
          shortcut = row[2]
          
          # Now print fetched result
          
    except:
       print ("Error: unable to fetch data")

    # disconnect from server
    db.close()
    return shortcut;
    
    


ramp1 = getMech(1)
ramp2 = getMech(2)
ramp3 = getMech(3)
ramp4 = getMech(4)
ramp5 = getMech(5)
ramp6 = getMech(6)
ramp7 = getMech(7)
ramp8 = getMech(8)
ramp9 = getMech(9)
ramp10 = getMech(10)


def getDataa():
    global copss
    return copss


def getcoupon():
    global coupon
    db= MySQLdb.connect("localhost", "sudish", "shrestha", "qms")
    cursor = db.cursor()

    
    sql = "SELECT * FROM copon_codes where enable=1 LIMIT 1"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          id = row[0]
          coupon = row[1]
          enable = row[2]
          # Now print fetched result
          
    except:
       print ("Error: unable to fetch data")

    # disconnect from server
    db.close()
    print("coupon code is " + coupon)
    printcoupon(coupon)

    
    
    return coupon



def printcoupon(coup):
    idss = coup[1:]
    try:
        r=requests.get("http://192.168.1.114:1300/printserver?id="+idss)
    except:
        print("no printer found")
    db = MySQLdb.connect("localhost","sudish","shrestha","qms" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE copon_codes SET enable =0 where coupon_number='"+coup+"'"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
    cursor = db.cursor()
    sql = "INSERT INTO `coupon_detail` (`id`, `coupon_id`, `job_card`, `created_date`, `start_time`, `finish_time`, `ramp`) VALUES (NULL, '"+idss+"', '', '"+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"', '"+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"', '"+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"', '0');"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

# disconnect from server


    db.close()

def nextcoupon(ramp):
    global copss
    global ramp1
    global ramp2
    global ramp3
    global ramp4
    global ramp5
    global ramp6
    global ramp7
    global ramp8
    global ramp9
    global ramp10
    
    ramp1 = getMech(1)
    ramp2 = getMech(2)
    ramp3 = getMech(3)
    ramp4 = getMech(4)
    ramp5 = getMech(5)
    ramp6 = getMech(6)
    ramp7 = getMech(7)
    ramp8 = getMech(8)
    ramp9 = getMech(9)
    ramp10 = getMech(10)
    
    #print(copss)
    coupon = "C00"
    db= MySQLdb.connect("localhost", "sudish", "shrestha", "qms")
    cursor = db.cursor()
    sql = "SELECT * FROM copon_codes where enable=0 LIMIT 1"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          id = row[0]
          coupon = row[1]
          enable = row[2]
          # Now print fetched result
          print(coupon)
    except:
       print ("Error: unable to fetch data")
       
    couponData = copss
    db= MySQLdb.connect("localhost", "sudish", "shrestha", "qms")
    cursor = db.cursor()
    sql = "SELECT * FROM display_data where id=1 LIMIT 1"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          id = row[0]
          couponData = row[1]
          # Now print fetched result
          print(coupon)
    except:
       print ("Error: unable to fetch data")

    # disconnect from server
    print("Data from db is "+ couponData)
    tempData = couponData.split(",")
    db.close()
    if ramp == "1":
        copss = coupon+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "2":
        copss = ""+tempData[0][:-2]+ramp1+","+coupon+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "3":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+coupon+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "4":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+coupon+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "5":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+coupon+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "6":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+coupon+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "7":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+coupon+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "8":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+coupon+ramp8+","+tempData[8][:-2]+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "9":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+coupon+ramp9+","+tempData[9][:-2]+ramp10
    if ramp == "10":
        copss = ""+tempData[0][:-2]+ramp1+","+tempData[1][:-2]+ramp2+","+tempData[2][:-2]+ramp3+","+tempData[3][:-2]+ramp4+","+tempData[4][:-2]+ramp5+","+tempData[5][:-2]+ramp6+","+tempData[6][:-2]+ramp7+","+tempData[7][:-2]+ramp8+","+tempData[8][:-2]+ramp9+","+coupon+ramp10
    print(copss)
    
    try:
        ser.write(copss)
        
    except:
        print("Display controller not found")
    db = MySQLdb.connect("localhost","sudish","shrestha","qms" )
    
    
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql1 = "UPDATE `display_data` SET `data` = '"+copss+"' WHERE `display_data`.`id` = 1;"
    print (sql1)
    try:
       # Execute the SQL command
       cursor.execute(sql1)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE copon_codes SET enable =2 where coupon_number='"+coupon+"'"
    sql1 = "UPDATE `display_data` SET `data` = '"+copss+"' WHERE `display_data`.`id` = 1;"
    try:
       # Execute the SQL command
       cursor.execute(sql)
       cursor.execute(sql1)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
    
       
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    idss = coupon[1:]
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()));
    # Prepare SQL query to UPDATE required records
    sql = "UPDATE coupon_detail SET start_time = '"+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"' , ramp ='"+ramp+"' where coupon_id='"+idss+"'"
    print(sql)
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Commit your changes in the database
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()
    
    # disconnect from server
    db.close()

    
    
    return coupon

    
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO17
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO21
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO22
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO24

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO17
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO21
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO22
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO24
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #LED to GPIO24

GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.HIGH)
tdata = 0;


def button1():
    prs1 = 0
    while True:
        button_state = GPIO.input(26)
        if button_state == False:
            prs1 = prs1 +1
            time.sleep(0.5)
        if prs1 == 6:
            print("3 second pressed in Ramp1")
            Process(target=nextcoupon, args=('1',)).start()
            #nextcoupon("1")
        if button_state == True:
            prs1=0

def button2():
    prs2 = 0
    while True:
        button_state = GPIO.input(19)
        if button_state == False:
            prs2 = prs2 +1
            time.sleep(0.5)
        if prs2 == 6:
            print("3 second pressed in Ramp2")
            Process(target=nextcoupon, args=('2',)).start()
            #nextcoupon("2")
        if button_state == True:
            prs2=0

def button3():
    prs3 = 0
    while True:
        button_state = GPIO.input(22)
        if button_state == False:
            prs3 = prs3 +1
            time.sleep(0.5)
        if prs3 == 6:
            print("3 second pressed in Ramp3")
            Process(target=nextcoupon, args=('3',)).start()
            #nextcoupon("3")
            
        if button_state == True:
            prs3=0

def button4():
    prs4 = 0
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            prs4 = prs4 +1
            time.sleep(0.5)
        if prs4 == 6:
            print("3 second pressed in Ramp4")
            Process(target=nextcoupon, args=('4',)).start()
            #nextcoupon("4")
            
        if button_state == True:
            prs4=0

def button5():
    prs5 = 0
    while True:
        button_state = GPIO.input(17)
        if button_state == False:
            prs5 = prs5 +1
            time.sleep(0.5)
        if prs5 == 6:
            print("3 second pressed in Ramp5")
            Process(target=nextcoupon, args=('5',)).start()
            #nextcoupon("5")
            
        if button_state == True:
            prs5=0

def button6():
    prs6 = 0
    while True:
        button_state = GPIO.input(25)
        if button_state == False:
            prs6 = prs6 +1
            time.sleep(0.5)
        if prs6 == 6:
            print("3 second pressed in Ramp6")
            Process(target=nextcoupon, args=('6',)).start()
            #nextcoupon("6")
            
        if button_state == True:
            prs6=0


def button7():
    prs7 = 0
    while True:
        button_state = GPIO.input(5)
        if button_state == False:
            prs7 = prs7 +1
            time.sleep(0.5)
        if prs7 == 6:
            print("3 second pressed in Ramp7")
            Process(target=nextcoupon, args=('7',)).start()
            #nextcoupon("7")
            
        if button_state == True:
            prs7=0

def button8():
    prs8 = 0
    while True:
        button_state = GPIO.input(13)
        if button_state == False:
            prs8 = prs8 +1
            time.sleep(0.5)
        if prs8 == 6:
            print("3 second pressed in Ramp8")
            Process(target=nextcoupon, args=('8',)).start()
            #nextcoupon("8")
            
        if button_state == True:
            prs8=0

def button9():
    prs9 = 0
    while True:
        button_state = GPIO.input(16)
        if button_state == False:
            prs9 = prs9 +1
            time.sleep(0.5)
        if prs9 == 6:
            print("3 second pressed in Ramp9")
            Process(target=nextcoupon, args=('9',)).start()
            #nextcoupon("9")
            
        if button_state == True:
            prs9=0

def button10():
    prs10 = 0
    while True:
        button_state = GPIO.input(6)
        if button_state == False:
            prs10 = prs10 +1
            time.sleep(0.5)
        if prs10 == 6:
            print("3 second pressed in Ramp10")
            Process(target=nextcoupon, args=('10',)).start()
            #nextcoupon("10")
            
        if button_state == True:
            prs10=0

def couponButton():
    while True:
        button_state = GPIO.input(24)
        if button_state == False:
            print('Coupon Button Pressed...')
            getcoupon()
            time.sleep(0.5)
'''    
def buttoner():
    while True:
        button_state = GPIO.input(26)
        if button_state == False:
            print('Ramp 1 Button Pressed...')
            nextcoupon("1")
            time.sleep(0.5)     
            
        button_state = GPIO.input(19)
        if button_state == False:
            print('Ramp 2 Button Pressed...')
            nextcoupon("2")
            time.sleep(0.5)
        
        button_state = GPIO.input(22)
        if button_state == False:
            print('Ramp 3 Button Pressed...')
            nextcoupon("3")
            time.sleep(0.5)
        
        button_state = GPIO.input(23)
        if button_state == False:
            print('Ramp 4 Button Pressed...')
            nextcoupon("4")
            time.sleep(0.5)
        
        button_state = GPIO.input(17)
        if button_state == False:
            print("Ramp 5 Button pressed")
            nextcoupon("5")
            time.sleep(0.5)
        
        button_state = GPIO.input(25)
        if button_state == False:
            print("Ramp 6 Button pressed")
            nextcoupon("6")
            time.sleep(0.5)
        
        button_state = GPIO.input(5)
        if button_state == False:
            print("Ramp 7 Button pressed")
            nextcoupon("7")
            time.sleep(0.5)
        
        
        button_state = GPIO.input(13)
        if button_state == False:
            print("Ramp 8 Button pressed")
            nextcoupon("8")
            time.sleep(0.5)
        
        button_state = GPIO.input(16)
        if button_state == False:
            print("Ramp 9 Button pressed")
            nextcoupon("9")
            time.sleep(0.5)
        
        
        button_state = GPIO.input(6)
        if button_state == False:
            print("Ramp 10 Button pressed")
            nextcoupon("10")
            time.sleep(0.5)
        
        button_state = GPIO.input(24)
        if button_state == False:
            print('Coupon Button Pressed...')
            getcoupon()
            time.sleep(0.5)
'''



def writeDisplay():
    tdata = 0
    global copss
    while True:
        if (tdata == 4):
            db= MySQLdb.connect("localhost", "sudish", "shrestha", "qms")
            cursor = db.cursor()
            sql = "SELECT * FROM display_data where id=1 LIMIT 1"
            try:
               # Execute the SQL command
               cursor.execute(sql)
               # Fetch all the rows in a list of lists.
               results = cursor.fetchall()
               for row in results:
                  id = row[0]
                  coupon = row[1]
                  print(coupon)
                  ser.write(coupon)
                  # Now print fetched result
                  print(coupon)
            except:
               print ("Error: unable to fetch data")

            # disconnect from server
            tempData = copss.split(",")
            db.close()
            data =getDataa()
            #ser.write(data)
            tdata=0
            #print(data)
        tdata = tdata +1
        
        
        time.sleep(2.5)
Process(target=button1).start()
Process(target=button2).start()
Process(target=button3).start()
Process(target=button4).start()
Process(target=button5).start()
Process(target=button6).start()
Process(target=button7).start()
Process(target=button8).start()
Process(target=button9).start()
Process(target=button10).start()
Process(target=button1).start()
Process(target=couponButton).start()
Process(target=writeDisplay).start()

        
#GPIO.cleanup()

