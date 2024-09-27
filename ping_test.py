from re import findall
from subprocess import Popen, PIPE

def ping (host,ping_count):

    for ip in host:
        data = ""
        output= Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{ip} : Successful Ping")
            return True
        else:
            print(f"{ip} : Failed Ping")
            return False

#nodes = ["192.168.50.130"]
nodes = [{$HOST}]

#ping(nodes,3)

def test_ping():
    assert ping(nodes, 3) == True, "PING FAILED"