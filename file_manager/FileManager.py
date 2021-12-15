import os

from file_manager.commands import ls, cd, pwd, copy, move, rm


class FileManager:

    def __init__(self):
        while True:
            command = input(os.getcwd() + ">> ").strip().split()
            self.resolve_command(command)

    def resolve_command(self, command):
        if command[0] == "ls":
            ls()
        elif command[0] == "cd" and len(command) > 1:
            cd(command[1])
        elif command[0] == "pwd":
            pwd()
        elif command[0] == "copy":
            copy(command[1].strip(), command[2].strip())
        elif command[0] == "move":
            move(command[1].strip(), command[2].strip())
        elif command[0] == "rm":
            rm(command[1])


FileManager()
