import socket
import os


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def split_command_list(x):
    # Splist the entire received command list into current command and next iteration command
    cur_cmd = x.split('||')[:1]
    return cur_cmd


def cur_cmd_list(x):
    # Splits the current command into a list
    return x[0].split(" ")


def next_cmd_list(x):
    # Removes the cur_cmd and returns the string
    return x.split("||", 1)[1]


if __name__ == "__main__":
    pid = os.fork()
    if pid == 0:
        localIP = "127.0.0.1"
        localPort = 20003
        bufferSize = 1024

        # Create a datagram socket

        UDPServerSocket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Bind to address and ip

        UDPServerSocket.bind((localIP, localPort))

        print("UDP server up and listening")

        # Listen for incoming datagrams

        while(True):

            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

            message = bytesAddressPair[0].decode('utf-8')

            address = bytesAddressPair[1]

            print(message)
            print(address)

            # Sending a reply to client
            msgFromServer = "Hello UDP Client"
            bytesToSend = str.encode(msgFromServer)

            UDPServerSocket.sendto(bytesToSend, address)
    else:
        user_input = input("Please enter some command\n")
        print("you have entered "+user_input)
