# Setup the mouse scroll wheel speed on Linux Mint
# https://mintguide.org/other/643-setup-the-mouse-scroll-wheel-speed.html

# 1. Install IMWHEEL
sudo apt install imwheel

# 2. I found an interesting script that facilitates the configuration utility.
#    (Thanks to Nick from http://www.nicknorton.net/?q=node/10)
mv imwheel-script.sh ~/
cd ~/
chmod +x imwheel-script.sh
sh imwheel-script.sh
exit

# 3. Startup. To utility imwheel worked at every system startup, add imwheel to startup list.
