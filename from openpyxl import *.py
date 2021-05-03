from tkinter import *
from tkinter import ttk
import sqlite3
window = Tk()
window.title("Registration Form")
window.geometry('900x800')
window.configure();
window.resizable(False,False)


ra123 = sqlite3.connect('Form_Store_Set3_RA123.db')
c = ra123.cursor()

def submit123():
    ra123 = sqlite3.connect('Form_Store_Set3_RA123.db')
    c = ra123.cursor()
    c.execute("INSERT INTO Data123 VALUES (:seat_cap123, :plate_num123, :other123, :letters123, :owner_name123, :tel_num123, :cus_num123, :address123, :city123, :state123, :zipcode123, :email_address123, :co_owner_name123, :co_tel_num123, :co_cus_num123, :co_address123, :co_city123, :co_state123, :co_zipcode123, :co_email_address123, :add_town123, :add_new_date123, :add_address123, :add_city123, :add_state123, :add_zipcode123)",
             {
                 'seat_cap123': seat_cap123.get(), 
                 'plate_num123': plate_num123.get(), 
                 'other123': other123.get(),
                 'letters123': letters123.get(),
                 'owner_name123': owner_name123.get(),
                 'tel_num123': tel_num123.get(),
                 'cus_num123': cus_num123.get(),
                 'address123': address123.get(),
                 'city123': city123.get(),
                 'state123': state123.get(),
                 'zipcode123': zipcode123.get(),
                 'email_address123': email_address123.get(),
                 'co_owner_name123': co_owner_name123.get(),
                 'co_tel_num123': co_tel_num123.get(),
                 'co_cus_num123': co_cus_num123.get(),
                 'co_address123': co_address123.get(),
                 'co_city123': co_city123.get(),
                 'co_state123': co_state123.get(),
                 'co_zipcode123': co_zipcode123.get(),
                 'co_email_address123': co_email_address123.get(),
                 'add_town123': add_town123.get(),
                 'add_new_date123': add_new_date123.get(),
                 'add_address123': add_address123.get(),
                 'add_city123': add_city123.get(),
                 'add_state123': add_state123.get(),
                 'add_zipcode123': add_zipcode123.get()
             })
                 
                 
    ra123.commit() 
    ra123.close()
                 
    r1.deselect()
    r2.deselect()
    r3.deselect()
    r111.deselect()
    r222.deselect()
    c1.deselect()
    c2.deselect()
    c3.deselect()
    r11.deselect()
    r22.deselect()
    r33.deselect()
    r44.deselect()
    r55.deselect()
    r55.deselect()
    r66.deselect()
    r77.deselect()
    r88.deselect()
    r99.deselect()
    r100.deselect()
    r111.deselect()
    seat_cap123.delete(0, END)
    plate_num123.delete(0, END)
    letters123.delete(0, END)
    other123.delete(0, END)
    owner_name123.delete(0, END)
    tel_num123.delete(0, END)
    cus_num123.delete(0, END)
    address123.delete(0, END)
    city123.delete(0, END)
    state123.delete(0, END)
    zipcode123.delete(0, END)
    email_address123.delete(0, END)
    co_owner_name123.delete(0, END)
    co_tel_num123.delete(0, END)
    co_cus_num123.delete(0, END)
    co_address123.delete(0, END)
    co_city123.delete(0, END)
    co_state123.delete(0, END)
    co_zipcode123.delete(0, END)
    co_email_address123.delete(0, END)
    add_town123.delete(0, END)
    add_new_date123.delete(0, END)
    add_address123.delete(0, END)
    add_city123.delete(0, END)
    add_state123.delete(0, END)
    add_zipcode123.delete(0, END)
    
    
def query123():   
    ra123 = sqlite3.connect('Form_Store_Set3_RA123.db')
    c = ra123.cursor()

    c.execute("SELECT * FROM Data123 ")
    records = c.fetchall()
   
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(window, text=print_records)
    query_label.place(x=1,y=750)
    
    
    ra123.commit() 
    ra123.close()
   
    
a = Frame(window, height=40, width=640, bg='pink', relief=SOLID)
a.pack(fill=X)
a = Label(window ,text = "REGISTRATION INFORMATION",fg='black',bg='pink',font=("Times",20,"bold"))
a.place(x=250,y=1)

