import csv
import json
from tkinter import*
import random
from tkinter import filedialog  
from tkinter import messagebox

def Ask_File():
    global CSV_File_Path
    CSV_File_Path = filedialog.askopenfilename()    #Asking for File Path
    #Write Label on correct posiution to Insert full path a Labe on Window

    L3 = Label(Window,text=CSV_File_Path,font=('Times New Roman',12,'bold'),fg='gray7',bg='navajowhite3',justify='center')
    L3.place(x=80,y=220)

def Ask():
    global JSON_Path
    JSON_Path = filedialog.askdirectory()                   #Asking for Dircetory Path
    #Write Label on correct posiution to Insert full path a Labe on Window

    L4 = Label(Window,text=JSON_Path,font=('Times New Roman',12,'bold'),fg='gray7',bg='navajowhite3',justify='center')
    L4.place(x=80,y=350)

def Show_Data(Json_File_Path):
    messagebox.showinfo('Success',f'File Converted Successfully and Present at {Json_File_Path}')
    Win = Tk()
    Win.title('Converted JSON Data')
    Win.geometry('500x500+500+150')
    #Win.resizable(False,False)
    Win.iconbitmap('Icon_Convert.ico')
    Win.config(background='yellow4')
    Label(Win, text='Converted JSON Data', font=('Arial', 20, 'bold'),bg='lightgoldenrodyellow')

    Q = Button(Win,text='Quit',fg='black',bg='red',font=('Times New Roman',15,'bold'),highlightbackground='gray24',highlightthickness=5,bd=5,relief='groove',command=lambda:Quit(Win))

    T = Text(Win,height=45,width=170,selectbackground='yellow',selectborderwidth=4,selectforeground='blue',inactiveselectbackground='pink')

    with open(Json_File_Path,'r',encoding='utf-8') as File:
        
        for I in File:   #Reading Each Diff Key valid Pir Collection from JSOn 
            D = json.loads(I)  
            T.insert(END,D)
            T.insert(END,'\n')
        T.pack()      #Seeting it Over window     
    Q.pack(side='right')

    Win.mainloop()


def Convert_File():
    global JSON_Path
    Window.destroy()
    global CSV_File_Path,JSON_Path

    try:
        with open(CSV_File_Path,'r',encoding='utf-8') as File_CSV: #Readling of data from CSV in dict form 
            Data_CSV = csv.DictReader(File_CSV)
            Data = list(Data_CSV)
            
            JSON_Path = JSON_Path+'/'+random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')+'.json'
            with open(JSON_Path,'a+',encoding='utf-8') as File_JSON:
                for D in Data:                                                  
                    json.dump(D,File_JSON,ensure_ascii=False)        #Writing data in JSOn like each Line or Eac Key Val Pair Collection      
                    File_JSON.write('\n')
        Show_Data(JSON_Path)
    except Exception as E:
        messagebox.showerror('Error',f'Error Occured : {E}')        

def Submit():   #This is Actually respoibsle for Checking that Corcet Paths have been selected
    global CSV_File_Path,JSON_Path

    if(len(CSV_File_Path)==0):
        messagebox.showerror('Error','Please Select CSV File')
    elif (CSV_File_Path[-3::1]!='csv'):
        messagebox.showerror('Error Invalid File','Please Select CSV File Only')
    elif(len(JSON_Path)==0):
        messagebox.showerror('Error','Please Select JSON File Path Where You Wanna Store Converted CSV to JSON')
    else:
        Convert_File()   #Means After Checking of Each Validation Now its time basically the Converting File if VErything is Correcy

def Quit(Window):
    Msg = messagebox.askyesno('Quit Request','Are You Sure You Wanna Quit ?')
    if(Msg==True):
        Window.quit()
        Window.destroy()    
    else:
        pass   

CSV_File_Path,JSON_Path = str(),str()
Window = Tk()
Window.title("  ------------ 🔁 CSV to JSON Converter ----------")
Window.geometry("570x520+570+170")
Window.resizable(False,False)
Window.iconbitmap('Icon_Convert.ico')

Window.config(background='navajowhite3')


L1 = Label(Window,text=' ** CSV to JSON Converter **',font=('Times New Roman',20,'bold'),fg='gray7',bg='lightgoldenrodyellow',cursor='hand1',highlightbackground='#872657',bd=7,highlightthickness=7,relief='groove')


L2 = Label(Window,text='Select CSV and JSON File By Click on Buttons',font=('Times New Roman',13,'bold'),fg='gray7',bg='navajowhite3')


B1 = Button(Window,text='Open CSV File ↗️',font=('MS Sans Serif',12,'bold'),fg='#FFFFFF',bg='#1E90FF',highlightbackground='#FDF5E6',highlightthickness=5,bd=5,command=Ask_File,relief='sunken')

B2 = Button(Window,text='Open JSON Path ↗️',font=('MS Sans Serif',12,'bold'),fg='#FFFFFF',bg='#1E90FF',highlightbackground='#FDF5E6',highlightthickness=5,bd=5,command=Ask,relief='sunken')


Sub = Button(Window,text=' Convert 🔁',bg='#5E2612',font=('DejaVu Sans',16,'bold'),fg='#F4F4F4',bd=8,highlightbackground='seashell4',highlightthickness=8,relief='ridge',activebackground='blue',activeforeground='white',cursor='hand2',command=Submit)

Q = Button(Window,text='Quit',fg='black',bg='red',font=('Times New Roman',15,'bold'),highlightbackground='gray24',highlightthickness=5,bd=5,relief='groove',command=lambda: Quit(Window))



# Window.bind('<Return>',lambda event:Submit)
# Window.bind('<Escape>',lambda event:Window.quit)


L1.place(x=90,y=10)
L2.place(x=112,y=88)
B1.place(x=180,y=165)
B2.place(x=175,y=290)
Sub.place(x=400,y=420)
Q.place(x=40,y=450)


Window.bind("<Return>",lambda event=None: Submit())
Window.bind("<Escape>",lambda event=None: Quit(Window))



#Various bcakforund Color Codes Best Conbination Give Like for Label and for Button aEveyrthing

#Label
#Tkinter fonts List

Window.mainloop()

