import subprocess
from pathlib import Path

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory

history_file = ".stacker_sh_history"
history_file_path = Path.home() / history_file


# List of allowed commands
ALLOWED_COMMANDS = [
    'ls', 'll', 'l', 'pwd', 'echo', 'cd', 'mkdir', 'rmdir',
    'touch', 'rm', 'cp', 'mv', 'cat', 'head',
    'tail', 'less', 'grep', 'find', 'df', 'du',
    'ps', 'top', 'htop', 'uname', 'uptime', 'free',
    'who', 'id', 'chmod', 'chown', 'man', 'ping',
    'traceroute', 'nslookup', 'dig', 'curl', 'wget',
    'history', 'clear', 'date', 'cal', 'kill',
    'ssh', 'scp', 'git', 'tar', 'ifconfig', 'ip', 'nmap'
]

STACKERSH_SH_COMMAND = [
    'exit',
    'delete_history'
]


def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
    except Exception as e:
        return str(e)


def delete_history():
    if history_file_path.exists():
        history_file_path.unlink()


def shell_mode():
    print("Entering shell mode. Type 'exit' to return to normal mode.")
    completer = WordCompleter(ALLOWED_COMMANDS + STACKERSH_SH_COMMAND)
    while True:
        command = prompt(
            "stacker(sh) > ",
            completer=completer,
            history=FileHistory(history_file_path)
        )
        if command.lower() == "exit":
            break
        if command.lower() == "delete_history":
            delete_history()
            continue
        if len(command) > 0:
            command_name = command.split()[0]
            if command_name in ALLOWED_COMMANDS:
                print(run_shell_command(command))
            else:
                print(f"Error: '{command_name}' is not allowed.")
    print("Exiting shell mode.")


def setup(stacker_core):
    stacker_core.register_plugin("sh", shell_mode)
