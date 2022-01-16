from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.157.3",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

f = open('results.txt', 'w')


for capability in m.server_capabilities:
    f.write(capability)
    f.write("\n")
f.close()
