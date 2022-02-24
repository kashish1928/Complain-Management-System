print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("+++++++++++++++++++++++++ ᗩᔕIᗩᑎ IᑎTEᖇᑎᗩTIOᑎᗩᒪ ᑭᐯT ᔕᑕᕼOOᒪ ++++++++++++++++++++++++++++")
print("")
print("++++++++++++++++++++++++++++++ ᑕOᗰᑭᒪᗩIᑎ ᗰᗩᑎᗩGEᗰEᑎT +++++++++++++++++++++++++++++++++++")
print("")
print("++++++++++++++++++++++++++++++++ KᗩᔕᕼIᔕᕼ ᒍOᔕᕼIᑭᑌᖇᗩ ++++++++++++++++++++++++++++++++++++")
print("")

import sys

#complaint number input
def complaintnumber():
    global cmpno
    cmpno=int(input("enter the complaint number===>"))
    cmpno=str(cmpno)


#name input
def name():
    global name
    name=input("enter a name==>")
    if(name==""):
       raise ValueError
    print(name)


#gender input
def gender():
    global ch
    ch=input("choose male or female==>")
    if(ch!="male" and ch!="female"):
        raise ValueError
    print(ch)


#building number input
def building():
    global bg
    bg=input("enter your building number==>")
    if(bg==""):
        raise ValueError
    print(bg)


#category input
def category():
    global cat
    cat=input("enter category:----\nwifi,\nrepair,\ntransport,\ncleaning-------")
    if(cat!="wifi" and cat!="repair" and cat!="transport" and cat!="cleaning"):
        raise ValueError
    print(cat)


#description input
def description():
    global des
    des=input("enter the complaint description==>")
    if(des==""):
        raise ValueError
    print(des)


#display all complaints in one table
def mysql():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("Insert into complain values ("+cmpno+",'"+name+"','"+ch+"','"+bg+"','"+cat+"','"+des+"')")
    db.commit() 
        

#wifi category mysql connectivity
class complain(): 
    def wifi(self):
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
        cur = db.cursor()
        cur.execute("Insert into wifi values ("+cmpno+",'"+name+"','"+ch+"','"+bg+"','"+cat+"','"+des+"')")
        db.commit()
        
        
#repair category mysql connectivity
    def repair(self):
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
        cur = db.cursor()
        cur.execute("Insert into repair values ("+cmpno+",'"+name+"','"+ch+"','"+bg+"','"+cat+"','"+des+"')")
        db.commit()
        
        
#transport category mysql connectivity
    def transport(self):
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
        cur = db.cursor()
        cur.execute("Insert into transport values ("+cmpno+",'"+name+"','"+ch+"','"+bg+"','"+cat+"','"+des+"')")
        db.commit()
        

#cleaning category mysql connectivity
    def cleaning(self):
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
        cur = db.cursor()
        cur.execute("Insert into cleaning values ("+cmpno+",'"+name+"','"+ch+"','"+bg+"','"+cat+"','"+des+"')")
        db.commit()
        

#sql connectivity execution        
def choose():
    if(cat=="wifi"):
        c1=complain()
        c1.wifi()
    elif(cat=="repair"):
        c1=complain()
        c1.repair()
    elif(cat=="transport"):
        c1=complain()
        c1.transport()
    elif(cat=="cleaning"):
        c1=complain()
        c1.cleaning()


#select all complains
def all_complains():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="kashishviha1928",
                                 database="complaint")
    cur = db.cursor()
    cur.execute("select * from complain")
    r=cur.fetchall()
    result=len(r)
    if(result!=0):
        for row in r:
            print("")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@Complaint Number-----",row[0])
            print("@Name-----",row[1])
            print("@Gender-----",row[2])
            print("@Building Number-----",row[3])
            print("@Category-----",row[4])
            print("@Description-----",row[5])
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("")
        #dfh
        file=open("csproject.txt","w")
        st=str(row)
        file.writelines(st)
        file.close()
    else:
        print("empty")
    db.close() 


