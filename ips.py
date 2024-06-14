arp = open("arp.txt", "r")
open("ips.txt", "w").close
ips = open("ips.txt", "a")

for i in arp:
   if (i[:3] == "192" or i[:2] == "172" or i[:2] == "10."):
      ips.write(i[:i.find(chr(9))] + "\n")
arp.close()
ips.close()

