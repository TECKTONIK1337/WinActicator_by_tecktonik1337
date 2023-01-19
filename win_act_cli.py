#coded by tecktonik1337

#imports
import os
from threading import Event

#strings
soft_name = 'Simple Win Act by TECKTONIK1337'
win10pro = "Win 10/11 Pro"
win10pro_fw = 'Windows 10/11 Pro для рабочих станций'
win10pro_edu = 'Windows 10/11 Pro для образовательных учреждений'
win10_edu = 'Windows 10/11 для образовательных учреждений'
win10_enterprise = 'Windows 10/11 Корпоративная'
choice_txt = "Выберите вашу редакцию и подтвердите выбор:  "
end_txt = "Операция завершена, выход..."

#functions
def win10pro_cmd(): 
    os.system('slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    
def win10pro_fw_cmd():
    os.system('slmgr/ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    
def win10pro_edu_cmd():
    os.system('slmgr/ipk 6TP4R-GNPTD-KYYHQ-7B7DP-J447Y')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    
def win10_edu_cmd():
    os.system('slmgr/ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    
def win10_enterprise_cmd():
    os.system('slmgr/ipk NPPR9-FWDCX-D2C8J-H872K-2YT43')
    os.system('slmgr /skms kms.digiboy.ir')
    os.system('slmgr /ato')
    Event().wait(3)
    
    
    
#start
print(soft_name)
print(" ")
print('1.', win10pro)
print('2.', win10pro_fw)
print('3.', win10pro_edu)
print('4.', win10_edu)
print('5.', win10_enterprise)
print(" ")
print(" ")
choice = input(choice_txt)
if choice == "1":
    print('Выбрано:', win10pro, ", активация...")
    win10pro_cmd()
    print(end_txt)
    Event().wait(3)
    quit()
elif choice == "2":
    print('Выбрано:', win10pro_fw, ", активация...")
    win10pro_fw_cmd()
    print(end_txt)
    Event().wait(3)
    quit()
elif choice == "3":
    print('Выбрано:', win10pro_edu, ", активация...")
    win10pro_edu_cmd()
    print(end_txt)
    Event().wait(3)
    quit()
elif choice == "4":
    print('Выбрано:', win10_edu, ", активация...")
    win10_edu_cmd()
    print(end_txt)
    Event().wait(3)
    quit()
elif choice == "5":
    print('Выбрано:', win10_enterprise, ", активация...")
    win10_enterprise_cmd()
    print(end_txt)
    Event().wait(3)
    quit()
else:
    print("Выбран неправильный вариант! Выход...")
    Event().wait(2)
    quit()
#end





