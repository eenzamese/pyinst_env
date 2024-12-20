import time
import random
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version')
args = parser.parse_args()

with open('pyinst_env\\ms_version.txt', 'r') as version_file:
  version_content = version_file.read()
print('######### CURRENT VERSION #########')
print(version_content)
version_value = f'11{args.version[-3:]}'
new_version = version_content.replace('__VERSION__', version_value)
print('######### NEW VERSION #########')
with open('..\\ms_version_1.txt', 'w') as version_file:
  version_file.write(new_version)
print(new_version)
