#Imports
import sys
import os
import zipfile
import wget

#Configuration
downloadpath = "./WEBSITE/update.zip" #Path or URL to a ZIPFILE (.zip)
onlineversionfile = "./WEBSITE/version.txt" #ONLINE VERSIONFILE! Path or URL to a textfile with the Versionnumber inside it.
versionfile = "./version.txt" #OFFLINE VERSIONFILE! Local File. Current installed Version.
enableupdatefile = "./enableupdate.txt" #Local File
programdirectory = "./example-program-directory/"
executeableprogramfile = "./exampleprogram/executeable.bat" #Path to the executable File which will be executed after the updater finished.

#Other variables
onlineversion = 0
currentversion = 0
eUversion = 1.0
enableupdate = 0

#Code
print("easyUPDATER " + str(eUversion) + " by jandie1505")
print("easyUPDATER is an open-source project.")
print("easyUpdater and/or jandie1505 accept no liability for any damage to the product.")
f=open(enableupdatefile, "r")
enableupdate = int(f.read())
f.close()
if enableupdate == 1:
    print("UPDATES ENABLED")
    #Step 1: Downloading the ONLINE VERSIONFILE.
    print("STEP 1...", end=" ")
    wget.download(onlineversionfile, "onlineversion.txt")
    print("COMPLETE")
    #Step 2: Read the local ONLINE VERSIONFILE
    print("STEP 2...", end=" ")
    f=open("onlineversion.txt", "r")
    onlineversion = int(f.read())
    f.close()
    print("COMPLETE")
    #Step 3: Overwrite the local ONLINE VERSIONFILE.
    print("STEP 3...", end=" ")
    f=open("onlineversion.txt", "w+")
    f.write("0")
    f.close()
    print("COMPLETE")
    #Step 4: Read the OFFLINE VERSIONFILE.
    print("STEP 4...", end=" ")
    f=open("version.txt", "r")
    currentversion = int(f.read())
    f.close()
    print("COMPLETE")
    #Step 5: Update process.
    print("STEP 5.1...", end=" ")
    if currentversion < onlineversion:
        print("COMPLETE --> Update found")
        #Download update.
        print("STEP 5.2...", end=" ")
        wget.download(downloadpath, "update.zip")
        print("COMPLETE")
        #Install update.
        print("STEP 5.3...", end=" ")
        with zipfile.ZipFile("update.zip","r") as zip_ref:
                zip_ref.extractall(programdirectory)
        print("COMPLETE")
        #Update offline versionfile.
        print("STEP 5.4...", end=" ")
        f=open(versionfile)
        f.write(onlineversion)
        print("COMPLETE")
        #Delete trashfiles
        print("STEP 5.5...", end=" ")
        os.remove("update.zip")
        print("COMPLETE")
    else:
        print("COMPLETE --> No update found")
else:
    print("UPDATES DISABLED")
#Run executeable.
print("RUNNING EXECUTEABLE...", end=" ")
os.startfile(executeableprogramfile)
print("COMPLETE")
print("EXIT")
sys.exit()