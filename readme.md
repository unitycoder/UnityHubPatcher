# Hub Patcher

Patches Unity Hub with a custom theme selector (which includes a custom light theme). Switch between themes by going to Preferences > Appearance. Fancy!

![Dark theme screenshot](/screenshot.png)

## Getting Started

_Make sure that Unity Hub is not running in the background before running Hub Patcher!_

Simply run hub_patcher.py with the path to your Unity Hub installation as the first arguement. You may have to run as administrator depending on where it is installed.

### Examples

Windows: `python hub_patcher.py "C:/Program Files/Unity Hub"`

macOS: `python3 ./hub_patcher.py /Applications/Unity\ Hub.app/Contents`

Note that Hub Patcher has only been tested on Windows 10, Linux, and macOS. While Windows 11 _should_ work in theory, your mileage may vary.

### Troubleshooting

If you get `PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'app.asar' -> 'app.asar.bak'` you likely have Unity Hub running in the background. Ensure the process is terminated before retrying.

### Prerequisites

* Node Package Manager (NPM)
* Python 3.5+
* Unity Hub 3.1.x (see branches for older versions)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Unity for creating Unity Hub
* Electron team for making packaged Electron apps easy to reverse engineer
