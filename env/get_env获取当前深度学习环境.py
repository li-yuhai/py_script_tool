

import torch;
print("cuda版本信息:")
print(torch.__version__)

import torch
print("pytorch版本信息:")
print(torch.version.cuda)

import platform
print("python版本信息:")
print(platform.python_version())

import psutil
import cpuinfo
import subprocess

# 获取CPU信息
cpu_info = cpuinfo.get_cpu_info()
cpu_name = cpu_info['brand_raw']
cpu_frequency = cpu_info['hz_actual_friendly']
cpu_core_count = psutil.cpu_count(logical=False)
print(f"CPU: {cpu_name}, {cpu_frequency}, {cpu_core_count} cores")

# 获取GPU信息
gpu_info = subprocess.check_output(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv"]).decode("utf-8")
gpu_list = gpu_info.strip().split('\n')[1:]
for gpu in gpu_list:
    gpu_name, gpu_memory = gpu.split(', ')
    gpu_memory = int(gpu_memory.strip()[:-4])
    print(f"GPU: {gpu_name}, {gpu_memory}MB VRAM")
