# PyDataMath-II Calculator
# A python gui calculator loosly based on the Texas Instruments DataMath-II
# https://www.1001fonts.com/digital+clock-fonts.html

import PySimpleGUI as sg 

''' Setup the Gui Interface '''
# button colors
bw = ("black","#F8F8F8") # black/white
bt = ("black","#F1EABC") # black/tan
bo = ("black","#ECA527") # black/orange

def Button(name, color, size=(7, 2), **kwargs):
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

''' setup the calculator functions '''
# calculator global variables
front = []
decimal = False
back = []
x_val = 0.0
y_val = 0.0
operator = ''
result = 0.0

def update_display(display_val):
    try:
        window['_DISPLAY_'].Update(value='{:,.2f}'.format(display_val))
    except:
        window['_DISPLAY_'].Update(value=display_val)

def format_number():
    return ''.join(front) + '.' + ''.join(back)    

def number_click(event):
    if decimal:
        back.append(event)
        update_display(float(format_number()))
    else:
        front.append(event)
        update_display(float(format_number()))    

def clear_click():
    global back, front, decimal
    back.clear()
    front.clear()
    decimal = False        

def operator_click(event):
    global operator, result, x_val, decimal
    operator = event
    if not front: # perform operation on prior result
        if not result: # if no prior result then return 0
            update_display(0.0)
        else: # set the value of x_val to prior result
            x_val = result            
    else: # perform new calculation
        x_val = float(format_number())
        update_display(x_val)
        clear_click()

def calculate_click():
    ''' = click, attempt to perform operation on x and y variables '''
    global x_val, y_val, operator, result 
    # check for values to operate
    if not front and not x_val and not y_val:
        return
    try: # set value of y_value
        y_val = float(format_number())
    except:
        y_val = 0.0
    try: # evaluate operation on x and y variables
        result = eval(f'{x_val}{operator}{y_val}')
        update_display(float(result))
        clear_click()
    except ZeroDivisionError:        
        update_display('ERROR! #DIV/0')
        result = 0.0
        x_val = 0.0
        clear_click()

''' main event loop '''
while True:
    event, values = window.read()
    if event is None:
        break
    if event in ['C','CE']:
        clear_click()
        result = 0.0
        update_display(0.0)
    if event in ['*','/','+','-']:
        operator_click(event)
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event == '.':
        decimal = True
    if event == '=':
        calculate_click()