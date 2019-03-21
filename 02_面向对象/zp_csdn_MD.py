import os
import sys
import subprocess

if not os.path.exists(sys.argv[1]):
    print("not exists")
    exit()

subprocess.call(["open",str(sys.argv[1])])