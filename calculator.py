import PySimpleGUI as sg 

sg.ChangeLookAndFeel("BrownBlue")

# https://www.1001fonts.com/digital+clock-fonts.html


class Calculator:
    def __init__(self):
        self.bwidth = 7
        self.bheight = 2
        self.font = ('Franklin Gothic Book', 24)
        self.layout = [[sg.Text("PyDataMath II", size=(50,1), background_color="#272533", 
                        font=('Franklin Gothic Book', 14, 'bold'), justification='right')],
                       [sg.Text('0.00', size=(19,1), font=('Digital-7',46), 
                            text_color='red', justification='right', pad=(1,10), 
                            background_color='black', relief='sunken', key='_OUT_')],
                       [sg.Button("C", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='c'), 
                        sg.Button("CE", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='ce'), 
                        sg.Button("%", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='%'), 
                        sg.Button("/", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='/')],
                       [sg.Button("7", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='7'), 
                        sg.Button("8", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='8'), 
                        sg.Button("9", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='9'), 
                        sg.Button("x", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='*')],
                       [sg.Button("4", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='4'), 
                        sg.Button("5", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='5'), 
                        sg.Button("6", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='6'), 
                        sg.Button("-", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"),key='-')],
                       [sg.Button("1", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='1'), 
                        sg.Button("2", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='2'), 
                        sg.Button("3", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='3'), 
                        sg.Button("+", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='+')],
                       [sg.Button("0", size=(self.bwidth+4, self.bheight), font=self.font, button_color=("black","#F8F8F8"), key='0'), 
                        sg.Button(".", size=(self.bwidth, self.bheight), font=self.font, button_color=("black","#F1EABC"), key='.'), 
                        sg.Button("=", size=(self.bwidth+4, self.bheight), font=self.font, button_color=("black","#ECA527"), focus=True, key='=')]]

        self.window = sg.Window("PyCalc 1.0", layout=self.layout, resizable=True, size=(560, 655), background_color="#272533", element_padding=(2,2))
        self.front_end = []
        self.back_end = []
        self.x_val = 0.0
        self.y_val = 0.0
        self.operator = ''
        self.decimal = False
        self.result = 0.0

    def update_display(self):
        if not self.front_end:
            self.front_end.append('0')
        display = float(''.join(self.front_end) + '.' + ''.join(self.back_end))
        self.window.Element('_OUT_').Update(value='{:,.2f}'.format(display))

    def func(self, event):
        if self.y_val:
            self.x_val = self.result
            self.operator = event
            self.front_end = []
            self.back_end = []
            self.decimal = False
        else:
            self.x_val = ''.join(self.front_end) + '.' + ''.join(self.back_end)
            self.operator = event
            self.front_end = []
            self.back_end = []
            self.decimal = False

    def calculate(self):
        if not self.x_val:
            print("Please enter a value to perform operation.")
        else:
            self.y_val = ''.join(self.front_end) + '.' + ''.join(self.back_end)
            if float(self.y_val) == 0.0:
                self.window.Element('_OUT_').Update(value='ERROR! DIV/0')

            else:
                self.result = str(eval(self.x_val + self.operator + self.y_val))
                self.window.Element('_OUT_').Update(value='{:,.2f}'.format(float(self.result)))

def main():
    calc = Calculator()

    while True:
        event, values = calc.window.Read()
        
        if event is None:
            break
        if event in ['1','2','3','4','5','6','7','8','9','0'] and calc.decimal:
            calc.back_end.append(event)
            calc.update_display()
        if event in ['1','2','3','4','5','6','7','8','9','0'] and not calc.decimal:
            calc.front_end.append(event)
            calc.update_display()
        if event in ['*','/','-','+']:
            calc.func(event)
        if event == '=':
            calc.calculate()
        if event == '.':
            if calc.decimal:
                pass
            else:
                calc.decimal = True


main()        