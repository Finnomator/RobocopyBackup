from pathlib import Path
import os

thispath = os.path.dirname(os.path.realpath(__file__))+"\\"

def storepaths():
    if not "backupandsavepaths.txt" in os.listdir(thispath):
        while True:
            pathstoadd = input("Enter the paths you want to backup, you can enter multiple paths and seperate them with a semicolon: ")
            allvalid = True

            try:
                pathstoaddlist = pathstoadd.split(";")
            except:
                pass

            for paths in pathstoaddlist:
                if not (os.path.isdir(paths) or os.path.isfile(paths)):
                    print(paths+" is not a directory or file, make sure you enter the full path")
                    allvalid = False
                    break

            if allvalid:
                break

        while True:
            destination = input("Enter destination path: ")
            if not os.path.isdir:
                print(destination+" is not a valid destination path")
            else:
                break

        pathfile = open(thispath+"backupandsavepaths.txt","w")
        pathfile.write(pathstoadd+"\n"+destination)
        pathfile.close()

    else:
        pathfile = open(thispath+"backupandsavepaths.txt","r")
        lines = pathfile.readlines()
        pathstoadd = lines[0].replace("\n","").split(";")
        destination = lines[1].replace("\n","")
        pathfile.close()

    return pathstoaddlist,destination

def backup(pathstobackup:list,backupdestination:str,backupoptions = "/s /MIR /v /eta"):
    
    copycommand = ["wt "]

    for i in range(0,len(pathstobackup)):
        if os.path.isdir(pathstobackup[i]):
            copycommand.append('--title SD="'+str(pathstobackup[i])+'DD='+backupdestination+'" robocopy "'+str(pathstobackup[i])+'" "'+backupdestination+str(pathstobackup[i].replace(str(Path(pathstobackup[i]).parent.absolute()),''))+'" '+backupoptions+';')
        else:
            filename = str(pathstobackup[i]).rsplit("\\",1)[1]
            pathstobackup[i] = pathstobackup[i].split("\\"+filename)[0]
            copycommand.append('--title SD="'+str(pathstobackup[i])+'DD='+backupdestination+'" robocopy "'+str(pathstobackup[i])+'" "'+backupdestination+'" "'+filename+'" /v /eta;')
    copycommand[len(copycommand)-1] = copycommand[len(copycommand)-1].replace(";","")
    copycommand = str(copycommand).replace("', '","").replace("[","").replace("]","").replace("'","")
    os.popen(copycommand)

if __name__ == "__main__":
    PathstocopytoBackup, destination = storepaths()
    backup(PathstocopytoBackup,destination)
