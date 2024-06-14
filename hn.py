import socket

f = open("ips.txt", "r")
for i in f:
   try:
      print(i[:len(i)-1] + ":   " + socket.gethostbyaddr(i[:len(i)-1])[0])
   except:
      print(i[:len(i)-1])
f.close()

