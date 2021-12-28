# This is a task 1 - for Evo

global_list_of_winds_dict = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315}


def direction(facing, turn):
    validate_turn_value(turn)
    validate_direction_value(facing)

    result = (direction_to_angle_with_dict(facing) + turn) % 360
    return angle_to_direction_with_dict(result)


def direction_to_angle_with_dict(argument):
    return global_list_of_winds_dict.get(argument, None)


def angle_to_direction_with_dict(argument):
    result = {k: v for k, v in global_list_of_winds_dict.items() if v == argument}
    return result


def validate_turn_value(turn):
    if (turn > 1080) or (turn < -1080):
        raise AttributeError('Not valid arguments. Check if turn value is in [-1080 .. 1080]')


def validate_direction_value(facing):
    if facing not in global_list_of_winds_dict:
        raise AttributeError(
            'Not valid arguments. Check if direction value is in the list: [{}]'.format(global_list_of_winds_dict.keys()))


if __name__ == '__main__':
    print(direction('N', 180))
    print(direction('N', 90))
    print(direction('SE', 180))
    # print(direction('SEs', 180))
    # print(direction('SE', 10080))
