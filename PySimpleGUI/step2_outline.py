# PyDataMath-II Calculator
import PySimpleGUI as sg 

# button colors
BW = ("black","#F8F8F8") # black/white
BT = ("black","#F1EABC") # black/tan
BO = ("black","#ECA527") # black/orange

def Button(name, color, size=(7, 2), **kwargs):
    ''' return an sg button with default parameters along with any changes
        passed as optional keyword arguments '''    
    button = sg.Button(name, size=size, button_color=color, font=('Franklin Gothic Book', 24), **kwargs)
    return button

layout = [
    [sg.Text("PyDataMath-II", size=(50,1), font=('Franklin Gothic Book', 14, 'bold'), justification='right', background_color="#272533", text_color='white')],
    [sg.Text("0.0000", size=(18,1), font=('Digital-7',47), text_color='red', justification='right', background_color='black', relief='sunken', key='_DISPLAY_')],
    [Button("C", BT), Button("CE", BT), Button("%", BT), Button("/", BT)],
    [Button("7", BW), Button("8", BW), Button("9", BW), Button("*", BT)],
    [Button("4", BW), Button("5", BW), Button("6", BW), Button("-", BT)],
    [Button("1", BW), Button("2", BW), Button("3", BW), Button("+", BT)],
    [Button("0", BW, size=(11,2)), Button(".", BW), Button("=", BO, size=(11,2), focus=True)]
]

window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(580, 660))

''' calculator functions '''
# global variables
# design pattern :: 1,234.57 --> [front] . [back]
front = [] 
back = []
decimal = False
x_val = 0.0
y_val = 0.0
result = 0.0
operator = ''

# helper functions
def update_display():
    ''' update the calc display with number click events, update with results, and update with error messages '''
    pass

def format_number():
    ''' create a consolidated string of numbers from front and back number lists '''
    pass
    
# click events
def number_click():
    ''' add digit to front or back list when clicked '''
    pass

def clear_click():
    ''' clear contents of front and back list, reset display, and reset decimal flag '''
    pass

def operator_click():
    ''' set the operator based on the event button, this may also trigger a calculation in the event
        that the result is used in a subsequent operation '''
    pass

def calculate_click():
    ''' attempt to perform operation on x and y variables if exist '''
    pass

''' main event loop '''
while True:
    event, values = window.read()
    if event is None:
        break