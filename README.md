# OpenGary

Self-hosted Gary API!

# Installation

Yes, you do have to install it.

#### 0. Clone the repo

```bash
git clone https://github.com/funicat1/OpenGary
cd OpenGary
```

### 1. Pull the pictures

By default, the repo doesnt contain gary, goober, or gully pictures.

You have to pull all the pictures from the gary cdn, heres how:

1. Move the scrapers to the root directory

2. Run them

   ```bash
    python garyscrape.py
    python gooberscrape.py
    python gullyscrape.py
   ```

3. Move the scrapers back or just delete them.

### 2. Install the requirements

```bash
pip install flask
```

### 3. Configure

in config.json, but yeah, this is optional

### 4. Run it

```bash
python app.py
```

# Feedback?

Contact me on discord: @funicatto

Or make an issue on the repo.