a = Label(window ,text = "Registration Period",fg='black',font=("Times",12,"bold"))
a.place(x=10,y=50)
v0=IntVar()
v0.set(1)
r1 = Radiobutton(window, text="One Year",variable=v0,value=1)
r2 = Radiobutton(window, text="Two Year ($2 discount applies)",variable=v0,value=2)
r3 = Radiobutton(window, text="Three Year ($3 discount applies)",variable=v0,value=3)
r1.place(x=250,y=50)
r2.place(x=350,y=50)
r3.place(x=560,y=50)

a = Label(window ,text = "Registration Type",fg='black',font=("Times",12,"bold"))
a.place(x=10,y=80)


v0=IntVar()
v0.set(2)
r11 = Radiobutton(window, text="Original",variable=v0,value=1)
r22 = Radiobutton(window, text="Renewable",variable=v0,value=2)
r33 = Radiobutton(window, text="Private",variable=v0,value=3)
r44 = Radiobutton(window, text="Reissue (Plates and Decals) (See Reissue Plates Below Under Plate Information)",variable=v0,value=4)
r55 = Radiobutton(window, text="Reissue (Decals only)",variable=v0,value=5)
r66 = Radiobutton(window, text="Rental vehicle",variable=v0,value=6)
r77 = Radiobutton(window, text="Transfer License Plate Number - ENTER PLATE NUM",variable=v0,value=7)
r88 = Radiobutton(window, text="For Hire (Complete 'For Higher Information' section )",variable=v0,value=8)
r99 = Radiobutton(window, text="Ridesharing (Vanpool) - Seating Capacity",variable=v0,value=9)
r100 = Radiobutton(window, text="Amateur Radio Operator Call Letters - Specify Letters",variable=v0,value=10)
r111 = Radiobutton(window, text="Other - SPECIFY",variable=v0,value=11)
r11.place(x=250,y=80)
r22.place(x=250,y=100)
r33.place(x=250,y=120)
r44.place(x=250,y=140)
r55.place(x=250,y=160)
r66.place(x=250,y=180)
r77.place(x=250,y=200)
r88.place(x=250,y=220)
r99.place(x=250,y=240)
r100.place(x=250,y=260)
r111.place(x=250,y=280)

plate_num123 = Entry(width=7)
plate_num123.place(x=550,y=200)
seat_cap123 = Entry(width=5)
seat_cap123.place(x=500,y=240)
letters123 = Entry(width=10)
letters123.place(x=560,y=260)
other123 = Entry()
other123.place(x=380,y=280)


b = Frame(window, height=38, width=900, bg='pink', relief=SOLID)
b.place(y=310)
b = Label(window ,text = "OWNER INFORMATION",fg='black',bg='pink',font=("Times",20,"bold"))
b.place(x=300,y=310)

