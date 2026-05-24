import os, time
# Custom FlightGear launcher
# Phoenix

# define memory variables
fgfs = '"C:\\Program Files\\FlightGear 2024.1\\bin\\fgfs.exe"'
settings = []        
callsign        = ""          
aircraft        = ""          
locationmode    = 0              
lat             = 0      
lon             = 0      
airport         = ""          
runway          = ""      
mp              = 0  
mpserver        = ""          
mpport          = ""      
numaddon        = 0          
addons          = []      
extraArgs       = 0          
arguments       = []          

def writeout():
    global settings
    global callsign
    global aircraft
    global locationmode
    global lat
    global lon
    global airport
    global runway
    global mp
    global mpserver
    global mpport
    global numaddon
    global addons
    global extraArgs
    global arguments
    # default: ["c172p","1","PHTO","08","0","0","0","mpserver01.flightgear.org:5000","5000","D-FGFS","0","0"]
    try:
        settings = [aircraft, locationmode, airport, runway, lat, lon, mp, f"{mpserver[0]}:{mpserver[1]}", mpport, callsign, numaddon]
    except:
        settings = ["c172p","1","PHTO","08","0","0","0","mpserver01.flightgear.org:5000","5000","D-FGFS","0"]
    # addons
    if numaddon != 0:
        for i in range(len(addons)):
            settings.append(addons[i])
            
    settings.append(extraArgs)    
    # arguments
    if extraArgs != 0:
        for i in range(len(arguments)):
            settings.append(arguments[i])

    with open("settings.cfg","w") as file:
        for i in range(len(settings)):
            file.write(f"{settings[i]}\n")
    print("Settings saved successfully!")
    time.sleep(1.5)

try:
    with open("settings.cfg","r") as file:
        for line in file:
            line = line.split("\n")
            line = line[0]
            settings.append(line)
            print(f"Parsed option: {line}")
except:
    settings = ["c172p","1","PHTO","08","0","0","0","mpserver01.flightgear.org:5000","5000","D-FGFS","0","0"] # this is the launch default settings
    writeout()
print(settings)
aircraft = settings[0]
locationmode = int(settings[1])
airport = settings[2]
runway = settings[3]
lat = settings[4]
lon = settings[5]
mp = int(settings[6])
mpserver = settings[7] # out (server:port)
try:
    # parse the :
    mpserver = mpserver.split(":")
    # mpserver[0] is address
    # mpserver[1] is port
except:
    mpserver = [f"{mpserver}","5000"]
mpport = settings[8] # in local (port) 
callsign = settings[9]
numaddon = int(settings[10])
addons = []
arguments = []
if numaddon != 0:
    for i in range(numaddon):
        index = i + 11
        addons.append(settings[index])
nextindex = 10 + numaddon # Skip over the addons
print(nextindex)
extraArgs = int(settings[nextindex])
if extraArgs != 0:
    for i in range(extraArgs):
        index = i + nextindex + 1
        arguments.append(settings[index])
nextindex = nextindex + extraArgs + 1 # Skip over the arguments
print(arguments)
print(addons)
#ae = input("Press any key to continue")

# multiplayer argument: --multiplay=in,10,,{mpport} --multiplay=out,10,{mpserver[0]},{mpserver[1]}

