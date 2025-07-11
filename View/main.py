import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import *
from tkcalendar import Calendar
import datetime as dt
import classconfig as classcfg
import sessionlog as sesslog
import anecdata as anec
import student as stud
import attendance as attend


# ******************Attendance methods start here ******************
def Attendance():
  hideAllFrames()
  root.title("PSBB Assist - Attendance")
  attend_frame.pack(fill="both", expand=1)

def attendanceSave():
  # scan the checkboxes for selections
  # Insert new rows in the attendance table for all new selections
  # look for the students whose absence is nullified by the checkbox unchecks.
  # delete the absence rows for the unchecks
  # AddAbsentee(idstudclass, dateabsent, absentreason="")
  # DeleteAbsentee(idattendance):  idattendance is at 8th index in dictAbsentee
  global dictAbsentee
  global absenteetracklist
  attend_date = cal_attend.selection_get()
  for i in absenteetracklist:
    if i[1].get() == 1: # this is true for all the checked ones
      if i[0] not in dictAbsentee.keys(): #absentee newly marked now, so insert absentee
        attend.AddAbsentee(i[0], attend_date, "")
    else:
      if i[0] in dictAbsentee.keys():  #original absentee but now marked as present by unchecking
        idattend = dictAbsentee.get(i[0])
        attend.DeleteAbsentee(idattend[8])
  messagebox.showinfo("Save...", "Absentee details saved")

def attendListStudents():
  global absenteetracklist
  btn_attend_save.grid_forget()
  for widget in lbl_frame_absentees.winfo_children():
    widget.destroy()

  # get the value from the Class combo box cbo_attend_class and find the corresponding idclass
  idclass = classlist[cbo_attend_class.current()][0]
  # query the list of students from the selected class
  # idstudent, studfname, studlname,idstudclass, idclass 
  liststud = stud.getStudentsbyClass(idclass) #"12F2202223"
  
  # get the date value from cal_attend
  attend_date = cal_attend.selection_get()
  # query the absentee details for the selected class and date from the attendance table
  global dictAbsentee
  dictAbsentee.clear()
  dictAbsentee = attend.QueryAbsentee(idclass, str(attend_date))
  absenteetracklist.clear()
  # in the below code a list of list absenteetrackerlist is appended with details of
  # all the students in the selected class. If any student is already marked absent in the db
  # they are also marked in the 1st index in the inner list.
  for student in liststud:
    isAbsent = tk.IntVar()
    if dictAbsentee.get(student[3]) == None:
      isAbsent = tk.IntVar(value=0)
    else:
      isAbsent = tk.IntVar(value=1)
    absenteetracklist.append([student[3],isAbsent, student[1],student[2]])
  
  # Create a label frame (lbl_frame_absentees) with one checkbox for each student
  # the check box will be checked if the student was absent on the selected date
  ctr = 0
  chk = None
  for i in absenteetracklist:
    ctr +=1
    chk = Checkbutton(lbl_frame_absentees,
              text= i[2] + " . " + i[3],
              variable=i[1],
              onvalue=1,
              offvalue=0)
    chk.grid(row=ctr, column=1, padx=20, pady=10, sticky='WN')
    i.append(chk)
  if len(liststud) > 0:
    btn_attend_save.grid(row=2, column=1,padx=20,pady=10,sticky='WN')
# ******************Attendance methods end here ******************



# ******************Anecdote methods start here ******************
def newAnecdote():
  hideAllFrames()
  root.title("PSBB Assist - Anecdote")
  anec_new_frame.pack(fill="both", expand=1) 

def anecdoteUpdate():
  selectedItem = tree_anec_data.selection()[0]
  idanecdote = tree_anec_data.item(selectedItem)['values'][8]
  oldanecdesc = tree_anec_data.item(selectedItem)['values'][5]
  anecdesc = text_anec_desc.get('1.0','end-1c')
  if oldanecdesc == anecdesc:
    messagebox.showinfo("Save...", "No Changes to save")
  else:
    anec.UpdateAnecdote(idanecdote, anecdesc)
    anecdoteSearch()

