try:
    input = raw_input # Ensures Python 2 & 3 capatibility
except NameError:
    pass


class TinyMenu(object):
    def __init__(self):
        self._commands = set()
        self.prompt = ''

        self.interrupt_handler = None # ()
        self.unknown_command_handler = None # (cmd [str], *args)
        self.invalid_args_handler = None # (cmd [Command], *args)

    def add_command(self, command):
        self._commands.add(command)

    def remove_command(self, command):
        self._commands.remove(command)

    def run(self):
        self._input_loop()

    def _input_loop(self):
        while True:
            try:
                cmd_parts = input(self.prompt).strip().split()
            except KeyboardInterrupt:
                if self.interrupt_handler is not None:
                    self.interrupt_handler()
                return

            self._handle_input(cmd_parts)

    def _handle_input(self, cmd_parts):
        if len(cmd_parts) < 1:
            return

        cmd = cmd_parts[0]
        cmd_args = cmd_parts[1:]

        for reg_cmd in self._commands:
            if reg_cmd.command == cmd:
                if (reg_cmd.arg_limit is not None and
                   len(cmd_args) not in reg_cmd.arg_limit):
                   # If invalid amount of arguments passed
                    if self.invalid_args_handler is not None:
                        self.invalid_args_handler(reg_cmd, *cmd_args)
                else:
                    # If the command and its args are valid
                    reg_cmd.handler(reg_cmd, *cmd_args)
                return

        if self.unknown_command_handler is not None:
            self.unknown_command_handler(cmd, *cmd_args)


class Command(object):
    def __init__(self, cmd_name, cmd_handler):
        self.command = cmd_name
        self.handler = cmd_handler # (cmd [Command], *args)
        self.arg_limit = None

    def __eq__(self, other):
        return self.command ==  other.command

    def __hash__(self):
        return hash(self.command)
