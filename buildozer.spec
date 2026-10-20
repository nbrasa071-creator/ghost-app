[app]
title = System Update
package.name = sysupdate
package.domain = org.sysupdate
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3==3.10.12,kivy,requests,urllib3,chardet,idna,certifi
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
