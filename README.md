# Nova

## Installation

### Set up .env file
Create a .env file by copying the .env.template file and fill in your data.
- Notion api key = key of database to make todo's

### Set up a Python Virtual Environment

1. Create a virtual environment (replace 'venv' with your preferred name)
```
python -m venv venv
```
2. Activate the virtual environment
- On Windows
```
venv\Scripts\activate
```
- On Unix or MacOS
```
source venv/bin/activate
```
3. Install required packages
```
pip install -r requirements.txt
```

## Run
1. Activate venv
- On Windows
```
venv\Scripts\activate
```

- On Unix or MacOS
```
source venv/bin/activate
```

2. Run nova.py
```
python src/nova.py
```