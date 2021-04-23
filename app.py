import gettext

#gettext.bindtextdomain('app', '/locale')
#gettext.textdomain('app')
t = gettext.translation('app', localedir='locale', languages=['pt_BR.UTF-8'])
#t.install()
_ = t.gettext

palavra = _('Hello World')
print(palavra)
