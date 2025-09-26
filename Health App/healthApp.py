import self
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDTextButton, MDRaisedButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import sqlite3


Window.size = (350, 600)

class Database:
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT UNIQUE,
                phone TEXT,
                password TEXT
            )
        """)

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS preferences (
                    id INTEGER PRIMARY KEY,
                    email TEXT,
                    remember INTEGER
                )
            """)

        self.conn.commit()

    def register_user(self, name, email, phone, password):
        try:
            self.cursor.execute(
                "INSERT INTO users (name, email, phone, password) VALUES (?, ?, ?, ?)",
                (name, email, phone, password)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login_user(self, email, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )
        return self.cursor.fetchone()

    def save_preference(self, email, remember):
        self.cursor.execute("DELETE FROM preferences")  # sempre um único registro
        self.cursor.execute("INSERT INTO preferences (id, email, remember) VALUES (1, ?, ?)",
                            (email, int(remember)))
        self.conn.commit()

    def load_preference(self):
        self.cursor.execute("SELECT email, remember FROM preferences WHERE id=1")
        return self.cursor.fetchone()

kv = """

ScreenManager:
    MenuScreen:
    LoginScreen:
    RegisterScreen:
    MainMenuScreen:
    WeightScreen:
    WaterScreen:
    MenstrualScreen:
    MedicationsScreen:
    VitaminsScreen:
    GenericScreen:
    MineralScreen:
    HomemadeScreen:
    
<MenuScreen>:
    name: "Menu"
    
    MDFloatLayout:
        md_bg_color:1, 1, 1, 1
        Image:
            source:"logo 2.png"
            pos_hint: {"center_x": 0.5, "center_y": .75}
            size_hint: None, None
            size: "365dp", "365dp"
            allow_stretch: True
            keep_ratio: True
            
        MDLabel:
            text: "W E L C O M E"
            pos_hint: {"center_x": .5, "center_y": .53}
            halign: "center"
            font_name: "Fontes/Montserrat-Bold.ttf"
            font_size: "35sp"   
            theme_text_color: "Custom"
            text_color: 0, 0, 0
            
        MDLabel:
            text:"Your health comes first, don't leave it for later" 
            pos_hint: {"center_x": .5, "center_y": .48}
            halign: "center"
            font_name: "Fontes/Quicksand-Light.ttf"
            font_size: "15sp"
            color: rgba(127,127,127 )
    
            
    MDFloatLayout:
        pos_hint: {"center_x": .5, "center_y": .38}

        MDFillRoundFlatButton:
            text: "LOGIN"
            text_color: "white"
            size_hint_x: "0.8"
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .5}
            font_name: "Fontes/Montserrat-Regular.ttf"
            md_bg_color: (76/255,168/255,35/255,0.9)
            font_size: "20sp"
            on_press: self.md_bg_color = (76/255,168/255,35/255,0.7)
            on_release:
                self.md_bg_color = (76/255,168/255,35/255,0.9)
                app.ir_login()
                
   

        MDFillRoundFlatButton:
            text: "REGISTER"
            text_color: "white"
            size_hint_x: "0.8"
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .40}
            font_name: "Fontes/Montserrat-Regular.ttf"
            md_bg_color: 76/255,168/255,35/255,0.9
            font_size: "20sp"
            on_press: self.md_bg_color = 76/255,168/255,35/255,0.7
            on_release:
                self.md_bg_color = 76/255,168/255,35/255,0.9
                app.ir_registro()
        
        MDLabel:    
            text: "Forgot your password?"
            pos_hint:{"center_x": .5, "center_y":.23}
            halign: "center"
            font_name: "Fontes/Roboto-Regular.ttf"
            font_size: "12sp"
            color: rgba(127,127,127) 
        
        MDTextButton:
            text:"Click Here"
            color: 41/255, 134/255, 204/255, 1
            pos_hint:{"center_x": .5, "center_y":.20}
            font_name: "Fontes/Roboto-Medium.ttf"
            font_size: "12sp"
            
        MDFloatLayout:
            md_bg_color: 230/255, 230/255, 230/255, 1    
            size_hint: .28, .001       
            pos_hint:{"center_x": .16, "center_y":.215}     
            
        MDFloatLayout:
            md_bg_color: 230/255, 230/255, 230/255, 1    
            size_hint: .28, .001       
            pos_hint:{"center_x": .840, "center_y":.215}   
        
                
                    
                    
    
                
<LoginScreen>:
    name:"login-form"
    
    MDFloatLayout:
        canvas.before:   
            Color:
                rgba: 1, 1, 1, 0.8                 
            Rectangle:
                source:"gradient2.png"
                size:self.size
                pos:self.pos 
    
        MDLabel:
            text:"LOGIN"
            halign:"center"
            font_style:"H4"
            font_name: "Fontes/Montserrat-Bold.ttf"
            pos_hint: {"center_x": 0.5, "center_y": 0.87}
    
    
                    
        MDFloatLayout:
            size_hint: .9, .60
            pos_hint:{"center_x": .5, "center_y":.49}
            canvas:
                Color:
                    rgba: 1, 1, 1, 0.58   
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius: [8]
                    
            
            MDFloatLayout:
                size_hint: .9, .14
                pos_hint:{"center_x": .5, "center_y":.85}
                canvas:
                    Color:
                        rgba: 241/255, 240/255, 240/255, 0.1    
                    RoundedRectangle:
                        size:self.size
                        pos:self.pos
                        radius: [50]
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 50)
                        width: 2   
                          
                MDBoxLayout:
                    orientation:"horizontal"
                    pos_hint: {"center_x": .55, "center_y": .37}
                    spacing: "8dp"
                    height: "24dp"
                            
                        
                    MDTextField:
                        id: login_email_field
                        hint_text: "E-Mail"
                        icon_left: "email"
                        size_hint_x: None
                        width: "250dp"
                        font_name: "Fontes/Roboto-Medium.ttf"
                        font_size: "12sp"
                        
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 0.64, 0.64, 0.64, 0.8
                        hint_text_color_normal: 1, 1, 1, 1
                        hint_text_color_focus: 0.64, 0.64, 0.64, 0.8
                        icon_left_color: 1, 1, 1, 1
                        icon_left_color_focus: 0.64, 0.64, 0.64, 0.8
                        text_color_focus: 1, 1, 1, 1
                    
                        
                                     
                        
            MDFloatLayout:
                size_hint: .9, .14
                pos_hint:{"center_x": .5, "center_y":.64}
                canvas:
                    Color:
                        rgba: 241/255, 240/255, 240/255, 0.1   
                    RoundedRectangle:
                        size:self.size
                        pos:self.pos
                        radius: [50]
                    Color:
                        rgba: 1, 1, 1, 1
                    Line:
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 50)
                        width: 2 
                        
                MDBoxLayout:
                    orientation:"horizontal"
                    pos_hint: {"center_x": .56, "center_y": .39}
                    spacing: "12dp"
                    height: "24dp"
                                            
                        
                    MDTextField:
                        id: login_password_field
                        hint_text: "Password"
                        password:True
                        icon_left: "key"
                        size_hint_x: None
                        width: "250dp"
                        font_name: "Fontes/Roboto-Medium.ttf"
                        font_size: "12sp"
                        
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 0.64, 0.64, 0.64, 0.8
                        hint_text_color_normal: 1, 1, 1, 1
                        hint_text_color_focus: 0.64, 0.64, 0.64, 0.8
                        icon_left_color: 1, 1, 1, 1
                        icon_left_color_focus: 0.64, 0.64, 0.64, 0.8
                        text_color_focus: 1, 1, 1, 1
        
        
        RelativeLayout:
            size_hint: .85, None  
            pos_hint: {"center_x": .5 , "center_y": .49}
            
            MDCheckbox:
                id: remember_check
                size_hint: None, None
                size: "24dp", "24dp"
                pos_hint: {"center_x": .09, "center_y": .49}
                
            MDLabel:    
                text: "Remember me" 
                font_size: "13sp"
                valign: "center"
                pos_hint: {"x": 0.13} 
                
            MDTextButton:
                text:"Forgot Password"
                color: 41/255, 134/255, 204/255, 1
                pos_hint: {"center_x": .78, "center_y": .5}
                font_name: "Fontes/Roboto-Medium.ttf"
                font_size: "12sp"
        
        MDFillRoundFlatButton:
            text:"LOGIN"
            text_color:"white"
            size_hint_x:"0.75"
            height:"40dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.40}
            md_bg_color: (0.5, 0.5, 0.5, 0.9)
            on_release: app.login()
        
        MDFillRoundFlatButton:
            text: "BACK"
            text_color: "white"
            size_hint_x: "0.75"
            height: "40dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.32}
            md_bg_color: (0.5, 0.5, 0.5, 0.9)
            on_release: app.voltar_menu()  
                         
                            
             
<RegisterScreen>:
    name:"register-form"
    
    MDFloatLayout:
        canvas.before:   
            Color:
                rgba: 1, 1, 1, 0.7                 
            Rectangle:
                source:"gradient3.png"
                size:self.size
                pos:self.pos 
    
        MDLabel:
            text:"REGISTER"
            halign:"center"
            font_style:"H4"
            font_name: "Fontes/Montserrat-Bold.ttf"
            pos_hint: {"center_x": 0.5, "center_y": 0.92}
            
     
            
    MDFloatLayout:
        size_hint: .9, .70
        pos_hint:{"center_x": .5, "center_y":.49}
        canvas:
            Color:
                rgba: 1, 1, 1, 0.58   
            RoundedRectangle:
                size:self.size
                pos:self.pos
                radius: [8]
            
                
        MDFloatLayout:
            size_hint: .9, .12
            pos_hint:{"center_x": .5, "center_y":.88}
            canvas:
                Color:
                    rgba: 241/255, 240/255, 240/255, 0.1    
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius: [50]
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 50)
                    width: 2   
                      
            MDBoxLayout:
                orientation:"horizontal"
                pos_hint: {"center_x": .55, "center_y": .37}
                spacing: "8dp"
                height: "24dp"
                        
                    
                MDTextField:
                    id: register_name_field
                    hint_text: "Full Name"
                    icon_left: "account"
                    size_hint_x: None
                    width: "250dp"
                    font_name: "Fontes/Roboto-Medium.ttf"
                    font_size: "12sp"
                    
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 0.64, 0.64, 0.64, 0.8
                    hint_text_color_normal: 1, 1, 1, 1
                    hint_text_color_focus: 0.64, 0.64, 0.64, 0.8
                    icon_left_color: 1, 1, 1, 1
                    icon_left_color_focus: 0.64, 0.64, 0.64, 0.8
                    text_color_focus: 1, 1, 1, 1
        
        MDFloatLayout:
            size_hint: .9, .12
            pos_hint:{"center_x": .5, "center_y":.70}
            canvas:
                Color:
                    rgba: 241/255, 240/255, 240/255, 0.1    
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius: [50]
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 50)
                    width: 2   
                      
            MDBoxLayout:
                orientation:"horizontal"
                pos_hint: {"center_x": .55, "center_y": .37}
                spacing: "8dp"
                height: "24dp"
                        
                    
                MDTextField:
                    id: register_email_field
                    hint_text: "E-Mail"
                    icon_left: "email"
                    size_hint_x: None
                    width: "250dp"
                    font_name: "Fontes/Roboto-Medium.ttf"
                    font_size: "12sp"
                    
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 0.64, 0.64, 0.64, 0.8
                    hint_text_color_normal: 1, 1, 1, 1
                    hint_text_color_focus: 0.64, 0.64, 0.64, 0.8
                    icon_left_color: 1, 1, 1, 1
                    icon_left_color_focus: 0.64, 0.64, 0.64, 0.8
                    text_color_focus: 1, 1, 1, 1
                
        MDFloatLayout:
            size_hint: .9, .12
            pos_hint:{"center_x": .5, "center_y":.52}
            canvas:
                Color:
                    rgba: 241/255, 240/255, 240/255, 0.1   
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius: [50]
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 50)
                    width: 2 
                    
            MDBoxLayout:
                orientation:"horizontal"
                pos_hint: {"center_x": .56, "center_y": .39}
                spacing: "12dp"
                height: "24dp"
                                        
                    
                MDTextField:
                    id: register_phone_field
                    hint_text: "Phone Number"
                    icon_left: "phone"
                    size_hint_x: None
                    width: "250dp"
                    font_name: "Fontes/Roboto-Medium.ttf"
                    font_size: "12sp"
                    
                    input_filter: "int"
                    input_type: "number"
                    
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 0.64, 0.64, 0.64, 0.8
                    hint_text_color_normal: 1, 1, 1, 1
                    hint_text_color_focus: 0.64, 0.64, 0.64, 0.8
                    icon_left_color: 1, 1, 1, 1
                    icon_left_color_focus: 0.64, 0.64, 0.64, 0.8
                    text_color_focus: 1, 1, 1, 1            
                                 
                    
        MDFloatLayout:
            size_hint: .9, .12
            pos_hint:{"center_x": .5, "center_y":.34}
            canvas:
                Color:
                    rgba: 241/255, 240/255, 240/255, 0.1    
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius: [50]
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 50)
                    width: 2 
                    
            MDBoxLayout:
                orientation:"horizontal"
                pos_hint: {"center_x": .56, "center_y": .39}
                spacing: "12dp"
                height: "24dp"
                                        
                    
                MDTextField:
                    id: register_password_field
                    hint_text: "Password"
                    password:True
                    icon_left: "key"
                    size_hint_x: None
                    width: "250dp"
                    font_name: "Fontes/Roboto-Medium.ttf"
                    font_size: "12sp"
                    
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 0.64, 0.64, 0.64, 0.8
                    hint_text_color_normal: 1, 1, 1, 1
                    hint_text_color_focus: 0.64, 0.64, 0.64, 0.8
                    icon_left_color: 1, 1, 1, 1
                    icon_left_color_focus: 0.64, 0.64, 0.64, 0.8
                    text_color_focus: 1, 1, 1, 1
                    
    
    BoxLayout:
        orientation: "horizontal"
        size_hint: 0.75, None
        height: "40dp"
        spacing: "10dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.26}

        MDFillRoundFlatButton:
            text:"REGISTER"
            text_color:"white"
            md_bg_color: (0.5, 0.5, 0.5, 0.9)
            size_hint_x: 1
            on_release:app.register()

        MDFillRoundFlatButton:
            text:"BACK"
            text_color:"white"
            md_bg_color: (0.5, 0.5, 0.5, 0.9)
            size_hint_x: 1
            on_release: app.voltar_menu()
                         
<MainMenuScreen>:
    name:"main-menu" 
    
    MDNavigationLayout: 
        ScreenManager:
            MDScreen:
                name:"home"
                md_bg_color: 1, 1, 1, 1
                
                MDBoxLayout:
                    orientation:"vertical"
                    pos_hint: {"center_y": 0.60}
                   
                    MDTopAppBar:
                        elevation: 1 
                        md_bg_color: 1, 1, 1, 1
                        
                        
                        MDIconButton:
                            icon:"menu"
                            theme_text_color:"Custom"
                            text_color: 0, 0, 0, 1
                            on_release: nav_drawer.set_state("toggle")    
                                  
                    MDGridLayout:
                        cols:2
                        adaptive_size: True
                        spacing: dp(20)
                        padding: dp(20)
                        pos_hint:{"center_x": 0.5}
                        size_hint_y: None
                        height: self.minimum_height
                        
                        MDCard:
                            orientation:"vertical"
                            ripple_behavior: True
                            size_hint: None, None
                            size: dp(140), dp(140)
                            md_bg_color: 0, 0.7, 0.5, 1
                            on_release: app.change_screen("weight")
                            
                            MDLabel:
                                text:"Weight"
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "20sp"
                                halign: "left"
                                padding_x: dp(12)
                                
                                  
                            FloatLayout:
                                size_hint_y: None
                                height: dp(100)
                                Image:
                                    source: "weight_bg.png"
                                    allow_stretch: True
                                    keep_ratio: True
                                    size_hint: None, None
                                    size: dp(110), dp(110)
                                    pos_hint:{"center_x": 0.68, "center_y": 0.42}
                            
                        
                        MDCard:
                            orientation:"vertical"
                            ripple_behavior: True
                            size_hint: None, None
                            size: dp(140), dp(140)
                            md_bg_color: 0, 0.7, 0.5, 1
                            on_release: app.change_screen("water")
                            
                            MDLabel:
                                text:"Water"
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "20sp"
                                halign: "left"
                                padding_x: dp(12)
                        
                            FloatLayout:
                                size_hint_y: None
                                height: dp(100)
                                Image:
                                    source: "water_bg.png"
                                    allow_stretch: True
                                    keep_ratio: True
                                    size_hint: None, None
                                    size: dp(70), dp(70)
                                    pos_hint:{"center_x": 0.7, "center_y": 0.45}
                        
                        MDCard:
                            orientation:"vertical"
                            ripple_behavior: True
                            size_hint: None, None
                            size: dp(140), dp(140)
                            md_bg_color: 0, 0.7, 0.5, 1
                            on_release: app.change_screen("menstrualCycle")
                            
                            MDLabel:
                                text:"Menstrual Cycle" 
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "20sp"
                                halign: "left"
                                padding_x: dp(12) 
                                
                            FloatLayout:
                                size_hint_y: None
                                height: dp(80)
                                Image:
                                    source: "menstrual_bg.png"
                                    allow_stretch: True
                                    keep_ratio: True
                                    size_hint: None, None
                                    size: dp(65), dp(65)
                                    pos_hint:{"center_x": 0.68, "center_y": 0.53}
                                
                        MDCard:
                            orientation:"vertical"
                            ripple_behavior: True
                            size_hint: None, None
                            size: dp(140), dp(140)
                            md_bg_color: 0, 0.7, 0.5, 1
                            on_release: app.change_screen("medications")
                            
                            MDLabel:
                                text:"Medications"
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "20sp"
                                halign: "left"
                                padding_x: dp(12)
                                
                            FloatLayout:
                                size_hint_y: None
                                height: dp(100)
                                Image:
                                    source: "medicine_bg.png"
                                    allow_stretch: True
                                    keep_ratio: True
                                    size_hint: None, None
                                    size: dp(60), dp(60)
                                    pos_hint:{"center_x": 0.68, "center_y": 0.38}
                   
                    MDCarousel:
                        id:carousel_area
                        size_hint_y: None
                        size_hint_x: 0.85
                        height: "120dp"
                        spacing: dp(20)
                        pos_hint:{"center_x":0.5, "center_y":0.2}
                        on_index: app.update_dots(self.index)
                        
                        
                        MDCard:
                            orientation: "vertical"
                            md_bg_color: 0, 0.6, 0, 1
                            radius: [15, 15, 15, 15]
                            padding: dp(20)
                            MDLabel:
                                text:"Regular exercise is the key to staying healthy and happy!"
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "18sp" 
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                            MDLabel:
                                text: "- Stay active, stay happy!"
                                font_size: "12sp" 
                                font_name: "Fontes/Poppins-Medium.ttf"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                
                        MDCard:
                            orientation: "vertical"
                            md_bg_color: 0, 0.6, 0, 1
                            radius: [15, 15, 15, 15]
                            padding: dp(20)
                            MDLabel:
                                text:"Water is essential for your organs to work properly!"
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "18sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                            MDLabel:
                                text: "- Stay hydrated, stay healthy!"
                                font_size: "12sp" 
                                font_name: "Fontes/Poppins-Medium.ttf"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                
                        MDCard:
                            orientation: "vertical"
                            md_bg_color: 0, 0.6, 0, 1
                            radius: [15, 15, 15, 15]
                            padding: dp(20)
                            MDLabel:
                                text:"Regular checkups with a doctor can prevent serious health problems!"
                                font_name: "Fontes/Roboto-Bold.ttf"
                                font_size: "16sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                            MDLabel:
                                text: "- Stay checked, stay safe!"
                                font_size: "12sp" 
                                font_name: "Fontes/Poppins-Medium.ttf"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                        
                    MDBoxLayout:
                        id: dots_area
                        orientation: "horizontal"
                        spacing: dp(15)
                        size_hint_y: None
                        height: "24dp"
                        width: carousel_area.width 
                        pos_hint: {"center_x": 0.89}
                    
        MDNavigationDrawer:
            id: nav_drawer
            
            
            MDBoxLayout:
                orientation: "vertical"
                spacing: "8dp"
                padding: "8dp"
                pos_hint:{"center_y": 1.12}
                

                MDLabel:
                    text: "Menu"
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDList:
                    OneLineIconListItem:
                        text: "Settings"
                        on_release:
                            nav_drawer.set_state("close")
                            app.change_screen("settings")
                        IconLeftWidget:
                            icon: "cog"

                    OneLineIconListItem:
                        text: "About"
                        on_release:
                            nav_drawer.set_state("close")
                            app.change_screen("about")
                        IconLeftWidget:
                            icon: "information"

                    OneLineIconListItem:
                        text: "Help"
                        on_release:
                            nav_drawer.set_state("close")
                            app.change_screen("help")
                        IconLeftWidget:
                            icon: "help-circle"           
            
            
<WeightScreen>
    name: "weight"
    on_pre_enter: root.reset_fields()

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        
        MDTopAppBar:
            title: "Weight Tracking"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menuzao()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1
            
            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)
            
        ScrollView:
        
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: dp(20), dp(20), dp(20), dp(20)  
                spacing: dp(20)
                
                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(60)
        
                    MDCard:
                        size_hint_x: None
                        width: dp(100)
                        md_bg_color: 0, 0.7, 0.5, 1
                        radius: [8]
                        MDLabel:
                            text: "Height"
                            halign: "center"
                            valign: "center"
        
                    MDCard:
                        md_bg_color: 1, 1, 1, 1
                        radius: [8]
                        padding: dp(10)
        
                        MDTextField:
                            id: height_field
                            hint_text: "  Insert your height"
                            disable_hint_text: True 
                            input_filter: "float"
                            mode: "rectangle"
                            size_hint_y: None
                            height: dp(40)             
                            pos_hint: {"center_y": 0.5}
                            
                            line_color_normal: 0.7, 0.7, 0.5, 1   
                            line_color_focus: 0, 0.7, 0.5, 1
                            
                            text_color_normal: 0, 0, 0, 1
                            text_color_focus: 0, 0, 0, 1
                            
                            hint_text_color_normal: 0, 0, 0, 0.4
                            hint_text_color_focus: 0, 0, 0, 1
                            
                            
                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(60)
        
                    MDCard:
                        size_hint_x: None
                        width: dp(100)
                        md_bg_color: 0, 0.7, 0.5, 1
                        radius: [8]
                        MDLabel:
                            text: "Weight"
                            halign: "center"
                            valign: "center"
        
                    MDCard:
                        md_bg_color: 1, 1, 1, 1
                        radius: [8]
                        padding: dp(10)
        
                        MDTextField:
                            id: weight_field
                            hint_text: "  Insert your weight"
                            disable_hint_text: True 
                            input_filter: "float"
                            mode: "rectangle"
                            size_hint_y: None
                            height: dp(40)             
                            pos_hint: {"center_y": 0.5}
                            
                            line_color_normal: 0.7, 0.7, 0.5, 1   
                            line_color_focus: 0, 0.7, 0.5, 1
                            
                            text_color_normal: 0, 0, 0, 1
                            text_color_focus: 0, 0, 0, 1
                            
                            hint_text_color_normal: 0, 0, 0, 0.4
                            hint_text_color_focus: 0, 0, 0, 1

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(60)
        
                    MDRaisedButton:
                        text: "Calculate"
                        pos_hint: {"center_x": 0.5}
                        size_hint_x: 1
                        md_bg_color: 0, 0.7, 0.5, 0.98
                        on_release: app.calculate_weight()
                        
                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(150)
                    
                    Image:
                        source: "weight_bg.png"
                        allow_stretch: True
                        keep_ratio: True
                        size_hint: None, None
                        size: dp(190), dp(190)
                        pos_hint: {"center_y": 0.55}
                    
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: dp(100)
                        pos_hint: {"center_y": 0.65}
                        
                        MDLabel:
                            text: "Your IMC is: "
                            font_size: "12sp" 
                            font_name: "Fontes/Poppins-Medium.ttf"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "left"
                            valign: "top" 
                            
                        MDLabel:
                            id: result_field
                            text: ""
                            font_size: "30sp" 
                            font_name: "Fontes/Montserrat-Medium.ttf"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            halign: "left"
                            valign: "middle" 
                  
                       
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(10)       
                    padding: dp(10)
                    size_hint_y: None
                    height: self.minimum_height
                    
                    Widget:
                        size_hint_y: None
                        height: dp(20)
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(5)
                        padding:dp(20) 
                        
                
                        MDIcon:
                            icon: "chevron-down"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                
                        MDLabel:
                            text: "Scroll down"
                            halign: "center"
                            font_size: "20sp"
                            font_name: "Fontes/Roboto-Bold.ttf"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                
                        MDIcon:
                            icon: "chevron-down"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        
                    Widget:
                        size_hint_y: None
                        height: dp(50)
                        
                    MDLabel:
                        text: "Classification table (IMC)"
                        halign: "center"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        padding: dp(0), dp(0), dp(0), dp(30)  
                    
                    MDGridLayout:
                        cols: 2
                        spacing: dp(10)
                        row_default_height: dp(30)
                        size_hint_y: None
                        height: self.minimum_height
                        col_default_width: dp(150)
                        col_force_default: True
                        
                        MDLabel:
                            text: "Classification"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text:"IMC"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                        MDLabel: 
                            text:"Underweight"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text: "< 18,5"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                        MDLabel:
                            text:"Healthy"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text: "18,5 ~ 24,9"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                        MDLabel:
                            text:"Overweight"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text: "25 ~ 29,9"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                        MDLabel:
                            text: "Class 1 Obesity"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text: "30 ~ 34,9"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                        MDLabel:
                            text: "Class 2 Obesity"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text: "35 ~  39,9"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                        MDLabel:
                            text:"Class 3 Obesity"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            text: "> 40"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1                                          
                    

<WaterScreen>
    name: "water" 
    on_pre_enter: root.reset_fields()
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        
        MDTopAppBar:
            title: "Water Tracking"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menuzao()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1
            
            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  
        ScrollView:         
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(15)
                spacing: dp(20)
                
                MDBoxLayout:
                    orientation:"vertical"
                    size_hint: 1, None
                    adaptive_height: True 
                    height: self.minimum_height + dp(60)
                    pos_hint: {"center_x": 0.5}
                    padding: dp(10), dp(0), dp(10), dp(0)
                    spacing: dp(40)
                
                    canvas.before:
                        Color:
                            rgba: 0.1176, 0.8706, 0.9608, 0.8
                        Line:
                            width: 1.5
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 20)
                            
                    Widget:
                        size_hint_y: None
                        height: dp(10)
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        pos_hint: {"center_x": .5}
                        spacing: dp(30)
                        
                        MDLabel:
                            text: "Drink"
                            font_size: "20sp" 
                            font_name: "Fontes/Montserrat-Medium.ttf"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                    
                        MDIcon:
                            icon: "drinking-water.png"          
                            halign: "center"       
                            size_hint: None, None
                            size: dp(64), dp(64)
                            font_size: "70sp"   
                            theme_text_color: "Custom"
                            text_color: 0, 0, 1, 1
                            pos_hint: {"center_x": .5} 
                            
                        MDLabel:
                            text: "Water"
                            font_size: "20sp" 
                            font_name: "Fontes/Montserrat-Medium.ttf"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                        
                    MDCard:
                        md_bg_color: 1, 1, 1, 1
                        
                        MDTextField:
                            id: age_water_field
                            hint_text:"  Insert your age"
                            disable_hint_text: True
                            input_filter: "float"
                            mode: "rectangle"
                            size_hint_y: None
                            height: dp(48)
                            
                            line_color_normal: 0.196, 0.243, 0.459, 0.60
                            line_color_focus: 0.0078, 0.1803, 0.9254, 1
                            
                            text_color_normal: 0, 0, 0, 1
                            text_color_focus: 0, 0, 0, 1
                            
                            hint_text_color_normal: 0, 0, 0, 0.4
                            hint_text_color_focus: 0, 0, 0, 1
                    
                    MDCard:
                        md_bg_color: 1, 1, 1, 1
                        
                        MDTextField:
                            id: weight_water_field
                            hint_text: "  Insert your weight"
                            disable_hint_text: True
                            input_filter: "float"
                            mode: "rectangle"
                            size_hint_y: None
                            height: dp(48)
                            
                            line_color_normal: 0.196, 0.243, 0.459, 0.60
                            line_color_focus: 0.0078, 0.1803, 0.9254, 1
                            
                            text_color_normal: 0, 0, 0, 1
                            text_color_focus: 0, 0, 0, 1
                        
                            hint_text_color_normal: 0, 0, 0, 0.4
                            hint_text_color_focus: 0, 0, 0, 1
                        
                        
                    MDRaisedButton:
                        text: "Calculate"
                        pos_hint:{"center_x": .5}
                        size_hint_y: None
                        height: dp(60)
                        on_release: app.water_calculate()
                        
                    MDLabel:
                        id: water_result_field
                        text: "Results Here"
                        text_color: 0, 0, 0, 1
                        font_size: "20sp" 
                        font_name: "Fontes/Montserrat-Medium.ttf"
                        halign: "center"
                        theme_text_color: "Custom"
                        size_hint_y: None
                        height: dp(30)   
                        padding: dp(0), dp(0), dp(0), dp(20) 
                                            
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: dp(35)
                    size_hint_y: None
                    height: self.minimum_height
                    
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)
                        size_hint_y: None
                        height: dp(30)
                        
                        MDIcon:
                            icon: "water-outline"
                            size_hint: None, None
                            size: dp(24), dp(24)
                            theme_text_color: "Custom"
                            text_color: 0, 0.5, 1, 1
                        
                        MDLabel:
                            text: "Drinking enough water is essential for keeping your body healthy."
                            halign: "left"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)
                        size_hint_y: None
                        height: dp(25)
                        
                        MDIcon:
                            icon: "water-outline"
                            size_hint: None, None
                            size: dp(24), dp(24)
                            theme_text_color: "Custom"
                            text_color: 0, 0.5, 1, 1
                        
                        MDLabel:
                            text: "It helps regulate body temperature, transport nutrients, and remove toxins."
                            halign: "left"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)
                        size_hint_y: None
                        height: dp(30)
                        
                        MDIcon:
                            icon: "water-outline"
                            size_hint: None, None
                            size: dp(24), dp(24)
                            theme_text_color: "Custom"
                            text_color: 0, 0.5, 1, 1
                        
                        MDLabel:
                            text: "Staying hydrated improves concentration, mood, and physical performance."
                            halign: "left"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)
                        size_hint_y: None
                        height: dp(30)
                        
                        MDIcon:
                            icon: "water-outline"
                            size_hint: None, None
                            size: dp(24), dp(24)
                            theme_text_color: "Custom"
                            text_color: 0, 0.5, 1, 1
                        
                        MDLabel:
                            text: "Proper hydration supports healthy skin, digestion, and joint lubrication."
                            halign: "left"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: dp(10)
                        size_hint_y: None
                        height: dp(25)
                        
                        MDIcon:
                            icon: "water-outline"
                            size_hint: None, None
                            size: dp(24), dp(24)
                            theme_text_color: "Custom"
                            text_color: 0, 0.5, 1, 1
                        
                        MDLabel:
                            text: "Make water your daily habit to maintain balance and overall well-being."
                            halign: "left"
                            theme_text_color: "Custom"
                            text_color: 0, 0, 0, 1
                            
                    
<MenstrualScreen>
    name: "menstrualCycle" 
    on_pre_enter: root.reset_fields()
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        
        MDTopAppBar:
            title: "Period Tracking"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menuzao()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1
            
            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  
        ScrollView:         
            MDBoxLayout: 
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)
                spacing: dp(10)
                
                
                MDTextField:
                    id: last_period
                    hint_text: "Last date of period(dd/mm/yyyy)"
                    
                    line_color_normal: 0.196, 0.243, 0.459, 0.60
                    line_color_focus: 0.9647, 0.0588, 0.3333, 0.8

                    text_color_normal: 0, 0, 0, 1
                    text_color_focus: 0, 0, 0, 1
                
                    hint_text_color_normal: 0, 0, 0, 0.4
                    hint_text_color_focus: 0, 0, 0, 1
                    
                MDTextField:
                    id: duration
                    hint_text: "Menstruation duration(days)"
                    input_filter: "int"
                    
                    line_color_normal: 0.196, 0.243, 0.459, 0.60
                    line_color_focus: 0.9647, 0.0588, 0.3333, 0.8

                    text_color_normal: 0, 0, 0, 1
                    text_color_focus: 0, 0, 0, 1
                
                    hint_text_color_normal: 0, 0, 0, 0.4
                    hint_text_color_focus: 0, 0, 0, 1
                    
                MDTextField:
                    id: cycle
                    hint_text: "Cycle Lenght"
                    input_filter: "int"
                    
                    line_color_normal: 0.196, 0.243, 0.459, 0.60
                    line_color_focus: 0.9647, 0.0588, 0.3333, 0.8

                    text_color_normal: 0, 0, 0, 1
                    text_color_focus: 0, 0, 0, 1
                
                    hint_text_color_normal: 0, 0, 0, 0.4
                    hint_text_color_focus: 0, 0, 0, 1
                    
                MDRaisedButton:
                    text: "Calculate"
                    pos_hint: {"center_x": .5}
                    on_release: app.calculate_cycle()
                
                MDBoxLayout:
                    id: month_bar
                    size_hint_y: None
                    height: 0       
                    opacity: 0 
                    md_bg_color: 0.95, 0.8, 0.8, 1

                    MDLabel:
                        id: month_label
                        text: ""
                        halign: "center"
                        font_style: "H5"
                        size_hint_y: None
                        height: dp(50)
                        theme_text_color: "Custom"
                        font_name: "Fontes/Poppins-Bold.ttf"
                        text_color_normal: 0, 0, 0, 1
                    
                GridLayout:
                    id: week_header
                    cols: 7
                    size_hint_y: None
                    row_default_height: dp(40)
                    row_force_default: True
                    height: self.minimum_height
            
                    canvas.before:
                        Color:
                            rgba: 0.95, 0.8, 0.8, 1   
                        Rectangle:
                            pos: self.pos
                            size: self.size 
                    
                GridLayout:
                    id: calendar_grid
                    cols: 7
                    spacing: dp(5)
                    padding: dp(10)
                    size_hint_y: None
                    row_default_height: dp(40)  
                    row_force_default: True  
                    height: self.minimum_height
                    
                    canvas.before:
                        Color:
                            rgba: root.calendar_color
                        Rectangle:
                            pos: self.pos
                            size: self.size


<MedicationsScreen>
    name: "medications" 
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Period Tracking"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menuzao()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1

            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  

        ScrollView:
            MDGridLayout:
                cols:2
                adaptive_size: True
                spacing: dp(20)
                padding: dp(20)
                pos_hint:{"center_x": 0.5}
                size_hint_y: None
                height: self.minimum_height
                
                MDCard:
                    orientation:"vertical"
                    ripple_behavior: True
                    size_hint: None, None
                    size: dp(140), dp(140)
                    md_bg_color: 0, 0.7, 0.5, 1
                    on_release: app.change_screen("generic")
                    
                    FloatLayout:
                        size_hint_y: None
                        height: dp(100)
                        Image:
                            source: "pills.png"
                            allow_stretch: True
                            keep_ratio: True
                            size_hint: None, None
                            size: dp(75), dp(75)
                            pos_hint:{"center_x": 0.50, "center_y": 0.40}
                    
                    MDLabel:
                        text:"Generic Medicine"
                        font_name: "Fontes/Roboto-Bold.ttf"
                        font_size: "14sp"
                        halign: "center"
                        padding_x: dp(12)
                    
                
                MDCard:
                    orientation:"vertical"
                    ripple_behavior: True
                    size_hint: None, None
                    size: dp(140), dp(140)
                    md_bg_color: 0, 0.7, 0.5, 1
                    on_release: app.change_screen("vitamin")
                    
                    FloatLayout:
                        size_hint_y: None
                        height: dp(100)
                        Image:
                            source: "vitamin.png"
                            allow_stretch: True
                            keep_ratio: True
                            size_hint: None, None
                            size: dp(70), dp(70)
                            pos_hint:{"center_x": 0.58, "center_y": 0.42}
                    
                    MDLabel:
                        text:"Vitamins"
                        font_name: "Fontes/Roboto-Bold.ttf"
                        font_size: "16sp"
                        halign: "center"
                        padding_x: dp(12)
                
                
                MDCard:
                    orientation:"vertical"
                    ripple_behavior: True
                    size_hint: None, None
                    size: dp(140), dp(140)
                    md_bg_color: 0, 0.7, 0.5, 1
                    on_release: app.change_screen("mineral")
                    
                    FloatLayout:
                        size_hint_y: None
                        height: dp(100)
                        Image:
                            source: "mineral.png"
                            allow_stretch: True
                            keep_ratio: True
                            size_hint: None, None
                            size: dp(70), dp(70)
                            pos_hint:{"center_x": 0.52, "center_y": 0.38}
                            padding_x: dp(12) 
                    
                    MDLabel:
                        text:"Mineral" 
                        font_name: "Fontes/Roboto-Bold.ttf"
                        font_size: "18sp"
                        halign: "center"
                        padding_x: dp(12) 
                        
                        
                MDCard:
                    orientation:"vertical"
                    ripple_behavior: True
                    size_hint: None, None
                    size: dp(140), dp(140)
                    md_bg_color: 0, 0.7, 0.5, 1
                    on_release: app.change_screen("homemade")
                    
                    FloatLayout:
                        size_hint_y: None
                        height: dp(100)
                        Image:
                            source: "homemade.png"
                            allow_stretch: True
                            keep_ratio: True
                            size_hint: None, None
                            size: dp(60), dp(60)
                            pos_hint:{"center_x": 0.54, "center_y": 0.38}
                    
                    MDLabel:
                        text:"Homemade"
                        font_name: "Fontes/Roboto-Bold.ttf"
                        font_size: "18sp"
                        halign: "center"
                        padding_x: dp(12)
                        
            
<GenericScreen>
    name: "generic"
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Generic"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menu()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1

            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  

        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                adaptive_height: True
            
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Tylenol", "Used to reduce fever and relieve mild pain", "Medicine/Tylenol.jpg")

                    Image:
                        source: "pills.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Tylenol"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Tylenol", "Used to reduce fever and relieve mild pain", "Medicine/Tylenol.jpg")


                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Bufferin A", "Used for general pain", "Medicine/Bufferin.jpg")

                    Image:
                        source: "pills.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Bufferin A"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Bufferin A", "Used for general pain", "Medicine/Bufferin.jpg")   
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Bufferin Premium", "Used for extreme pain", "Medicine/BufferinP.jpg")

                    Image:
                        source: "pills.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Bufferin Premium"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Bufferin Premium", "Used for extreme pain", "Medicine/BufferinP.jpg")
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Eve", "Used for headache, colic, toothache, fever, cramps", "Medicine/Eve.jpg")

                    Image:
                        source: "pills.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Eve"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Eve", "Used for headache, colic, toothache, fever, cramps", "Medicine/Eve.jpg")
        
        
<VitaminsScreen>
    name: "vitamin"
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Vitamins"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menu()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1

            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  

        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                adaptive_height: True
            
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Vitamin A", "Crucial for healthy vision, immunity, growth, and skin integrity", "Medicine/VitaA.png")

                    Image:
                        source: "vitamin.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Vitamin A"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Vitamin A", "Crucial for healthy vision, immunity, growth, and skin integrity", "Medicine/VitaA.png")


                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Vitamin B12", "Crucial for energy, blood formation, nerve health, and cell function", "Medicine/VitaB.png")

                    Image:
                        source: "vitamin.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Vitamin B12"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Vitamin B12", "Crucial for energy, blood formation, nerve health, and cell function", "Medicine/VitaB.png")   
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Vitamina C", "Vital for immunity, skin health, healing, and protection against cell damage.", "Medicine/VitaC.png")

                    Image:
                        source: "vitamin.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Vitamin C"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Vitamin C", "Vital for immunity, skin health, healing, and protection against cell damage.", "Medicine/VitaC.png")
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Vitamin D", "Essential for strong bones, immunity, and muscle health.", "Medicine/VitaD.png")

                    Image:
                        source: "vitamin.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Vitamin D"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Vitamin D", "Essential for strong bones, immunity, and muscle health.", "Medicine/VitaD.png")
                        
                        
<MineralScreen>
    name: "mineral"
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Mineral"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menu()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1

            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  

        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                adaptive_height: True
            
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Calcium", "Crucial for strong bones, muscle function, nerve health, and heart rhythm", "Medicine/MineCa.png")

                    Image:
                        source: "mineral.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Calcium(Ca)"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Calcium", "Crucial for strong bones, muscle function, nerve health, and heart rhythm", "Medicine/MineCa.png")


                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Zinc", "Crucial for immunity, healing, growth, and senses", "Medicine/MineZn.png")

                    Image:
                        source: "mineral.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Zinc(Zn)"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Zinc", "Crucial for immunity, healing, growth, and senses", "Medicine/MineZn.png")   
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Potassium", "Essential for heart, muscles, nerves, and fluid balance", "Medicine/MineK.png")

                    Image:
                        source: "mineral.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Potassium(K)"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Potassium", "Essential for heart, muscles, nerves, and fluid balance", "Medicine/MineK.png")
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Magnesium", "Vital for energy, muscles, nerves, heart, and bones", "Medicine/MineMg.png")

                    Image:
                        source: "mineral.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Magnesium(Mg)"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Magnesium", "Vital for energy, muscles, nerves, heart, and bones", "Medicine/MineMg.png")
                        
                        
<HomemadeScreen>
    name: "homemade"
    
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Homemade"
            elevation: 0
            left_action_items: [["arrow-left", lambda x: app.ir_menu()]]
            padding: dp(0), dp(0), dp(45), dp(0) 
            md_bg_color: 0, 0.7, 0.5, 1
            specific_text_color: 1, 1, 1, 1

            canvas.after:
                Color:
                    rgba: 0, 0, 0, 1  
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, dp(1)  

        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                adaptive_height: True
            
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Garlic Honey Syrup", "Natural remedy that supports immunity, heart health, and respiratory relief","Medicine/Home1.jpg")

                    Image:
                        source: "homemade.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Garlic Honey Syrup"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Garlic Honey Syrup", "Natural remedy that supports immunity, heart health, and respiratory relief","Medicine/Home1.jpg" )


                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Turmeric Golden Milk", "Helps with inflammation, immunity, heart, brain, and relaxation","Medicine/Home2.png" )

                    Image:
                        source: "homemade.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Turmeric Golden Milk"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Turmeric Golden Milk", "Helps with inflammation, immunity, heart, brain, and relaxation","Medicine/Home2.png")  
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Chamomile Sleep Tea", "Helps with sleep, relaxation, digestion, and gentle immune support","Medicine/Home3.png" )

                    Image:
                        source: "homemade.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Chamomile Sleep Tea"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Chamomile Sleep Tea", "Helps with sleep, relaxation, digestion, and gentle immune support","Medicine/Home3.png")
                        
                MDCard:
                    orientation: "horizontal"
                    size_hint_x: 1
                    height: self.parent.height * 0.12
                    radius: [15, 15, 15, 15]
                    md_bg_color: 1, 1, 1, 1
                    padding: dp(10)
                    ripple_behavior: True
                    elevation: 1
                    shadow_radius: 15                   
                    on_release: app.show_medicine("Ginger Tonic", "Supports digestion, immunity, circulation, and respiratory health", "Medicine/Home4.png")

                    Image:
                        source: "homemade.png"
                        size_hint: None, None
                        size: self.parent.height * 0.3, self.parent.height * 0.3
                        pos_hint: {"center_y": 0.5}

                    BoxLayout:
                        orientation: "vertical"
                        padding: dp(10), 0
                        MDLabel:
                            text: "Ginger Tonic"
                            font_style: "H6"
                            halign: "left"
                            theme_text_color: "Custom"

                    MDIconButton:
                        icon: "arrow-right"
                        theme_icon_color: "Custom"
                        icon_color: 1, 1, 1, 1
                        size_hint: None, None
                        size: dp(40), dp(40)
                        md_bg_color: 0, 0.7, 0.5, 1
                        on_release: app.show_medicine("Ginger Tonic", "Supports digestion, immunity, circulation, and respiratory health", "Medicine/Home4.png")
"""


class LoginPage(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        self.menstrual_days = []
        self.db = Database()
        root = Builder.load_string(kv)
        Clock.schedule_once(self.start_carousel, 0)

        pref = self.db.load_preference()
        if pref and pref[1] == 1:
            email_salvo = pref[0]
            login_screen = root.get_screen("login-form")
            login_screen.ids.login_email_field.text = email_salvo

        return root

    def start_carousel(self, dt):
        carousel = self.root.get_screen("main-menu").ids.carousel_area
        dots_area = self.root.get_screen("main-menu").ids.dots_area
        dots_area.clear_widgets()
        self.dots = []

        for i in range(len(carousel.slides)):
            dot = MDIcon(
                icon = "checkbox-blank-circle-outline",
                theme_text_color = "Custom",
                text_color = (0.7, 0.7, 0.7, 1)
            )
            dot.font_size = "16sp"
            dots_area.add_widget(dot)
            self.dots.append(dot)

        self.update_dots(0)
        Clock.schedule_interval(lambda _dt: self.next_slide(carousel), 4)

    def update_dots(self, index):
        for i, dot in enumerate(self.dots):
            if i == index:
                dot.icon = "checkbox-blank-circle"
                dot.text_color = (0, 0, 0, 1)
            else:
                dot.icon = "checkbox-blank-circle-outline"
                dot.text_color = (0.7, 0.7, 0.7, 1)

    def next_slide(self, carousel):
        if carousel.index < len(carousel.slides) - 1:
            carousel.load_next()
        else:
            carousel.index = 0

        self.update_dots(carousel.index)

    def voltar_menu(self):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = "Menu"

    def ir_login(self):
        self.root.transition = SlideTransition(direction="left")
        self.root.current = "login-form"

    def ir_registro(self):
        self.root.transition = SlideTransition(direction="left")
        self.root.current = "register-form"

    def ir_menuzao(self):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = "main-menu"

    def ir_menu(self):
        self.root.transition = SlideTransition(direction="right")
        self.root.current = "medications"

    def change_screen(self, screen_name):
        self.root.transition = SlideTransition(direction="left")
        self.root.current = screen_name

    def calculate_weight(self):
        screen = self.root.get_screen("weight")

        height = screen.ids.height_field.text
        weight = screen.ids.weight_field.text

        if not height or not weight:
            print("Please, fill up the labels!")
            return

        try:
            height = float(height)
            weight = float(weight)

            if height > 10:
                height = height/100

            imc = weight/(height * height)

            screen.ids.result_field.text = f"{imc:.2f}"
        except:
            print("Invalid Values!")


    def water_calculate(self):
        screen = self.root.get_screen("water")

        age = screen.ids.age_water_field.text
        weight = screen.ids.weight_water_field.text

        if not age or not weight:
            print("Please fill up the labels!")

        try:
            age = int(age)
            weight = int(weight)
            total = 0

            if age <= 17:
                total = 40 * weight
            elif age >= 18 or age <= 55:
                total = 35 * weight
            elif age >= 56 or age <= 65:
                total = 30 * weight
            elif age >= 66:
                total = 25 * weight

            if total >= 1000:
                total = total/1000
                screen.ids.water_result_field.text = f"{total:.1f} Liters"
            elif total < 1000:
                screen.ids.water_result_field.text = f"{total:.1f} Mililiters"

        except:
            screen.ids.water_result_field.text = "Invalid values!"

    def calculate_cycle(self):
        from datetime import datetime, timedelta
        screen = self.root.get_screen("menstrualCycle")

        try:
            last_period_str = screen.ids.last_period.text
            duration = int(screen.ids.duration.text)
            cycle = int(screen.ids.cycle.text)

            last_period_date = datetime.strptime(last_period_str,"%d/%m/%Y")

            next_period_start = last_period_date + timedelta(days=cycle)

            self.menstrual_days = [
                (next_period_start + timedelta(days=i)).day for i in range(duration)
            ]

            screen.ids.month_bar.height = dp(50)
            screen.ids.month_bar.opacity = 1

            screen.calendar_color = [1, 0.9, 0.9, 1]
            self.show_calendar(next_period_start.year, next_period_start.month)

        except Exception as e:
            print("Error", e)

    def show_calendar(self, year, month):
        print("monstrando", year, month, "dias:", self.menstrual_days)
        import calendar

        screen = self.root.get_screen("menstrualCycle")
        screen.ids.month_label.text = f"{calendar.month_name[month]} {year}"

        month_days = calendar.monthcalendar(year, month)

        screen.ids.week_header.clear_widgets()
        screen.ids.calendar_grid.clear_widgets()

        for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
            screen.ids.week_header.add_widget(
                MDLabel(text=d,
                        halign="center",
                        bold=True,
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1))
            )

        for week in month_days:
            for day in week:
                if day == 0:
                    screen.ids.calendar_grid.add_widget(
                        MDLabel(text="", halign="center")
                    )
                elif day in self.menstrual_days:
                    screen.ids.calendar_grid.add_widget(
                        MDLabel(
                            text=str(day),
                            halign="center",
                            theme_text_color="Custom",
                            text_color=(1,0,0,1),
                            font_name = "Fontes/Poppins-BoldItalic.ttf"
                        )
                    )
                else:
                    screen.ids.calendar_grid.add_widget(
                        MDLabel(
                            text=str(day),
                            halign="center",
                            theme_text_color="Custom",
                            text_color=(0, 0, 0, 1),
                            font_name="Fontes/Poppins-BoldItalic.ttf"
                        )
                    )

        screen.ids.calendar_grid.height = screen.ids.calendar_grid.minimum_height

    dialog = None

    def show_medicine(self, name, description, image_source):
        content = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10,
            size_hint_y=None,
            height = "200dp"
        )

        img = Image(
            source=image_source,
            size_hint=(1, None),
            height="120dp",
            allow_stretch=True,
            keep_ratio=True
        )
        content.add_widget(img)

        label_desc = MDLabel(
            text=description,
            halign="center",
            theme_text_color="Secondary"
        )
        content.add_widget(label_desc)

        dialog = MDDialog(
            title=f"{name}",
            type="custom",
            content_cls=content,
            size_hint=(0.9, None),
            height="350dp",
            buttons=[
                MDRaisedButton(text="Fechar", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()

    def login(self):
        email = self.root.get_screen("login-form").ids.login_email_field.text
        senha = self.root.get_screen("login-form").ids.login_password_field.text
        remember = self.root.get_screen("login-form").ids.remember_check.active

        user = self.db.login_user(email, senha)
        if user:
            self.db.save_preference(email, remember)
            self.root.transition = SlideTransition(direction="left")
            self.ir_menuzao()
        else:
            print("Invalid Login!")

    def register(self):
        name = self.root.get_screen("register-form").ids.register_name_field.text
        email = self.root.get_screen("register-form").ids.register_email_field.text
        phone = self.root.get_screen("register-form").ids.register_phone_field.text
        password = self.root.get_screen("register-form").ids.register_password_field.text

        ok = self.db.register_user(name, email, phone, password)
        if ok:
            print("User registered!")
            self.root.current = "login-form"
        else:
            print("This e-mail already exists!")



class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class MainMenuScreen(Screen):
    def on_pre_enter(self, *args):
        try:
            self.ids.nav_drawer.set_state("close")
        except AttributeError:
            pass

class WeightScreen(Screen):
    def reset_fields(self):
        self.ids.height_field.text = ""
        self.ids.weight_field.text = ""
        self.ids.result_field.text = ""

    pass

class WaterScreen(Screen):
    def reset_fields(self):
        self.ids.age_water_field.text = ""
        self.ids.weight_water_field.text = ""
        self.ids.water_result_field.text = "Results Here"

    pass

class MenstrualScreen(Screen):
    calendar_color = ListProperty([0, 0, 0, 0])

    def reset_fields(self):
        self.ids.last_period.text = ""
        self.ids.duration.text = ""
        self.ids.cycle.text = ""

    pass

class MedicationsScreen(Screen):
    pass

class GenericScreen(Screen):
    pass

class VitaminsScreen(Screen):
    pass

class MineralScreen(Screen):
    pass

class HomemadeScreen(Screen):
    pass


if __name__ == "__main__":
    LoginPage().run()


"Note:  [padding_left, padding_top, padding_right, padding_bottom]"