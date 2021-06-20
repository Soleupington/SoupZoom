#Imports
from tkinter import *
import pyautogui
import time

#Code...
def save_info():
  firstname_info = firstname.get()
  lastname_info = lastname.get()
  pyautogui.moveTo(47, 527, 1)
  pyautogui.click()
  pyautogui.click()
  pyautogui.moveTo(765, 476, 5)
  pyautogui.click()
  pyautogui.moveTo(906, 468, 3)
  pyautogui.click()

  #Enter Your Metting Id
  pyautogui.write( firstname_info , interval=0.30)
  pyautogui.moveTo(997, 684, 3)
  pyautogui.click()
  pyautogui.moveTo(875, 468, 3)
  pyautogui.click()

  #Enter Meeting Password Here
  pyautogui.write( lastname_info , interval=0.30)
  pyautogui.moveTo(979, 679, 3)
  pyautogui.click() 
  
  file = open("user.txt", "w")
  file.write(firstname_info)
  file.write(lastname_info)
  file.close()

  firstname_entry.delete(0, END)
  lastname_entry.delete(0, END)
  
screen = Tk()
screen.geometry("500x500")
screen.title("SoupZoom 0.0.12")
heading = Label(text = "SoupZoom", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()
 
firstname_text = Label(text = "Meeting ID",)
lastname_text = Label(text = "Meeting Password",)
firstname_text.place(x = 15, y = 70)
lastname_text.place(x = 15, y = 140)


firstname = StringVar()
lastname = StringVar()

firstname_entry = Entry(textvariable = firstname, width = "30")
lastname_entry = Entry(textvariable = lastname, width = "30")

firstname_entry.place(x = 15, y = 100)
lastname_entry.place(x = 15, y = 180)

register = Button(screen,text = "Apply", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 15, y = 290)
