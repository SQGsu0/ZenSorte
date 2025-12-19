#---------------------------------------------------------------------------------------------------------------------| Importing Modul :
import shutil
import os
import sys
#---------------------------------------------------------------------------------------------------------------------| Values  :
Pat_Src = ""
Dire_List = {
    "Totals" : 0, #Total All Patch
    "Files": {
        "All-Files" : [] #Files list
    },
    "Directories":[], #Directorys list
    "Other_File":[] #Others list
}#Status Full Patch
#---------------------------------------------------------------------------------------------------------------------| Functions All :y
#----------------------------------------------------------| File&Moving
def fi_mv():
        global Dire_List, Pat_Src
        for Type in Dire_List["Files"]:
            Pat_Scf = os.path.join(Pat_Src, f"┣━ {Type}")
            os.makedirs(Pat_Scf, exist_ok=True)
            if os.path.exists(Pat_Scf):
                for Types in Dire_List["Files"][Type]:
                    try:
                        #print(Types)
                        shutil.move(os.path.join(Pat_Src, Types), os.path.join(Pat_Scf, Types))
                    except Exception as e:
                        print(f"Error Moving {os.path.join(Pat_Src, Types)} to {os.path.join(Pat_Scf, Types)} => {e}")
#----------------------------------------------------------| Filter&Type&File
def fil_ty_fi():
    global Dire_List , Pat_Src
    List = Dire_List["Files"]
    for File in Dire_List["Files"]["All-Files"]:
        for Index in range(-1, len(str(File)) * -1 + 1, -1):
            if File[Index] == '.':
                Name = File[Index + 1 :]
                if Name in List:
                    List[Name] = List[Name] + [File]
                    break
                else:
                    List[Name] = [File]
                    break
    del Dire_List["Files"]["All-Files"]
    if len(Dire_List["Directories"]) >= 1 :
        Dire_List["Files"]["Folders"]= Dire_List["Directories"]
    print("Report All Contents ِDirectory Is :")
    print("")
    print("")
    for File in Dire_List["Files"]:
        print(f"Found DataType : {File} Number : {len(Dire_List['Files'][File])}")
        Report = f"View Preview : {Dire_List['Files'][File][0]}"
        if len(Dire_List["Files"][File]) == 3:
            for Number in range(0,3):
                Report += (f"View Preview : {Dire_List['Files'][File][Number]} ,, ")
            Report += "..."
        else:
            for Number in range(0, len(Dire_List["Files"][File])):
                Report += (f"View Preview : {Dire_List['Files'][File][Number]}")
    print("")
    print("Report All Contents ِDirectory  :Finish !!!")
    print("")
    print("")
    while True:
        Use_Res = input("Please  Exit App Not Change Directory Modified Type ( e ) Or\n For Accept Setting And Start Directory Modified Type ( y )  :: ")
        print("")
        if Use_Res == "y":
            break
        elif Use_Res == "e":
            return
        else:
            print("Invalid Input Try Again !!!")
            print("")
    fi_mv()
#----------------------------------------------------------| Directory&File
def di_fi():
    global Pat_Src
    Pat_Src = os.path.dirname(os.path.abspath(sys.argv[0]))
    try:
        with os.scandir(Pat_Src) as files:
            for Files in files:
                Dire_List["Totals"] += 1
                if Files.is_dir():
                    if Files.name[1] !="┣━":
                        Dire_List["Directories"].append(Files.name)
                        print(Files.name)
                elif Files.is_file():
                    if Files.name != "File-Sorter.py":
                        Dire_List["Files"]["All-Files"].append(Files.name)
                else:
                    Dire_List["Other_File"].append(Files.name)
    except FileNotFoundError:
        print("Directory not found !!!")
        return
    except PermissionError:
        print("Permission denied !!!")
        return
    except Exception as e:
        print(f"Error !!! => {e}")
    if Dire_List["Totals"] >= 1 :
        '''
        print("Report Address Directory : ")
        print("")
        print(f"Totals All => {Dire_List["Totals"] - 1}")
        print("")
        print(f"Directories => {len(Dire_List['Directories'])}")
        print(Dire_List["Directories"])
        print("")
        print(f"Files => {len(Dire_List['Files']['All-Files']) - 1}")
        print(Dire_List["Files"]["All-Files"])
        print("")
        print(f"Other File => {len(Dire_List['Other_File'])}")
        print(Dire_List["Other_File"])
        print("")
        print("Report Address Directory :  Finish !!!")
        print("")
        print("")
        '''
        print("Report Address Directory : ")
        print("")
        print(f"Totals All => {Dire_List["Totals"]}")
        print("")
        print(f"Directories => {len(Dire_List['Directories'])}")
        print("")
        print(f"Files => {len(Dire_List['Files']['All-Files'])}")
        print("")
        print(f"Other File => {len(Dire_List['Other_File'])}")
        print("")
        print("Report Address Directory :  Finish !!!")
        print("")
        print("")
        fil_ty_fi()
    else:
        print("Note Found File In Folder !!!")
        print("")
        return
#---------------------------------------------------------------------------------------------------------------------| Main Program :
di_fi()
print("")
print(" ! ! ! Programs Finished ! ! ! ")
