# metrics
This project is entry task for GL DevOps ProCamp. This is simple script that show CPU and memory stats of linux server.
## Getting started
These instructions will get you a copy of the project up and running on your local machine for gathering perfomance metrics.
### Prerequisites
Local machine with linux distro with python3 and python3-pip installed on it.
To install python and pip on Ubuntu, Debian you need this command:
```
sudo apt-get install python3 python3-pip
```
For CentOS,Fedora or RedHat command looks like this:
```
sudo yum install -y python37 python37-pip
```
### Installing
To install script on your machine you need psutil (python system and process utilities) package for python.
To do this you have to execute command
```
pip3 install psutil
```
Or use requirment.txt (you have to move in terminal to directory where requirments.txt is or set full path in following command):
```
pip3 install -r requirments.txt
```
More details about psutil is here: https://psutil.readthedocs.io/en/latest/

Than you can download metrics.py directly or pull in from this repository.
### Runing
To run the script make use that it is executable for your user.
To make script executable you need command:
```
chmod +x \path_to_metrics\metrics.py
```
Where path_to_metrics is full path to metrics.py file if you are not opened directory where metrics.py is in terminal

To run the script and see CPU utilization you need to execute command
```
./metrics.py cpu
```
And see following information
system.cpu.user: time spent by normal processes executing in user mode; on Linux this also includes guest time.
system.cpu.system: time spent by processes executing in kernel mode.
system.cpu.idle: time spent doing nothing.
system.cpu.guest: time spent running a virtual CPU for guest operating systems under the control of the Linux kernel.
system.cpu.iowait: time spent waiting for I/O to complete. This is not accounted in idle time counter. 
system.cpu.stolen: time spent by other operating systems running in a virtualized environment.

OR execute this to view memory utilization
```
./meteics.py mem
```
And see following information:
virtual total: total physical memory
virtual used: memory used, calculated differently depending on the platform and designed for informational purposes only.
virtual free: memory not being used at all (zeroed) that is readily available; note that this doesn’t reflect the actual memory available/
swap total: total swap memory in bytes/
swap used: used swap memory in bytes/
swap free: free swap memory in bytes/

## Built With
Python 3.7
