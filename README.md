# Optimizing Mind Python Client Demo

## Run on Mybinder.org
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Optimizing-Mind/omcloud/master)
[Click Here to run the notebook on mybinder.org](https://mybinder.org/v2/gh/Optimizing-Mind/omcloud/master)


## Run Locally (Python version 3)
### Setup
```
$ pip install -r requirements.txt
$ git clone https://gitlab.com/optimizingmind/algorithmia/demo.git
$ cd demo
```

### Python Client
```
python optclient.py -h
   usage: optclient.py [-h] --api_key API_KEY [--api_path API_PATH]
   
   optional arguments:
     -h, --help           show this help message and exit
     --api_key API_KEY    API key for using Algorithmia service
     --api_path API_PATH  API Path for using Algorithmia service```
```

```
$ python optclient.py --api_key='your-key'
```

### Jupiter Client
Install Jupyter:
https://jupyter.readthedocs.io/en/latest/install.html#new-to-python-and-jupyter

#### Run Jupyter
```$ jupyter notebook```

- A browser will popup, click on the optclient.ipynb link .
- On the notebook, enter the required parameters.
- Run the cells.