def newanecdoteSave():
  # get the data entered for anecdote and call the AddAnecdote function in anecdata.py file.
  # idstudclass, anecdate, idteacher, anectype, anecdesc are the fields in anecdote table 
  # get the idstudclass by looking up studlist list for the selected student name from the cbo_stud_name 
  global studlist
  anectype = ""
  if len(studlist) > 0:
    idstudclass = studlist[cbo_stud_name.current()][3]
    # get the anecdotedate from the calendar 
    anecdate = cal_new_anecdate.selection_get()
    # idteacher is assumed 1 for now
    idteacher = 1
    # anectype need to be taken from cbo_new_anectype
    anectype = cbo_new_anectype.get()
    # anecdesc need to be taken from text_new_anecdesc
    anecdesc = text_new_anecdesc.get('1.0','end')
    if idstudclass > 0 and len(anectype) > 0:
      anec.AddAnecdote(idstudclass, anecdate, idteacher, anectype, anecdesc)
      anecdoteSearch()
    else:
      messagebox.showinfo("Save...", "Student Name and Category needed")
  else:
    messagebox.showinfo("Save...", "No Changes to save")
    
def anecdoteAdd():
  lbl_anec_desc.grid_forget()
  text_anec_desc.grid_forget()
  btn_anec_update.grid_forget()
  scrl_vert_anec.grid_forget()
  cbo_stud_name.set('')
  cbo_new_anectype.set('')
  text_new_anecdesc.delete('1.0','end')
  global studlist 
  lststudname = []
  tree_anec_data.grid_forget()
  idclass = classlist[cbo_anec_class.current()][0]
  studlist = stud.getStudentsbyClass(idclass)
  #idstudent, studfname, studlname,idstudclass, idclass
  for i in studlist:
    lststudname.append(i[1] +" . "+i[2])
  cbo_stud_name['values'] = lststudname
  cbo_stud_name.grid(row=2, column=1,padx=20, pady=10, sticky='W')
  lbl_stud_name.grid(row=2, column=0,padx=20, pady=10, sticky='W')
  lbl_new_anecdate.grid(row=3, column=0, padx=20, pady=10, sticky='WN')
  cal_new_anecdate.grid(row=3, column=1, padx=20, pady=10, sticky='WN')
  lbl_new_anecdesc.grid(row=4, column=0, padx=20, pady=10,sticky='WN')
  text_new_anecdesc.grid(row=4, column=1, padx=20, pady=10,sticky='WN')
  lbl_new_anectype.grid(row=5, column=0, padx=20, pady=10,sticky='WN')
  cbo_new_anectype.grid(row=5, column=1, padx=20, pady=10,sticky='WN')
  btn_new_anecsave.grid(row=6,column=2,padx=20, pady=10,sticky='WN')

def anecdoteSearch():
  global classlist
  global listclasssubject
  lbl_anec_desc.grid_forget()
  text_anec_desc.grid_forget()
  btn_anec_update.grid_forget()
  cbo_stud_name.grid_forget()
  lbl_stud_name.grid_forget()
  lbl_new_anecdate.grid_forget()
  cal_new_anecdate.grid_forget()
  lbl_new_anecdesc.grid_forget()
  text_new_anecdesc.grid_forget()
  lbl_new_anectype.grid_forget()
  cbo_new_anectype.grid_forget()
  btn_new_anecsave.grid_forget() 
  #clear the existing data from the tree
  for row in tree_anec_data.get_children():
    tree_anec_data.delete(row)
  #get the class division id from the combo box
  idclass = classlist[cbo_anec_class.current()][0]

  lstanec = anec.QueryAnecdote(idclass)
  # 0-idanecdote,1-idstudclass,2-anecdate,3-idteacher,4-anectype,5-anecdesc,
  # 6-idstudent,7-studfname,8-studlname,9-gender,10-idclass,11-rollnumber,12-standard,13-division,14-acadyr,
  # 15-teacherfname,16-teacherlname
  # "6-idstudent","7-studfname","8-studlname","11-rollnumber","4-anectype","5-anecdesc","15-teacherfname","2-anecdate"
  anecList =[]
  if len(lstanec) > 0:
    for i in lstanec:
      anecList.append([i[6],i[7],i[8],i[11],i[4],i[5],i[15],i[2],i[0]])
    for i in anecList:
      tree_anec_data.insert(parent='', index='end',iid=i[8], text="", values=i)
  tree_anec_data.grid(row=2, column=1,pady=10, columnspan=5, sticky='W')
  scrl_vert_anec.grid(row=2, column=6, sticky='NS')

