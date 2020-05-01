#################################################################################
#
#    HddSleep plugin for OpenPLi Enigma2
#
#
#    by ims(ims21) (c)2010
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#################################################################################
from Plugins.Plugin import PluginDescriptor

def HddSleepMain(session, **kwargs):
	import ui
	session.open(ui.HddSleep, plugin_path)

def Plugins(path,**kwargs):
	global plugin_path
	plugin_path = path
	result = [PluginDescriptor(name="HddSleep",description = _("HDD sleeptime settings"),where = PluginDescriptor.WHERE_PLUGINMENU,icon = 'plugin.png',fnc = HddSleepMain)]
	return result
