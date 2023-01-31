import re
import tkinter as tk
from tkinter import END, StringVar, ttk
import sqlite3
from tkinter import messagebox
from tkinter import font
from unicodedata import name
from cv2 import erode
from matplotlib import style
from matplotlib.pyplot import get, text
import psycopg2
from sqlalchemy import null, values
from config import config
import datetime
from calendar import monthrange
import psycopg2
from srt_config import config




def change1(*args):
	#print(year_val.get(), mon_val.get(), day_val.get())
    if (len(year.get())>=1) or (len(mon.get())>=1) or (len(day.get())>=1):
	
        x,y= year.get(), int(months.index(str(mon_val.get())))+1
        days= monthrange(int(x),int(y))
        #print(days)
        day["values"]= [i for i in range(1, int(days[1])+1)]
        #year.config(text=year_val.get()) 
    
         
def select_click(event):
    global selected
    for selected_item in tree.selection():

        item= tree.item(selected_item)
        
        selected= item["values"]
    
        

def show_data():
    
        front_page()

def update():
    #print(selected)
      
    global save_val, tm,ID    
    save_val= StringVar()
    save_val.set("existing")

    try:

        account_entry.delete(0, 'end')
        account_entry.insert(0, selected[0])

        hour_entry.delete(0, 'end')
        tm= selected[1].split(":")
        #print(tm)
        hour_entry.insert(0, tm[0])

        minutes_entry.delete(0, 'end')
        minutes_entry.insert(0, tm[1])



    
        deta= selected[2].split("/")
        #print(deta)
        year.delete(0, "end")
        year.set(deta[-1])

        
        mon.delete(0,'end')
        #print(datetime.datetime(int(deta[0]), int(deta[1]),int(deta[2])).strftime("%B"))
        mon.set(datetime.datetime(int(deta[-1]), int(deta[1]),int(deta[0])).strftime("%B"))

        day.delete(0, 'end')
        day.set(deta[0])

        #print(record)
    except Exception as error:
        messagebox.showerror('Postgres', "Select data to update on Treeview")
    check()


def check():
    global ID
    ID=[]
    for i in range(len(record)):

        if record[i][0]==selected[0] and  record[i][-1]== selected[1] and record[i][3]==selected[-1] :
            #print(record[i][-2])
            ID+=[record[i][-2]]
    

def new_data():
    global save_val
    save_val= StringVar()
    save_val.set("new_data")
    #new_ids= all_ids()
    #print(new_ids)

    try:
        
        account_entry.delete(0, 'end')

        hour_entry.delete(0, 'end')
        hour_entry.insert(END, '0')

        minutes_entry.delete(0, 'end')
        minutes_entry.insert(END, '0')

        x = datetime.datetime.now()
        day.set(x.strftime("%d"))
        mon.set(x.strftime("%B"))
        year.set(x.strftime("%Y"))




       
    except Exception as error:
        messagebox.showerror('Postgres', error)
       
def save():
    #print(save_val)
    if (save_val.get())=="existing"  and (account_entry.get()).isalpha() and  (hour_entry.get()).isnumeric() and  (minutes_entry.get()).isnumeric():
        
        sql = """ UPDATE srt_work_data
                    SET account= %s, hours=%s, mins=%s, date= %s where sn=%s"""
        try:
            
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the UPDATE  statement
            cur.execute(sql, 
                (
                    ((account_entry.get()).capitalize()).strip(),
                    int(hour_entry.get()),
                    int(minutes_entry.get()),
                        ("{}/{}/{}".format(day.get(),  ((datetime.datetime.strptime(str(mon.get()),"%B")).month), year.get())),
                        ID[0]
                        ))
            # get the number of updated rows
            #updated_rows = cur.rowcount
            ans= messagebox.askyesno("Confirmation", "DO you want to save this data??")
            if ans==True:
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
                messagebox.showinfo("Data Manager", """Record updated successfully.""")
            else:
                pass
            
        except Exception as error:
            print(error)
            messagebox.showerror('Postgres', error)
        finally:
            if conn is not None:
                conn.close()
                show_data()

                

    elif (save_val.get())=="new_data" and (account_entry.get()).isalpha() and  (hour_entry.get()).isnumeric() and  (minutes_entry.get()).isnumeric():
        
        sql = """insert into  srt_work_data (account, hours, mins,date) values
                    (%s, %s, %s, %s)
                    """
        conn = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, ((account_entry.get().capitalize()).strip(),
                            int(hour_entry.get()), 
                            int(minutes_entry.get()),
                            ("{}/{}/{}".format(day.get(), ((datetime.datetime.strptime(str(mon.get()),"%B")).month),  year.get()))
                    ))
            ans= messagebox.askyesno("Confirmation", "DO you want to save this data??")
            if ans==True:
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
                messagebox.showinfo("Data Manager", """New record created successfully !!! """)
            else:
                pass
        except (Exception, psycopg2.DatabaseError) as error:
            messagebox.showerror("DataBase Manager", error)
            print(error)
        finally:
            if conn is not None:
                conn.close()
                show_data()
    else:
        messagebox.showerror("DataBase Manager" ,"Multiple input fielded.")


