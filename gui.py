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
        self.img_path = './img/'
        self.number_path = self.img_path+'number/'
        self.img_list = {'top_bg':self.img_path+'Top_background.png','closet_btn':self.img_path+'closet_button.png',
                         'goout_btn':self.img_path+'go_out_Button.png','closet_bg':self.img_path+'select.png'}
        self.img_number = {'A':self.number_path+'A.png','B':self.number_path+'B.png','C':self.number_path+'C.png',
                          'D':self.number_path+'D.png','E':self.number_path+'E.png','F':self.number_path+'F.png',
                          'G':self.number_path+'G.png','H':self.number_path+'H.png','save':self.number_path+'save.png'} 
        self.name_list = ["tkimg","tkimg1","tkimg2","tkimg3","tkimg4","tkimg5","tkimg6","tkimg7","tkimg8"]

        self.comboname_list = ['color','type','brightness','saturation','flags']
        self.color_list=['White','Black','Red','Pink','Orange','Blue','Yellow','Green','Purple','grey','brown']

        self.func_count = 0
        self.combo_count = 0
        
        self.master.title('Menu')
        self.master.geometry("800x480")       
        self.refresh_frame()
        self.top_menu()
        
    def refresh_frame(self):
        if inspect.stack()[1].function != '__init__':
            self.frame_list[0].destroy()
        self.frame_list[0] = ttk.Frame(root,width=800,height=480)
        self.frame_list[0].place(x=0,y=0)
        self.func_count = 0
          
    def make_img(self,img_path,*size):
        fn = img_path
        img = Image.open(fn)
        if size != ():
            img = img.resize(size)
        return img
    
    def make_button(self,img_name,place_x,place_y):
        self.func_count += 1
        print(self.func_count)
        img = self.make_img(self.img_number[img_name],100,100)
        self.name_list[self.func_count-1]= ImageTk.PhotoImage(img,master=self.master)
        tkimg = tk.Button(self.frame_list[0],image=self.name_list[self.func_count-1],command= lambda : self.setting_menu(img_name))
        tkimg.place(x=place_x,y=place_y)

    def make_combobox(self,place_x,place_y,value):
        self.combo_count += 1
        self.comboname_list[self.combo_count-1] = ttk.Combobox(self.frame_list[0], values=value)
        self.comboname_list[self.combo_count-1].place(x=place_x,y=place_y)   

    def save_combobox(self):
        data=self.comboname_list[0].get()
        print(data)

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
        self.make_button('A',85,80)
        #button2
        self.make_button('B',245,80)
        #button3 
        self.make_button('C',405,80)
        #button4 
        self.make_button('D',565,80)
        #button5
        self.make_button('E',85,250)
        #button6
        self.make_button('F',245,250)
        #button7
        self.make_button('G',405,250)
        #button8
        self.make_button('H',565,250)


    def setting_menu(self,alphabet):
        self.refresh_frame()
        img_key = alphabet
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
        self.make_combobox(245,250,self.color_list)
        #button(save)
        save_btn = tk.Button(self.frame_list[0],bg='White',compound="top",command= lambda :self.save_combobox())
        save_btn.place(x=85,y=90)


root = tk.Tk()
app = GUI(master=root)
app.mainloop()
        
        
        
        
        
        
        


        
        
        
        
        
    
