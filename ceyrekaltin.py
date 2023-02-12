import requests

req = requests.get("https://api.genelpara.com/embed/altin.json")

satis, degisim = req.json()["C"]["satis"], req.json()["C"]["degisim"]

print(f"Fiyat: {satis}\nDeğişim: {degisim}")