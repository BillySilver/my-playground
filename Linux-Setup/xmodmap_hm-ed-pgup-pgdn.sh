xmodmap -e "keycode 66  = Mode_switch Caps_Lock"
xmodmap -e "keycode 111 = Up NoSymbol Prior Prior Up"
xmodmap -e "keycode 113 = Left NoSymbol Home Home Left"
xmodmap -e "keycode 114 = Right NoSymbol End End Right"
xmodmap -e "keycode 116 = Down NoSymbol Next Next Down"
xmodmap -pke > ~/.Xmodmap
# Startup Applications
# https://help.ubuntu.com/stable/ubuntu-help/startup-applications.html
echo "xmodmap ~/.Xmodmap" >> ~/.xinitrc
chmod +x ~/.xinitrc
gnome-session-properties
# Add an entry within '/home/USERNAME/.xinitrc'.
# Note that the absolute path is necessery.
