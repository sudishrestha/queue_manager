from Tkinter import *
import MySQLdb
import time


class Application(Frame):
    def say_hi(self):
        print ("RESETING THE CODES")
        
    db = MySQLdb.connect("localhost","sudish","shrestha","qms" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE copon_codes SET enable =1"
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


    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["height"]   = "20"
        self.QUIT["width"]   = "20"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "RESET",
        self.hi_there["height"]   = "20"
        self.hi_there["width"]   = "20"
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.minsize(width=666, height=666)
        master.maxsize(width=666, height=666)
        self.pack()
        self.createWidgets()
        

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()