from tkinter import *
import pymysql as pms
import tkinter.messagebox as mb
def admin():
    a=pms.connect(user='root',password='123456',host='localhost',db='Project1')


    login=Tk()
    login.title("Login Page")
    login.geometry('500x300')
    def login1():
        cursor=a.cursor()
        query="select * from login"
        cursor.execute(query)
        lst=cursor.fetchall()
        x=id.get()
        y=ps.get()
        flag=0
        for i in lst:
            if i[0]==x and i[1]==y:
                mb.showinfo("Pop","Login successfully")
                flag=1
                front=Tk()
                front.title("Front page:")
                front.geometry('800x800')
                #f = Frame(front,bg="yellow",width=100,height=350)
                #f.grid(row=0,column=0,sticky="NW")
                #f.grid_propagate(0)
                #f.update()
                #front.config(background='white')

                def command_for_view():
                    w=Tk()
                    w.title("Display the total")
                    w.geometry('1200x800')
                    v=Label(w,text="The data is here ")
                    v.grid(column=0,row=0)
                    ct=1
                    with a.cursor() as cursor:
                        cursor=a.cursor()
                        query="select* from Criminal,Record,Officer,Victum where Record.c_id=Criminal.c_id AND Record.c_id=Officer.c_id AND Record.c_id=Victum.c_id"
                        cursor.execute(query)

                        for row in cursor:
                            row=list(row)
                            xxx=0
                            p=Label(w,text="Case Details:",bg="red")
                            p.grid(column=0,row=ct)
                            ct=ct+1
                            p=Label(w,text="Case id--'"+row[0]+"'")
                            p.grid(column=xxx,row=ct)
                            #ct=ct+1
                            xxx=xxx+1
                            p=Label(w,text="Criminal Name--'"+row[1]+"'")
                            p.grid(column=xxx,row=ct)
                            #ct=ct+1
                            xxx+=1
                            p=Label(w,text="Case Type--'"+row[2]+"'")
                            p.grid(column=xxx,row=ct)
                            ct=ct+1
                            xxx=0
                            p=Label(w,text="Year--'"+row[4]+"'")
                            p.grid(column=xxx,row=ct)
                            xxx+=1
                            #ct=ct+1
                            p=Label(w,text="Place of Crime--'"+row[6]+"'")
                            p.grid(column=xxx,row=ct)
                            #ct=ct+1
                            xxx+=1
                            p=Label(w,text="Case status--'"+row[10]+"'")
                            p.grid(column=xxx,row=ct)
                            #ct=ct+1
                            #ct=ct+1
                            xxx+=1
                            p=Label(w,text="Case Officer--'"+row[9]+"'")
                            p.grid(column=xxx,row=ct)
                            ct=ct+1
                            p=Label(w,text="Victim Name--'"+row[12]+"'")
                            p.grid(column=0,row=ct)
                            p=Label(w,text="Victim Address--'"+row[13]+"'")
                            p.grid(column=1,row=ct)
                            p=Label(w,text="Date of crime--'"+row[15]+"'")
                            p.grid(column=2,row=ct)
                            ct=ct+1
                            p=Label(w,text="Statement of the Victim--'"+row[14]+"'")
                            p.grid(column=0,row=ct)
                            ct=ct+1
                            p=Label(w,text="Description --'"+row[7]+"'")
                            p.grid(column=0,row=ct)
                            ct=ct+1
                    w.mainloop()
                btn=Button(front,text="Click here to view details",command=command_for_view,bg="green")
                btn.grid(column=0,row=1)

                def command_for_insert():
                    window=Tk()
                    window.title("Input page:")
                    window.geometry('800x800')
                    c_id = Label(window, text="Enter the case id:")
                    c_id.grid(column=0, row=0)
                    c_id= Entry(window,width=10)
                    c_id.grid(column=1, row=0)
                    c_type= Label(window, text="Enter the crime type:")
                    c_type.grid(column=0, row=1)
                    c_type= Entry(window,width=10)
                    c_type.grid(column=1, row=1)
                    c_name = Label(window, text="Enter the name of criminal:")
                    c_name.grid(column=0, row=2)
                    c_name= Entry(window,width=10)
                    c_name.grid(column=1, row=2)
                    c_off= Label(window, text="Enter the name of investigating officer")
                    c_off.grid(column=0, row=3)
                    c_off = Entry(window,width=10)
                    c_off.grid(column=1, row=3)
                    c_dist = Label(window, text="Enter the place(District) of  crime")
                    c_dist.grid(column=0, row=4)
                    c_dist = Entry(window,width=10)
                    c_dist.grid(column=1, row=4)
                    c_year= Label(window, text="Enter the year of  crime")
                    c_year.grid(column=0, row=5)
                    c_year = Entry(window,width=10)
                    c_year.grid(column=1, row=5)
                    status=Label(window, text="Enter the case status")
                    status.grid(column=0, row=6)
                    status = Entry(window,width=10)
                    status.grid(column=1, row=6)

                    v_name= Label(window, text="Enter Victim name")
                    v_name.grid(column=0, row=7)
                    v_name = Entry(window,width=10)
                    v_name.grid(column=1, row=7)
                    v_add = Label(window, text="Enter address of Victim")
                    v_add.grid(column=0, row=8)
                    v_add = Entry(window,width=30)
                    v_add.grid(column=1, row=8)
                    v_date= Label(window, text="Enter date(DD/MM/YYYY)")
                    v_date.grid(column=0, row=9)
                    v_date = Entry(window,width=10)
                    v_date.grid(column=1, row=9)
                    v_statement=Label(window, text="Enter Victim's statement")
                    v_statement.grid(column=0, row=10)
                    v_statement = Entry(window,width=50)
                    v_statement.grid(column=1, row=10)


                    desc=Label(window, text="Enter the description about case")
                    desc.grid(column=0, row=11)
                    desc = Entry(window,width=50)
                    desc.grid(column=1, row=11)

                    def insert():
                        bb=c_id.get()
                        cc=(c_type.get()).upper()
                        dd=(c_name.get()).upper()
                        ee=(c_dist.get()).upper()
                        ff=c_year.get()
                        gg=(c_off.get()).upper()
                        stts=(status.get()).upper()
                        hh=(desc.get()).upper()
                        ii=(v_name.get()).upper()
                        jj=(v_add.get()).upper()
                        kk=(v_date.get())
                        ll=(v_statement.get()).upper()

                        cursor=a.cursor()
                        cursor=a.cursor()
                        query="INSERT into Record(c_id,year,c_type,c_dist,description) VALUES('"+bb+"','"+ff+"','"+cc+"','"+ee+"','"+hh+"')"
                        q1="INSERT into Criminal(c_id,name,c_type) VALUES('"+bb+"','"+dd+"','"+cc+"')"
                        q2="INSERT into Officer(c_id,name,status) VALUES('"+bb+"','"+gg+"','"+stts+"')"
                        q3="INSERT into Victum(c_id,name,address,statement,date) VALUES('"+bb+"','"+ii+"','"+jj+"','"+ll+"','"+kk+"')"
                        q4="INSERT into Record_of(c_id) VALUES('"+bb+"')"
                        cursor.execute(q1)
                        cursor.execute(q2)
                        cursor.execute(q3)
                        cursor.execute(q4)
                        cursor.execute(query)
                        a.commit()
                        count=cursor.rowcount
                        if count>0:
                            mb.showinfo("Congratulation","Data inserted successfully")
                        else:
                            mb.showinfo("UFF","Data insertion fails.")


                    btn = Button(window, text="Click here to enter the details :", command=insert,bg='red')
                    btn.grid(column=0, row=12)

                    window.mainloop()

                btn=Button(front,text="Click here to Enter details",command=command_for_insert,bg="blue")
                btn.grid(column=0,row=0)
                def command_for_search():
                    SI=Tk()
                    SI.title("Search page 1")
                    SI.geometry('700x700')
                    s_id=Label(SI,text="Enter case id:",)
                    s_id.grid(column=0,row=0)
                    s_id=Entry(SI,width=10)
                    s_id.grid(column=1,row=0)
                    def search_id():
                            w=Tk()
                            w.title("Display the Searched result")
                            w.geometry('800x800')
                            v=Label(w,text="The Result is here ")
                            v.grid(column=0,row=0)
                            ct=1
                            cursor=a.cursor()
                            with a.cursor() as cursor:
                                query="select * from Record,Officer where Record.c_id=Officer.c_id"
                                cursor.execute(query)
                                data=s_id.get()
                                for row in cursor:
                                    if row[0]==data:
                                        row=list(row)
                                        xxx=0
                                        p=Label(w,text="Case Details:",bg="blue")
                                        p.grid(column=0,row=ct)
                                        ct=ct+1
                                        p=Label(w,text="Case id--'"+row[0]+"'")
                                        p.grid(column=xxx,row=ct)
                                        #ct=ct+1
                                        xxx=xxx+1
                                        p=Label(w,text="Year of crime--'"+row[1]+"'")
                                        p.grid(column=xxx,row=ct)
                                        #ct=ct+1
                                        xxx+=1

                                        p=Label(w,text="Place of Crime--'"+row[3]+"'")
                                        p.grid(column=xxx,row=ct)
                                        xxx+=1
                                        ct=ct+1
                                        #yr=str(row[4])
                                        p=Label(w,text="Crime Type'"+row[2]+"'")
                                        p.grid(column=0,row=ct)
                                        #ct=ct+1
                                        p=Label(w,text="Case status'"+row[7]+"'")
                                        p.grid(column=1,row=ct)
                                        p=Label(w,text="Description about the case--'"+row[4]+"'")
                                        p.grid(column=0,row=ct+1)
                                        ct+=2
                            w.mainloop()
                    btn = Button(SI, text="Click to check details:",command=search_id,bg='brown')
                    btn.grid(column=0, row=1)
                    SI.mainloop()

                btn=Button(front,text="Click here to Search any data",command=command_for_search,bg="indigo")
                btn.grid(column=0,row=2)

                def command_for_search1():
                    SC=Tk()
                    SC.title("Display the searched results:")
                    SC.geometry("800x800")
                    s_crim=Label(SC,text="Enter criminal name:")
                    s_crim.grid(column=0,row=0)
                    s_crim=Entry(SC,width=10)
                    s_crim.grid(column=1,row=0)
                    def search_criminal():
                        w=Tk()
                        w.title("Display the Searched result")
                        w.geometry('800x800')
                        v=Label(w,text="The Result is here ")
                        v.grid(column=0,row=0)
                        ct=1
                        cursor=a.cursor()
                        with a.cursor() as cursor:
                            query="select * from Criminal"
                            cursor.execute(query)
                            data=(s_crim.get()).upper()
                            for row in cursor:
                                if row[1]==data:
                                    row=list(row)
                                    xxx=0
                                    p=Label(w,text="Criminal Details:",bg="blue")
                                    p.grid(column=0,row=ct)
                                    ct=ct+1
                                    p=Label(w,text="Case id--'"+row[0]+"'")
                                    p.grid(column=xxx,row=ct)
                                    #ct=ct+1
                                    xxx=xxx+1
                                    p=Label(w,text="Criminal Name--'"+row[1]+"'")
                                    p.grid(column=xxx,row=ct)
                                    #ct=ct+1
                                    xxx+=1
                                    p=Label(w,text="Case Type--'"+row[2]+"'")
                                    p.grid(column=xxx,row=ct)

                        w.mainloop()
                    btn = Button(SC, text="Click here to view details:",command=search_criminal,bg='brown')
                    btn.grid(column=0, row=1)

                    SC.mainloop()
                btn=Button(front,text="Click here to search the history of the criminal",command=command_for_search1,bg="red")
                btn.grid(column=0,row=3)

                def command_for_search2():
                        SO=Tk()
                        SO.title("Display the search results")
                        SO.geometry("800x800")
                        s_off=Label(SO,text="Enter officer name:")
                        s_off.grid(column=0,row=0)
                        s_off=Entry(SO,width=10)
                        s_off.grid(column=1,row=0)
                        def search_officer():
                            w=Tk()
                            w.title("Display the Searched result")
                            w.geometry('800x800')
                            v=Label(w,text="The Result is here ")
                            v.grid(column=0,row=0)
                            ct=1
                            efficency=0
                            total=0
                            unsolved=0
                            cursor=a.cursor()
                            with a.cursor() as cursor:
                                query="select * from Officer"
                                cursor.execute(query)
                                data=(s_off.get()).upper()
                                for row in cursor:
                                    if row[1]==data:
                                        row=list(row)
                                        xxx=0
                                        p=Label(w,text="Officer Details:",bg="blue")
                                        p.grid(column=0,row=ct)
                                        ct=ct+1
                                        p=Label(w,text="Case id--'"+row[0]+"'")
                                        p.grid(column=xxx,row=ct)
                                        #ct=ct+1
                                        xxx=xxx+1
                                        p=Label(w,text="Officer Name--'"+row[1]+"'")
                                        p.grid(column=xxx,row=ct)
                                        #ct=ct+1
                                        xxx+=1
                                        p=Label(w,text="Case status--'"+row[2]+"'")
                                        p.grid(column=xxx,row=ct)
                                        ct=ct+1
                                        if row[2]=='SOLVED':
                                            efficency+=1
                                        if row[2]=='UNSOLVED':
                                            unsolved+=1
                                        total+=1
                            eff=(efficency/total)*100
                            efficency=str(efficency)
                            total=str(total)
                            unsolved=str(unsolved)
                            eff=str(eff)
                            p=Label(w,text="The number of cases attended by the officer is --'"+total+"'",bg="green")
                            p.grid(column=0,row=ct)
                            ct=ct+1
                            p=Label(w,text="The number of cases solved by the officer is --'"+efficency+"'",bg="green")
                            p.grid(column=0,row=ct)
                            ct=ct+1
                            p=Label(w,text="The number of pending cases by the officer is--'"+unsolved+"'",bg="green")
                            p.grid(column=0,row=ct)
                            ct=ct+1
                            p=Label(w,text="Efficency of the offficer is --'"+eff+"'%",bg="red")
                            p.grid(column=0,row=ct)

                            w.mainloop()
                        btn = Button(SO, text="Click here to view details:",command=search_officer,bg='brown')
                        btn.grid(column=0, row=1)
                        SO.mainloop()

                btn=Button(front,text="Click here to search the history of officer",command=command_for_search2,bg="pink")
                btn.grid(column=0,row=4)
                def command_for_search3():
                    with a.cursor() as cursor:
                        query="select c_dist from Record"
                        cursor.execute(query)
                        freq=0
                        place=' '
                        lst=[]
                        for rows in cursor:
                            ct=1
                            for pps in cursor:
                                if pps==rows:
                                    ct+=1
                            if ct> freq:
                                freq=ct
                                place=rows
                            elif ct==freq:
                                lst.append(rows)
                    #print(place)
                    lst.append(place)
                    lst=tuple(lst)
                    lst=str(lst)
                    area=Tk()
                    area.title("Most unsafe area :")
                    area.geometry('300x300')
                    p=Label(area,text="The most unsafe area is --'"+lst+"'",bg="red")
                    p.grid(column=1,row=1)
                    area.mainloop()
                    #mb.showinfo("Most unsafe area",lst)
                btn=Button(front,text="Click here to find the most unsafe area",command=command_for_search3,bg="blue")
                btn.grid(column=0,row=5)
                def command_efficent():
                    EFF=Tk()
                    EFF.title("Efficency of the department:")
                    EFF.geometry("500x500")
                    total=0
                    solved=0
                    unsolved=0
                    with a.cursor() as cursor:
                        query="select status from Officer"
                        cursor.execute(query)
                    aa="SOLVED"
                    bb="UNSOLVED"
                    for row in cursor:
                        if row[0]==aa:
                            solved+=1
                        if row[0]==bb:
                            unsolved+=1
                        total+=1

                    eff=(solved/total)*100
                    efficency=str(solved)
                    total=str(total)
                    unsolved=str(unsolved)
                    eff=str(eff)
                    p=Label(EFF,text="The number of cases attended by the department is --'"+total+"'",bg="pink")
                    p.grid(column=0,row=0)
                    p=Label(EFF,text="The number of cases solved by the department is --'"+efficency+"'",bg="blue")
                    p.grid(column=0,row=1)
                    p=Label(EFF,text="The number of pending cases by the department is--'"+unsolved+"'",bg="green")
                    p.grid(column=0,row=2)
                    p=Label(EFF,text="Efficency of the department is --'"+eff+"'%",bg="red")
                    p.grid(column=0,row=3)
                    EFF.mainloop()
                btn=Button(front,text="Click here to check the efficency of the police department",command=command_efficent,bg="green")
                btn.grid(column=0,row=6)

                front.mainloop()

        if flag==0:
            mb.showinfo("Error","Invalid Password")
    f = Frame(login,bg="white",width=150,height=130)
    f.grid(row=0,column=0,sticky="NW")
    f.grid_propagate(0)
    f.update()
    login.config(background='white')
    id=Label(login,text="Enter your id",bg='green')
    id.grid(column=0,row=1)
    id=Entry(login,width=30)
    id.grid(column=1,row=1)
    ps=Label(login,text="Enter your password:",bg='blue')
    ps.grid(column=0,row=2)
    ps=Entry(login,width=30)
    ps.grid(column=1,row=2)

    #ps.place(relx=0.5,rely=0.5,anchor=CENTER)

    btn=Button(login,text="Login",command=login1)
    btn.grid(column=0,row=3)
    #btn.pack(side=CENTER)
    #btn.place(relx=0.5,rely=0.5,anchor=CENTER)
    login.mainloop()

