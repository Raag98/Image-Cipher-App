import PySimpleGUI as sg


encode_layout = [[sg.Text('Enter Text to hide:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Multiline(size=(45,5), k='-MLINE-')],
          [sg.Text("Enter a password")],
          [sg.Input(key='-IN-')],
          [sg.Button('Encode'), sg.ProgressBar(1000, orientation='h', size=(20, 20), key='-PROGRESS BAR-')]]

decode_layout = [[sg.Text("Enter a password")],
          [sg.Input(key='-IN-')],
          [sg.Button('Decode'), sg.ProgressBar(1000, orientation='h', size=(20, 20), key='-PROGRESS BAR-')],
          ]

if_layout = [[sg.Text("Input image file")],
            [sg.Button("Open File")]]

if_layout +=[[sg.TabGroup([[sg.Tab('ENCODE', encode_layout),
                               sg.Tab('DECODE', decode_layout)]], key='-TAB GROUP-')]]



window = sg.Window('Steganography Software', if_layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == "Open File":
        print("[LOG] Clicked Open File!")
        folder_or_file = sg.popup_get_file('Choose your file')
        sg.popup("You chose: " + str(folder_or_file))
        print("[LOG] User chose file: " + str(folder_or_file))

window.close()