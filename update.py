import requests
from bs4 import BeautifulSoup

base_link = "http://files.teamspeak-services.com/releases/client"

# Get versions

r = requests.get(base_link)
soup = BeautifulSoup(r.text, 'html.parser')
invalid_versions = ("../", "")

versions = [a.text for a in soup.findAll("a") if not a.text in invalid_versions]
print(f"Found versions: {versions}")

latest = versions[-1]
print(f"Selected latest version: {latest}")

# Download

link_win = f"{base_link}/{latest}/TeamSpeak3-Client-win64-{latest}.exe"
link_mac = f"{base_link}/{latest}/TeamSpeak3-Client-macosx-{latest}.dmg"

def download(link, dest):
    r = requests.get(link)
    open(dest, "wb").write(r.content)
    print(f"Downloaded {link} to {dest}")

download(link_win, "dist/ts-win.exe")
download(link_mac, "dist/ts-mac.dmg")

print("Completed")
