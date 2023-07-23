from tkinter import *
import serial
import time

root = Tk()
root.title("OutputRelayCOM8")
root.geometry("500x250")
onCmd = bytearray(1)
onCmd[0]=0x50
openCmd = bytearray(2)
openCmd[0]=0x51
openCmd[1]=0xFF
ser = serial.Serial("COM8",9600,timeout=1,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
parity=serial.PARITY_NONE)
if ser.isOpen() == True:
    ser.write(onCmd)
    time.sleep(1)
    ser.write(openCmd)
    time.sleep(1)
    onCmd[0]=0xFF
    ser.write(onCmd)
print("Start")
#bytearray openCmd = 0x50
# onCmd = bytearray(1)
# onCmd[0]=0x51

# def btnOpen_cmd():
#     ser.Serial("COM3",9600,timeout=1,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     parity=serial.PARITY_NONE)
#     if ser.isOpen() == True:
#         ser.write(b'\x50')
#         time.sleep(1)


#def btn1_cmd():
#    print("test")
#    ser.write(onCmd)
#def btn2_cmd():
#    print("test2")
#    ser.write(b'\x51F0')

def rad_cmd():
    ser.close()
    ser.open()
    onCmd[0]=0xFF
    #K1 : 1/5
    if radVar.get() == 1:
        #Out1 : No change
        onCmd[0]=onCmd[0]
        # print("radio 1 clicked")
    elif radVar.get() == 2:
        #Out5 : K1 ON
        onCmd[0]=onCmd[0]&(~0b00000001)
        # print("radio 2 clicked")
    #K5 : 2/6
    if radVarC.get() == 1:
        #Out1 : No change
        onCmd[0]=onCmd[0]
        #print("radio 3 clicked")
    elif radVarC.get() == 2:
        #Out4 : K5 ON
        onCmd[0]=onCmd[0]&(~0b00010000)
    #K4 : 3/4
    #K3: K2/K4
    #K2 : 9/11
    if radVarB.get() == 1:
        #Out3 : No change
        onCmd[0]=onCmd[0]
    elif radVarB.get() == 2:
        #Out4 : K4 ON
        onCmd[0]=onCmd[0]&(~0b00001000)
    elif radVarB.get() == 3:
        #Out9 : K3 ON
        onCmd[0]=onCmd[0]&(~0b00000100)
    elif radVarB.get() == 4:
        #Out11 : K2/K3 ON
        onCmd[0]=onCmd[0]&(~0b00000110)
    #K6 : 7
    #K7 : K6/K8
    #K8 : 10/12
    if radVarD.get() == 1:
        #Out7 : No change
        onCmd[0]=onCmd[0]
    elif radVarD.get() == 2:
        #Out10 : K7 ON
        onCmd[0]=onCmd[0]&(~0b01000000)
    elif radVarD.get() == 3:
        #Out12 : K7/K8 ON
        onCmd[0]=onCmd[0]&(~0b11000000)
    ser.write(onCmd)
    

#buttons 
# btnOpen = Button(root, text="Open", command=btnOpen_cmd)
# btnOpen.grid(row=0,column=0)
#btn1 = Button(root, text="Out1", command=btn1_cmd)
#btn1.grid(row=1,column=0)
#btn2 = Button(root, text="Out2", command=btn2_cmd)
#btn2.grid(row=1,column=1)

#select A
Label(root, text="Scope Input A").grid(row=2)
radVar = IntVar()
btn_Radio1 = Radiobutton(root, text="Out1(FL)", value=1, variable=radVar, command=rad_cmd)
btn_Radio1.select()
btn_Radio2 = Radiobutton(root, text="Out5(RL)", value=2, variable=radVar, command=rad_cmd)
#btn_Radio3 = Radiobutton(root, text="Ch3", value=3, variable=radVar, command=rad_cmd)
#btn_Radio4 = Radiobutton(root, text="Ch4", value=4, variable=radVar, command=rad_cmd)
btn_Radio1.grid(row=3,column=0)
btn_Radio2.grid(row=3,column=1)
#btn_Radio3.grid(row=3,column=2)
#btn_Radio4.grid(row=3,column=3)

#select B
Label(root, text="Scope Input B").grid(row=4)
radVarB = IntVar()
btn_RadioB1 = Radiobutton(root, text="Out3(SWF1)", value=1, variable=radVarB, command=rad_cmd)
btn_RadioB1.select()
btn_RadioB2 = Radiobutton(root, text="Out4(SWF2)", value=2, variable=radVarB, command=rad_cmd)
btn_RadioB3 = Radiobutton(root, text="Out9(LMID)", value=3, variable=radVarB, command=rad_cmd)
btn_RadioB4 = Radiobutton(root, text="Out11(LSUR)", value=4, variable=radVarB, command=rad_cmd)
btn_RadioB1.grid(row=5,column=0)
btn_RadioB2.grid(row=5,column=1)
btn_RadioB3.grid(row=5,column=2)
btn_RadioB4.grid(row=5,column=3)

#select C
Label(root, text="Scope Input C").grid(row=6)
radVarC = IntVar()
btn_RadioC1 = Radiobutton(root, text="Out2(FR)", value=1, variable=radVarC, command=rad_cmd)
btn_RadioC1.select()
btn_RadioC2 = Radiobutton(root, text="Out6(RR)", value=2, variable=radVarC, command=rad_cmd)
#btn_RadioB3 = Radiobutton(root, text="Ch7", value=3, variable=radVarB, command=rad_cmd)
#btn_RadioB4 = Radiobutton(root, text="Ch8", value=4, variable=radVarB, command=rad_cmd)
btn_RadioC1.grid(row=7,column=0)
btn_RadioC2.grid(row=7,column=1)
#btn_RadioB3.grid(row=5,column=2)
#btn_RadioB4.grid(row=5,column=3)

#select D
Label(root, text="Scope Input D").grid(row=8)
radVarD = IntVar()
btn_RadioD1 = Radiobutton(root, text="Out7(Ctr)", value=1, variable=radVarD, command=rad_cmd)
btn_RadioD1.select()
btn_RadioD2 = Radiobutton(root, text="Ch10(RMID)", value=2, variable=radVarD, command=rad_cmd)
btn_RadioD3 = Radiobutton(root, text="Out12(RSur)", value=3, variable=radVarD, command=rad_cmd)
# btn_RadioD4 = Radiobutton(root, text="NC", value=4, variable=radVarD, command=rad_cmd)
btn_RadioD1.grid(row=9,column=0)
btn_RadioD2.grid(row=9,column=1)
btn_RadioD3.grid(row=9,column=2)
# btn_RadioD4.grid(row=9,column=3)

root.mainloop()
