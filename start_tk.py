#! /usr/bin/env python3.8

import tkinter as tk
from fgt_api_simplified import fgtConnector
import requests

def handle_click(event):
    ip = ent_ip.get()
    lbl_output["text"] = ip


window = tk.Tk()

#frm_mac = tk.Frame()
#lbl_mac = tk.Label(text="Enter MAC Address: ", width=30, master = frm_mac)
#ent_mac = tk.Entry(width = 40, master = frm_mac)
#mac = ent_mac.get()

frm_ip = tk.Frame()
lbl_ip = tk.Label(text="Enter IP Address: ", width=30, master = frm_ip)
ent_ip = tk.Entry(width = 40, master = frm_ip)
ip = ent_ip.get()

frm_user = tk.Frame()
lbl_user = tk.Label(text="Username: ", width=30, master = frm_user)
ent_user = tk.Entry(width = 40, master = frm_user)
user = ent_user.get()

frm_pw = tk.Frame()
lbl_pw = tk.Label(text="Password: ", width=30, master = frm_pw)
ent_pw = tk.Entry(width = 40, master = frm_pw)
pw = ent_pw.get()

lbl_output = tk.Label(text="",width = 40) 

button = tk.Button(text="Send")

button.bind("<ButtonRelease>", handle_click)

lbl_user.pack()
ent_user.pack()
frm_user.pack()

lbl_pw.pack()
ent_pw.pack()
frm_pw.pack()

lbl_ip.pack()
ent_ip.pack()
frm_ip.pack()

lbl_output.pack()

button.pack ()




window.mainloop()




# NAMIG CONVENTION
# Widget    Variable-Prefix 	    Example
# Button 	btn 	                btn_submit
# Label 	lbl 	                lbl_name
# Entry 	ent 	                ent_age
# Text 	    txt 	                txt_notes
# Frame 	frm 	                frm_addres 