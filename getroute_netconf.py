import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host="192.168.157.3",
    port=830,username="cisco",
    password="cisco123!",
    hostkey_verify=False)

FILTER = """
<filter>
    <native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
            <route>
                <ip-route-interface-forwarding-list></ip-route-interface-forwarding-list>
            </route>
        </ip>
    </native>
</filter>"""

netconf_reply = m.get_config("running", FILTER)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
m.close_session()