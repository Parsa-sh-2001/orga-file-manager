import json
import sys
import subprocess as sp
import os
from time import sleep
import shutil

usern = os.path.expanduser('~')
path = r"OneDrive\Desktop\Files"
codes = r"OneDrive\Desktop\Files\Codes"
exorbinary = r"OneDrive\Desktop\Files\Exe/Binary"
imgs = r"OneDrive\Desktop\Files\Images"
videos = r"OneDrive\Desktop\Files\Videos"
sci = r"OneDrive\Desktop\Files\Scientific files"
discimg = r"OneDrive\Desktop\Files\Disc images"
docs = r"OneDrive\Desktop\Files\Documents"
codes = os.path.join(usern, codes)
exorbinary = os.path.join(usern, exorbinary)
imgs = os.path.join(usern, imgs)
videos = os.path.join(usern, videos)
sci = os.path.join(usern, sci)
discimg = os.path.join(usern, discimg)
docs = os.path.join(usern, docs)
elses = os.path.join(usern, r"OneDrive\Desktop\Files\Other")

# OH NO THERES MORE....
def typewriter(text, speed=0.5):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        sleep(speed)
    print()

with open('joined.json', 'r') as f:
    data = json.load(f)

def makeyes():
    value = {"sub": "yes"}
    with open('joined.json', 'w') as f:
        json.dump(value, f, indent=4)

    typewriter("MAKING DIRECTORY...", 0.01)
    try:
        lo = os.path.join(usern, path)
        os.makedirs(lo, exist_ok=True)
    except OSError as e:
        typewriter(f"Error: {e}", 0.01)

    typewriter("MAKING FILES IN DIRECTORY...", 0.01)
    try:
        os.makedirs(codes, exist_ok=True)
        os.makedirs(exorbinary, exist_ok=True)
        os.makedirs(imgs, exist_ok=True)
        os.makedirs(videos, exist_ok=True)
        os.makedirs(sci, exist_ok=True)
        os.makedirs(discimg, exist_ok=True)
        os.makedirs(docs, exist_ok=True)
        os.makedirs(elses, exist_ok=True)

        shutil.copy("codes_extention.txt", codes)
        shutil.copy("sysorbinary_extention.txt", exorbinary)
        shutil.copy("img_extention.txt", imgs)
        shutil.copy("media_or_video_extention.txt", videos)
        shutil.copy("data_or_sci.txt", sci)
        shutil.copy("discimg.txt", discimg)
        shutil.copy("dosx_extention.txt", docs)
    except OSError as e:
        typewriter(f"Error: {e}", 0.00001)

    command = [sys.executable, 'filee.py']

    try:
        typewriter("FINISHED FIRST TOUCHES...", 0.01)
        typewriter("STARTING APPLICATION...", 0.01)
        sp.Popen(command)
    except Exception as e:
        typewriter(f"Launch error: {e}", 0.01)

def passout():
    value = {"sub": "yes"}
    with open('joined.json', 'w') as f:
        json.dump(value, f, indent=4)

    typewriter("welcome back", 0.1)
    typewriter("STARTING APPLICATION...", 0.01)

    command = [sys.executable, 'filee.py']

    try:
        sp.Popen(command)
    except Exception as e:
        typewriter(f"Launch error: {e}", 0.01)

val = data.get('sub')
if val == 'no':
    makeyes()
else:
    passout()