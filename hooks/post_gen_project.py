import os
import subprocess


print("Configuring Poetry to create new venv")
subprocess.call(['python3.12', '-m', 'poetry', 'config', 'virtualenvs.in-project', 'true'])
print("Installing poetry project")
subprocess.call(['python3.12', '-m', 'poetry', 'install'])


print("Creating initial commit")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

