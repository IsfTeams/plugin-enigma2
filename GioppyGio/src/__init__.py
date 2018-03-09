#from Source.LocaleInit import _

# GioppyGio: [Translation] begin
# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os, gettext

PluginLanguageDomain = "GioppyGio"
PluginLanguagePath = "Extensions/GioppyGio/locale/"

def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))

def _(txt):
	if gettext.dgettext(PluginLanguageDomain, txt):
		return gettext.dgettext(PluginLanguageDomain, txt)
	else:
		print "[" + PluginLanguageDomain + "] fallback to default translation for " + txt
		return gettext.gettext(txt)

language.addCallback(localeInit())
# GioppyGio: [Translation] end
