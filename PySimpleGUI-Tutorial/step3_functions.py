# PyDataMath-II Calculator
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
    [sg.Text("PyDataMath-II", size=(50,1), font=('Franklin Gothic Book', 14, 'bold'), justification='right', background_color="#272533", text_color='white')],
    [sg.Text("0.0000", size=(18,1), font=('Digital-7',47), text_color='red', justification='right', background_color='black', relief='sunken', key='_DISPLAY_')],
    [Button("C", BT), Button("CE", BT), Button("%", BT), Button("/", BT)],
    [Button("7", BW), Button("8", BW), Button("9", BW), Button("*", BT)],
    [Button("4", BW), Button("5", BW), Button("6", BW), Button("-", BT)],
    [Button("1", BW), Button("2", BW), Button("3", BW), Button("+", BT)],
    [Button("0", BW), Button(".", BW), Button("=", BO, size=(15,2), focus=True)]
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
def update_display(display_value):
    ''' update the calc display with number click events, update with results, and update with error messages '''
    try: # to display float number
        window['_DISPLAY_'].Update(value='{:,.4f}'.format(display_value))
    except: # to display error message
        window['_DISPLAY_'].Update(value=display_value)

def format_number():
    ''' create a consolidated string of numbers from front and back number lists '''
    return ''.join(front) + '.' + ''.join(back)

# click events
def number_click(event):
    ''' add digit to front or back list when clicked '''
    global front, back
    if decimal:
        back.append(event)
    else:
        front.append(event)

    display_value = float(format_number())
    update_display(display_value)

def clear_click():
    ''' clear contents of front and back list, reset display, and reset decimal flag '''
    global front, back, decimal
    front.clear()
    back.clear()
    decimal = False

def operator_click(event):
    ''' set the operator based on the event button, this may also trigger a calculation in the event
        that the result is used in a subsequent operation '''
    global operator, x_val
    operator = event
    x_val = float(format_number())
    clear_click()

def calculate_click():
    ''' attempt to perform operation on x and y variables if exist '''
    global y_val, result
    y_val = float(format_number())
    result = float(eval(str(x_val) + operator + str(y_val)))
    update_display(result)
    clear_click()

''' main event loop '''
while True:
    event, values = window.read()
    if event is None:
        break
    if event in ['CE','C']:
        clear_click()
        update_display(0.0)
        result = 0.0
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['*','/','+','-']:
        operator_click(event)
    if event == '.':
        decimal = True 
    if event == '%':
        update_display(result / 100.0)        
    if event == '=':
        calculate_click()
