# Get Learning Words in ShanBay
choco.exe install -y PhantomJS
pip install  -t ./site-packages -r .\requirements.txt

python main.py username password > words.html


# Get Words in pdf
## Install textract
```
bash
zsh
sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr flac lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
sudo apt-get install libpulse-dev zlib1g-dev
sudo apt-get install python3-pip
pip3 install textract
```

## Install Pattern
```
bash
zsh
git clone --depth=1 -b development https://github.com/clips/pattern.git
cd pattern
sudo python3 setup.py install
```