devices={
    "router": "Cisco",
    "switch": "Juniper",
    "firewall": "Palo Alto",
    "ip_address": "192.168.1.1",
    "Device_count": 4,
    "Device_count": 40,
    "colors": ["red", "green", "blue"]
}
print(devices["colors"][2])
print(type(devices))
new1=devices.keys()
new2=devices.values()
print(new1)
devices["access point"]="Ubiquiti"
print(new1)
print(new2)
new3=devices.items()
print(new3)

if "router" in devices:
    print("present")
else:
        print("not present")

devices.update({"acces point":"ap1"})
print(devices)

del devices["Device_count"]
print(devices)

#evices.clear()
#rint(devices)

#el devices
#rint(devices)

for key in devices:
      print(key)
for router in devices:
      print(devices[router])


for kry in devices:
      