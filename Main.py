import tkinter as tk
from tkinter import filedialog,Text
import os

root = tk.Tk()
apps =[]

if os.path.isfile('save.txt'):
    with open('save.txt') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps =[x for x in tempApps if x.strip()]

def AddApp():
     
    filename = filedialog.askopenfilename(initialdir="C:/program Files (x86)",title="Select Files",filetypes=(("executables","*.exe"),("All Files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame,text=app,bg ="Light gray")
        label.pack()
        

def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=500,width=500,bg="#234567")
canvas.pack()
frame = tk.Frame(root,bg ="White")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

OpenBtn = tk.Button(root, text="Select App",padx=10, pady=5,fg="White",bg="#234567",command=AddApp)
OpenBtn.pack()

RunappBtn = tk.Button(root, text="Run App",padx=10, pady=5,fg="White",bg="#234567", command =runApps)
RunappBtn.pack()

for app in apps:
    label = tk.Label(frame, text = "App")
    label.pack()

root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')
        