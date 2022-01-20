#!/usr/bin/python3

import subprocess

subprocess.call(["touch", "subprocess.txt"])
subprocess.call(["ls"])
print("Sample file created")

