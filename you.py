with open("file.txt","r") as file:
        devices=file.readlines()

for ip in devices:
        ip=ip.strip()

        if ip.endswith("1"):
                with open("success.txt","a") as success:
                        success.write(f"succ connect to {ip}\n")
        else:
            with open("fasilure.txt","a") as failure :
             failure.write(f"failed to connect {ip}\n")