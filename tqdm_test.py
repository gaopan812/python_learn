import time
from tqdm import tqdm

for i in tqdm(range(100)):
    time.sleep(0.01)  # 进度条每0.01s前进一次，总时间为1000*0.01=10s