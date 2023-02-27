import mysql.connector as sqlcon
import csv
import datetime
def extract(G):
        mycon=sqlcon.connect(host="localhost",user="root",passwd="root",database="RESTAURANT",autocommit='True')
        cursor=mycon.cursor()
        cursor.execute(G)
        records=cursor.fetchall()
        for row in records:
                print(row)
        mycon.close()
def query(X):
        mycon=sqlcon.connect (host="localhost",user="root",passwd="root",database="RESTAURANT",autocommit='True')
        cursor=mycon.cursor()
        cursor.execute(X)
        records=cursor.fetchall()
        mycon.close()
        return records
def enteras_newfile(W,V):
        with open("bill.csv","w") as f1:
                t=["order_name","price"]
                csv_wr=csv.writer(f1)
                csv_wr.writerow(t)
                rec=[W,V]
                csv_wr.writerow(rec)
def appendin_file(R,Q):
        with open("bill.csv","a") as f2:
                csv_wr=csv.writer(f2)
                h=[R,Q]
                csv_wr.writerow(h)
def create_detailsfile():
        with open("customers_details","w") as f3:
                n=["cname","mobile_no","total_price","date_time"]
                csv_wr=csv.writer(f3)
                csv_wr.writerow(n)
def append_details(X,Y,Z,I):
        with open("customers_details","a") as f4:
                j=[X,Y,Z,I]
                csv_wr=csv.writer(f4)
                csv_wr.writerow(j)
def date_time():
        x=datetime.datetime.now()
        return x
def print_bill():
        with open("bill.csv","r") as f5:
                csv_rd=csv.reader(f5)
                for i in csv_rd:
                        if len(i)!=0:
                                print(i[0],i[1],sep="                   ")
                        else:
                                continue
def show_customers_details():
        with open("customers_details","r") as f6:
                csv_rd=csv.reader(f6)
                for i in csv_rd:
                        if len(i)!=0:
                                print(i[0],i[1],i[2],i[3],sep="                     ")
                        else:
                                continue
