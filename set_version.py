import time
import random
print(time.ctime())
with open('ms_version.txt', 'r') as version_file:
  version_content = version_file.read()
print('CURRENT#########VERSION')
print(version_content)
version_value = str(random.randint(10000, 99999)) 
new_version = version_content.replace('30920', version_value)
print('NEW#########VERSION')
with open('..\\ms_version_1.txt', 'w') as version_file:
  version_file.write(new_version)
print(new_version)
