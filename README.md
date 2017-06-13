choco.exe install -y PhantomJS
pip install  -t ./site-packages -r .\requirements.txt

python main.py username password > words.html