#select wifi complains
def wifi_complains():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("select * from wifi")
    r=cur.fetchall()
    result=len(r)
    if(result!=0):
        for row in r:
            print("")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@Complaint Number-----",row[0])
            print("@Name-----",row[1])
            print("@Gender-----",row[2])
            print("@Building Number-----",row[3])
            print("@Category-----",row[4])
            print("@Description-----",row[5])
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("")
        #dfh
        file=open("csproject.txt","w")
        st=str(row)
        file.writelines(st)
        file.close()
    else:
        print("empty")
    db.close()
        
        
#select repair complains
def repair_complains():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("select * from repair")
    r=cur.fetchall()
    result=len(r)
    if(result!=0):
        for row in r:
            print("")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@Complaint Number-----",row[0])
            print("@Name-----",row[1])
            print("@Gender-----",row[2])
            print("@Building Number-----",row[3])
            print("@Category-----",row[4])
            print("@Description-----",row[5])
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("")
        #dfh
        file=open("csproject.txt","w")
        st=str(row)
        file.writelines(st)
        file.close()
    else:
        print("empty")
    db.close()
        
        
#select transport complains
def transport_complains():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("select * from transport")
    r=cur.fetchall()
    result=len(r)
    if(result!=0):
        for row in r:
            print("")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@Complaint Number-----",row[0])
            print("@Name-----",row[1])
            print("@Gender-----",row[2])
            print("@Building Number-----",row[3])
            print("@Category-----",row[4])
            print("@Description-----",row[5])
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("")
        #dfh
        file=open("csproject.txt","w")
        st=str(row)
        file.writelines(st)
        file.close()
    else:
        print("empty")
    db.close()
        
        
#select cleaning complains
def cleaning_complains():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("select * from cleaning")
    r=cur.fetchall()
    result=len(r)
    if(result!=0):
        for row in r:
            print("")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("@Complaint Number-----",row[0])
            print("@Name-----",row[1])
            print("@Gender-----",row[2])
            print("@Building Number-----",row[3])
            print("@Category-----",row[4])
            print("@Description-----",row[5])
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("")
        #dfh
        file=open("csproject.txt","w")
        st=str(row)
        file.writelines(st)
        file.close()
    else:
        print("empty")
    db.close()


#display table
def display():
    print("select the category of the complaint you wish to display")
    print("====>all complains")
    print("====>wifi")
    print("====>repair")
    print("====>transport")
    print("====>cleaning")
    print("====>none")
    dsp=input("")
    if(dsp=="all complains"):
        all_complains()
    elif(dsp=="wifi"):
        wifi_complains()
    elif(dsp=="repair"):
        repair_complains()
    elif(dsp=="transport"):
        transport_complains()
    elif(dsp=="cleaning"):
        cleaning_complains()
    elif(dsp=="none"):
        sys.exit
    else:
        raise ValueError

#delete name
def delopt():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ᗪEᒪETE ᖇEᑕOᖇᗪᔕ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("enter the name of the category from which you want to delete the complaint")
    print("1----all complains")
    print("2----wifi")
    print("3----repair")
    print("4----transport")
    print("5----cleaning")
    print("6----I have changed my mind I don't want to delete any record")
    global deltable
    deltable=input("")
    
    
def delname():
    global deletename
    print("enter the name of the person whose complaint you want to remove====>")
    deletename=input("")


#delete records
def delall():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("delete from complain where name='"+deletename+"'")
    db.commit()


def delwifi():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("delete from wifi where name='"+deletename+"'")
    db.commit()


def delrepair():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("delete from repair where name='"+deletename+"'")
    db.commit()
    
    
def deltransport():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("delete from transport where name='"+deletename+"'")
    db.commit()


def delcleaning():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                     user="root",
                     passwd="kashishviha1928",
                     database="complaint")
    cur = db.cursor()
    cur.execute("delete from cleaning where name='"+deletename+"'")
    db.commit()
    
#variable for upg
def var():
    global ugname
    global ugdes
    print("enter the name used while registering the complaint")
    ugname=input("")
    if(ugname==""):
        raise ValueError()
    else:
        print("")
    print("Enter the new description")
    ugdes=input("")
    if(ugdes==""):
        raise ValueError()
    else:
        print("")

#mysql update for all tables
def all_complains_update():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="kashishviha1928",
                                 database="complaint")
    cur = db.cursor()
    cur.execute("update complain set description='"+ugdes+"' where name='"+ugname+"'")
    db.commit()

