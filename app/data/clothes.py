

import os
import json
base_path = os.path.dirname(os.path.abspath(__file__))
def load_clothes_data(f_path: str = None) -> dict:
    if f_path is None:
        base_path = os.path.dirname(os.path.abspath(__file__))   
        f_path = os.path.join(base_path, 'clothes.json')

    with open(f_path) as file:
        data = json.load(file)
    return data
    

