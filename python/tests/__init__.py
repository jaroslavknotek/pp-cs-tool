import os, sys, inspect

current_path = inspect.getfile(inspect.currentframe())
script_path = os.path.join(current_path, os.pardir)
abpath = os.path.abspath(script_path)
current_dir = os.path.dirname(abpath)
current_dir = os.path.join(current_dir, "src")
print("fooo bar")
print(current_dir)
sys.path.insert(0, current_dir)
