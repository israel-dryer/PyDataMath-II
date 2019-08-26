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

''' calculator functions '''
# global variables
front = []
back = []
decimal = False
operator = ''
x_val = 0.0
y_val = 0.0
result = 0.0

# helper functions
def format_number():
    ''' create a consolidated string of numbers from front and back lists '''
    return float(''.join(front) + '.' + ''.join(back))

def update_display(display_value):
    ''' update the calculator display after an event click '''
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

# click events
def number_click(event):
    ''' number button button click event '''
    global front, back
    if decimal:
        back.append(event)
    else:
        front.append(event)
    update_display(format_number())
    
def clear_click():
    ''' ce or c button click event '''
    global front, back, decimal 
    front.clear()
    back.clear()
    decimal = False 

def operator_click(event):
    ''' + - / * button click event '''
    global operator, x_val
    operator = event
    try:
        x_val = format_number()
    except:
        x_val = result
    clear_click()

def calculate_click():
    ''' equals button click event '''
    global y_val, result 
    y_val = format_number()
    try:
        result = eval(str(x_val) + operator + str(y_val))
        update_display(result)
        clear_click()    
    except:
        update_display("ERROR! DIV/0")
        clear_click()

while True:
    event, values = window.read()
    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['c','ce']:
        clear_click()
        update_display(0.0)
        result = 0.0
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        decimal = True
    if event == '%':
        update_display(result / 100.0)