import requests

for i in range(1, 56):
    url = f'https://cdn.garythe.cat/Goober/Goober{i}.jpg'
    response = requests.get(url)
    response.raise_for_status()
    print("got:",url)
    with open(f"gooberpics/Goober{i}.jpg", 'wb') as f:
        f.write(response.content)