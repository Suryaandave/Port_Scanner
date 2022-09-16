import scapy.all as scapy


def scanner(ip):
    request = scapy.ARP(pdst=ip)
    #request.show()
    boardcast = scapy.Ether()
    boardcast.dst = "ff:ff:ff:ff:ff:ff"
    #boardcast.show()
    request_boardcast = boardcast/request

    #request_boardcast.show()

    res1 = scapy.srp(request_boardcast, timeout=1)[0]

    for el in res1:
        print(el[1].psrc)
        print(el[1].hwsrc)
        print("-------------------------------------------------------------------")

entry=input("Enter the ip address with or without sunet masking : ")
scanner(entry)
