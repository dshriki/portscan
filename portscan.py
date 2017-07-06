import socket
import argparse

#parser=argparse.ArgumentParser()
#parser.add_argument("dest")
#parser.add_argument("start")
#parser.add_argument("stop")

#args = parser.parse_args()



class port_inspect:

    def __init__(self,addr):
        self.addr=addr
    def run_ports(self,startport,endport):
        print ("===============================")
        print("Check ports for ip " + self.addr)
        print ("===============================")
        for port in range(startport,endport):
            self.inspect_port(port)

    def inspect_port(self,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result=sock.connect_ex((self.addr,port))
        if result==0:
            print ("Port " + str(port) + " is open")
        else:
            print ("port " + str(port) + " is close")

def main():
    #host_ip=args.dest
    host_ip="8.8.8.8"
    google=port_inspect(host_ip)
    start_port=int(20)#args.start)
    stop_port=int(30)#args.stop)
    google.run_ports(start_port,stop_port)
#main()
