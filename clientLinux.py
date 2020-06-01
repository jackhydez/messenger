import socket, threading, time, os

key = 8194

shutdown = False
join = False

os.system("clear")

def receving (name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
#code
                decrypt = ""; k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt +=i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i)^key)
                print(decrypt)
#code
                time.sleep(0.2)

        except:
            pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("5.187.5.162",9099)
#server = ("192.168.43.33",9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target = receving, args = ("RecvThread", s))
rT.start()

while shutdown == False:
    if join == False:
        s.sendto(("[" + alias + "] => join chat").encode("utf-8"), server)
        join = True
    else:
        try:
            message = input()
#code
            crypt = ""
            for i in message:
                crypt += chr(ord(i)^key)
            message = crypt
#code
            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)

        except:
            s.sendto(("[" + alias + "] <= left chat").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
