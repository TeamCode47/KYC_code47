import tkinter as tk
import tkinter.messagebox as tkmessageBox
import base64
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
label2 = tk.Label(root, text='Enter ID of fingerPrint TO verify:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
#messagebox=

def verify ():  
    x1 = entry1.get()
    with open("img11.tif",'rb') as image:
        cv=base64.b64encode(image.read())

       # cv=cv.decode('utf-8')
        

    tkmessageBox.showinfo(cv,"Verified")

    with open("img_22.tif",'rb') as image:
        cv2=base64.b64encode(image.read())

       # cv2=cv2.decode('utf-8')

        if cv==cv2:
            tkmessageBox.showinfo("info","Verified")
        else:
            tkmessageBox.showinfo("info"," Not Verified")

    
    #canvas1.create_window(200, 230, window=label1)
   # messagebox.showerror("error","Error Could not verify") 
    
button1 = tk.Button(text='VERIFY FINGERPRINT', command=verify)
canvas1.create_window(200, 180, window=button1)
root.mainloop()