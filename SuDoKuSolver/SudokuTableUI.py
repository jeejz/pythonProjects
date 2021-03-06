import PySimpleGUI as psg
from SuDoKuSolver import SudokuRefManipClass as refc

def draw_box():
    #SIMPLE
    #test_val={'11': '1', '12': '6', '13': '', '14': '4', '15': '', '16': '', '17': '2', '18': '7', '19': '', '21': '', '22': '', '23': '', '24': '1', '25': '7', '26': '6', '27': '', '28': '', '29': '', '31': '', '32': '', '33': '4', '34': '9', '35': '', '36': '', '37': '', '38': '', '39': '3', '41': '8', '42': '4', '43': '', '44': '5', '45': '', '46': '', '47': '3', '48': '', '49': '', '51': '', '52': '1', '53': '2', '54': '', '55': '6', '56': '', '57': '5', '58': '9', '59': '', '61': '', '62': '', '63': '5', '64': '', '65': '', '66': '3', '67': '', '68': '1', '69': '7', '71': '9', '72': '', '73': '', '74': '', '75': '', '76': '4', '77': '6', '78': '', '79': '', '81': '', '82': '', '83': '', '84': '6', '85': '2', '86': '7', '87': '', '88': '', '89': '', '91': '', '92': '2', '93': '6', '94': '', '95': '', '96': '9', '97': '', '98': '3', '99': '1'}

    #EVIL
    #test_val={'11': '7', '12': '', '13': '', '14': '', '15': '', '16': '', '17': '', '18': '8', '19': '', '21': '', '22': '', '23': '2', '24': '', '25': '', '26': '6', '27': '', '28': '4', '29': '', '31': '', '32': '', '33': '5', '34': '9', '35': '4', '36': '', '37': '', '38': '', '39': '', '41': '', '42': '', '43': '', '44': '3', '45': '', '46': '', '47': '7', '48': '1', '49': '', '51': '9', '52': '', '53': '', '54': '', '55': '1', '56': '', '57': '', '58': '', '59': '8', '61': '', '62': '1', '63': '8', '64': '', '65': '', '66': '4', '67': '', '68': '', '69': '', '71': '', '72': '', '73': '', '74': '', '75': '7', '76': '5', '77': '3', '78': '', '79': '', '81': '', '82': '7', '83': '', '84': '2', '85': '', '86': '', '87': '4', '88': '', '89': '', '91': '', '92': '2', '93': '', '94': '', '95': '', '96': '', '97': '', '98': '', '99': '6'}

    #HARD
    #test_val={'11': '', '12': '', '13': '', '14': '4', '15': '', '16': '', '17': '6', '18': '8', '19': '', '21': '9', '22': '', '23': '', '24': '7', '25': '', '26': '1', '27': '', '28': '', '29': '2', '31': '', '32': '5', '33': '', '34': '', '35': '', '36': '', '37': '', '38': '', '39': '', '41': '', '42': '', '43': '7', '44': '', '45': '4', '46': '9', '47': '', '48': '6', '49': '', '51': '6', '52': '', '53': '', '54': '', '55': '', '56': '', '57': '', '58': '', '59': '4', '61': '', '62': '4', '63': '', '64': '1', '65': '8', '66': '', '67': '9', '68': '', '69': '', '71': '', '72': '', '73': '', '74': '', '75': '', '76': '', '77': '', '78': '3', '79': '', '81': '3', '82': '', '83': '', '84': '2', '85': '', '86': '7', '87': '', '88': '', '89': '8', '91': '', '92': '1', '93': '8', '94': '', '95': '', '96': '5', '97': '', '98': '', '99': ''}z cZ

    #Medium
    test_val={'11': '', '12': '5', '13': '', '14': '', '15': '7', '16': '3', '17': '9', '18': '', '19': '1', '21': '6', '22': '7', '23': '9', '24': '', '25': '', '26': '', '27': '', '28': '', '29': '8', '31': '', '32': '', '33': '', '34': '', '35': '', '36': '', '37': '5', '38': '', '39': '', '41': '', '42': '', '43': '8', '44': '', '45': '5', '46': '', '47': '', '48': '3', '49': '', '51': '', '52': '', '53': '2', '54': '1', '55': '8', '56': '7', '57': '6', '58': '', '59': '', '61': '', '62': '6', '63': '', '64': '', '65': '4', '66': '', '67': '1', '68': '', '69': '', '71': '', '72': '', '73': '6', '74': '', '75': '', '76': '', '77': '', '78': '', '79': '', '81': '7', '82': '', '83': '', '84': '', '85': '', '86': '', '87': '4', '88': '9', '89': '6', '91': '1', '92': '', '93': '5', '94': '2', '95': '6', '96': '', '97': '', '98': '7', '99': ''}

    #test_val[keyGen]
    column = [[]]
    input1 = []
    for i in range(1,10):
        for j in range(1,10):
            keyGen = str(i)+str(j)
            input1.append(psg.InputText(default_text=test_val[keyGen], do_not_clear=True,
                                        size=(3, 3), key=keyGen, change_submits=True, justification='center'))
            if j == 3 or j == 6 :
                input1.append(psg.Text('|'))
        column.append(input1)
        input1 = []
        if i%3 == 0:
            column.append([psg.Text('_' * 50,justification='CENTER')])

    layout = [  [psg.Column(column, size=(800,800))],
              [psg.OK(), psg.Cancel() ]]

    window =  psg.Window('Submit Question',auto_size_text=True ).Layout(layout)

    prev_val = {}
    while True:
        event, value = window.Read()
        if prev_val.__len__() == 0:
            prev_val = value
        rc = refc.SudokuRefListClass()
        if event is None or event == 'Exit' or event == 'Cancel':
            break

        inp_tx = window.FindElement(event)
        is_upd_flag = False
        if not inp_tx.Get().isdigit():
            inp_tx.Update('')
        elif inp_tx.Get() == '0':
            inp_tx.Update('')
        else:
            is_upd_flag = True
            if inp_tx.Get().__len__() > 1 :
                inp_tx.Update(str(inp_tx.Get()).__getitem__(1))
            else:
                inp_tx.Update(inp_tx.Get())

        if not is_upd_flag:
            if prev_val[event] is not inp_tx.Get():
                print('prev {0} - curr {1}'.format(prev_val[event], inp_tx.Get()))
                is_upd_flag = True

        value[event] = inp_tx.Get()
        print("value: ", value)

        if is_upd_flag:
            rc.update_sudoku_with_event_value(event, value)
        prev_val = value

draw_box()