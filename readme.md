# Randbit
Generate random bitcoin private key and check it's balance automatically.

## How to use

1. Install python 3 and then,
```python
pip install -r requirment
```

2. Copy `config.sample.ini` and rename it to `config.ini`.

3. Run it
```python
python main.py
```

## Features

* Multithread
* Support multiple website for checking balance
* Log to file and logrotate
* Send email when find address with some balance
