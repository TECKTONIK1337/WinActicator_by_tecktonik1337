#coded by tecktonik1337

#imports
from tkinter import*
from tkinter import ttk
import subprocess
import os
from threading import Event
import tempfile, base64, zlib

#strings
soft_name = 'Simple Win Act by TECKTONIK1337'
win10pro_btn = "Win 10/11 Pro"
win10pro_fw = 'Windows 10/11 Pro для рабочих станций'
win10pro_edu = 'Windows 10/11 Pro для образовательных учреждений'
win10_edu = 'Windows 10/11 для образовательных учреждений'
win10_enterprise = 'Windows 10/11 Корпоративная'

# transparent icon
ICON = zlib.decompress(base64.b64decode("eJxjYGAEQgEBBiDJwZDBysAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="))
_,ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)

#functions
def win10pro_cmd(): 
    os.system('slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    root.destroy()
    
def win10pro_fw_cmd():
    os.system('slmgr/ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    root.destroy()
    
def win10pro_edu_cmd():
    os.system('slmgr/ipk 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    root.destroy()
    
def win10_edu_cmd():
    os.system('slmgr/ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    root.destroy()
    
def win10_enterprise_cmd():
    os.system('slmgr/ipk NPPR9-FWDCX-D2C8J-H872K-2YT43')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    root.destroy()

#init ui
root = Tk() #init
root.title(soft_name) #title
root.geometry("380x275") #window size
root.iconbitmap(ICON_PATH)
root.resizable(False, False) #window unresizeable

#elements props
main_label1 = ttk.Label(text="Windows Activator by TECKTONIK1337", width=100, justify=CENTER, borderwidth=0, relief="ridge", background="#FFCDD2", foreground="#B71C1C", padding=15, font=("Arial", 14))
win10pro_act_btn = ttk.Button(text=win10pro_btn, command=win10pro_cmd)
win10pro_fw_btn = ttk.Button(text=win10pro_fw, command=win10pro_fw_cmd)
win10pro_edu_btn = ttk.Button(text=win10pro_edu, command=win10pro_edu_cmd)
win10_edu_btn = ttk.Button(text=win10_edu, command=win10_edu_cmd)
win10_enterprise_btn = ttk.Button(text=win10_enterprise, command=win10_enterprise_cmd)

#put on window
main_label1.pack(pady=[0, 25])
win10pro_act_btn.pack(fill=X, pady=[0, 10])
win10pro_fw_btn.pack(fill=X, pady=[0, 10]) 
win10pro_edu_btn.pack(fill=X, pady=[0, 10])
win10_edu_btn.pack(fill=X, pady=[0, 10])
win10_enterprise_btn.pack(fill=X, pady=[0, 25])

root.mainloop()