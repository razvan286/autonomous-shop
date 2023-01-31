#!/usr/bin/python

# Avoid using wrong py version depending on the os
from pyembedded.rfid_module.rfid import RFID

import tkinter as tk
from view.root import create_main_window
# from tkinter import *
# from tkinter import ttk

# import serial

# ser = serial.Serial('/dev/input/event6')
# ser.baudrate = 9600
# ser.bytesize = serial.EIGHTBITS
# ser.parity = serial.PARITY_NONE
# ser.stopbits = serial.STOPBITS_ONE
# ser.timeout = 1

# ser.open()
# print(ser.is_open)
# ser.close()
rfid = RFID(port='/dev/bus/usb/001/008', baud_rate=9600)
print(rfid.get_id())

# # Create root window
main_window = tk.Tk()
# main_window.geometry("1700x600")

# main_window.title("Autonomous Shop")
# # Set fullscreen
# # width = main_window.winfo_screenwidth()               
# # height = main_window.winfo_screenheight()               
# # main_window.geometry("%dx%d" % (width, height))


# # Scan User ID
# label_scan_user_id = tk.Label(main_window, text="Scan client ID", font=('Arial', 16))
# entry_user_id = tk.Entry(main_window, textvariable=rfid.get_id(), state='disabled')

# # label_scan_user_id.pack()
# label_scan_user_id.place(x=50, y=50)
# entry_user_id.place(x=50, y=100, height=30, width=135)

# # Check if the Client ID exists in the json file
# user_id = entry_user_id.get()
# print(user_id)

# # def helloCallBack():
# #    tk.messagebox.showinfo( "Hello Python", "Hello World")

# # B = tk.Button(top, text ="Hello", command = helloCallBack)

# # B.pack()


# # Launch GUI
# main_window.mainloop()
# create_main_window(main_window, rfid)


