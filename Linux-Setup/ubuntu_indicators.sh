sudo add-apt-repository ppa:indicator-multiload/stable-daily
sudo add-apt-repository ppa:fossfreedom/indicator-sysmonitor
sudo apt-get update

sudo apt-get install indicator-multiload
sudo apt-get install indicator-sysmonitor
# [indicator-sysmonitor]
# {cpufreq} GHz {cputemp} / {cpu} CPU / {mem} Mem
# cpufreq
# Display CPU Frequency in GHz.
# lscpu | grep 'CPU MHz' | awk '{printf("%3.2f\n", $3/1000)}'
