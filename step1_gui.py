# PyDataMath-II Calculator
import PySimpleGUI as sg 

# button colors
bw = ("black","#F8F8F8") # black/white
bt = ("black","#F1EABC") # black/tan
bo = ("black","#ECA527") # black/orange

def Button(name, color, size=(7, 2), **kwargs):
    ''' return an sg button with default parameters along with any changes
        passed as optional keyword arguments '''    
    button = sg.Button(name, size=size, button_color=color, font=('Franklin Gothic Book', 24), **kwargs)
    return button

layout = [
    [sg.Text("PyDataMath-II", size=(50,1), font=('Franklin Gothic Book', 14, 'bold'), justification='right', background_color="#272533", text_color='white')],
    [sg.Text("0.00", size=(18,1), font=('Digital-7',47), text_color='red', justification='right', background_color='black', relief='sunken', key='_DISPLAY_')],
    [Button("C", bt), Button("CE", bt), Button("%", bt), Button("/", bt)],
    [Button("7", bw), Button("8", bw), Button("9", bw), Button("*", bt)],
    [Button("4", bw), Button("5", bw), Button("6", bw), Button("-", bt)],
    [Button("1", bw), Button("2", bw), Button("3", bw), Button("+", bt)],
    [Button("0", bw, size=(11,2)), Button(".", bw), Button("=", bo, size=(11,2), focus=True)]
]

window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(580, 660))

''' main event loop '''
while True:
    event, values = window.read()
    if event is None:
        break