# Setup

## Set venv

1. Run

```
python3 -m venv venv
```

1. Use this venv in vscode instead of global
   (ALT+COMMAND P and select Python:Select interpreter)

2. Enable venv in vscode command line terminal

```
source venv/bin/activate
```

Then install fastapi:

```

pip install "fastapi[standard]"
```

## Start server

```
fastapi dev main.py
```
