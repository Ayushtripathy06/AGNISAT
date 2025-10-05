'''def tilt_w():
    print("working")
def tilt_s():
    print("working")
def tilt_a():
    print("working")
def tilt_d():
    print("working")
upright = False
while not upright:
    system =input("is upring y/n ")
    if system == "y":
        print("is upright")
        upright = True
    else:
        tilt =input("which direction is it tilting (N/S/E/W) ")
        dict = {"N":tilt_w() , "S":tilt_s() , "E":tilt_d() ,  "W":tilt_d()}
        print(dict[tilt])'''

def tilt_w():
    print("working")
    coping = input("start eng ")

def tilt_s():
    print("working")
    coping = input("start eng ")

def tilt_a():
    print("working")
    coping = input("start eng ")

def tilt_d():
    print("working")
    coping = input("start eng ")

upright = False

while not upright:
    system = input("Is upright? (y/n): ")
    if system == "y":
        print("Is upright ")
        upright = True
    else:
        tilt = input("Which direction is it tilting (N/S/E/W)? ")
        
        # Store function references, not calls
        tilt_dict = {
            "N": tilt_w,
            "S": tilt_s,
            "E": tilt_d,
            "W": tilt_d
        }

        # Call the function only if the key exists
        if tilt in tilt_dict:
            tilt_dict[tilt]()  # This calls the correct function
        else:
            print("Invalid direction.")
        





    



