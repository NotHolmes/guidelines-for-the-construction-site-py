import tkinter as tk
from tkinter import ttk
from tkinter import * 
# define LEFT = 40
LEFT = 40
MID = 400
result = ''

def string_to_bool(string):
    if string == "True":
        return True
    else:
        return False

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = c_site_size.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = free_space.get()
	return userInput


# this is the function called when the button is clicked
def submit():
    # if c_site_size or free_space is not a number or empty then return
    if c_site_size.get().isnumeric() == False or free_space.get().isnumeric() == False:
        print("Please enter a number")
        return

    showResult()

def getResult():
    free = free_space.get()
    area = c_site_size.get()
    # if free space is more than 1600 sq.m.
    if (free > 1600):
        # if free space is less than 2000 sq.m. or 25% of the site area
        if free < 2000 or free < 25/100 * area:
            print ("Move site offices and the store into the constucting building or place them over each other to form a 2-floor site office and store.")
            check_store_move()
            check_office_movement()
        else:
            print ("The store's size is around 45-70 sq.m. The size of the site office is judged from the staff's number.")

        # Check if free space is still > 1600 sq.m. after the usage of other components.
        more = input("Is the free space still > 1600 sq.m. after the usage of other components? (True/False) : ")
        more = string_to_bool(more)
        if more:
            print("Consider the usage of the batching plant.")
        else:
            print("Cannot use the batching plant.")

    elif(free < 1600):
        print("Cannot use the batching plant.")
        steel_yard_size = (area + 5*free)/100
        if(steel_yard_size < 100):
            print("Consider to do the cutting and bending from outside, then, transport to the site.")
        else:
            print("Consider to do the cutting and bending on the site.")

# show result(s)    
def showResult():
    Label(root, text='Result', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=LEFT, y=270)
    Label(root, text=f"Laydown area's size (sq.m) = {100+20}", bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=LEFT, y=300)


root = Tk()

# This is the section of code which creates the main window
root.geometry('800x600')
root.configure(background='#F0F8FF')
root.title('Guidelines for Construction Site Layout Planning')


# This is the section of code which creates the a label
Label(root, text='Construction site size (sq.m)', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=LEFT, y=70)


# This is the section of code which creates the a label
Label(root, text='Free space (sq.m)', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=LEFT, y=120)


# This is the section of code which creates a text input box
c_site_size=Entry(root)
c_site_size.place(x=MID, y=70)


# This is the section of code which creates a text input box
free_space=Entry(root)
free_space.place(x=MID, y=120)


# This is the section of code which creates a button
Button(root, text='Submit', bg='#F0F8FF', font=('arial', 12, 'normal'), command=submit).place(x=LEFT, y=170)

root.mainloop()