
import rumps
import os

class DarkMode(rumps.App):
    @rumps.clicked("Toggle Dark Mode")
    def toggle_dark_mode(self, _): os.system("""open -a 'ToggleDarkMode'""")

if __name__ == "__main__": DarkMode("Dark Mode").run()

