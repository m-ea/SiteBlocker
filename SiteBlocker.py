from pathlib import WindowsPath

# Get input on options
domain = input("Enter domain to manage: ")
unblock = '_'
while unblock != 'block' and unblock != 'unblock':
    unblock = str(input("Block or unblock site? (block/unblock) "))
www = "_"
while www != 'y' and www != 'n':
    www = input("Apply changes to www subdomain too? (y/n) ")

# Set variables
CONST_QUADS = '0.0.0.0 '
wwwsub = 'www.' + domain

# Locate and open the hosts file
folder = WindowsPath('C:/Windows/System32/drivers/etc')
file = folder / 'hosts'

# Write to file
# Remove hosts entry
if unblock == 'unblock':
    f = open(file, mode='r')
    lines = f.readlines()
    f = open(file, mode='w')
    for line in lines:
        if line != CONST_QUADS + domain + '\n' and (line != CONST_QUADS + wwwsub + '\n' or www == 'n'):
            f.write(line)
# Add hosts entry
else:
    f = open(file, mode='a')
    f.write(CONST_QUADS + domain + '\n')
    if www == 'y':
        f.write(CONST_QUADS + wwwsub + '\n')

print("Done!")