print('Welcome to the Paradise Restaurant')
print('What do u want to eat sir/mam')
S=0
while True:
    print('1) Starters')
    print('2) Chaats')
    print('3) Drinks')
    print('4) MainCource(Veg)')
    print('5) MainCource(NonVeg)')
    print('6) Meals')
    print('7) Desserts')
    c=input('sir/mam what would u like to choose?(please choose in numbers) : ')
    if c=='1':
        l=input('sir/mam have you ordered anything else before ordering starters?(y/n) : ')
        x='SELECT * FROM STARTERS'
        extract(x)
        if l[0].upper()=='N':
            y=input('sir/mam what would you like to order in starters?(please enter there slno) : ')
            a='SELECT VARIETY FROM STARTERS WHERE SLNO='+y
            b='SELECT PRICE FROM STARTERS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in starters?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM STARTERS WHERE SLNO='+g
                i='SELECT PRICE FROM STARTERS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in starters?(please enter there slno) : ')
            a='SELECT VARIETY FROM STARTERS WHERE SLNO='+y
            b='SELECT PRICE FROM STARTERS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in starters?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM STARTERS WHERE SLNO='+g
                i='SELECT PRICE FROM STARTERS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    elif c=='2':
        l=input('sir/mam have you ordered anything else before ordering chaats?(y/n) : ')
        x='SELECT * FROM CHAATS'
        extract(x)
        if l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in chaats?(please enter there slno) : ')
            a='SELECT VARIETY FROM CHAATS WHERE SLNO='+y
            b='SELECT PRICE FROM CHAATS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in chaats?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM CHAATS WHERE SLNO='+g
                i='SELECT PRICE FROM CHAATS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='N':
            y=input('sir/mam what would you like to order in chaats?(please enter there slno) : ')
            a='SELECT VARIETY FROM CHAATS WHERE SLNO='+y
            b='SELECT PRICE FROM CHAATS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in chaats?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM CHAATS WHERE SLNO='+g
                i='SELECT PRICE FROM CHAATS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    elif c=='3':
        l=input('sir/mam have you ordered anything else before ordering drinks?(y/n) : ')
        x='SELECT * FROM DRINKS'
        extract(x)
        if l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in drinks?(please enter there slno) : ')
            a='SELECT VARIETY FROM DRINKS WHERE SLNO='+y
            b='SELECT PRICE FROM DRINKS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in drinks?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM DRINKS WHERE SLNO='+g
                i='SELECT PRICE FROM DRINKS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='N':
            y=input('sir/mam what would you like to order in drinks?(please enter there slno) : ')
            a='SELECT VARIETY FROM DRINKS WHERE SLNO='+y
            b='SELECT PRICE FROM DRINKS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in drinks?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM DRINKS WHERE SLNO='+g
                i='SELECT PRICE FROM DRINKS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    elif c=='4':
        l=input('sir/mam have you ordered anything else before ordering main course(veg)?(y/n) : ')
        x='SELECT * FROM MAINCOURSE_VEG'
        extract(x)
        if l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in main course(veg)?(please enter there slno) : ')
            a='SELECT VARIETY FROM MAINCOURSE_VEG WHERE SLNO='+y
            b='SELECT PRICE FROM MAINCOURSE_VEG WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in main course(veg)?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM MAINCOURSE_VEG WHERE SLNO='+g
                i='SELECT PRICE FROM MAINCOURSE_VEG WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='N':
            y=input('sir/mam what would you like to order in main course(veg)?(please enter there slno) : ')
            a='SELECT VARIETY FROM MAINCOURSE_VEG WHERE SLNO='+y
            b='SELECT PRICE FROM MAINCOURSE_VEG WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in main course(veg)?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM MAINCOURSE_VEG WHERE SLNO='+g
                i='SELECT PRICE FROM MAINCOURSE_VEG WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    elif c=='5':
        l=input('sir/mam have you ordered anything else before ordering main course(nonveg)?(y/n) : ')
        x='SELECT * FROM MAINCOURSE_NONVEG'
        extract(x)
        if l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in main course(nonveg)?(please enter there slno) : ')
            a='SELECT VARIETY FROM MAINCOURSE_NONVEG WHERE SLNO='+y
            b='SELECT PRICE FROM MAINCOURSE_NONVEG WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in main course(nonveg)?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM MAINCOURSE_NONVEG WHERE SLNO='+g
                i='SELECT PRICE FROM MAINCOURSE_NONVEG WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='N':
            y=input('sir/mam what would you like to order in main course(nonveg)?(please enter there slno) : ')
            a='SELECT VARIETY FROM MAINCOURSE_NONVEG WHERE SLNO='+y
            b='SELECT PRICE FROM MAINCOURSE_NONVEG WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in main course(nonveg)?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM MAINCOURSE_NONVEG WHERE SLNO='+g
                i='SELECT PRICE FROM MAINCOURSE_NONVEG WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    elif c=='6':
        l=input('sir/mam have you ordered anything else before ordering meals?(y/n) : ')
        x='SELECT * FROM MEALS'
        extract(x)
        if l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in meals?(please enter there slno) : ')
            a='SELECT VARIETY FROM MEALS WHERE SLNO='+y
            b='SELECT PRICE FROM MEALS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in meals?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM MEALS WHERE SLNO='+g
                i='SELECT PRICE FROM MEALS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='N':
            y=input('sir/mam what would you like to order in meals?(please enter there slno) : ')
            a='SELECT VARIETY FROM MEALS WHERE SLNO='+y
            b='SELECT PRICE FROM MEALS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in meals?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM MEALS WHERE SLNO='+g
                i='SELECT PRICE FROM MEALS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    elif c=='7':
        l=input('sir/mam have you ordered anything else before ordering desserts?(y/n) : ')
        x='SELECT * FROM DESSERTS'
        extract(x)
        if l[0].upper()=='Y':
            y=input('sir/mam what would you like to order in desserts?(please enter there slno) : ')
            a='SELECT VARIETY FROM DESSERTS WHERE SLNO='+y
            b='SELECT PRICE FROM DESSERTS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            appendin_file(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in desserts?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to desserts?(please enter there slno) : ')
                h='SELECT VARIETY FROM DESSERTS WHERE SLNO='+g
                i='SELECT PRICE FROM DESSERTS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
        elif l[0].upper()=='N':
            y=input('sir/mam what would you like to order in desserts?(please enter there slno) : ')
            a='SELECT VARIETY FROM DESSERTS WHERE SLNO='+y
            b='SELECT PRICE FROM DESSERTS WHERE SLNO='+y
            d=query(a)
            e=query(b)
            d=d[0][0]
            e=e[0][0]
            S+=e
            enteras_newfile(d,e)
            while True:
                f=input('sir/mam would u like to order anything else in desserts?(y/n) : ')
                if f[0].upper()=='N':
                    break
                g=input('sir/mam what would you like to order?(please enter there slno) : ')
                h='SELECT VARIETY FROM DESSERTS WHERE SLNO='+g
                i='SELECT PRICE FROM DESSERTS WHERE SLNO='+g
                j=query(h)
                k=query(i)
                j=j[0][0]
                k=k[0][0]
                S+=k
                appendin_file(j,k)
    choice=input('Do you want to continue ordering?(y/n) : ')
    if choice[0].upper()=='N':
        break
line='-----------------------------------------'
LINE='  '
appendin_file(line,LINE)
Str='Total Rs'
appendin_file(Str,S)
name=input('Enter your name sir/mam \n')
name=name.upper()
mobileno=int(input('Enter your mobile number \n'))
check=input('This is your first coustomer of the Paradise Restaurant?(y/n)(Question to the manager) : ')
if check[0].upper()=='Y':
    create_detailsfile()
    q=date_time()
    append_details(name,mobileno,S,q)
else:
    q=date_time()
    append_details(name,mobileno,S,q)
print(name)
print(mobileno)
print(date_time())
print_bill()
print('***********************   THANK YOU FOR YOUR ORDER   *************************')
print('***************   WE HOPE YOU ENJOY YOUR MEAL AND STAY   *****************')
print('*************************   PLEASE VISIT US AGAIN   ******************************')
cd=input('Do you want all coustomer details?(y/n)(Question to the manager) : ')
if cd[0].upper()=='Y':
        show_customers_details()
        print('Thank you for using our billing system')
else:
        print('Thank you for using our billing system')

        
        
            
        
