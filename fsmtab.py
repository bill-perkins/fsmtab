#!/usr/bin/env python3
#
# fsmtab:
# simple script to compare /etc/fstab and /etc/mtab
#
# fstab is the "master list" of filesystems
# mtab has the actual list of mounted filesystems
# this script points out any differences

broken = False

with open("/etc/fstab") as fstabfile:
    fstablines = fstabfile.readlines()

with open("/etc/mtab", "r") as mtabfile:
    mtabs = mtabfile.read()

for line in fstablines:
    # skip blanks, comments, localhost lines:
    if len(line) == 1 \
            or line.startswith('#') \
            or line.startswith('UUID=') \
            or '-swap' in line:
        continue

    entrylist = line.split()
    if entrylist[0] in mtabs:
        pass
        # print entrylist[0] + ": found!"
    else:
        print(entrylist[0] + ": not found in /etc/mtab")
        broken = True

if not broken:
    print("filesystem mounts OK")

# EOF:
