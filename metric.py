#! /usr/bin/python3

import psutil, sys

try:
    if sys.argv[1] == "cpu":
        print("system.cpu.user :" + str(psutil.cpu_times_percent(interval=0.1).user) +"\nsystem.cpu.idle :" + str(psutil.cpu_times_percent(interval=0.1).idle) + "\nsystem.cpu.system :" + str (psutil.cpu_times_percent(interval=0.1).system) + "\nsystem.cpu.guest :" + str(psutil.cpu_times_percent(interval=0.1).guest) + "\nsystem.cpu.iowait :" +str(psutil.cpu_times_percent(interval=0.1).iowait) + "\nsystem.cpu.stolen :" + str(psutil.cpu_times_percent(interval=0.1).steal))
    elif sys.argv[1] == "mem":
        print("virtual total :" + str(psutil.virtual_memory().total) + "\nvirtual used :" + str(psutil.virtual_memory().used) + "\nvirtyal free :" + str(psutil.virtual_memory().free) + "\nvirtual shared :" + str(psutil.virtual_memory().shared) + "\nswap total :" + str(psutil.swap_memory().total) + "\nswap used :" + str(psutil.swap_memory().used) + "\nswap free" + str(psutil.swap_memory().free))
    else: print("Invalid Argument")
except IndexError:
    print("No argument given")
