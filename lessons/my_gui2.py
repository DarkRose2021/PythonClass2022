#create a gui that takes a file name and shows the image when a button is pressed

import PySimpleGUI as sg

layout = [
    [sg.Text('Enter a File Name')],
    [sg.Input(key='-INPUT-')],
    [sg.Image(key='-IMAGE-')],
    [sg.Button('Show Image')]
]

window = sg.Window('open image', layout)

while True:
    event, values = window.read()
    print(event, values)
    
    if event == 'Show Image':
        window['-IMAGE-'].update(filename=values['-INPUT-'])
    
    if event == sg.WIN_CLOSED:
        break
    
window.close()