def front_page():
    for item in tree.get_children():
                tree.delete(item)
    sql= """select *, concat(hours, ':', mins) as time from srt_work_data order by date;"""
    
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        records= cur.fetchall()
        global record
        record= records
        print(records)
        #Filter
        records=[ (records[i][0], records[i][-1], records[i][3]) for i in range(len(records))]
        
        #records= records.append("{}:{}".format(records[1], record[2]))
        #print(records)
        # add data to the treeview
        for i in range(len(records)):
            #tree.insert('', tk.END, values=data, )
            if ((i+1)%2)!=0:
                tree.insert(parent='', index=i, iid=i, text='', values= records[i],tag=('even',))
                tree.tag_configure('even', background='white')
            else:
                tree.insert(parent='', index=i, iid=i, text='', values= records[i],tag=('odd',))
                tree.tag_configure('odd', background='#DBF3FA')
            
        
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        messagebox.showerror("Database Manager", 'error')
    finally:
        if conn is not None:
            conn.close()
    


def delete():
    check()
    sql= """delete from srt_work_data where sn= %s;"""
    #print(record[1])

    conn= None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (ID[0],))
        
        #print(records)
        # add data to the treeview
        ans= messagebox.askyesno("DataBase Manager - Confirmation", "Do you know delete record ??")

        if ans==True:
            conn.commit()
            cur.close()
            messagebox.showinfo("DataBase Manager", "Data deleted")
        else:
            pass
    except (Exception, psycopg2.DatabaseError) as error:
        #print(error)
        messagebox.showerror("Database Manager", error)
    finally:
        if conn is not None:
            conn.close()
            front_page()

def destro():
    ans= messagebox.askyesno("Exit", "Do you want to exit??")
    if ans is True:
        root.destroy()
    else:
        pass


