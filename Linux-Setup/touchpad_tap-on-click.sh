if [ ! -d "/etc/X11/xorg.conf.d/" ]; then
    mkdir /etc/X11/xorg.conf.d
fi

cp /usr/share/X11/xorg.conf.d/*-synaptics.conf /etc/X11/xorg.conf.d/
CONF="/etc/X11/xorg.conf.d/*-synaptics.conf"
echo '' >> $CONF
echo 'Section "InputClass"' >> $CONF
echo '        Identifier "touchpad catchall"' >> $CONF
echo '        Driver "synaptics"' >> $CONF
echo '        MatchIsTouchpad "on"' >> $CONF
echo '        Option "TapButton1" "1"' >> $CONF
echo '        Option "TapButton2" "3"' >> $CONF
echo '        Option "TapButton3" "2"' >> $CONF
echo 'EndSection' >> $CONF
echo '' >> $CONF
