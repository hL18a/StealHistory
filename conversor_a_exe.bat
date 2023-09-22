@echo off

echo Iniciando proceso de a .exe

set /p nom="Introduce la ruta absoluta del archivo .py o .pyw: "

echo Creando archivo ejecutable...
pyinstaller --onefile %nom%

echo El archivo ejecutable se ha creado exitosamente en la misma ubicación que este script.
pause
    
