import subprocess
from paramiko import SSHClient


class RemoteExecutionException(Exception):
    pass


class LocalExecutionException(Exception):
    pass


def execute_local_command(cmd):
    """
    Use subprocess to execute a command locally
    Checks the command's return code and raises an exception if it fails
    Waits for the process' termination
    :param cmd: the command to be executed
    :return: list of lines of the stdout
    """
    try:
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        ps.wait()
        if ps.returncode != 0:
            raise LocalExecutionException("local command execution return non-zero status code: \
cmd [{0}] - status code [{1}]".format(cmd, ps.returncode))
        return ps.stdout.readlines()
    except Exception, e:
        raise e


def execute_remote_command(cmd, host, username='autoengine', password=''):
    """
    Use paramiko to connect to a host and execute a command
    Checks the command's return code and raises an exception if it fails
    :param cmd: command to be executed
    :param host: remote hostname
    :param username: defaults to 'autoengine'
    :param password: defaults to ''
    :return:
    """
    try:
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(host, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(cmd)
        stdout_status_code = stdout.channel.recv_exit_status()
        if stdout_status_code != 0:
            raise RemoteExecutionException("remote command execution return non-zero status code: \
cmd [{0}] - status code [{1}]".format(cmd, stdout_status_code))
        return stdout.readlines()
    except Exception, e:
        raise e
