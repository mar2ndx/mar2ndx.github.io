#!/bin/sh

# Raise DPI from 96 to 276 to makes text size front
xfconf-query -c xsettings -p /Xft/DPI -s 144
#276

# Enlarge cursor size
xfconf-query -c xsettings -p /Gtk/CursorThemeSize -s 72

# Raise xfce panel height
xfconf-query -c xfce4-panel -p /panels/panel-1/size -s 64

# Enlarge notification area icon
xfconf-query -c xfce4-panel -p /plugins/plugin-6/size-max -s 64

# Enlarge window size
xfconf-query -c xfce4-desktop -p /last/window-height -s 1240
xfconf-query -c xfce4-desktop -p /last/window-width -s 909

# Enlarge desktop icon
xfconf-query -n -t uint -c xfce4-desktop -p /desktop-icons/icon-size -s 96

# Use xhdpi theme, you can alsto use "Default-hdpi"
xfconf-query -c xfwm4 -p /general/theme -s "Default-xhdpi"

# Enlarge most of the icons
xfconf-query -c xsettings -p /Gtk/IconSizes -s gtk-menu=48,48:gtk-button=48,48:gtk-dialog=48,48:gtk-dnd=48,48:gtk-small-toolbar=48,48:gtk-large-toolbar=64,64