b = Label(window ,text = "OWNERS FULL LEGAL NAME",fg='black')
b.place(x=10,y=350)
b = Label(window ,text = "TELEPHONE NUMBER",fg='black')
b.place(x=320,y=350)
b = Label(window ,text = "DMV CUSTOMER NUMBER",fg='black')
b.place(x=515,y=350)
owner_name123 = Entry()
owner_name123.place(x=190, y=350)
tel_num123 = Entry(width=10)
tel_num123.place(x=445, y=350)
cus_num123=Entry()
cus_num123.place(x=665, y=350)
b = Label(window ,text = "CO-OWNERS FULL LEGAL NAME",fg='black')
b.place(x=10,y=380)
b = Label(window ,text = "TELEPHONE NUMBER",fg='black')
b.place(x=320,y=380)
b = Label(window ,text = "DMV CUSTOMER NUMBER",fg='black')
b.place(x=515,y=380)
co_owner_name123 = Entry()
co_owner_name123.place(x=190, y=380)
co_tel_num123 = Entry(width=10)
co_tel_num123.place(x=445, y=380)
co_cus_num123=Entry()
co_cus_num123.place(x=665, y=380)
b = Label(window ,text = "NOTE: Owners MUST provide their residence/business/home address, this address can not be a P.O Box",fg='black',font=("Times",15,"bold"))
b.place(x=10,y=410)
b = Label(window ,text = "OWNERS RESIDENCE/BUSINESS/HOME ADDRESS")
b.place(x=10,y=440)
b = Label(window ,text = "CITY")
b.place(x=430,y=440)
b = Label(window ,text = "STATE")
b.place(x=595,y=440)
b = Label(window ,text = "ZIPCODE")
b.place(x=725,y=440)
address123 = Entry()
address123.place(x=300,y=440)
city123=Entry()
city123.place(x=465,y=440)
state123=Entry(width=12)
state123.place(x=640,y=440)
zipcode123 = Entry(width=9)
zipcode123.place(x=785,y=440)
b = Label(window ,text = "CO-OWNERS RESIDENCE/BUSINESS/HOME ADDRESS")
b.place(x=10,y=470)
b = Label(window ,text = "CITY")
b.place(x=430,y=470)
b = Label(window ,text = "STATE")
b.place(x=595,y=470)
b = Label(window ,text = "ZIPCODE")
b.place(x=725,y=470)
co_address123 = Entry()
co_address123.place(x=300,y=470)
co_city123 = Entry()
co_city123.place(x=465,y=470)
co_state123 = Entry(width=12)
co_state123.place(x=640,y=470)
co_zipcode123 = Entry(width=9)
co_zipcode123.place(x=785,y=470)
b = Label(window ,text = "OWNER E-MAIL ADDRESS")
b.place(x=10,y=500)
b = Label(window ,text = "CO-OWNER E-MAIL ADDRESS")
b.place(x=430,y=500)
email_address123 = Entry()
email_address123.place(x=300,y=500)
co_email_address123 = Entry()
co_email_address123.place(x=640,y=500)

c = Frame(window, height=38, width=900, bg='pink', relief=SOLID)
c.place(y=540)
c = Label(window ,text = "ADDITIONAL INFORMATION",fg='black',bg='pink',font=("Times",20,"bold"))
c.place(x=270,y=540)

c = Label(window ,text = "LOCATION WHERE VEHICLES PRINCIPALLY GRADED")
c.place(x=10,y=580)
city=IntVar()
county=IntVar()
town=IntVar()
c1=Checkbutton(window,text="CITY", variable= city, onvalue=1 )
c1.place(x=310,y=580)
c2=Checkbutton(window,text="COUNTY", variable= county, onvalue=2 )
c2.place(x=400,y=580)
c3=Checkbutton(window,text="TOWN OF", variable= town, onvalue=3 )
c3.place(x=500,y=580)
add_town123 = Entry()
add_town123.place(x=580,y=580)
c = Label(window ,text = "IF NEW LOCATION ENTER DATE CHANGED")
c.place(x=10,y=610)
add_new_date123 = Entry()
add_new_date123.place(x=315,y=610)
c = Label(window ,text = "ACTIVE MILITARY SERVICE")
c.place(x=505,y=610)
v0=IntVar()
v0.set(2)
r111=Radiobutton(window, text="YES",variable=v0,value=1)
r222=Radiobutton(window, text="NO",variable=v0,value=2)
r111.place(x=650,y=610)
r222.place(x=700,y=610)
c = Label(window ,text = "IF YOU WOULD LIKE YOUR REGISTRATION RENEWALS SENT TO AN ADDRESS OTHER THAN RESIDENCE/BUSINESS ADDRESS.ENTER IT BELOW ",fg='black',font=("Times",10,"bold"))
c.place(x=10,y=640)
c = Label(window ,text = "REGISTRATION MAILING ADDRESS")
c.place(x=10,y=670)
c = Label(window ,text = "CITY")
c.place(x=430,y=670)
c = Label(window ,text = "STATE")
c.place(x=595,y=670)
c = Label(window ,text = "ZIPCODE")
c.place(x=725,y=670)
add_address123 = Entry()
add_address123.place(x=300,y=670)
add_city123 = Entry()
add_city123.place(x=465,y=670)
add_state123 = Entry(width=12)
add_state123.place(x=640,y=670)
add_zipcode123 = Entry(width=9)
add_zipcode123.place(x=785,y=670)


submit_btn = ttk.Button(window, text="Submit", command=submit123)
submit_btn.place(x=400,y=700)
show_btn = ttk.Button(window, text="Show Data", command=query123)
show_btn.place(x=400,y=725)


ra123.commit() 
ra123.close()
window.mainloop()