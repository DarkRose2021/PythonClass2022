
import PySimpleGUI as sg

# elements
layout = [
    [sg.Text('my gui app')],
    [sg.Input(key='-INPUT-'), sg.Output(key='-OUTPUT-')],
    [sg.Multiline(size=(30, 5))]
    [sg.Button('but why')]
    [sg.Image(key='-IMAGE-')]
]

#window = sg.Window(title='simple window', layout=[[]], margins=(400, 200))
# sg.theme('Dark')

window = sg.Window('simple elements', layout)

# window.read()

while True:
    event, values = window.read()
    print(event, values)
    
    if event == 'but why':   
        window['-OUTPUT-'].update(values['-INPUT-'])
        window['-IMAGE-'].update(filename='foxpin.png')

    if event == sg.WIN_CLOSED:
        break
    

window.close()
