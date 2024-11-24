import os

os.system("pyinstaller ./sb/sb_cli.py --onefile")
os.system("rm -rf ./build/*")
os.system("mv ./dist/sb_cli ./build/sb")
os.system("rm -r dist")
os.system("rm ./sb_cli.spec")
