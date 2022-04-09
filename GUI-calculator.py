#GUI-calculator.py
from tkinter import * #star คือ import ทั้งหมด
from tkinter import ttk, messagebox #ttk เป็นแพคเกจย่อยที่อยู่ในแพคเกจหลักของ tkinter เลยต้อง import อีกรอบ

GUI = Tk() #ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณปลา รถพุ่มพวง')
GUI.geometry('500x400')


bg = PhotoImage(file ='car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา(กิโลกรัม)',font=('Angsana new',20))
L.pack()


v_quantity = StringVar() #เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable= v_quantity, font=(None,20))
E1.pack()


def Cal():
	try:
		quan = float(v_quantity.get()) # แปลงค่าจากช่องกรอกเป็น float
		calc = quan * 39 #fix ราคาปลาโลละ 39 บาท เอามาคูณจำนวนปลา
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
		v_quantity.set('1') #ใส่ค่า default ไว้เป็น 1 kg หรือจะให้มันเป็นช่องว่างไว้ก็ได้
		E1.focus() # เพื่อให้เคอเซอร์กลับไป stand by รอที่ช่องกรอก
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1') #ใส่ค่า default ไว้เป็น 1 kg หรือจะให้มันเป็นช่องว่างไว้ก็ได้
		E1.focus()

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30, ipady=20, pady=20) #ipadx ขยายความกว้าง x/y






GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา