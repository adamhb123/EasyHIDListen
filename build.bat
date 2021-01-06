pyinstaller --noconfirm --onefile --console --icon "./rsc/icon.ico" --distpath "./builds" --add-data "./rsc;rsc/"  "./EasyHIDListen.py" 
del /f "./EasyHIDListen.spec"
rmdir /S /Q "./build"
rmdir /S /Q "./__pycache__" 