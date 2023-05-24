import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
import csv
import os
from PIL import Image
from PIL import ImageTk
import inspect  #呼び出された関数を知るために使用

class GUI(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        
        self.frame_list = ["top_frame","second_frame"]
        self.number_path = '******'
        self.img_path = '******'
        self.img_list = {'top_bg':self.img_path+'Top_background.png','closet_btn':self.img_path+'closet_button.png',
                         'goout_btn':self.img_path+'go_out_Button.png','closet_bg':self.img_path+'select.png'}
        self.img_number = {'A_btn':self.number_path+'A.png','B_btn':self.number_path+'B.png','C_btn':self.number_path+'C.png',
                          'D_btn':self.number_path+'D.png','E_btn':self.number_path+'E.png','F_btn':self.number_path+'F.png',
                          'G_btn':self.number_path+'G.png','H_btn':self.number_path+'H.png',}
        
        self.color_list=['White','Black','Red','Pink','Orange','Blue','Yellow','Green','Purple','grey','brown']
        
        self.master.title('Menu')
        self.master.geometry("800x480")       
        self.refresh_frame()
        self.top_menu()
        
    def refresh_frame(self):
        if inspect.stack()[1].function != '__init__':
            self.frame_list[0].destroy()
        self.frame_list[0] = ttk.Frame(root,width=800,height=480)
        self.frame_list[0].place(x=0,y=0)
          
    def make_img(self,img_path,*size):
        fn = img_path
        img = Image.open(fn)
        if size != ():
            img = img.resize(size)
        return img
        
    def top_menu(self):
        self.refresh_frame()
        self.master.title('top_Menu')
        #canvas1
        canvas1 = tk.Canvas(self.frame_list[0],width=800,height=480)
        img = self.make_img(self.img_list['top_bg'],800,480)
        self.tkimg = ImageTk.PhotoImage(img,master=root)
        canvas1.create_image(0,0,anchor='nw',image=self.tkimg)
        canvas1.place(x=0,y=0)
        #button1(closet)
        img = self.make_img(self.img_list['closet_btn'])
        self.tkimg2 = ImageTk.PhotoImage(img,master=root)
        closet_btn = tk.Button(self.frame_list[0],image=self.tkimg2,compound="top",command= lambda :self.closet_menu())
        closet_btn.place(x=85,y=90)
        #button2(go out)
        img = self.make_img(self.img_list['goout_btn'],256,256)
        self.tkimg3 = ImageTk.PhotoImage(img,master=self.master)
        goout_btn = tk.Button(self.frame_list[0],image=self.tkimg3,compound="top",command= lambda :print('goout'))
        goout_btn.place(x=485,y=90)
    
    def closet_menu(self):
        self.refresh_frame()
        self.master.title('closet')
        #canvas
        canvas = tk.Canvas(self.frame_list[0],width=800,height=480)
        img = self.make_img(self.img_list['closet_bg'],800,480)
        self.tkimg = ImageTk.PhotoImage(img,master=self.master)
        canvas.create_image(400,240,image=self.tkimg)
        canvas.place(x=0,y=0)
        #button1
        img = self.make_img(self.img_number['A_btn'],100,100)
        self.tkimg1 = ImageTk.PhotoImage(img,master=self.master)
        A_btn = tk.Button(self.frame_list[0],image=self.tkimg1,command= lambda :self.setting_menu('A'))
        A_btn.place(x=85,y=80)
        #button2
        img = self.make_img(self.img_number['B_btn'],100,100)
        self.tkimg2 = ImageTk.PhotoImage(img,master=self.master)
        B_btn = tk.Button(self.frame_list[0],image=self.tkimg2,command= lambda :self.setting_menu('B'))
        B_btn.place(x=245,y=80)
        #button3
        img = self.make_img(self.img_number['C_btn'],100,100)
        self.tkimg3 = ImageTk.PhotoImage(img,master=self.master)
        C_btn = tk.Button(self.frame_list[0],image=self.tkimg3,command= lambda :print('C'))
        C_btn.place(x=405,y=80)  
        #button4
        img = self.make_img(self.img_number['D_btn'],100,100)
        self.tkimg4 = ImageTk.PhotoImage(img,master=self.master)
        D_btn = tk.Button(self.frame_list[0],image=self.tkimg4,command= lambda :print('D'))
        D_btn.place(x=565,y=80) 
        #button5
        img = self.make_img(self.img_number['E_btn'],100,100)
        self.tkimg5 = ImageTk.PhotoImage(img,master=self.master)
        E_btn = tk.Button(self.frame_list[0],image=self.tkimg5,command= lambda :print('E'))
        E_btn.place(x=85,y=250)
        #button6
        img = self.make_img(self.img_number['F_btn'],100,100)
        self.tkimg6 = ImageTk.PhotoImage(img,master=self.master)
        F_btn = tk.Button(self.frame_list[0],image=self.tkimg6,command= lambda :print('F'))
        F_btn.place(x=245,y=250)
        #button7
        img = self.make_img(self.img_number['G_btn'],100,100)
        self.tkimg7 = ImageTk.PhotoImage(img,master=self.master)
        G_btn = tk.Button(self.frame_list[0],image=self.tkimg7,command= lambda :print('G'))
        G_btn.place(x=405,y=250)
        #button8
        img = self.make_img(self.img_number['H_btn'],100,100)
        self.tkimg8 = ImageTk.PhotoImage(img,master=self.master)
        H_btn = tk.Button(self.frame_list[0],image=self.tkimg8,command= lambda :print('H'))
        H_btn.place(x=565,y=250)
        
    def setting_menu(self,alphabet):
        self.refresh_frame()
        img_key = alphabet+'_btn'
        print(img_key)
        #canvas
        canvas = tk.Canvas(self.frame_list[0],bg='White',width=800,height=480)
        canvas.place(x=0,y=0)
        #label(alphabet)
        img = self.make_img(self.img_number[img_key],100,100)
        self.tkimg = ImageTk.PhotoImage(img,master=self.master)
        alphabet_label = ttk.Label(self.frame_list[0],background='black',compound='left',image=self.tkimg)
        alphabet_label.place(x=350,y=0)
        #combobox1(color)
        color = ttk.Combobox(self.frame_list[0], values=self.color_list)
        color.place(x=245,y=250)
        data=color.get()
        print(data)

root = tk.Tk()
app = GUI(master=root)
app.mainloop()
        
        
        
        
        
        
        


        
        
        
        
        
    
