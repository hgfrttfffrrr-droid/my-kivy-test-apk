[app]
title = My Kivy Test App
package.name = mykivytest
package.domain = org.test

source.main_filename = main.py
source.dir = .

requirements = python3,kivy

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.0.0

fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