def Civilian():
                    front=Tk()
                    front.title("Front page:")
                    front.geometry('800x800')
                    a=pms.connect(user='root',password='123456',host='localhost',db='Project1')
                    def command_for_view():
                        w=Tk()
                        w.title("Display the total")
                        w.geometry('1200x800')
                        v=Label(w,text="The data is here ")
                        v.grid(column=0,row=0)
                        ct=1
                        with a.cursor() as cursor:
                            cursor=a.cursor()
                            query="select* from Criminal,Record,Officer,Victum where Record.c_id=Criminal.c_id AND Record.c_id=Officer.c_id AND Record.c_id=Victum.c_id"
                            cursor.execute(query)

                            for row in cursor:
                                row=list(row)
                                xxx=0
                                p=Label(w,text="Case Details:",bg="red")
                                p.grid(column=0,row=ct)
                                ct=ct+1
                                p=Label(w,text="Case id--'"+row[0]+"'")
                                p.grid(column=xxx,row=ct)
                                #ct=ct+1
                                xxx=xxx+1
                                p=Label(w,text="Criminal Name--'"+row[1]+"'")
                                p.grid(column=xxx,row=ct)
                                #ct=ct+1
                                xxx+=1
                                p=Label(w,text="Case Type--'"+row[2]+"'")
                                p.grid(column=xxx,row=ct)
                                ct=ct+1
                                xxx=0
                                p=Label(w,text="Year--'"+row[4]+"'")
                                p.grid(column=xxx,row=ct)
                                xxx+=1
                                #ct=ct+1
                                p=Label(w,text="Place of Crime--'"+row[6]+"'")
                                p.grid(column=xxx,row=ct)
                                #ct=ct+1
                                xxx+=1
                                p=Label(w,text="Case status--'"+row[10]+"'")
                                p.grid(column=xxx,row=ct)
                                #ct=ct+1
                                #ct=ct+1
                                xxx+=1
                                p=Label(w,text="Case Officer--'"+row[9]+"'")
                                p.grid(column=xxx,row=ct)
                                ct=ct+1
                                p=Label(w,text="Victim Name--'"+row[12]+"'")
                                p.grid(column=0,row=ct)
                                p=Label(w,text="Victim Address--'"+row[13]+"'")
                                p.grid(column=1,row=ct)
                                p=Label(w,text="Date of crime--'"+row[15]+"'")
                                p.grid(column=2,row=ct)
                                ct=ct+1
                                p=Label(w,text="Statement of the Victim--'"+row[14]+"'")
                                p.grid(column=0,row=ct)
                                ct=ct+1
                                p=Label(w,text="Description --'"+row[7]+"'")
                                p.grid(column=0,row=ct)
                                ct=ct+1
                        w.mainloop()
                    btn=Button(front,text="Click here to view details",command=command_for_view,bg="green")
                    btn.grid(column=0,row=1)

                    def command_for_search():
                        SI=Tk()
                        SI.title("Search page 1")
                        SI.geometry('700x700')
                        s_id=Label(SI,text="Enter case id:",)
                        s_id.grid(column=0,row=0)
                        s_id=Entry(SI,width=10)
                        s_id.grid(column=1,row=0)
                        def search_id():
                                w=Tk()
                                w.title("Display the Searched result")
                                w.geometry('800x800')
                                v=Label(w,text="The Result is here ")
                                v.grid(column=0,row=0)
                                ct=1
                                cursor=a.cursor()
                                with a.cursor() as cursor:
                                    query="select * from Record,Officer where Record.c_id=Officer.c_id"
                                    cursor.execute(query)
                                    data=s_id.get()
                                    for row in cursor:
                                        if row[0]==data:
                                            row=list(row)
                                            xxx=0
                                            p=Label(w,text="Case Details:",bg="blue")
                                            p.grid(column=0,row=ct)
                                            ct=ct+1
                                            p=Label(w,text="Case id--'"+row[0]+"'")
                                            p.grid(column=xxx,row=ct)
                                            #ct=ct+1
                                            xxx=xxx+1
                                            p=Label(w,text="Year of crime--'"+row[1]+"'")
                                            p.grid(column=xxx,row=ct)
                                            #ct=ct+1
                                            xxx+=1

                                            p=Label(w,text="Place of Crime--'"+row[3]+"'")
                                            p.grid(column=xxx,row=ct)
                                            xxx+=1
                                            ct=ct+1
                                            #yr=str(row[4])
                                            p=Label(w,text="Crime Type'"+row[2]+"'")
                                            p.grid(column=0,row=ct)
                                            #ct=ct+1
                                            p=Label(w,text="Case status'"+row[7]+"'")
                                            p.grid(column=1,row=ct)
                                            p=Label(w,text="Description about the case--'"+row[4]+"'")
                                            p.grid(column=0,row=ct+1)
                                            ct+=2
                                w.mainloop()
                        btn = Button(SI, text="Click to check details:",command=search_id,bg='brown')
                        btn.grid(column=0, row=1)
                        SI.mainloop()

                    btn=Button(front,text="Click here to Search any data",command=command_for_search,bg="indigo")
                    btn.grid(column=0,row=2)

                    def command_for_search1():
                        SC=Tk()
                        SC.title("Display the searched results:")
                        SC.geometry("800x800")
                        s_crim=Label(SC,text="Enter criminal name:")
                        s_crim.grid(column=0,row=0)
                        s_crim=Entry(SC,width=10)
                        s_crim.grid(column=1,row=0)
                        def search_criminal():
                            w=Tk()
                            w.title("Display the Searched result")
                            w.geometry('800x800')
                            v=Label(w,text="The Result is here ")
                            v.grid(column=0,row=0)
                            ct=1
                            cursor=a.cursor()
                            with a.cursor() as cursor:
                                query="select * from Criminal"
                                cursor.execute(query)
                                data=(s_crim.get()).upper()
                                for row in cursor:
                                    if row[1]==data:
                                        row=list(row)
                                        xxx=0
                                        p=Label(w,text="Criminal Details:",bg="blue")
                                        p.grid(column=0,row=ct)
                                        ct=ct+1
                                        p=Label(w,text="Case id--'"+row[0]+"'")
                                        p.grid(column=xxx,row=ct)
                                        #ct=ct+1
                                        xxx=xxx+1
                                        p=Label(w,text="Criminal Name--'"+row[1]+"'")
                                        p.grid(column=xxx,row=ct)
                                        #ct=ct+1
                                        xxx+=1
                                        p=Label(w,text="Case Type--'"+row[2]+"'")
                                        p.grid(column=xxx,row=ct)

                            w.mainloop()
                        btn = Button(SC, text="Click here to view details:",command=search_criminal,bg='brown')
                        btn.grid(column=0, row=1)

                        SC.mainloop()
                    btn=Button(front,text="Click here to search the history of the criminal",command=command_for_search1,bg="red")
                    btn.grid(column=0,row=3)

                    def command_for_search2():
                            SO=Tk()
                            SO.title("Display the search results")
                            SO.geometry("800x800")
                            s_off=Label(SO,text="Enter officer name:")
                            s_off.grid(column=0,row=0)
                            s_off=Entry(SO,width=10)
                            s_off.grid(column=1,row=0)
                            def search_officer():
                                w=Tk()
                                w.title("Display the Searched result")
                                w.geometry('800x800')
                                v=Label(w,text="The Result is here ")
                                v.grid(column=0,row=0)
                                ct=1
                                efficency=0
                                total=0
                                unsolved=0
                                cursor=a.cursor()
                                with a.cursor() as cursor:
                                    query="select * from Officer"
                                    cursor.execute(query)
                                    data=(s_off.get()).upper()
                                    for row in cursor:
                                        if row[1]==data:
                                            row=list(row)
                                            xxx=0
                                            p=Label(w,text="Officer Details:",bg="blue")
                                            p.grid(column=0,row=ct)
                                            ct=ct+1
                                            p=Label(w,text="Case id--'"+row[0]+"'")
                                            p.grid(column=xxx,row=ct)
                                            #ct=ct+1
                                            xxx=xxx+1
                                            p=Label(w,text="Officer Name--'"+row[1]+"'")
                                            p.grid(column=xxx,row=ct)
                                            #ct=ct+1
                                            xxx+=1
                                            p=Label(w,text="Case status--'"+row[2]+"'")
                                            p.grid(column=xxx,row=ct)
                                            ct=ct+1
                                            if row[2]=='SOLVED':
                                                efficency+=1
                                            if row[2]=='UNSOLVED':
                                                unsolved+=1
                                            total+=1
                                eff=(efficency/total)*100
                                efficency=str(efficency)
                                total=str(total)
                                unsolved=str(unsolved)
                                eff=str(eff)
                                p=Label(w,text="The number of cases attended by the officer is --'"+total+"'",bg="green")
                                p.grid(column=0,row=ct)
                                ct=ct+1
                                p=Label(w,text="The number of cases solved by the officer is --'"+efficency+"'",bg="green")
                                p.grid(column=0,row=ct)
                                ct=ct+1
                                p=Label(w,text="The number of pending cases by the officer is--'"+unsolved+"'",bg="green")
                                p.grid(column=0,row=ct)
                                ct=ct+1
                                p=Label(w,text="Efficency of the offficer is --'"+eff+"'%",bg="red")
                                p.grid(column=0,row=ct)

                                w.mainloop()
                            btn = Button(SO, text="Click here to view details:",command=search_officer,bg='brown')
                            btn.grid(column=0, row=1)
                            SO.mainloop()

                    btn=Button(front,text="Click here to search the history of officer",command=command_for_search2,bg="pink")
                    btn.grid(column=0,row=4)
                    def command_for_search3():
                        with a.cursor() as cursor:
                            query="select c_dist from Record"
                            cursor.execute(query)
                            freq=0
                            place=' '
                            lst=[]
                            for rows in cursor:
                                ct=1
                                for pps in cursor:
                                    if pps==rows:
                                        ct+=1
                                if ct> freq:
                                    freq=ct
                                    place=rows
                                elif ct==freq:
                                    lst.append(rows)
                        #print(place)
                        lst.append(place)
                        lst=tuple(lst)
                        lst=str(lst)
                        area=Tk()
                        area.title("Most unsafe area :")
                        area.geometry('300x300')
                        p=Label(area,text="The most unsafe area is --'"+lst+"'",bg="red")
                        p.grid(column=1,row=1)
                        area.mainloop()
                        #mb.showinfo("Most unsafe area",lst)
                    btn=Button(front,text="Click here to find the most unsafe area",command=command_for_search3,bg="blue")
                    btn.grid(column=0,row=5)
                    def command_efficent():
                        EFF=Tk()
                        EFF.title("Efficency of the department:")
                        EFF.geometry("500x500")
                        total=0
                        solved=0
                        unsolved=0
                        with a.cursor() as cursor:
                            query="select status from Officer"
                            cursor.execute(query)
                        aa="SOLVED"
                        bb="UNSOLVED"
                        for row in cursor:
                            if row[0]==aa:
                                solved+=1
                            if row[0]==bb:
                                unsolved+=1
                            total+=1

                        eff=(solved/total)*100
                        efficency=str(solved)
                        total=str(total)
                        unsolved=str(unsolved)
                        eff=str(eff)
                        p=Label(EFF,text="The number of cases attended by the department is --'"+total+"'",bg="pink")
                        p.grid(column=0,row=0)
                        p=Label(EFF,text="The number of cases solved by the department is --'"+efficency+"'",bg="blue")
                        p.grid(column=0,row=1)
                        p=Label(EFF,text="The number of pending cases by the department is--'"+unsolved+"'",bg="green")
                        p.grid(column=0,row=2)
                        p=Label(EFF,text="Efficency of the department is --'"+eff+"'%",bg="red")
                        p.grid(column=0,row=3)
                        EFF.mainloop()
                    btn=Button(front,text="Click here to check the efficency of the police department",command=command_efficent,bg="green")
                    btn.grid(column=0,row=6)

                    front.mainloop()

