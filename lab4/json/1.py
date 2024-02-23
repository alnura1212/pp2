
import json
print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""
)
f=open("data.json", "r")
y = json.loads(f.read())
for x in y["imdata"]:
    if len(x["l1PhysIf"]["attributes"]["dn"])==42:
        print(x["l1PhysIf"]["attributes"]["dn"], "                              ", x["l1PhysIf"]["attributes"]["speed"], x["l1PhysIf"]["attributes"]["mtu"] )
    else:
        print(x["l1PhysIf"]["attributes"]["dn"], "                               ", x["l1PhysIf"]["attributes"]["speed"], x["l1PhysIf"]["attributes"]["mtu"] )