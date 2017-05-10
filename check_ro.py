#!/bin/sh

import subprocess
import sys

cmd = 'grep "\sro[\s,]" /proc/mounts'

ignorepaths = ['tmpfs', '/dev/sr0', '172.27.4.68']

output = 'OK\ file system writeable'

proc = subprocess.Popen([cmd,], shell=True, stdout=subprocess.PIPE)

for line in iter(proc.stdout.readline,''):
        if line.rstrip().partition(' ')[0] not in ignorepaths and line.rstrip().partition(':')[0] not in ignorepaths:
                output = 'CRITICAL\ detected read only file system ' + line.rstrip()
                print(output)
                sys.exit(2)
        else:
                pass
print(output)
sys.exit(0)
