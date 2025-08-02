from kivy.lang import Builder
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDTextButton
from kivymd.uix.button import MDFillRoundFlatButton
Window.size = (350, 600)

kv = """

ScreenManager:
    Screen:
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
                    self.md_bg_color = self.md_bg_color = (76/255,168/255,35/255,0.9)
                    app.root.current = "login-form"
                    
       
    
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
                    app.root.current = "register-form"            
            
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
            
                    
                        
                        
        
                    
    Screen:
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
                            rgba: 241,240,240,255, 0.1    
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
                            id: email_field
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
                            rgba: 241,240,240,255, 0.1    
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
                            id: password_field
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
                        

                
                        
                        
                                
                 
    Screen:
        name:"register-form"
        
        MDFloatLayout:
        
            MDLabel:
                text:"REGISTER"
                halign:"center"
                font_style:"H4"
                pos_hint: {"center_x": 0.5, "center_y": 0.85}
            
        
                    
                    
            

            
    
        
        
"""

class LoginPage(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(kv)


if __name__ == "__main__":
    LoginPage().run()