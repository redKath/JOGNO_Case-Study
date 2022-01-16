import xml.dom.minidom
from ncclient import manager

m = manager.connect(
    host="192.168.157.3",
    port=830,username="cisco",
    password="cisco123!",
    hostkey_verify=False)

netconf_ospf = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router operation="replace">
            <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                <id>100</id>
                    <router-id>1.1.1.1</router-id>
                        <network>
                            <ip>192.168.157.3</ip>
                            <mask>0.0.0.0</mask>
                            <area>0</area>
                        </network>
            </ospf>
        </router>

        </native>
    </config>
    
    """

netconf_reply = m.edit_config(target="running", config=netconf_ospf)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
