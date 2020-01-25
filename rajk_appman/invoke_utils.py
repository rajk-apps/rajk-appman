import importlib


class ServerConnection:
    def __init__(
        self,
        user: str,
        host: str,
        port: int = 22,
        remote_python_interpreter: str = "python",
    ):

        self.user = user
        self.host = host
        self.port = port
        self.python_interpreter = remote_python_interpreter

    def copy_to_server_command(
        self, local_path: str, remote_path: str, directory: bool = False
    ):

        return "scp {} -o StrictHostKeyChecking=no -P {} {} {}@{}:{}".format(
            "-r" if directory else "",
            self.port,
            local_path,
            self.user,
            self.host,
            remote_path,
        )

    def copy_from_server_command(
        self, local_path: str, remote_path: str, directory: bool = False
    ):
        return "scp {} -o StrictHostKeyChecking=no -P {} {}@{}:{} {}".format(
            "-r" if directory else "",
            self.port,
            self.user,
            self.host,
            remote_path,
            local_path,
        )

    def remote_python_command(self, command: str):

        return "ssh -p {} -o StrictHostKeyChecking=no {}@{} '{} {}'".format(
            self.port, self.user, self.host, self.python_interpreter, command
        )

    def run_sudo_command(self, command: str, sudo_password: str):

        return "echo {} | ssh -p {} -tt -o StrictHostKeyChecking=no {}@{} 'sudo {}' > /dev/null".format(
            sudo_password, self.port, self.user, self.host, command
        )

    def run_ssh_command(self, command):

        return "ssh -p {} -tt -o StrictHostKeyChecking=no {}@{} '{}'".format(
            self.port, self.user, self.host, command
        )


def inplace_modify_file(file_path, mod_function):

    with open(file_path) as fp:
        modified_dump = mod_function(fp.read())

    with open(file_path, "w") as fp:
        fp.write(modified_dump)


def use_dump_modifier_function(function_loc_str: str, local_dump_fname: str):

    module_id = ".".join(function_loc_str.split(".")[:-1])
    function_id = function_loc_str.split(".")[-1]
    loaded_module = importlib.import_module(module_id)

    modify_dump_function = getattr(loaded_module, function_id)

    inplace_modify_file(local_dump_fname, modify_dump_function)
