from tkinter import * #this star for we are using to use all module from this library

window=Tk()
window.geometry("500x500")
window.title("mas solutions")
window.configure(background="green")

#function for button click
def hello():
    print("button clicked")


#create button and label
button=Button(text="ok",command=hello)
label=Label(window,text="welcome")

#show button and label in the window
button.pack()
label.pack()

#its working as a loop for if any changes it will show here
window.mainloop()