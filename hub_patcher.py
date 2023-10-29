import subprocess
import os
import sys
import fileinput

css = """<style>
/* cloud services column header */
.pl-header__column.pl-header__column--cloudServices {display:none !important;}

/* version control column header */
.pl-header__columns-wrapper > :nth-child(2) {display: none !important;}

/* version control column value */
.hCtBAQ {display: none !important;}

/* cloud services column value */
.pl-item__row :nth-child(4) {display: none !important;}
</style>
"""

print(":::::[ HubPatcher ]:::::")
print("must run as an Administrator!")

if len(sys.argv) == 1:
    path = "C:/Program Files/Unity Hub/"
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    print("Usage: python script.py [path]")
    sys.exit(1)

if not os.path.exists(path):
    print(f"The specified path '{path}' does not exist.")
    sys.exit(1)

app_asar_path = os.path.join(path, "resources", "app.asar")
if not os.path.isfile(app_asar_path):
    print(f"The 'app.asar' file does not exist in the specified path '{app_asar_path}'.")
    print("This is because you have already patched the hub! You can find unpacked resources inside Unity Hub/resources/app/ folder, and you can modify them there")
    sys.exit(1)
	
print(path)
os.chdir(os.path.join(path, "resources"))
print("Extracting app..")
subprocess.run("npx asar extract app.asar app", shell=True)
print("Backing up...")
os.copy("app.asar", "app.asar.bak")
os.chdir(os.path.join("app", "build", "renderer"))

print("Patching...")
for line in fileinput.FileInput("index.html", inplace=1):
	if "<body>" in line:
		line=line.replace(line,line + css)
	print(line, end="")

print("Done! All patched!")
