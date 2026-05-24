# Alternative-FlightGear-Launcher
This is a custom FlightGear launcher intended to aide with running FG on Windows 7. 
i386's VxKex is able to get FG 2024.1.5 working on Windows 7!
The only issue is the launcher will not start
<img width="614" height="842" alt="image" src="https://github.com/user-attachments/assets/686073ca-afd6-4f6a-9af0-fc8024aebae3" />
There is probably a way to fix this, But I just wanted to write my own mini launcher.
It gives an error stating "Failed to Initalize Graphics Backend for D3D11"

So instead of troubleshooting the error, I decided to make my own launcher!
<img width="734" height="373" alt="image" src="https://github.com/user-attachments/assets/294d5838-b0bf-4618-895d-ec152055280c" />

It keeps its settings persistant through settings.cfg
If settings.cfg does not already exist when the launcher is executed, the default settings will be used and itll auto generate the config file!

To run this code on Windows 7, Make sure you have Python 3.8.8 Installed. 
Modify Line 6 of the python code to point to where ever you installed FlightGear.
For Windows with 2024.1.5 fgfs.exe is located in: "C:\Program Files\FlightGear 2024.1\bin\fgfs.exe"
Also note if the directory has spaces in it, You need to add qoutation marks for the variable. 
Use double quotes like this fgfs = '"directory here"'

If you need help, Check my F-22A Raptor github repository as theres a discord server link in which I can help you there.
Enjoy!


To compile it:
install python 3.8.8 
Be sure to check add to PATH during the installation
After its done, open a command prompt and type 
pip install pyinstaller

In the same directory as main.py, enter 
pyinstaller --onefile --console main.py

Once thats done, the compiled executeable will be in the "dist" folder
