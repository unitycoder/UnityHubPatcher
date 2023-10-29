### Info
Patch Hub 3.6.0 to hide unwanted columns.

### Usage
- start commandprompt as admin
- type: python hub_patcher.py
- optionally you can give hub root folder: python hub_patcher.py c:\Program Files\Unity Hub\

### How it works
- it unpacks app.asar file into C:\Program Files\Unity Hub\resources\app\
- app.asar is renamed as app.asar.bak
- next time hub runs, it uses the unpacked "app\" folder, instead of "app.asar"
- so you can modify anything inside app\ folder, this script modifies app\build\renderer\index.html template to add custom CSS styles (for hiding those columns)

### Cloned from other site and modified here
https://gitlab.com/GuitarBro/hub-patcher

### Warning
- For educational use only!
- if you mess up the templates, reinstall hub (better if you take backup of original app.asar, so you can always deleted modified or unpacked files)

### Images
before<br>
![image](https://github.com/unitycoder/UnityHubPatcher/assets/5438317/9461925c-6513-4faa-b8f8-e61eeefa01f8)

after<br>
![hub2023-10-29 13-07-52](https://github.com/unitycoder/UnityHubPatcher/assets/5438317/03d08762-1e20-4b63-a5ba-a5aa4a8816a3)
