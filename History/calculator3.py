# PyDataMath-II Calculator
# A python gui calculator loosly based on the Texas Instruments DataMath-II
# https://www.1001fonts.com/digital+clock-fonts.html

import PySimpleGUI as sg 


'''
Development Notes
- add result to new x_val if another operation is started
- if first button pressed is an operation, then x_val is 0 and y_val is the next numbers entered
- the x and y values should be erased after an operation is performed since result will still exist

'''

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
# calculator variables
front = []
decimal = False
back = []
x_val = 0.0
y_val = 0.0
operator = ''
result = 0.0

def format_number():
    return ''.join(front) + '.' + ''.join(back)    

def calc_func(event):
    global front, decimal, back, x_val, y_val, operator, result
    if not x_val:
        front.append('0')
        x_val = result
    # new operation
    if not y_val:
        x_val = format_number()
    # operation on existing result
    else:
        x_val = result
    # reset gloval variables
    operator = event
    front.clear()
    back.clear()
    decimal = False        

def update_display(display_val):
    global window
    #if not front:
    #    front.append('0')
    try:
        window['_DISPLAY_'].Update(value='{:,.2f}'.format(display_val))
    except:
        window['_DISPLAY_'].Update(value=display_val)

def calculate():
    global result
    if not x_val:
        print("Please enter a value to perform operation.")
    else:
        y_val = format_number()
        if float(y_val) == 0.0:
            update_display('ERROR! DIV/0')
        else:
            result = str(eval(x_val + operator + y_val))
            update_display(float(result))

while True:
    event, values = window.read()
    
    if event is None:
        break
    if event in ['1','2','3','4','5','6','7','8','9','0']: 
        if decimal:
            back.append(event)
            update_display(float(format_number()))
            print(format_number)
        else:
            front.append(event)
            update_display(float(format_number()))
            print(format_number())
    if event in ['*','/','-','+']:
        calc_func(event)
    if event == '=':
        calculate()
        x_val = 0
        y_val = 0
        front.clear()
        back.clear()
    if event == 'CE':
        if back:
            back.clear()
            update_display(0.0)
        else:
            front.clear()
            operator = ''
            update_display(0.0)
    if event == 'C':
        back.clear()
        front.clear()
        operator = ''
        x_val = 0.0
        y_val = 0.0
        update_display(0.0)
    if event == '.':
        if decimal:
            pass
        else:
            decimal = True    



