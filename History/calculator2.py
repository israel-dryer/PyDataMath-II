# PyDataMath-II Calculator
# A python gui calculator loosly based on the Texas Instruments DataMath-II

import PySimpleGUI as sg 

# default button values
size1 = (7, 2)
size2 = (11, 2)
btn_font = ('Franklin Gothic Book', 24)

bw = ("black","#F8F8F8") # black/white
bt = ("black","#F1EABC") # black/tan
bo = ("black","#ECA527") # black/orange

def number_btn(name, key, **args):
    btn = sg.Button(name, size=(7, 2), font=('Franklin Gothic Book', 24), 
        button_color=('black','#F8F8F8'), key=key, **args)
    return btn

def Button(name, size, color, key):
    button = sg.Button(name, size=size, button_color=color, key=key, font=btn_font)
    return button

layout = [
    [sg.Text("PyDataMath-II", size=(50,1), font=('Franklin Gothic Book', 14, 'bold'), justification='right',
        background_color="#272533", text_color='white')],
    [sg.Text("0.00", size=(18,1), font=('Digital-7',47), text_color='red', justification='right',  
        background_color='black', relief='sunken', key='_DISPLAY_')],
    [sg.Button("C", size=size1, font=btn_font, button_color=bt, key="c"),
     sg.Button("CE", size=size1, font=btn_font, button_color=bt, key="ce"),
     sg.Button("%", size=size1, font=btn_font, button_color=bt, key="%"),
     sg.Button("/", size=size1, font=btn_font, button_color=bt, key="/")],
    [sg.Button("7", size=size1, font=btn_font, button_color=bw, key="7"),
     sg.Button("8", size=size1, font=btn_font, button_color=bw, key="8"),
     sg.Button("9", size=size1, font=btn_font, button_color=bw, key="9"),
     sg.Button("x", size=size1, font=btn_font, button_color=bt, key="*")],
    [sg.Button("4", size=size1, font=btn_font, button_color=bw, key="4"),
     sg.Button("5", size=size1, font=btn_font, button_color=bw, key="5"),
     sg.Button("6", size=size1, font=btn_font, button_color=bw, key="6"),
     sg.Button("-", size=size1, font=btn_font, button_color=bt, key="-")],
    [sg.Button("1", size=size1, font=btn_font, button_color=bw, key="1"),
     sg.Button("2", size=size1, font=btn_font, button_color=bw, key="2"),
     sg.Button("3", size=size1, font=btn_font, button_color=bw, key="3"),
     sg.Button("+", size=size1, font=btn_font, button_color=bt, key="+")],
    [sg.Button("0", size=size2, font=btn_font, button_color=bw, key="0"),
     sg.Button(".", size=size1, font=btn_font, button_color=bw, key="."),
     sg.Button("=", size=size2, font=btn_font, button_color=bo, key="=", focus=True)]
]

window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(560, 660))
window.read()
    

