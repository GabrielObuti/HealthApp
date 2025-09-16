from kivy.lang import Builder
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDTextButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.textfield import MDTextField
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from kivy.clock import Clock

Window.size = (350, 600)

kv = """

ScreenManager:
    MenuScreen:
    LoginScreen:
    RegisterScreen:
    MainMenuScreen:
    WeightScreen:
    
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
                
        MDFillRoundFlatButton:
            text: "MENUZAO"
            text_color: "white"
            size_hint_x: "0.8"
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .20}
            font_name: "Fontes/Montserrat-Regular.ttf"
            md_bg_color: 76/255,168/255,35/255,0.9
            font_size: "20sp"
            on_press: self.md_bg_color = 76/255,168/255,35/255,0.7
            on_release:
                self.md_bg_color = 76/255,168/255,35/255,0.9
                app.ir_menuzao()
        
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

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1

        MDTopAppBar:
            title: "Weight Tracking"
            elevation: 2
            left_action_items: [["arrow-left", lambda x: app.voltar_menuzao()]]
            
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

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(60)
        
                    MDRaisedButton:
                        text: "Calcular"
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
                        size: dp(170), dp(170)
                    
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
                            font_name: "Fontes/Poppins-Medium.ttf"
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
                    
                    MDLabel:
                        text: "Classification table (IMC)"
                        halign: "center"
                        font_style: "H6"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                    
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
                    
                                               
                            
        
        
"""

class LoginPage(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        root = Builder.load_string(kv)
        Clock.schedule_once(self.start_carousel, 0)
        return root

    def start_carousel(self,dt):
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

    def next_slide(self,carousel):
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
        self.root.transition = SlideTransition(direction="left")
        self.root.current = "main-menu"


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
    pass


if __name__ == "__main__":
    LoginPage().run()