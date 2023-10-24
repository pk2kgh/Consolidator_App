import kivy
import kivymd
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import pandas as pd
import os
from android.permissions import request_permissions,Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])
helpstr = '''
ScreenManager:
    WelcomeScreen:
    UsernameScreen:
    
    
    
<WelcomeScreen>:
    name : 'welcomescreen'
    text:"hi"
    MDLabel:
        text:'Consolidator'
        font_style: 'H4'
        halign:'center'
        pos_hint: {'center_y':0.80}
    MDLabel:
        text:'By Pawan'
        font_style: 'Caption'
        halign:'center'
        pos_hint: {'center_x':0.7,'center_y':0.75}
    MDFloatingActionButton:
        id:disabled_button_wcs
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.83,'center_y':0.10}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    MDLabel:
        text:'Load the CSV File'
        font_style: 'H6'
        halign: 'center'
        pos_hint: {'center_y':0.35}
    MDFloatingActionButton:
        icon:'file-upload'
        md_bg_color:app.theme_cls.primary_color
        user_font_size : '45sp'
        pos_hint: {'center_x':0.5,'center_y':0.45}
        on_press:
            app.file_manager_open()
            
            
    MDProgressBar:
        value:50
        pos_hint:{'center_y' : 0.02}
<UsernameScreen>
    name:'usernamescreen'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.17,'center_y':0.10}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    
    MDProgressBar:
        value:100
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:"Enter the Student's IDs"
        font_style: 'Subtitle1'
        halign: 'center'
        pos_hint : {'center_y':0.90}
    MDTextField:
        id:st_ids
        pos_hint: {'center_x':0.5,'center_y':0.82}
        size_hint: (0.7,0.1)
        hint_text : 'IDs Seperated by Comma'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'smart-card'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDLabel:
        text:"Enter Header fields"
        font_style: 'Subtitle1'
        halign: 'center'
        pos_hint : {'center_y':0.70}
    MDTextField:
        id:field
        pos_hint: {'center_x':0.5,'center_y':0.62}
        size_hint: (0.7,0.1)
        hint_text : 'Fields Seperated by Comma'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'card-text'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDLabel:
        text:"Enter Output File name"
        font_style: 'Subtitle1'
        halign: 'center'
        pos_hint : {'center_y':0.50}
    MDTextField:
        id:opname
        pos_hint: {'center_x':0.5,'center_y':0.42}
        size_hint: (0.7,0.1)
        hint_text : 'Without File Extension'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'file-excel'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDFloatingActionButton:
        icon:'check-circle'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.25}
        user_font_size: '35sp'
        on_press: app.check_username(st_ids.text,field.text,opname.text)
    MDFloatingActionButton:
        id:disabled_button_wc
        disabled: False
        icon: 'exit-run'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.83,'center_y':0.10}
        user_font_size : '40sp'
        on_press:app.get_running_app().stop()    
'''
class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))

class NewApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.manager = None
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            #preview=True,
        )
        self.file_manager.ext = [".csv"]
    
    def send(self,path):
        self.csv_path=path
        print("send working " + self.csv_path)
        self.strng.get_screen('welcomescreen').ids.text=self.csv_path
    def file_manager_open(self):
        self.file_manager.show('/storage/emulated/0/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        
        toast(path)
        file_path=path
        self.send(file_path)
        self.exit_manager()
        self.strng.get_screen('welcomescreen').ids.disabled_button_wcs.disabled = False
        
        
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True



    
    def build(self):
        self.strng = Builder.load_string(helpstr)
        return self.strng

    def check_username(self,STID,STRF,OPN):
        self.username_text = self.strng.get_screen('usernamescreen').ids.st_ids.text
        lst=self.list_cov(STID)
        print(lst)
        order=self.liststr_cov(STRF)
        print(order)
        
        data = pd.read_csv (self.strng.get_screen('welcomescreen').ids.text)
        df = pd.DataFrame(data,index=lst, columns= order)
        #ss = df.loc[(df['TAG'] =='21') | (df['Course'] =='Python')]

        
        op_n=OPN
        #df.to_csv ('B.csv', index = False, header=True)
        
        if not os.path.exists(r'/storage/emulated/0/Consolidater'):
            os.makedirs('/storage/emulated/0/Consolidater')
        df.to_excel(r'/storage/emulated/0/Consolidater/'+op_n+'.xlsx',index=False)
        #df.to_excel(op_n+'.xlsx',index=False)
        print (df)
        
        toast("Output file saved in /storage/emulated/0/Consolidater")
        
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()

    """def send(self,cit):
        print(self.list_cov(cit))
        self.dialog.dismiss()"""
    def list_cov(self,STID):
        #STID="1,2,3,4"
        
        st_id=STID.split(",")
        print("\n",st_id)
        for i in range(len(st_id)):
            st_id[i]=(int(st_id[i])-1)
        #print("\n",st_id)
        return st_id
    def liststr_cov(self,STRF):
        key_value={'tg':'TAG','rn':'REGISTER NUMBER','n':'NAME','mi':'MAIL ID','rln':'ROLL NO','te':'SSLC(Percentage)','tw':'HSC (percentage)','dip':'Diploma:(Percentage)','cg':'CGPA','do':'D.O.B','pn':'PHONE NUMBER','g':'GENDER','br':'BRANCH','bl':'BACKLOG','ha':'HISTORY OF ARREARS','loc':'LOCATION'}
        #STID="1,2,3,4"
        strf=STRF.split(",")
        print("\n",strf)
        for i in range(len(strf)):
            strf[i]=key_value[strf[i]]
        print("\n",strf)
        return strf
    

NewApp().run()
