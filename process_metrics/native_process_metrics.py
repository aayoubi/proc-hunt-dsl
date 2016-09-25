from process_utils import execute_local_command, execute_remote_command

class CPU:
    def __init__(self):
        pass

    def get(self, host, pid):
        command = 'ps -p {0} -otime'.format(pid)
        output = execute_local_command(command) if host == 'localhost' else execute_remote_command(command, host)
        return output[-1].strip()

    def __repr__(self):
        return "cumulative CPU time, '[DD-]HH:MM:SS' format."


class PMAP:
    def __init__(self):
        pass

    def get(self, host, pid):
        command = 'pmap -x {0}'.format(pid)
        output = execute_local_command(command) if host == 'localhost' else execute_remote_command(command, host)
        return output[-1].strip()

    def __repr__(self):
        return "Memory map of a process"


class RSS:
    def __init__(self):
        pass

    def __repr__(self):
        return "resident set size, the non-swapped physical memory that a task has used in KiB"


class VSZ:
    def __init__(self):
        pass

    def __repr__(self):
        return "virtual memory size of the process in KiB"

