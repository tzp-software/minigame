'''
    minigame.control.py

    most/all control logic for minigame package

    by: kyle roux
'''
#just sett ing up skeleton, i plan on splitting this up
# in future releases
from dice import Roll, Die, DieCounter
from tools import FileLocker as DieLocker 
from tools import FileLocker as ScoreLocker
from player import Player

def get_data(instruction):
    ''' send instruction to a model unit to receive data
    to send to a view

    argument:   str - an instruction

    returns:    data from model for view
    '''
    insList = ['blank list']
    if instruction in insList:
        path = instruction
    else:
        raise ValueError('need an instruction')
    # insert code to retrieve data here
    #
    #
    #
    # remove the next line when you do
    data = 'test'
    return data

def set_view(data):
    # add the code to send data to
    # the view here. 
    #
    #
    #
    return '''
    00000000000000000000
    |                  |
    |A TEST VIEW       |
    |   LOOKS GOOD     |
    | {0}              |
    00000000000000000000
    '''.format(data)


def main():
    y = Roll(6)
    y.roll()
    roll = y.return_roll()
    x = set_view(roll)
    print x

if __name__ == "__main__":
    main()


