import PySimpleGUI as psg
from SuDoKuSolver import SudokuRefManipClass as refc

def draw_box(rc):
    column = [[]]
    input1 = []
    for i in range(1,10):
        for j in range(1,10):
            keyGen = str(i)+str(j)
            input1.append(psg.InputText(default_text='', do_not_clear=True,
                                        size=(3, 3), key=keyGen, change_submits=True, justification='center'))
            if j%3 == 0 :
                input1.append(psg.Text('|'))
        column.append(input1)
        input1 = []
        if i%3 == 0:
            column.append([psg.Text('_' * 50,justification='CENTER')])

    layout = [  [psg.Column(column, size=(800,800))],
              [psg.OK(), psg.Cancel() ]]

    window =  psg.Window('Submit Question',auto_size_text=True ).Layout(layout)

    prev_value = {}
    oldrefmatrix = rc.allPossList
    while True:
        oldval = ''
        event, value = window.Read()
        print("event: ", event)

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

        value[event] = inp_tx.Get()
        print("value: ", value)

        if is_upd_flag:
            #rc.apply_value_at_position(value[event], event)
            # compare and identify the old value
            rc.replace_old_value(value[event], oldval, oldrefmatrix)
            oldrefmatrix = rc.allPossList
            rc.update_sudoku_with_event_value(event, value)
            prev_value = value
        #print(" length of event : " ,value[event] , " = " , len(value[event]))


rclass = refc.SudokuRefListClass()
draw_box(rclass)