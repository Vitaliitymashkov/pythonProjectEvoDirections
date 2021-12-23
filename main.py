# This is a task 1 - for Evo

global_list_of_winds = {'N': 'N', 'NE': 'NE', 'E': 'E', 'SE': 'SE', 'S': 'S', 'SW': 'SW', 'W': 'W', 'NW': 'NW'}


def direction(facing, turn):
    validate_turn_value(turn)
    validate_direction_value(facing)

    initial_angle = direction_to_angle(facing)
    result = initial_angle + turn
    return angle_to_direction(result % 360)


def direction_to_angle(argument):
    switcher = {
        global_list_of_winds['N']: 0,
        global_list_of_winds['NE']: 45,
        global_list_of_winds['E']: 90,
        global_list_of_winds['SE']: 135,
        global_list_of_winds['S']: 180,
        global_list_of_winds['SW']: 225,
        global_list_of_winds['W']: 270,
        global_list_of_winds['NW']: 315
    }
    return switcher.get(argument, None)


def angle_to_direction(argument):
    switcher = {
        0: global_list_of_winds['N'],
        45: global_list_of_winds['NE'],
        90: global_list_of_winds['E'],
        135: global_list_of_winds['SE'],
        180: global_list_of_winds['S'],
        225: global_list_of_winds['SW'],
        270: global_list_of_winds['W'],
        315: global_list_of_winds['NW']
    }
    return switcher.get(argument, None)


def validate_turn_value(turn):
    if (turn > 1080) or (turn < -1080):
        raise AttributeError('Not valid arguments. Check if turn value is in [-1080 .. 1080]')


def validate_direction_value(facing):
    if facing not in global_list_of_winds:
        raise AttributeError(
            'Not valid arguments. Check if direction value is in the list: [{}]'.format(global_list_of_winds.keys()))


if __name__ == '__main__':
    print(direction('N', 180))
    print(direction('SE', 180))
    # print(direction('SEs', 180))
    # print(direction('SE', 10080))
