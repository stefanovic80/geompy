# config.py
config = {
    'xmin': -10,
    'xmax': 10
}

def update_config(new_xmin=None, new_xmax=None):
    if new_xmin is not None:
        config['xmin'] = new_xmin
    if new_xmax is not None:
        config['xmax'] = new_xmax
