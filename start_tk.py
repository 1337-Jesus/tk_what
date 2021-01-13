#! /usr/bin/env python3.8

import tkinter as tk

window = tk.Tk()

frm_mac = tk.Frame()
lbl_mac = tk.Label(text="Enter MAC Address: ", width=30, master = frm_mac)
ent_mac = tk.Entry(width = 40, master = frm_mac)
mac = ent_mac.get()

frm_ip = tk.Frame()
lbl_ip = tk.Label(text="Enter IP Address: ", width=30, master = frm_ip)
ent_ip = tk.Entry(width = 40, master = frm_ip)
ip = ent_ip.get()

lbl_mac.pack()
lbl_ip.pack()
ent_mac.pack()
ent_ip.pack()
frm_mac.pack()
frm_ip.pack()

window.mainloop()
