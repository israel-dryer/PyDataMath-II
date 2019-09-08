# PyDataMath-II Calculator
import tkinter as tk

# button colors
WHITE = "#F8F8F8" # black/white
TAN = "#F1EABC" # black/tan

root = tk.Tk()
root.title('PyDataMath-II')
root.config(bg='#272533')

display_text = tk.StringVar()
display_text.set('0.0000')

canvas = tk.Canvas(root, bg='#272533', bd=0, highlightthickness=0)
canvas.pack(padx=15, pady=15)

def std_btn(text, bg, row, col, width=7, height=2, font=('Franklin Gothic Book', 24)):
    btn = tk.Button(canvas, text=text, bg=bg, width=width, height=height, font=font, command=lambda: event_click(text))
    return btn.grid(row=row, column=col, padx=4, pady=4)

tk.Label(canvas, text='PyDataMath-II', anchor='e', bg='#272533', fg='white', font=('Franklin Gothic Book', 14, 'bold')).grid(row=0, columnspan=4, sticky='ew', padx=4, pady=2)
tk.Label(canvas, textvariable=display_text, anchor='e', bg='black', fg='red', relief=tk.SUNKEN, font=('Digital-7',47)).grid(row=1, columnspan=4, sticky='ew', padx=4, pady=2)
std_btn("C", TAN, 2, 0),   std_btn("CE", TAN, 2, 1),  std_btn("%", TAN, 2, 2),   std_btn("/", TAN, 2, 3)
std_btn("7", WHITE, 3, 0), std_btn("8", WHITE, 3, 1), std_btn("9", WHITE, 3, 2), std_btn("*", TAN, 3, 3)
std_btn("4", WHITE, 4, 0), std_btn("5", WHITE, 4, 1), std_btn("6", WHITE, 4, 2), std_btn("-", TAN, 4, 3)
std_btn("1", WHITE, 5, 0), std_btn("2", WHITE, 5, 1), std_btn("3", WHITE, 5, 2), std_btn("+", TAN, 5, 3)
std_btn("0", WHITE, 6, 0), std_btn(".", WHITE, 6, 1)

rtn_btn = tk.Button(canvas, text='=', bg='#ECA527', width=15, height=2, font=('Franklin Gothic Book', 24), command=lambda: event_click("="))
rtn_btn.focus()
rtn_btn.grid(row=6, column=2, columnspan=2, padx=4, pady=4)

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

def event_click(event):
    global operator, decimal, result
    if event in ['CE','C']:
        clear_click()
        update_display(0.0)
        operator = ''
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

# helper functions
def update_display(display_value):
    global display_text
    ''' update the calc display with number click events, update with results, and update with error messages '''
    try: # to display float number
        display_text.set('{:,.4f}'.format(display_value))
    except: # to display error message
        display_text.set(display_value)

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
    try: # if no x_val exists, use prior result
        x_val = float(format_number())
    except:
        x_val = result
    clear_click()

def calculate_click():
    ''' attempt to perform operation on x and y variables if exist '''
    global x_val, y_val, result

    # check for x value
    if not x_val:
        return 
    try: # check for y value
        y_val = float(format_number())
    except:
        y_val = 0.0
    try: # check for division by zero
        result = float(eval(str(x_val) + operator + str(y_val)))
        update_display(result)
    except ZeroDivisionError:
        error = "ERROR! DIV/0"
        x_val = 0.0
        clear_click()
        update_display(error)

    clear_click()

root.mainloop()

''' ERROR Handling
    - division by zero errors (calculate_click)
    - click = without having a y value (calculate_click)
    - click = without having any values to operate on (calculate_click)

    OTHER Features
    - perform calculation on prior result (operator_click)

'''