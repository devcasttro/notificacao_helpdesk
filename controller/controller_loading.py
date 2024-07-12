from tqdm import tqdm
import time

def loading():
    for i in tqdm(range(10)):
        time.sleep(2)