while True:
    # begin!
    os.system("cls")
    print("Custom FlightGear Launcher Version 1.10a")
    print("")
    print("Current settings:")
    print(f"Aircraft: {aircraft}")
    if locationmode == 1: # differs between lat/lon and apt/rwy
        print(f"Airport: {airport}")
        print(f"Runway: {runway}")
    else:
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
    if mp == 1:
        print(f"Multiplayer out: {mpserver[0]}:{mpserver[1]} | Multiplayer in: {mpport}")
        print(f"Callsign: {callsign}")
    if numaddon != 0:
        print(f"Addons enabled: {numaddon}")
    if extraArgs != 0:
        print(f"Extra argumments")
        for i in range(len(arguments)):
            print(arguments[i])

    print("")
    print("What would you like to do?")
    print("Press enter if you want to fly with these settings!")
    print("[1] Change aircraft")
    print("[2] Change Location")
    print("[3] Change Multiplayer Settings")
    if numaddon != 0:
        print("[4] Register Addons")
    else:
        print("[4] Edit Registered Addons")
    if extraArgs != 0:
        print("[5] Edit Extra Arguments")
    else:
        print("[5] Add Extra Arguments")
    ae = input("> ")

    # parse the answer
    if ae == "":
        # Fly!
        if locationmode == 1:
            locationstring = f"--airport={airport} --runway={runway}" # trail a space after the args
        else:
            locationstring = f"--lat={lat} --lon={lon}"
        
        if mp == 1:
            multiplaystring = f"--multiplay=in,10,,{mpport} --multiplay=out,10,{mpserver[0]},{mpserver[1]}"
        else:
            multiplaystring = ""
        
        if numaddon != 0:
            addonstring = f""
            for i in range(len(addons)):
                addonstring = f'{addonstring}--addon={addons[i]} '
        else:
            addonstring = ""
            
        if extraArgs != 0:
            argstring = f""
            for i in range(len(arguments)):
                argstring = f"{argstring} {arguments[i]}"
        else:
            argstring = ""
        
        argumentstring = f"{fgfs} --aircraft={aircraft} --callsign={callsign} {locationstring} {multiplaystring} {addonstring}{argstring}"
        print(f"Launching FlightGear with the command: {argumentstring}")
        os.system(argumentstring)
        print("FlightGear has finished executing. Returning to launcher main menu...")
        time.sleep(1)
    elif ae == "1":
        os.system("cls")
        print("Enter the Aircrafts -set name you want to fly")
        ae = input("> ")
        aircraft = ae
        writeout()
    elif ae == "2":
        # Location
        os.system("cls")
        print("Which type of location do you want to use?")
        print("[1] Use Airport / Runway")
        print("[2] Use latitude-deg / longitude-deg")
        ae = input("> ")
        locationmode = int(ae)
        if locationmode == 1:
            print("Enter the ICAO of the airport")
            ae = input("> ")
            airport = ae
            print("Enter the runway to spawn at")
            ae = input("> ")
            runway = ae
        else:
            print("Enter the Latitude (deg)")
            ae = input("> ")
            latitude = ae
            print("Enter the Longitude (deg)")
            ae = input("> ")
            longitude = ae

    elif ae == "3": # mp settings
        os.system("cls")
        print("Would you like to use Multiplayer? (y/n)" )
        ae = input("> ")
        if ae == "y":
            mp = 1
            print("Enter the server you want to connect to.\nTo include a port, use server:port")
            ae = input("> ")
            mpserver = ae
            print("Enter the local port to use for this instance (default is 5000)")
            print("This allows you to run multiple instances of\nFlightGear on the same MP Server")
            ae = input("> ")
            mpport = ae
            print("Enter a callsign to use")
            ae = input("> ")
            callsign = ae
            writeout()
        else:
            mp = 0
            print("Multiplayer disabled")
            writeout()
    
    elif ae == "4":
        print("Enter the full paths to the addons you want to use (line by line)")
        print("Enter a ~ when you have added them all")
        addons = []
        numaddon = 0
        while True:
            ae = input("> ")
            if ae == "~":
                print("Finished!")
                print(f"FlightGear will use: {numaddon} Addons")
                writeout()
                break
            numaddon = numaddon + 1
            addons.append(ae)
            print(f"Successfully added addon: {ae}")
            
    elif ae == "5":
        print("Enter the extra arguments you want to use (line by line)")
        print("Enter a ~ when you have added them all")
        arguments = []
        extraArgs = 0
        while True:
            ae = input("> ")
            if ae == "~":
                print("Finished!")
                print(f"FlightGear will use: {extraArgs} extra arguments")
                writeout()
                break
            extraArgs = extraArgs + 1
            arguments.append(ae)
            print(f"Successfully added argument: {ae}")


# =================== end file 