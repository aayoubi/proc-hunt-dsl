class CPU:
    def __init__(self):
        pass

    def get(self):
        import paramiko

        return os.times()

    def __repr__(self):
        return "cumulative CPU time, '[DD-]HH:MM:SS' format."


class PMAP:
    def __init__(self):
        pass

    def get(self):
        return 0

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

