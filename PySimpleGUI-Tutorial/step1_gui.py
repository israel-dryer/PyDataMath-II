import PySimpleGUI as sg 

# default settings
BW = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
BT = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F1EABC")}
BO = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ECA527"), 'focus':True}

layout = [
    [sg.Text('PyDataMath-II', size=(50,1), justification='right', background_color="#272533", text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('0.0000', size=(18,1), justification='right', background_color='black', text_color='red', font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
    [sg.Button('C',**BT), sg.Button('CE',**BT), sg.Button('%',**BT), sg.Button("/",**BT)],
    [sg.Button('7',**BW), sg.Button('8',**BW), sg.Button('9',**BW), sg.Button("*",**BT)],
    [sg.Button('4',**BW), sg.Button('5',**BW), sg.Button('6',**BW), sg.Button("-",**BT)],
    [sg.Button('1',**BW), sg.Button('2',**BW), sg.Button('3',**BW), sg.Button("+",**BT)],    
    [sg.Button('0',**BW), sg.Button('.',**BW), sg.Button('=',**BO)],
]
window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(580, 660))

while True:
    event, values = window.Read()
    if event is None:
        break
    else:
        try:
            val = float(event)
            window['_DISPLAY_'].update(value=f'{val:,.4f}')
        except:
            val = event
            window['_DISPLAY_'].update(value=event)