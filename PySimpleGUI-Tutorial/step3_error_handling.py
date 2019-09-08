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
    if event in ['C','CE']:
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