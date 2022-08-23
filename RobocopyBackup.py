from genericpath import isfile
import os
import json
from pathlib import Path
import subprocess
import sys


class Backupper:
    def __init__(self) -> None:
        self.paths_file = "BackupPaths.json"

        self.backup_paths = self.read_backup_paths()
        self.paths_to_backup = self.backup_paths["Paths to Backup"]
        self.destination_path = self.backup_paths["Destination Path"]

        changed = False

        if not self.paths_to_backup:
            self.paths_to_backup = self.request_paths_to_backup()
            changed = True

        if self.destination_path == "":
            self.destination_path = self.request_destination_path()
            changed = True

        if changed:
            self.update_paths()
            self.write_backup_paths()
        else:
            self.validate_paths()

    def start_backup(self, copy_options="/s /MIR"):
        self.validate_paths()

        for path_to_backup in self.paths_to_backup:
            path = Path(path_to_backup)
            name = path.name
            dest_path = f"{self.destination_path}/{name}"

            if os.path.isfile(path_to_backup):
                command = f'robocopy "{Path(path_to_backup).parent.absolute()}" "{self.destination_path}" "{name}"'
            else:
                if not os.path.isdir(dest_path):
                    os.mkdir(dest_path)
                command = f'robocopy "{path_to_backup}" "{dest_path}" {copy_options}'

            process = subprocess.Popen(command, stdout=subprocess.PIPE)
            for line in iter(process.stdout.readline, b""):
                sys.stdout.buffer.write(line)

    def update_paths(self):
        self.backup_paths["Paths to Backup"] = self.paths_to_backup
        self.backup_paths["Destination Path"] = self.destination_path

    def validate_paths(self):
        res = True
        if not os.path.isdir(self.destination_path):
            print(
                f'The directory "{self.destination_path}" was not found, please reenter the path'
            )
            self.destination_path = self.request_destination_path()
            self.update_paths()
            res = False

        for i, path in enumerate(self.paths_to_backup):
            if (not os.path.isfile(path)) and (not os.path.isdir(path)):
                print(f'The path "{path}" was not found, please reenter the path')
                self.paths_to_backup[i] = self.request_path_to_backup()
                self.update_paths()
                res = False

        if not res:
            self.write_backup_paths()

        return res

    def read_backup_paths(self):
        with open(self.paths_file, "r") as f:
            return json.load(f)

    def write_backup_paths(self):
        with open(self.paths_file, "w") as f:
            json.dump(self.backup_paths, f, indent=4)

    def request_path_to_backup(self):
        while True:
            inp_bkp_path = input("Please enter a path to backup: ")

            if (
                os.path.isfile(inp_bkp_path)
                or os.path.isdir(inp_bkp_path)
                or inp_bkp_path == "END"
            ):
                return inp_bkp_path

            print(f'"{inp_bkp_path}" is not a directory or file')

    def request_paths_to_backup(self):
        print("Enter 'END' when you are done entering the paths")
        paths_to_backup = []
        while True:

            inp = self.request_path_to_backup()

            if inp == "END":
                return paths_to_backup

            paths_to_backup.append(inp)
            print(f'Added "{inp}" succesfully')

    def request_destination_path(self):
        while True:
            inp_dest_path = input("Please enter the destination path: ")

            if os.path.isdir(inp_dest_path):
                return inp_dest_path

            print(f'"{inp_dest_path}" is not a directory')


if __name__ == "__main__":
    b = Backupper()
    b.start_backup()
