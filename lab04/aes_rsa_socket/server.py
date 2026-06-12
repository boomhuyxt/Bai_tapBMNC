from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.bind(('localhot', 12345))
sever_socket.listen(5)

sever_key = RSA.generate(2048)

clinents = []

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext.decode()

def handle_client(client_socket):
    print("Client connected:", client_socket.getpeername())
   
clinet_socket.send(sever_key.publickey().export_key()).export_key()