def create_input_frame(container):
    s=ttk.Style()

    
    #s.theme_names()
    global frame, account_entry, hour_entry,minutes_entry, year_val, mon_val,day_val, year,months, day, save_val
    s.configure('frame1.TFrame',font=('Segoe UI', 12), foreground = 'black', background="white")
    frame= ttk.Frame(container, style= 'frame1.TFrame', borderwidth= 5, padding=5)
    '''frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(1, weight=1)'''
    save_val= StringVar()
    save_val.set("new_data")

    #print(sch_dept.keys())
    x = datetime.datetime.now()
    #print(monthrange(2021, 2))
    years= [i for i in range(1950,int(x.strftime("%Y"))+1)]
    #print(years)
    months= ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #
    # ID 
   
    s.configure('label.TLabel', font=('Franklin Gothic Book', 10, ), foreground = 'black', background="white", padding=8)
    s.configure('l1.TLabel', font=('Franklin Gothic Book', 10, "bold"), foreground = 'black', background="white", padding=8)
    s.configure('entry.TEntry', font=('Franklin Gothic Book', 10), foreground = 'black', background="white")
    s.theme_use('alt')


    fn= ttk.Label(frame, text="SRT Job Record ", style="l1.TLabel").grid(column=0, row=0, sticky=tk.W)
    #Matric Number
    global ID_entry, surname_entry, last_name_entry, first_name_entry, mon



    #Surname label
    
    account_label= ttk.Label(frame, text='Account Name', style= 'label.TLabel').grid(column=0, row=2, sticky=tk.W)
    account_entry= ttk.Entry(frame, width=33, style= 'entry.TEntry',font = ('Franklin Gothic Book', 10))
    account_entry.focus()
    account_entry.grid(column=1, row=2, sticky=tk.W)


    #First Name label
    hours_label= ttk.Label(frame, text='Hours', style= 'label.TLabel').grid(column=0, row=3, sticky=tk.W)
    hour_entry= ttk.Entry(frame, width=33,style= 'entry.TEntry', font = ('Franklin Gothic Book', 10))
    hour_entry.focus()
    hour_entry.grid(column=1, row=3, sticky=tk.W)

    #Last Name label
    minutes_label= ttk.Label(frame, text='Minutes', style= 'label.TLabel').grid(column=0, row=4, sticky=tk.W)
    minutes_entry= ttk.Entry(frame, width=33,style= 'entry.TEntry', font = ('Franklin Gothic Book', 10))
    minutes_entry.focus()
    minutes_entry.grid(column=1, row=4, sticky=tk.W)


    #DOB label
    DOB_label= ttk.Label(frame, text='Date', style= 'label.TLabel').grid(column=0, row=9, sticky=tk.W)
    day_val= StringVar()
    day= ttk.Combobox(frame,width=3, textvariable=day_val, state="readonly", font = ('Franklin Gothic Book', 10))
    day.focus()
    
    day.set(x.strftime("%d"))
    day.grid(column=1,row=9, sticky='w')
    
    mon_val= StringVar()
    mon= ttk.Combobox(frame,width=10, textvariable=mon_val, values= months, state="readonly",font = ('Franklin Gothic Book', 10))
    mon.focus()
    mon.set(x.strftime("%B"))
    
    mon.grid(column=1, row=9,)

    
    year_val= StringVar()
    year= ttk.Combobox(frame,width=4, textvariable=year_val, values=([2022,x.strftime("%Y")]), state="readonly",font = ('Franklin Gothic Book', 10))
    year.focus()
    year.set(x.strftime("%Y"))
    
    year.grid(column=1, row=9, sticky=tk.E)

    return frame

def Button_frame(container):
    
    siu=ttk.Style()
    siu.theme_use('alt')
    
    siu.configure('frame3.TFrame', font=('Franklin Gothic Book', 12), foreground = 'black', background="white", )
   
    frame= ttk.Frame(container, style='frame3.TFrame', borderwidth= 5)
    siu.configure('C.TButton', font=('Franklin Gothic Book', 12), foreground = '#DADADA', background="#003166",focusthickness=3,relief= 'flat') #focusthickness=3,relief= 'flat'
    siu.map("C.TButton", 
    foreground=[('pressed', 'white'), ('active', 'white')], 
    background=[('pressed', '#003166'), ('active', '#003166')]) #background=[('pressed', '#4A521E'), ('active', '#597D39')]
   
    '''frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(1, weight=1)'''
    res= {'width':12, 'style':"C.TButton", 'padding':(10,10,10,10), 'cursor': 'hand2' }
    global update_button, save_button, add_button, delete_button, refresh_button
    
    update_button = ttk.Button(frame, text= 'Update Data',**res, command= update )
    update_button.grid(column=0, row=0, padx=20, pady=10 )    

    save_button = ttk.Button(frame, text= 'Save Data', **res, command= save)
    save_button.grid(column=1, row=0, padx=40, pady=10)

    add_button = ttk.Button(frame, text= 'New Data', **res,command= new_data)
    add_button.grid(column=2, row=0, padx=40, pady=10)

    delete_button = ttk.Button(frame, text= 'Delete Data', **res, command= delete)
    delete_button.grid(column=3, row=0, padx=40, pady=10)

    refresh_button = ttk.Button(frame, text= 'Refresh',  **res,command=front_page )
    refresh_button.grid(column=4, row=0, padx=40, pady=10)

    exit_button = ttk.Button(frame, text= 'Exit', **res, command= destro )
    exit_button.grid(column=5, row=0, padx=40, pady=10)




    
    return frame



