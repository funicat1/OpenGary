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

you dont need to do it now - the repo has everything already.

but, if you do want to likely re-pull the pictures, do this:

<details>
  <summary>How to pull the pictures</summary>
  
#### 0. Add important directories

```bash
mkdir garypics
mkdir gooberpics
mkdir gullypics
```

#### 1. Pull the images

1. Move the scrapers to the root directory

2. Run them

   ```bash
   python garyscrape.py
   python gooberscrape.py
   python gullyscrape.py
   ```

3. Move the scrapers back or just delete them.
</details>

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
