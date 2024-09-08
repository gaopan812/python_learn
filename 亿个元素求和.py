import numpy as np
import time

# 创建一个包含1亿个元素的数组
data = np.arange(1e8+1)
start_time = time.time()
sum_result = np.sum(data)
end_time = time.time()
print(f'Sum: {sum_result}')
print(f"Time taken: {end_time - start_time} seconds")