def treeAnecdoteSelect(event):
  selectedItem = tree_anec_data.selection()[0]
  anecdotetext = tree_anec_data.item(selectedItem)['values'][5]
  text_anec_desc.delete('1.0','end')
  text_anec_desc.insert('1.0',anecdotetext)
  lbl_anec_desc.grid(row=3, column=0, padx=20, pady=10,sticky='WN')
  text_anec_desc.grid(row=3, column=1, padx=20, pady=10,sticky='WN')
  btn_anec_update.grid(row=3,column=2,padx=20, pady=10,sticky='WN')
# ************************Anecdote methods end here ***************************




# ************************Session log methods start here ***************************
def newSessionLog():
  hideAllFrames()
  root.title("PSBB Assist - Session Log")
  slog_new_frame.pack(fill="both", expand=1) 


def hideAllFrames():
  canvas.pack_forget()
  slog_new_frame.pack_forget()
  anec_new_frame.pack_forget()
  attend_frame.pack_forget()

def sessionLogSave():
  global sesslogtext
  global listclasssubject
  sesslogtext = text_sessionlog.get('1.0','end-1c')
  if cbo_subject.current() <= 0:
    messagebox.showerror("Error", "Please select a subject")
  elif len(sesslogtext) <= 0:
    messagebox.showerror("Error", "Please enter session summary")
  else:
    #determine if this is a Add/Insert or Update
    selectedItem = tree_slog_data.selection()[0]
    #this is the update code
    if tree_slog_data.item(selectedItem)['values'][1]:
      if sesslogtext == tree_slog_data.item(selectedItem)['values'][2]:
        messagebox.showinfo("Save...", "No Changes to save")
      else:
        logcontent = sesslogtext
        idsessionlog = tree_slog_data.item(selectedItem)['values'][3]
        sesslog.UpdateSessionLog(idsessionlog, logcontent)
    else: #Insert/Add new session summary log
      #assign the id of the selected class to idclass
      idclass = classlist[cbo_slog_class.current()][0]
      idsubject = listclasssubject[cbo_subject.current()-1][1]
      sessionnum = tree_slog_data.item(tree_slog_data.selection()[0])['values'][0]
      logcontent = sesslogtext
      logdate = cal.selection_get()
      sesslog.AddSessionLog(idclass, idsubject, sessionnum, logcontent,logdate)
    sessionLogSearch()