def about():
    mb.showinfo("This project is developed by:","Avanish Gupta,Roll No:-14")

admin1=Tk()
admin1.title("Login type")
admin1.geometry("450x400")
C = Canvas(admin1, bg="blue", height=250, width=300)
filename = PhotoImage(file = "/home/avanish/Pictures/back.png")
background_label = Label(admin1, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
btn=Button(admin1,text="Click here for Officer login ",command=admin,bg='green')
btn.pack(side=TOP)
btn=Button(admin1,text="Click here for Civilian login ",command=Civilian,bg='blue')
btn.pack(side=BOTTOM)
btn=Button(admin1,text="About us ",command=about,bg='red')
btn.pack(side=LEFT)
admin1.mainloop()




amdin1=Tk()
frame=Frame(admin1)
Button(frame,text="Click here for Officer login ",command=admin,bg='green').pack(side=LEFT,fill=Y)
Button(frame,text="Click here for Civilian login ",command=Civilian,bg='blue').pack(side=RIGHT,fill=NONE)
Button(admin1,text="About us ",command=about,bg='red').pack(side=BOTTOM,fill=X)
frame.pack()
admin1.mainloop()
'''
from tkinter import *
root = Tk()
frame = Frame(root)
# demo of side and fill options

Label(frame, text="Pack Demo of side and fill").pack()
Button(frame, text="A",command=done).pack(side=LEFT, fill=Y)
Button(frame, text="B").pack(side=TOP, fill=X)
Button(frame, text="C").pack(side=RIGHT, fill=NONE)
Button(frame, text="D").pack(side=TOP, fill=BOTH)
frame.pack()
# note the top frame does not expand nor does it fill in
# X or Y directions
# demo of expand options - best understood by expanding the root
#widget and seeing the effect on all the three buttons below.
Label (root, text="Pack Demo of expand").pack()
Button(root, text="I do not expand").pack()
Button(root, text="I do not fill x but I expand").pack(expand = 1)
Button(root, text="I fill x and expand").pack(fill=X, expand=1)
root.mainloop()
'''
