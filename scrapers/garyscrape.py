import requests

for i in range(1, 649):
    url = f'https://api.garythe.cat/Gary/Gary{i}.jpg'
    response = requests.get(url)
    response.raise_for_status()
    print("got:",url)
    with open(f"garypics/Gary{i}.jpg", 'wb') as f:
        f.write(response.content)