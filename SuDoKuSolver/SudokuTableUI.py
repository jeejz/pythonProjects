import PySimpleGUI as psg
from SuDoKuSolver import SudokuRefManipClass as refc

def draw_box(rc):
    column = [[]]
    input1 = []
    for i in range(1,10):
        for j in range(1,10):
            key = str(i)+str(j)
            input1.append(psg.InputText(default_text='',do_not_clear=True,
                                        size=(3, 3), key=(key),change_submits=True,justification='center'))
            if j%3 == 0 :
                input1.append(psg.VerticalSeparator())
        column.append(input1)
        input1 = []
        if i%3 == 0:
            column.append([psg.Text('_' * 50,justification='CENTER')])

    layout = [  [psg.Column(column, size=(800,800))],
              [psg.OK(), psg.Cancel() ]]

    window =  psg.Window('Submit Question',auto_size_text=True ).Layout(layout)

    while True:
        event, value = window.Read()
        print(event, value)
        if event is None or event == 'Exit' or event == 'Cancel':
            break
        if not value[event].isdigit():
            pass
        if len(value[event]) > 1 and value[event].isdigit():
            x = value[event]
            inpTx = window.FindElement(event)
            print('x = ',x, ' ---',x.__getitem__(1))
            inpTx.Update('{}'.format(x.__getitem__(1)))
            window.Refresh()
        if value[event].isdigit() and 1 <= int(value[event]) <=9:
            rc.apply_value_at_position(value[event], event)
            print(rc)
        print(" length of event : " ,value[event] , " = " , len(value[event]))

rclass = refc.SudokuRefListClass()
draw_box(rclass)