def wifi_update():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="kashishviha1928",
                                 database="complaint")
    cur = db.cursor()
    cur.execute("update wifi set description='"+ugdes+"' where name='"+ugname+"'")
    db.commit()

def repair_update():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="kashishviha1928",
                                 database="complaint")
    cur = db.cursor()
    cur.execute("update repair set description='"+ugdes+"' where name='"+ugname+"'")
    db.commit()

def transport_update():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="kashishviha1928",
                                 database="complaint")
    cur = db.cursor()
    cur.execute("update transport set description='"+ugdes+"' where name='"+ugname+"'")
    db.commit()
    
def cleaning_update():
    import mysql.connector
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="kashishviha1928",
                                 database="complaint")
    cur = db.cursor()
    cur.execute("update cleaning set description='"+ugdes+"' where name='"+ugname+"'")
    db.commit() 

#edit/update
def update():
    print("Select the category of the complaint which is to be altered")
    print("1----all complains")
    print("2----wifi")
    print("3----repair")
    print("4----transport")
    print("5----cleaning")
    print("6----none")
    ud=input("")
    if(ud=="1"):
        var()
        all_complains_update()
    elif(ud=="2"):
        var()
        wifi_update()
    elif(ud=="3"):
        var()
        repair_update()
    elif(ud=="4"):
        var()
        transport_update()
    elif(ud=="5"):
        var()
        cleaning_update()
    elif(ud=="6"):
        sys.exit
    else:
        raise ValueError()

#another update for name 
def nupdate():
    global bgupdate    
    print("Enter the building number whose name you wish to alter")
    bgupdate=input("")
    if(bgupdate==""):
        raise ValueError()
    else:
        print("")
    global namupdate
    print("Enter the new name")
    namupdate=input("")
    if(namupdate==""):
        raise ValueError()
    else:
        print("")
def updatechoice():
    print("Enter the category containing the name to be altered-------\n1----all complains \n2----wifi \n3----repair \n4----transport \n5----cleaning")
    updc=input("")
    if(updc=="1"):
        nupdate()
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="kashishviha1928",
                                     database="complaint")
        cur = db.cursor()
        cur.execute("update complain set name='"+namupdate+"' where buildingnum='"+bgupdate+"'")
        db.commit()
    elif(updc=="2"):
        nupdate()
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="kashishviha1928",
                                     database="complaint")
        cur = db.cursor()
        cur.execute("update wifi set name='"+namupdate+"' where buildingnum='"+bgupdate+"'")
        db.commit()
    elif(updc=="3"):
        nupdate()
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="kashishviha1928",
                                     database="complaint")
        cur = db.cursor()
        cur.execute("update repair set name='"+namupdate+"' where buildingnum='"+bgupdate+"'")
        db.commit()
    elif(updc=="4"):
        nupdate()
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="kashishviha1928",
                                     database="complaint")
        cur = db.cursor()
        cur.execute("update transport set name='"+namupdate+"' where buildingnum='"+bgupdate+"'")
        db.commit()
    elif(updc=="5"):
        nupdate()
        import mysql.connector
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="kashishviha1928",
                                     database="complaint")
        cur = db.cursor()
        cur.execute("update cleaning set name='"+namupdate+"' where buildingnum='"+bgupdate+"'")
        db.commit()
    else:
        raise ValueError()
        
#delete complain options
def delch():
    if(deltable=="1"):
        delname()
        delall()
    elif(deltable=="2"):
        delname()
        delwifi()
    elif(deltable=="3"):
        delname()
        delrepair()
    elif(deltable=="4"):
        delname()
        deltransport()
    elif(deltable=="5"):
        delname()
        delcleaning()
    elif(deltable=="6"):
        sys.exit
    else:
        raise ValueError
    
    
#admin
def admin():
    print("_____________________")
    print("|Enter your username|")
    print("|___________________|")
    ad=input()
    if(ad!="kashish"):
        print("!!!!!!!!! INVALID USERNAME !!!!!!!!!")
        print("!!!!!!!!!! ACCESS DENIED !!!!!!!!!!!")
        sys.exit
    else:
        print("___________________")
        print("|Enter you password|")
        print("|__________________|")
        pw=input()
        if(pw!="no"):
            print("!!!!!!!!! INVALID PASSWORD !!!!!!!!!")
            print("!!!!!!!!!! ACCESS DENIED !!!!!!!!!!!")
        else:
            print("$$$$$$$$$$ ACCESS GRANTED $$$$$$$$$$")
            fnctcall1()
            loop1()

