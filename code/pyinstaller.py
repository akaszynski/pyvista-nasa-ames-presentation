pip install -r requirements_build.txt
pyinstaller \
    --add-data=Library;Library \
    --additional-hooks-dir=Hooks \
    --icon library\icons\icon.ico \
    --windowed VesselVio.py
