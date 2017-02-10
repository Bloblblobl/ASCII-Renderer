from RMap import RMap


def _assert_args(args, amax, amin=None, atypes=[]):
    if len(args) != amax:
        if amin:
            if len(args) < amin or len(args) > amax:
                return False
        else:
            return False
    # Checking for string is unnecessary if its the only type
    if atypes:
        if len(atypes) < len(args):
            return False
        for i in range(len(args)):
            try:
                args[i] = atypes[i](args[i])
            except TypeError:
                return False

    return args


def _find_component_by_name(components, name):
    component = None
    for c in components:
        if c.name == name:
            component = c
    return component


def _create_rmap(command_args, components):
    command_args = _assert_args(command_args, 4, 3, [str, int, int, str])
    if not command_args:
        print('Invalid Arguments')
        return components
    real_args = dict(name=command_args[0], bounds=dict(x=command_args[1], y=command_args[2]))
    if len(command_args) == 4:
        real_args['emptychar'] = command_args[3]

    new_rmap = RMap(**real_args)
    new_rmap.generate_map_frame()
    new_rmap.generate_border('X')
    components.append(new_rmap)
    return components


def _render_rmap(command_args, components):
    command_args = _assert_args(command_args, 1)
    if not command_args:
        print('Invalid Arguments')
        return components
    rmap = _find_component_by_name(components, command_args[0])
    if not rmap:
        print('No Component by that Name')
        return components
    rmap.render_map()
    return components


def _get_rmap_info(command_args, components):
    command_args = _assert_args(command_args, 1)
    if not command_args:
        print('Invalid Arguments')
        return components
    rmap = _find_component_by_name(components, command_args[0])
    if not rmap:
        print('No Component by that Name')
        return components
    print(rmap)
    return components


def _print_help_message(components):
    try:
        help_file = open('sandbox/help.txt')
        print(help_file.read())
    except FileNotFoundError:
        print('Help File not found')
    return components


def handle_command(command, components):
    command_list = {'create rmap': _create_rmap,
                    'render rmap': _render_rmap,
                    'get info': _get_rmap_info,
                    'help': _print_help_message}
    if '|' not in command:
        if command not in command_list.keys():
            print('Unknown Command')
            return components
        return command_list[command](components)

    command_split = command.split('|')
    if len(command_split) != 2:
        print('Invalid Command')
        return components

    command_func = command_split[0]
    command_args = command_split[1].split(',')

    if command_func not in command_list.keys():
        print('Unknown Command')
        return components

    return command_list[command_func](command_args, components)


def main():
    components = []
    while True:
        components = handle_command(input('>>>'), components)


if __name__ == '__main__':
    main()
