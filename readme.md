# Darkmode

Dark mode toggle for the toolbar (MacOS)

## Create ToggleDarkMode.app

1. Open Script Editor
2. Paste
    tell application "System Events"
        tell appearance preferences
            set dark mode to not dark mode
        end tell
    end tell
3. Save as Application (ToggleDarkMode)

## Build

```bash
pip install -r requirements.txt
```
```
python setup.py py2app
```

Run darkmode.app in /dist folder.