def sessionLogSearch():
  lbl_subejct.grid_forget()
  cbo_subject.grid_forget()
  lbl_sessionlog.grid_forget()
  text_sessionlog.grid_forget()
  btn_slog_save.grid_forget()
  global classlist
  global listclasssubject
  #clear the existing data from the tree
  for row in tree_slog_data.get_children():
    tree_slog_data.delete(row)
  #get the class division id from the combo box
  idclass = classlist[cbo_slog_class.current()][0]

  #get the list of subjects for the selected class and division from database
  listclasssubject = classcfg.QueryClassSubject(idclass)
  
  #add the subject list to the combo box at the bottom not shown yet
  subjvalues = [""]
  for val in listclasssubject:
    subjvalues.append(val[2])
  cbo_subject['values'] = subjvalues
  
  datelog = cal.selection_get()
  lstsessionlog = sesslog.QuerySessLog(idclass, "", "", str(datelog), "")
  sessionList = [[1,"","","","","",""],[2,"","","","","",""],[3,"","","","","",""],[4,"","","","","",""],
                 [5,"","","","","",""],[6,"","","","","",""],[7,"","","","","",""],[8,"","","","","",""],[9,"","","","","",""]]
  if len(lstsessionlog) > 0:
    for slog in lstsessionlog:
      sessionList[slog[4]-1][1] = slog[3]
      sessionList[slog[4]-1][2] = slog[6]
      sessionList[slog[4]-1][3] = slog[0]
      sessionList[slog[4]-1][4] = slog[2]
      sessionList[slog[4]-1][5] = slog[1]
      sessionList[slog[4]-1][6] = slog[5]
  for i in sessionList:
    tree_slog_data.insert(parent='', index='end',iid=i[0]-1, text="", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
  tree_slog_data.grid(row=3, column=0,padx=20, pady=10, columnspan=5, sticky='W')

def treeSessionSelect(event):
  global sesslogtext
  #clear earlier values
  text_sessionlog.delete("1.0","end")
  cbo_subject.current(0)
  selectedItem = tree_slog_data.selection()[0]
  lbl_subejct.grid(row=4, column=0, padx=20, pady=10,sticky='W')
  if tree_slog_data.item(selectedItem)['values'][1]:
    cbo_subject.set(tree_slog_data.item(selectedItem)['values'][1])
  cbo_subject.grid(row=4,column=1,padx=20,pady=10,sticky='W')
  lbl_sessionlog.grid(row=5, column=0,padx=20, pady=10,sticky='WN')
  sesslogtext = tree_slog_data.item(selectedItem)['values'][2]
  text_sessionlog.insert('1.0',sesslogtext)
  text_sessionlog.grid(row=5,column=1,padx=20,pady=10,sticky='W')
  btn_slog_save.grid(row=5,column=2,padx=20, pady=10,sticky='W')

# ************************Session log methods end here ***************************




# *******************This is the start of the program ****************************
# *******************all the above are user defined functions for various actions *********
root = tk.Tk()
root.title("PSBB Assist")
menubar = tk.Menu(root)
#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 10
y= int(root.winfo_screenheight() * 0.01)
root.geometry('1000x800+' + str(x) + '+' + str(y))
root.config(menu = menubar)

menu_sessionlog = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Session Log', menu = menu_sessionlog)
menu_sessionlog.add_command(label ='New Session Log', command = newSessionLog)
menu_sessionlog.add_separator()
menu_sessionlog.add_command(label ='Exit', command = root.destroy)

menu_anecdote = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Anecdotal records', menu = menu_anecdote)
menu_anecdote.add_command(label ='New/Edit Anecdote', command = newAnecdote)

menu_attendance = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Attendance', menu = menu_attendance)
menu_attendance.add_command(label ='Enter Attendance', command = Attendance)

#create frame for session log screen
slog_new_frame = tk.Frame(root, width=600, height=600, bg='mistyrose2')
#Below this line we are creating the UI for Session log Add/Update/View frame
lbl_slog_date = Label(slog_new_frame, text = "Date")
lbl_slog_date.grid(row=1, column=0, padx=20, pady=10, sticky='WN')
today = dt.datetime.now()
cal = Calendar(slog_new_frame, selectmode = 'day',
               year = today.year, month = today.month,
               day = today.day,
               showweeknumbers = False)
cal.grid(row=1, column=1, padx=20, pady=10)
lbl_slog_class = Label(slog_new_frame, text="Class ")
lbl_slog_class.grid(row=1, column=2, padx=20, pady=10,sticky='WN')
# Build the combobox for list of classes and divisions
classlist = classcfg.QueryClassConfig()
classdiv = []
for val in classlist:
  classdiv.append(str(val[1])+" - "+ val[2])
cbo_slog_class = Combobox(slog_new_frame, state="readonly", width=10, values = classdiv)
cbo_slog_class.current(0)
cbo_slog_class.grid(row=1, column=3,padx=20, pady=10,sticky='WN')
btn_slog_search = Button(slog_new_frame,text="Search...", command=sessionLogSearch )
btn_slog_search.grid(row=1, column=4, padx=20, pady=10,sticky='W')

# result tree creation
tree_slog_data = Treeview(slog_new_frame, selectmode='browse', height=9)
# create columns
#idsessionlog, idclass, idsubject, subjectname, sessionnum, datelog, logcontent
tree_slog_data['columns'] = ("Session #", "Subject", "Session Summary","SessionLog id","Subject id","Class id","Date Log")
tree_slog_data.column("#0", width=0, stretch='no')
tree_slog_data.column("Session #", anchor='center', width=80) #sessionnum
tree_slog_data.column("Subject", anchor='w', width=80) #subjectname
tree_slog_data.column("Session Summary", anchor='w', width=400) #logcontent
tree_slog_data.column("SessionLog id", anchor='w', width=0) #idsessionlog
tree_slog_data.column("Subject id", anchor='w', width=0) #idsubject
tree_slog_data.column("Class id", anchor='w', width=0) #idclass
tree_slog_data.column("Date Log", anchor='w', width=0) #datelog
tree_slog_data["displaycolumns"] = ("Session #","Subject","Session Summary")
# create Headings in tree
tree_slog_data.heading("#0",text="")
tree_slog_data.heading("Session #", text="Session #",anchor='center')
tree_slog_data.heading("Subject", text="Subject",anchor='w')
tree_slog_data.heading("Session Summary", text="Session Summary",anchor='w')
tree_slog_data.bind("<<TreeviewSelect>>", treeSessionSelect)

listclasssubject = []
sesslogtext = tk.StringVar()
lbl_subejct = Label(slog_new_frame, text = "Subject")
cbo_subject = Combobox(slog_new_frame, state="readonly", width=10, values =[])
lbl_sessionlog = Label(slog_new_frame, text = "Summary")
text_sessionlog = tk.Text(slog_new_frame, height = 3, width = 30)
btn_slog_save = Button(slog_new_frame,text="Save", command=sessionLogSave)

# *****************End of Session log frame *****************************







#********************Beginning of the Anecdote UI code***************************
#create frame for Anecdote screen
anec_new_frame = tk.Frame(root, width=800, height=800, bg='wheat')

#Class and division combo box
lbl_anec_class = Label(anec_new_frame, text="Class")
lbl_anec_class.grid(row=1, column=0, padx=20, pady=10,sticky='WN')
# Build the combobox for list of classes and divisions
cbo_anec_class = Combobox(anec_new_frame, state="readonly", width=10, values = classdiv)
cbo_anec_class.current(0)
cbo_anec_class.grid(row=1, column=1,padx=20, pady=10,sticky='WN')
#Search button to search for existing anecdotes in the class
btn_anec_search = Button(anec_new_frame,text="Search...", command=anecdoteSearch)
btn_anec_search.grid(row=1, column=2, padx=20, pady=10,sticky='WN')

btn_anec_new = Button(anec_new_frame,text="New Anecdote...", command=anecdoteAdd)
btn_anec_new.grid(row=1, column=3, padx=20, pady=10,sticky='WN')

studlist=[]
lbl_stud_name = Label(anec_new_frame, text="Student")
cbo_stud_name = Combobox(anec_new_frame, state="readonly", width=15)

#Date of Anecdote
lbl_new_anecdate = Label(anec_new_frame, text = "Date")
today = dt.datetime.now()
cal_new_anecdate = Calendar(anec_new_frame, selectmode = 'day',
               year = today.year, month = today.month,
               day = today.day,
               showweeknumbers = False)
lbl_new_anecdesc = Label(anec_new_frame, text="Description")
text_new_anecdesc = tk.Text(anec_new_frame, height = 3, width = 50)
lbl_new_anectype = Label(anec_new_frame, text="Category")
cbo_new_anectype = Combobox(anec_new_frame, state="readonly", width=15, values=["Positive","Negative"])
btn_new_anecsave = Button(anec_new_frame,text="Save ", command=newanecdoteSave)

# result tree creation for anecdotes
tree_anec_data = Treeview(anec_new_frame, selectmode='browse', height=5)
tree_anec_data['columns'] = ("idstudent","studfname","studlname","rollnumber","anectype","anecdesc","teacherfname","anecdate",
                             "idanecdote","idstudclass","idteacher","gender","idclass","standard","division","acadyr",
                             "teacherlname")
tree_anec_data.column("#0", width=0, stretch='no')
tree_anec_data.column("idstudent", anchor='center', width=60)
tree_anec_data.column("studfname", anchor='w', width=100) 
tree_anec_data.column("studlname", anchor='w', width=100) 
tree_anec_data.column("rollnumber", anchor='center', width=50)
tree_anec_data.column("anectype", anchor='w', width=60) 
tree_anec_data.column("anecdesc", anchor='w', width=300)
tree_anec_data.column("teacherfname", anchor='w', width=0)
tree_anec_data.column("anecdate", anchor='w', width=100)
tree_anec_data.column("idanecdote", anchor='w', width=0)
tree_anec_data.column("idstudclass", anchor='w', width=0)
tree_anec_data.column("idteacher", anchor='w', width=0)
tree_anec_data.column("gender", anchor='w', width=0)
tree_anec_data.column("idclass", anchor='w', width=0)
tree_anec_data.column("standard", anchor='w', width=0)
tree_anec_data.column("division", anchor='w', width=0)
tree_anec_data.column("acadyr", anchor='w', width=0)
tree_anec_data.column("teacherlname", anchor='w', width=0)

tree_anec_data["displaycolumns"] = ("idstudent","studfname","studlname","rollnumber","anectype","anecdesc","anecdate")
# create Headings in tree
tree_anec_data.heading("#0",text="")
tree_anec_data.heading("idstudent", text="USN",anchor='center')
tree_anec_data.heading("studfname", text="First Name",anchor='w')
tree_anec_data.heading("studlname", text="Last Name",anchor='w')
tree_anec_data.heading("rollnumber", text="Roll #",anchor='center')
tree_anec_data.heading("anectype", text="Type",anchor='w')
tree_anec_data.heading("anecdesc", text="Anecdote",anchor='w')
#tree_anec_data.heading("teacherfname", text="Teacher",anchor='w')
tree_anec_data.heading("anecdate", text="Date",anchor='w')
tree_anec_data.bind("<<TreeviewSelect>>", treeAnecdoteSelect)

scrl_vert_anec = Scrollbar(anec_new_frame,
                           orient ="vertical",
                           command = tree_anec_data.yview)
# Configuring treeview
tree_anec_data.configure(yscrollcommand = scrl_vert_anec.set)

lbl_anec_desc = Label(anec_new_frame, text="Description")
text_anec_desc = tk.Text(anec_new_frame, height = 3, width = 50)
btn_anec_update = Button(anec_new_frame,text="Save ", command=anecdoteUpdate)

#********************End of Anecdote UI code *********************








# **************Begin UI code for Attendance***************
attend_frame = tk.Frame(root, width=800, height=800, bg='azure')
absenteetracklist = []
dictAbsentee = {}
#Class and division combo box
lbl_attend_class = Label(attend_frame, text="Class")
lbl_attend_class.grid(row=1, column=0, padx=20, pady=10,sticky='WN')
# Build the combobox for list of classes and divisions
cbo_attend_class = Combobox(attend_frame, state="readonly", width=10, values = classdiv)
cbo_attend_class.current(0)
cbo_attend_class.grid(row=1, column=1,padx=20, pady=10,sticky='WN')

#Date of Attendance
lbl_attend_date = Label(attend_frame, text = "Date")
lbl_attend_date.grid(row=1,column=2, padx=20,pady=10,sticky='WN')
today = dt.datetime.now()
#format_date = f"{date:%a, %b %d %Y}"
cal_attend = Calendar(attend_frame, selectmode = 'day',
               year = today.year, month = today.month,
               day = today.day,
               showweeknumbers = False)
cal_attend.grid(row=1,column=3, padx=20,pady=10,sticky='WN')
studlist=[]
#Search button to search for existing anecdotes in the class
btn_attend_studlist = Button(attend_frame,text="List Students...", command=attendListStudents)
btn_attend_studlist.grid(row=1, column=4, padx=20, pady=10,sticky='WN')

lbl_frame_absentees = LabelFrame(attend_frame, text="Select the Absentees")
lbl_frame_absentees.grid(row=2,column=0,padx=20, pady=10, sticky='WN')

btn_attend_save = Button(attend_frame,text="Save...", command=attendanceSave)

# **************End UI code for Attendance***************


#This creates the main window of an application with logo
logoimg = Image.open("View\\psbblogo.jpg")
logo = ImageTk.PhotoImage(logoimg)
canvas = tk.Canvas(root, width = 300, height = 300)
canvas.pack()
canvas.create_image(50, 50, anchor='nw', image=logo) 

root.mainloop()