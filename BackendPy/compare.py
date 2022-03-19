import update_entry
import update
import firebase.firebase as fpy
from time import sleep


def compareEntry(plate):
    firebaseComp = fpy.FirebaseApplication('https://anpr-15f03-default-rtdb.firebaseio.com/', None)
    plates = (firebaseComp.get('/Cars/', "")).keys()
    print(plates)
    for i in plates:
        if plate.lower() == i.lower():
            update_entry.entry(plate)
            print("entered")
            return 1
    return 0


def compareExit(plate):
    firebaseComp = fpy.FirebaseApplication('https://anpr-15f03-default-rtdb.firebaseio.com/', None)
    plates = (firebaseComp.get('/Cars/', "")).keys()
    print(plates)
    for i in plates:
        if plate.lower() == i.lower():
            update.exit(plate)
            print("exited")
            return 1
    return 0

def whenEntery(plate):
    # print(plate)
    flag = compareEntry(plate)
    # print("delay started")
    # sleep(60)
    # print("delay stopped")
    # whenExit(plate)
    return flag


def whenExit(plate):
    flag = compareExit(plate)
    return flag
if __name__=="__main__":
    plateG = "CA455822"
    whenEntery(plateG)
    
    whenExit(plateG)
