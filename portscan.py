import socket
import argparse

def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("dest")
    parser.add_argument("start")
    parser.add_argument("stop")

    args = parser.parse_args()
    return args



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
    ARGS=get_args()
    host_ip=ARGS.dest
    host_ip="8.8.8.8"
    google=port_inspect(host_ip)
    start_port=int(ARGS.start)
    stop_port=int(ARGS.stop)
    google.run_ports(start_port,stop_port)
main()
