import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host="192.168.157.3",
    port=830,username="cisco",
    password="cisco123!",
    hostkey_verify=False)

netconf_iproute = """ 
<config>
    <native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
            <route>
                <ip-route-interface-forwarding-list>
                    <prefix>10.10.20.0</prefix>
                    <mask>255.255.255.0</mask>
                    <fwd-list>
                        <fwd>192.168.0.1</fwd>
                    </fwd-list>
                </ip-route-interface-forwarding-list>
            </route>
        </ip>
    </native>
</config>
"""
    

netconf_reply = m.edit_config(target="running", config=netconf_iproute)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
m.close_session()