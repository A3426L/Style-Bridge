import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
import csv
import os
from PIL import Image
from PIL import ImageTk
import inspect  #呼び出された関数を知るために使用



class base(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        
        self.frame_list = ["top_frame","second_frame"]
        self.img_path = './img/'
        self.number_path = self.img_path+'number/'
        self.img_list = {'top_bg':self.img_path+'Top_background.png','closet_btn':self.img_path+'closet_button.png',
                         'goout_btn':self.img_path+'go_out_Button.png','closet_bg':self.img_path+'select.png',
                         'A':self.number_path+'A.png','B':self.number_path+'B.png','C':self.number_path+'C.png',
                          'D':self.number_path+'D.png','E':self.number_path+'E.png','F':self.number_path+'F.png',
                          'G':self.number_path+'G.png','H':self.number_path+'H.png','save':self.number_path+'save.png'} 
        self.name_list = ["tkimg","tkimg1","tkimg2","tkimg3","tkimg4","tkimg5","tkimg6","tkimg7","tkimg8"]

        self.comboname_list = ['select','color','type','brightness','saturation','flags']
        self.color_list=['White','Black','Red','Pink','Orange','Blue','Yellow','Green','Purple','grey','brown']
        self.type_list={'please Select':['a'],'tops':['','jaket','T-shurts'],
                        'botoms':['','jeans','tino']}
        self.brightness_list = ['high','normal','low']
        self.saturation_list = ['high','normal','low']

        self.func_count = 0
        self.combo_count = 0

        self.data = {}

    
        
        self.master.title('Menu')
        self.master.geometry("800x480")       
        self.refresh_frame()
        self.top_menu(NONE)
        
    def refresh_frame(self):
        if inspect.stack()[1].function != '__init__':
            self.frame_list[0].destroy()
        self.frame_list[0] = ttk.Frame(root,width=800,height=480)
        self.frame_list[0].place(x=0,y=0)
        self.func_count = 0
        self.combo_count = 0
          
    def make_img(self,img_path,*size):
        fn = img_path
        img = Image.open(fn)
        if size != ():
            img = img.resize(size)
        return img
    
    def make_button(self,img_name,place_x,place_y,cmd,input,*size):
        self.func_count += 1
        print(self.func_count)
        img = self.make_img(self.img_list[img_name],*size)
        self.name_list[self.func_count-1]= ImageTk.PhotoImage(img,master=self.master)
        tkimg = tk.Button(self.frame_list[0],image=self.name_list[self.func_count-1],command= lambda :cmd(input))
        tkimg.place(x=place_x,y=place_y)

    def make_combobox(self,place_x,place_y,value):
        self.combo_count += 1
        self.comboname_list[self.combo_count-1] = ttk.Combobox(self.frame_list[0], values=value)
        self.comboname_list[self.combo_count-1].place(x=place_x,y=place_y)   

    def save_combobox(self,input):
        
        self.data.update({input:[self.comboname_list[0].get(),self.comboname_list[1].get(),self.comboname_list[2].get(),self.comboname_list[3].get(),self.comboname_list[4].get()]})
        print(self.data)
    

class frame(base):
    def top_menu(self,input):
        self.refresh_frame()
        self.master.title('top_Menu')
        #canvas1
        canvas1 = tk.Canvas(self.frame_list[0],width=800,height=480)
        img = self.make_img(self.img_list['top_bg'],800,480)
        self.tkimg = ImageTk.PhotoImage(img,master=root)
        canvas1.create_image(0,0,anchor='nw',image=self.tkimg)
        canvas1.place(x=0,y=0)
        #button1(closet)
        self.make_button('closet_btn',85,90,self.closet_menu,None)
        #button2(go out)
        self.make_button('goout_btn',485,90,print,'goout',256,256)
    
    def closet_menu(self,input):
        self.refresh_frame()
        self.master.title('closet')
        #canvas
        canvas = tk.Canvas(self.frame_list[0],width=800,height=480)
        img = self.make_img(self.img_list['closet_bg'],800,480)
        self.tkimg = ImageTk.PhotoImage(img,master=self.master)
        canvas.create_image(400,240,image=self.tkimg)
        canvas.place(x=0,y=0)
        #button1
        self.make_button('A',85,80,self.setting_menu,'A')
        #button2
        self.make_button('B',245,80,self.setting_menu,'B')
        #button3 
        self.make_button('C',405,80,self.setting_menu,'C')
        #button4 
        self.make_button('D',565,80,self.setting_menu,'D')
        #button5
        self.make_button('E',85,250,self.setting_menu,'E')
        #button6
        self.make_button('F',245,250,self.setting_menu,'F')
        #button7
        self.make_button('G',405,250,self.setting_menu,'G')
        #button8
        self.make_button('H',565,250,self.setting_menu,'H')


    def setting_menu(self,alphabet):
        self.refresh_frame()
        img_key = alphabet
        print(img_key)
        #canvas
        canvas = tk.Canvas(self.frame_list[0],bg='White',width=800,height=480)
        canvas.place(x=0,y=0)
        #label(alphabet)
        img = self.make_img(self.img_list[img_key],100,100)
        self.tkimg = ImageTk.PhotoImage(img,master=self.master)
        alphabet_label = ttk.Label(self.frame_list[0],background='black',compound='left',image=self.tkimg)
        alphabet_label.place(x=350,y=0)
        #combobox0(tops or buttoms)
        self.make_combobox(75,50,list(self.type_list.keys()))
        self.comboname_list[0].current(0)
        #combobox1(color)
        self.make_combobox(75,180,self.color_list)
        #combobox2(type)
        self.make_combobox(300,180,self.type_list['tops'])
        self.comboname_list[0].bind("<<ComboboxSelected>>",lambda e: self.comboname_list[2].configure(values=self.type_list[self.comboname_list[0].get()]))
        self.comboname_list[0].bind("<<ComboboxSelected>>",lambda e: self.comboname_list[2].set(self.type_list[self.comboname_list[0].get()][0]),"+")
        #combobox3(brightness)
        self.make_combobox(525,180,self.brightness_list)
        #combobox4(saturation)
        self.make_combobox(75,300,self.saturation_list)
        #button(back)
        self.make_button('A',525,50,self.closet_menu,NONE)
        #button(Top)
        self.make_button('B',625,50,self.top_menu,NONE)
        #button(save)
        self.make_button('save',350,380,self.save_combobox,alphabet,100,50)



root = tk.Tk()
# app = GUI(master=root)
# app.mainloop()
app=frame()
app.mainloop()
        
        
        
        
        
        
        


        
        
        
        
        
    
