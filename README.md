# RobocopyBackup

# What it does
It is a simple program that uses [robocopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) to copy files you choose to the backup destination

# Requirements
- [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701#activetab=pivot:overviewtab)
- [Python](https://www.python.org/downloads/)

# How to use
- Download the files
- Double click ```Backup.bat``` and follow the instructions

## Note
- After entering Source files and destination it will store the paths in a text file. The file has to be in the same location as ```autobackup.py```, otherwise it will ask for paths again
- You can edit the text file or just delete it to change source or destination
- ```autobackup.py``` should be in a location without any whitespaces in its path

## Autobackup on Startup
Create a shortcut to ```Backup.bat``` and place it into ```C:\Users\<UserName>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```.
This will run ```Backup.bat``` everytime you start your computer

## Robocopy
You can change how robocopy copys the files by changing ```backupoptions``` in ```autobackup.py``` in line ```46```. By default it is set to "/s /MIR /v /eta".

|**Option**|**Description**|
|---|---|
|/s|Copies subdirectories. This option automatically excludes empty directories.|
|/MIR|Mirrors a directory tree (equivalent to /e plus /purge). Using this option with the /e option and a destination directory, overwrites the destination directory security settings.|
|/v|Produces verbose output, and shows all skipped files.|
|/eta|Shows the estimated time of arrival (ETA) of the copied files.|

[More Information](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
