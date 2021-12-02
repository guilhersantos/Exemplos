from webdav3.client import Client
import time
from threading import Thread

options = {
 'webdav_hostname': "https://mysite.com:2078",
 'webdav_login':    "myemail@mysite.com",
 'webdav_password': "DJKCALD",
}



client = Client(options)
sair = False
def conecta_wedav(n):
    global sair
    while sair == False:
        try:
            #client.execute_request("mkdir", 'dir1')
            #client.mkdir("dir1")
            #files = client.list("dir1")
            client.upload_sync(remote_path="dir1/exemplo.txt", local_path="exemplo.txt")
            #client.download_sync(remote_path="dir1/cat_avn_tmf1.txt", local_path="cat_avn_tmf1_down2.txt")
            files = client.list("dir1")
            print("Numero thread "+str(n), flush=True)
            sair = True
        except Exception as e:
            print(str(e))
            time.sleep(2)

thread_sav = Thread(target= conecta_wedav, args=( cont, ), daemon=True) 
thread_sav.start()


while sair == False:
    time.sleep(0.1)
