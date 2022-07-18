#Katie King 2022
import scrape
import PySimpleGUI as sg

layout = [
    [sg.Text('Explore The Events at Neumont')],
    [sg.Button('Get Events')], [sg.Button('Save Events')],
    [sg.Multiline(key='-MULTILINE-', size=(55,5))]
]

sg.theme('DarkTeal1')

window = sg.Window('Events At Neumont', layout)

while True:
    event, values = window.read() 
    print(event, values)
    
    if event == 'Get Events':
        scrape.scrape()
        window['-MULTILINE-'].update(scrape.scrape())
    elif event == 'Save Events':
        scrape.saveEvents()
    elif event == sg.WIN_CLOSED:
        break
    
window.close()
