import requests
import json
import zipfile
import os
#import subprocess
EXTERNAL = requests.get("https://truecord-database.thechadcoders.repl.co").json()
LOCAL = json.load(open("main.json", "r"))
EXTERNALver = EXTERNAL["version"]
if EXTERNAL["version"] != LOCAL["version"]:
    yn = input("An update is available...\nWould you like to install it?\n[Y/N]")
    if yn == "y":
        url = requests.get('https://truecord-database.thechadcoders.repl.co/latest').text
        path = f"./versions/{EXTERNALver}"
        r = requests.get(url, allow_redirects=True)
        open(path, "wb").write(r.content)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            os.remove(path)
            zip_ref.extractall("./versions")
        with open("main.json", "r") as f:
            version = json.load(f)
    
        version["version"] = EXTERNALver

        with open("main.json", "w") as f:
            version = json.dump(version, f, indent=4)
        os.system(f"python3 {path}/main.py")
    else:
        
        folder = LOCAL["version"]
        os.system(f"python3 ./versions/{folder}/main.py")
        #subprocess.call([f"./versions/{folder}/main.py"])
else:
    url = LOCAL["version"]
    os.system(f"python3 ./versions/{url}/main.py")