def show_frame(container):
    
    s=ttk.Style()
    
    
    # s.theme_names()
    s.configure('frame2.TFrame', font=('Helvetica', 14), foreground = 'black', background="white")
    frame= ttk.Frame(container, style= "frame2.TFrame" )
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    #ttk.Label(text='Show Me').grid(row=0)
    columns = ("account", "date", "time")

    #columns = ("account", "hours", "mins", "date")
    #columns= ("account", "time", "date")
    customed_style = ttk.Style(frame)
    #customed_style.configure('Custom.TButton', font=('Helvetica', 11), background="red", foreground='white')
    customed_style.configure('Custom.Treeview', highlightthickness=0, bd=0, font=('Franklin Gothic Book', 10))
    customed_style.configure('Custom.Treeview.Heading', font=('Franklin Gothic Book', 10), background="#FFFFFF", foreground="black",)
    customed_style.map("Treeview", 
    foreground=[('disabled', 'white'), ('selected', 'black')], 
    background=[('disabled', '#003166'), ('selected', '#ACCEF7')])
    global tree
    tree = ttk.Treeview(frame, columns= columns,  show='headings',selectmode ='browse', style= 'Custom.Treeview')
    
        
    opt= {'anchor':'w','stretch':'yes'}

    tree.column('#0',**opt ,width= 30)
    tree.heading("account", text='Account Name', anchor='w')

    tree.column('#1',**opt,width= 30)
    tree.heading('date', text='Production Time', anchor='w')

    tree.column('# 2', **opt,width= 30)
    tree.heading('time', text='Date',anchor='w')

    '''tree.column('# 3',anchor='w',  width= 30)
    tree.heading('date', text='Date',anchor='w')'''

    tree.bind('<<TreeviewSelect>>', select_click)
    tree.grid(row=0, column=0, sticky='nsew')
    #tree.pack(fill='x')

    scrollbar = ttk.Scrollbar(frame, orient= 'horizontal', command=tree.xview)
    #scrollbar.place(relx=0.014, rely=0.875, relheight=0.020, relwidth=0.965)
    scrollbar.grid(row=1, column=0, sticky='ew')
    tree.configure(xscrollcommand = scrollbar.set)
    
    scrollbar = ttk.Scrollbar(frame, orient= 'vertical', command=tree.yview)
    #scrollbar.place(relx=0.014, rely=0.875, relheight=0.020, relwidth=0.965)
    scrollbar.grid(row=0, column=1, sticky='ns')
    tree.configure(yscrollcommand = scrollbar.set)
    return frame


def main_body():
    global root, save_val
    

    root= tk.Tk()
    root.title("SRT Management System")
    root.geometry("1300x730")
    root.resizable(0,0)
    s=ttk.Style()


    #s.configure('frame3.TFrame', font=('Helvetica', 14), foreground = 'white', background="black")
    but_frame= Button_frame(root)
    options = {'side':'bottom', 'expand':'False', 'fill':'both'}
    but_frame.pack(**options, ipady=8 )



    #onfigure('frame1.TFrame', font=('Helvetica', 14), foreground = 'white', background="black")
    input_frame=create_input_frame(root)
    options = {'side':'left', 'expand':'False', 'fill':'y'}
    input_frame.pack(**options,  ipadx=10)

    # s.configure('frame2.TFrame', font=('Helvetica', 14), foreground = 'white', background="black")
    framework= show_frame(root)
    options = {'side':'right', 'expand':'False', 'fill':'y'}
    framework.pack(**options, ipadx=1000)
    print(s.theme_names())

    front_page()
    new_data()
    year_val.trace("w", change1)
    mon_val.trace("w", change1)
    day_val.trace("w", change1 )
    root.mainloop()
    
    

if __name__=="__main__":
    main_body()




