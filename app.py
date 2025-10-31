print("[OpenGary]: Starting up")
from flask import Flask,jsonify,request,Response
import random
import os, json

if not os.path.exists("config.json"):
    print("[OpenGary]: No config.json found.")
    raise Exception

config = json.load(open("config.json"))
print("[OpenGary]: Config loaded")

app = Flask(__name__)
print("[OpenGary]: Loading quotes")
quotes = open(config["quotespath"],encoding="utf-8").read().splitlines()
print("[OpenGary]: Loading jokes")
jokes = open(config["jokespath"],encoding="utf-8").read().splitlines()
print(f"[OpenGary]: quotes: {len(quotes)}")
print(f"[OpenGary]: jokes: {len(jokes)}")




@app.route('/')
def hello_world():
    return open("index.html", encoding="utf-8").read().replace("{localurl}",request.url_root)

@app.route('/docs.html')
def docs():
    return open("docs.html", encoding="utf-8").read().replace("{localurl}",request.url_root)

@app.route('/gary.ico')
def favicon():
    return open("gary.ico","rb").read()

# --------------
#     gary
# --------------

@app.route("/gary")
def gary():
    num = random.randint(1, len(os.listdir(config["garypicspath"])))
    return jsonify({
        "number": num,
        "url": request.url_root + "Gary/Gary" + str(num) + ".jpg"
    })

@app.route("/gary/image")
def garyimage():
    num = random.randint(1, len(os.listdir(config["gooberpicspath"])))
    return Response(open(f"{config["garypicspath"]}/Gary{num}.jpg","rb").read(),headers={'Content-Type': 'image/jpeg'})


@app.route("/Gary/<path:filename>")
def garypic(filename):
    if ".." in filename:
        return "theres nothing interesting bro"
    if not os.path.exists(f"{config["garypicspath"]}/{filename}"):
        return Response("404 Not Found", status=404)
    return Response(open(f"{config["garypicspath"]}/{filename}","rb").read(),headers={'Content-Type': 'image/jpeg'})

# --------------
#    goober
# --------------

@app.route("/goober")
def goober():
    num = random.randint(1, len(os.listdir(config["gooberpicspath"])))
    return jsonify({
        "number": num,
        "url": request.url_root + "Goober/Goober" + str(num) + ".jpg"
    })

@app.route("/goober/image")
def gooberimage():
    num = random.randint(1, len(os.listdir(config["gooberpicspath"])))
    return Response(open(f"gooberpics/Goober{num}.jpg","rb").read(),headers={'Content-Type': 'image/jpeg'})


@app.route("/Goober/<path:filename>")
def gooberpic(filename):
    if ".." in filename:
        return "theres nothing interesting bro"
    if not os.path.exists(f"{config["gooberpicspath"]}/{filename}"):
        return Response("404 Not Found", status=404)
    return Response(open(f"{config["gooberpicspath"]}/{filename}","rb").read(),headers={'Content-Type': 'image/jpeg'})

# --------------
#    gully??
# --------------

def find(prefix,path):
    for i in os.listdir(path):
        if i.startswith(prefix):
            return i

@app.route("/gully")
def gully():
    num = random.randint(1, len(os.listdir(config["gullypicspath"])))
    filename = find(f"Gully{num}",config["gullypicspath"])
    return jsonify({
        "number": num,
        "url": request.url_root + "Gully/" + filename
    })

@app.route("/gully/image")
def gullyimage():
    num = random.randint(1, len(os.listdir(config["gullypicspath"])))
    filename = find(f"Gully{num}",config["gullypicspath"])
    return Response(open(f"{config["gullypicspath"]}/{filename}","rb").read(),headers={'Content-Type': 'image/jpeg'})


@app.route("/Gully/<path:filename>")
def gullypic(filename):
    if ".." in filename:
        return "theres nothing interesting bro"
    if not os.path.exists(f"{config["gullypicspath"]}/{filename}"):
        return Response("404 Not Found", status=404)
    return Response(open(f"{config["gullypicspath"]}/{filename}","rb").read(),headers={'Content-Type': 'image/jpeg'})

# --------------
#     misc
# --------------

@app.route("/quote")
def quote():
    return jsonify({
        "quote": random.choice(quotes)
    })

@app.route("/joke")
def joke():
    return jsonify({
        "joke": random.choice(jokes)
    })

@app.route("/gary/count")
def gary_count():
    return jsonify({
        "count": len(os.listdir(config["garypicspath"]))
    })
@app.route("/goober/count")
def goober_count():
    return jsonify({
        "count": len(os.listdir(config["gooberpicspath"]))
    })
@app.route("/gully/count")
def gully_count():
    return jsonify({
        "count": len(os.listdir(config["gullypicspath"]))
    })

print(f"[OpenGary]: Ready")

# Run the app
if __name__ == '__main__':
    app.run(port=config["port"])