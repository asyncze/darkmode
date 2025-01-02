# py312 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# deactivate

# .venv/bin/python darkmode.py

# Script Editor -> Save as Application
#
# tell application "System Events"
#     tell appearance preferences
#         set dark mode to not dark mode
#     end tell
# end tell

import rumps
import os

class Darkmode(rumps.App):
    @rumps.clicked("Toggle Dark Mode")
    def toggle_dark_mode(self, _): os.system("""open -a 'ToggleDarkMode'""")

if __name__ == "__main__": Darkmode("Darkmode").run()

