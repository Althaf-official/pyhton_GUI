from tkinter import * #this star for we are using to use all module from this library

window=Tk()
#create button and label
button=Button(text="ok",width=10,height=10)
label=Label(window,text="welcome")

#show button and label in the window
button.pack()
label.pack()

#its working as a loop for if any changes it will show here
window.mainloop()