#random dfh again
def dfhagain():
    f=open("instructions.txt")
    print(f.read())
    f.close()


#function calls
def fnctcall1():
    print("What do you want to do ?")
    print("1---Enter a complaint")
    print("2---Display complaints")
    print("3---Delete complaint records")
    print("4---Alter the complain description")
    print("5---Alter the complain name")
    print("6---Instructions")
    print("7---Exit")
    user=int(input(""))
    if(user==1):
        complaintnumber()
        name()
        gender()
        building()
        category()
        description()
        mysql()
        choose()
    elif(user==2):
        display()
    elif(user==3):
        delopt()
        delch()
    elif(user==4):
        update()
    elif(user==5):
        updatechoice()
    elif(user==6):
        dfhagain()
    elif(user==7):
        sys.exit
    else:
        raise ValueError



def fnctcall2():
    print("")
    print("What do you want to do ?")
    print("1---Enter a complaint")
    print("2---Displayy complaints")
    print("3---Alter a complaint")
    print("4---Instructions")
    print("5---Exit")
    user=int(input(""))
    if(user==1):
        complaintnumber()
        name()
        gender()
        building()
        category()
        description()
        mysql()
        choose()
    elif(user==2):
        display()
    elif(user==3):
        update()
    elif(user==4):
        dfhagain()
    elif(user==5):
        sys.exit
    else:
        raise ValueError



#dfh again
def developerdetails():
    f=open("developerdetails.txt")
    print(f.read())
    f.close()
def about():
    f=open("about.txt")
    print(f.read())
    f.close()
def kyr():
    f=open("kyr.txt")
    print(f.read())
    f.close()
def call():
    print("")
    print("For more information select")
    print("1-----Developer Details")
    print("2-----About")
    print("3-----Know Your Rights")
    print("4-----NO!!!!!")
    call=input("")
    if(call=="1"):
        developerdetails()
    elif(call=="2"):
        
        about()
    elif(call=="3"):
        kyr()
    elif(call=="4"):
        sys.exit
    else:
        raise ValueError()
def callloop():
    call()
    calop=input("")
    if(calop==""):
        call()
#looping the call
'''def loop1():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("DO YOU WANT TO CONTINUE???")
    print("~~~~~~")
    print("y-YES")
    print("~~~~")
    print("n-NO")
    print("~~~~")
    cho=input()
    if(cho=="y"):
        fnctcall1()
    elif(cho=="n"):
        print("")
        print("THANK YOU FOR VISITING!!!!!!!!!!")
        print("")
        callloop()
    else:
        raise ValueError()'''
        
        
'''def loop2():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("DO YOU WANT TO CONTINUE???")
    print("~~~~~~")
    print("y-YES")
    print("~~~~")
    print("n-NO")
    print("~~~~")
    cho=input()
    if(cho=="y"):
        fnctcall2()
    elif(cho=="n"):
        print("")
        print("THANK YOU FOR VISITING!!!!!!!!!!")
        print("")
        callloop()
    else:
        raise ValueError()'''

def loop1():
    ch="y"
    print("")
    while (ch=="y"):
        fnctcall1()
        ch=input(" Do you want to continue : y or n ")
        if(ch=="n"):
            callloop()

def loop2():
    ch="y"
    print("")
    while (ch=="y"):
        fnctcall2()
        ch=input(" Do you want to continue : y or n ")
        if(ch=="n"):
            callloop()
#select mode
def mode():
    print("")
    print("   s̳e̳l̳e̳c̳t̳ ̳t̳h̳e̳ ̳m̳o̳d̳e̳  ")
    print("")
    print("--------------------")
    print("|1----ADMIN MODE   |")
    print("|2----CUSTOMER MODE|")
    print("--------------------")
    mode=input("")
    if (mode=="1"):
        print("=====================")
        print("WELCOME TO ADMIN MODE")
        admin()
    elif(mode=="2"):
        print("=========================")
        print("WELCOME TO CUSTORMER MODE")
        fnctcall2()
        loop2()
    else:
        raise ValueError()
mode()       



        
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
