from cryptography.fernet import Fernet



key = Fernet.generate_key()
f = Fernet(key)

key_dec = key.decode('utf-8')

teste = "testevida"
teste = (teste.encode('utf-8'))


enc = f.encrypt(teste)


resu = (f.decrypt(enc)).decode('utf-8')

print(resu)
