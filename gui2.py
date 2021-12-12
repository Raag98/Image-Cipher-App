import PySimpleGUI as sg
import enc_dec

encode_layout = [[sg.Text("Enter PlainText: "), sg.Text(size=(15,1))],
          [sg.Multiline(size=(45,5), k='PlainText')],
          [sg.Text("Enter Password: "), sg.Input(size=(25,1), key='PasswordEncode')],
          [sg.Text("Enter Output Filename(with extension): "), sg.Input(size=(25,1), key='OutputFile')],
          [sg.Button('Encode')]]

decode_layout = [[sg.Text("Enter Password: "), sg.Input(size=(25,1), key='PasswordDecode')],
          [sg.Button('Decode')]]

if_layout = [[sg.Text("Input Image File: "), sg.Button("Open File")]]

if_layout += [[sg.TabGroup([[sg.Tab('Encode Tab', encode_layout), sg.Tab('Decode Tab', decode_layout)]], key='Tab Group')]]

window = sg.Window('Steganography Software', if_layout)


file = None
while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Open File":
        file = sg.popup_get_file('Choose Image: ')
        # print("[LOG] File: " + str(file))
    elif event == "Encode":
        if file is None:
            sg.popup("Please choose an image file!")
            continue
        elif values['PlainText'] == '':
            sg.popup("Please enter Plaintext!")
            continue
        elif values['PasswordEncode'] == '':
            sg.popup("Please enter Password!")
            continue
        elif values['OutputFile'] == '':
            sg.popup("Please enter Output filename!")
            continue
        # Encode Process
        try:
            enc_dec.encode(file, values['PlainText'], values['OutputFile'], values['PasswordEncode'])
            sg.popup("Encode Success!")
        except:
            sg.popup("Encode Failed!")
            pass
    elif event == "Decode":
        if file is None:
            sg.popup("Please choose an image file!")
            continue
        elif values['PasswordDecode'] == '':
            sg.popup("Please enter Password!")
            continue
        # Decode Process
        try:
            res = enc_dec.decode(file, values['PasswordDecode'])
            sg.popup("Decode Success!\nDecoded Plaintext: " + res)
        except:
            sg.popup("Decode Failed!")
            pass

window.close()