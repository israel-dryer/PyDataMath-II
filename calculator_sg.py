import PySimpleGUI as sg 

# default settings
bw = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
bt = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F1EABC")}
bo = {'size':(15,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ECA527"), 'focus':True}

layout = [
    [sg.Text('PyDataMath-II', size=(50,1), justification='right', background_color="#272533", 
        text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('0.0000', size=(18,1), justification='right', background_color='black', text_color='red', 
        font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
    [sg.Button('C',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button("/",**bt)],
    [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button("*",**bt)],
    [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("-",**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("+",**bt)],    
    [sg.Button('0',**bw), sg.Button('.',**bw), sg.Button('=',**bo, bind_return_key=True)],
]
window = sg.Window('PyDataMath-II', layout=layout, background_color="#272533", size=(580, 660), return_keyboard_events=True)

''' calculator functions '''
var = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

# helper functions
def format_number():
    ''' create a consolidated string of numbers from front and back lists '''
    return float(''.join(var['front']) + '.' + ''.join(var['back']))

def update_display(display_value):
    ''' update the calculator display after an event click '''
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

# click events
def number_click(event):
    ''' number button button click event '''
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())
    
def clear_click():
    ''' CE or C button click event '''
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False 

def operator_click(event):
    ''' + - / * button click event '''
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()

def calculate_click():
    ''' equals button click event '''
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
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
        var['result'] = 0.0
    if event in ['+','-','*','/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)