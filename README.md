# RobocopyBackup

## What it does

It is a simple wrapper [robocopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) to copy files you choose to a backup location.

## How to use

- Download the files
- Run `RobocopyBackup.py`

## Change Paths

After you entered the paths, they will be stored in the `BackupPaths.json` file. You can always alter the paths there.

## Robocopy

You can change the way how robocopy will copy the files by altering the `copy_options` in `start_backup()`.

|**Option**|**Description**|
|---|---|
|/s|Copies subdirectories. This option automatically excludes empty directories.|
|/MIR|Mirrors a directory tree (equivalent to /e plus /purge). Using this option with the /e option and a destination directory, overwrites the destination directory security settings.|

[More Information](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
