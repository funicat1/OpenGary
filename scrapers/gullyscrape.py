import requests

for i in range(1, 30):
    try:
        url = f'https://cdn.garythe.cat/Gully/Gully{i}.jpg'
        response = requests.get(url)
        response.raise_for_status()
        print("got:",url)
        with open(f"gullypics/Gully{i}.jpg", 'wb') as f:
            f.write(response.content)
    except requests.exceptions.HTTPError as errh:
        try:
            url = f'https://cdn.garythe.cat/Gully/Gully{i}.jpeg'
            response = requests.get(url)
            response.raise_for_status()
            print("got:",url)
            with open(f"gullypics/Gully{i}.jpg", 'wb') as f:
                f.write(response.content)
        except requests.exceptions.HTTPError as errh:
            url = f'https://cdn.garythe.cat/Gully/Gully{i}.JPG'
            response = requests.get(url)
            response.raise_for_status()
            print("got:",url)
            with open(f"gullypics/Gully{i}.jpg", 'wb') as f:
                f.write(response.content)