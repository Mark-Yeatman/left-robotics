This contains instructions of how to generate the webpage from this directory.

One time setup:
```
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy jupyter plotly
```

Generate:
```
quarto render . --output-dir ../docs
```