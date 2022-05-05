from tkinter import *
root = Tk()

root.title ("School percentage manager")
root.geometry("600x600")

label_g3 = Label(root,text="Grade 3")
label_g3.place(relx = 0.5,rely = 0.2,anchor=CENTER)
label_g3_p = Label(root)
label_g3_p.place(relx = 0.5,rely = 0.25,anchor=CENTER)

label_g5 = Label(root,text="Grade 5")
label_g5.place(relx = 0.5,rely = 0.5,anchor=CENTER)
label_g5_p = Label(root)
label_g5_p.place(relx = 0.5,rely = 0.55,anchor=CENTER)

label_g7 = Label(root,text = "grade 7")
label_g7.place(relx=0.5,rely=0.8,anchor=CENTER)
label_g7_p = Label(root)
label_g7_p.place(relx=0.5,rely=0.85,anchor=CENTER)

class g3():
    def __init__(self,english,maths,hindi):
        self.english = english
        self.maths = maths
        self.hindi = hindi
        
    def percentage(self):
        marks = self.english + self.maths + self.hindi
        total_marks = marks/300
        g3_percent=total_marks*100
        label_g3_p["text"]=str(g3_percent)+ " %"
          
class g5():
    def __init__(self,english,maths,hindi,science):     
        self.english = english
        self.maths = maths
        self.hindi = hindi
        self.science = science
        
    def percentage(self):
        marks = self.english + self.maths + self.hindi + self.science
        total_marks = marks/400
        g5_percent=total_marks*100
        label_g5_p["text"]=str(g5_percent)+" %"

class g7():
    
    def __init__(self,english,maths,hindi,science,biology):
        self.english = english
        self.maths = maths
        self.hindi = hindi
        self.science = science
        self.biology = biology
        
    def percentage(self):
        marks = self.english + self.maths + self.hindi + self.science + self.biology
        total_marks = marks/500
        g7_percent=total_marks*100
        label_g7_p["text"]=str(g7_percent)+" %"
        
Prithvi = g3(91,92,98)
jordan = g5(99,91,97,99)
nimay = g7(40,49,70,90,30)

   
btn_g3 = Button(root,text="show percentage",command = Prithvi.percentage)
btn_g3.place(relx=0.5,rely=0.3)

btn_g5 = Button(root,text="show percentage",command = jordan.percentage)
btn_g5.place(relx=0.5,rely=0.6)

btn_g7 = Button(root,text="show percentage",command = nimay.percentage)
btn_g7.place(relx=0.5,rely=0.9)

        
root.mainloop()        