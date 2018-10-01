SERVER python3.6 server.py *Start with triggers

python3.6 server.py --silent * Start in silent mode * Do not trigger email when percent > 80 (CPU, RAM, SWAP) * Do not trigger when md5 sum is diffrent (/etc/passwd, /var/log/source, /var/log/wtmp)

CHK: Requirments: psutil (link = https://pypi.org/project/psutil/) os sys subprocess socket hashlib

Doc Info:

console_print(String) *Print message in console

sub_process(Param) Callback method for bash function Eg: console_print(sub_process("free -m")) *Prints: total used free shared buff/cache available Mem: 1838 127 1547 8 163 1545 Swap: 2047 0 2047

get_md5_sum(Path_To_File) Return md5 sum of file Eg get_md5_sum("/etc/passwd")

get_hostname() *Return hostname of server

get_cpu_percent(Interval=None) Return cpu percent of server When interval is > 0.0 compares system CPU times elapsed before and after the interval (blocking)

get_cpu_logical() *Return logical cpu's

get_cpu_psychical() *Return psychical's cpu's

get_virtual_memory(Param=False) Returns virtual memory Params : * get_virtual_memory() or get_virtual_memory("total") * return total virtual memory * get_virtual_memory("percent") * return in percents virtual memory * get_virtual_memory("available") * return available virtual memory * get_virtual_memory("used") * return used virtual memory * get_virtual_memory("free") * return free virtual memory

get_swap_memory(Param=False) Returns swap memory Params : * get_swap_memory() or get_swap_memory("total") * return total swap memory * get_swap_memory("percent") * return in percents swap memory * get_swap_memory("used") * return used swap memory * get_swap_memory("free") * return free swap memory

get_disk_usage(Path = False, Params = False) Returns disk usage for specific path Path * get_disk_usage() * return disk usage for / * get_disk_usage(Path) * return disk usage for path *Params * get_disk_usage(False, "total") * return total disk usage for path * get_disk_usage(False, "used") * return used disk usage for path * get_disk_usage(False, "free") * return free disk usage for path

get_disk_partitions(Params=False) Return disk partition if false print all Params "removable", "fixed", "remote", "cdrom", "unmounted" or "ramdisk"

get_disk_total() *Return total disk space(Eg 30Gb)

get_disk_available() *Return available disk space (Eg 10Gb

get_load() *Return "cat /proc.loadavg"

get_local_ip() *Return local ip

get_public_ip() *Return public ip

get_pwd() *Return curent directory

get_kernel_os() *Return system os

get_kernel_release(): *Return kernel release

get_kernel_architecture() *Return kernel architecture

get_kernel() *Return all kernel info

get_login() *Return current login

get_group_id() *Return the id of the current process group.

Api ussage: import chk

chk.console_print(chk.get_login())

Output: root