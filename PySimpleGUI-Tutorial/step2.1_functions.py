import PySimpleGUI as sg 

# button colors
BW = ("black","#F8F8F8") # black/white
BT = ("black","#F1EABC") # black/tan
BO = ("black","#ECA527") # black/orange

def Button(name, color, size=(7, 2), **kwargs):
    ''' return an sg button with default parameters '''    
    button = sg.Button(name, size=size, button_color=color, font=('Franklin Gothic Book', 24), **kwargs)
    return button

layout = [
    [sg.Text('PyDataMath-II', size=(50,1), justification='right', background_color="#272533", text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('0.0000', size=(18,1), justification='right', background_color='black', text_color='red', font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
    [Button('C',BT), Button('CE',BT), Button('%',BT), Button("/",BT)],
    [Button('7',BW), Button('8',BW), Button('9',BW), Button("*",BT)],
    [Button('4',BW), Button('5',BW), Button('6',BW), Button("-",BT)],
    [Button('1',BW), Button('2',BW), Button('3',BW), Button("+",BT)],    
    [Button('0',BW), Button('.',BW), Button('=',BO, size=(15,2), focus=True)],
]
window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(580, 660))

while True:
    event, values = window.Read()
    if event is None:
        break
    else:
        print(event, values)