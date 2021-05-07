# What script does
#
# This script creates a random string and saves it to a user-specified location
# in vault.  Helpful when creating passwords for database connections.
#
# The default string length is set to 18, but it can be changed.
#
# Basic example:
#   python3 ./random_password_to_vault.py puppet/myserver.stanford.edu/random_foo
#   python3 ./random_password_to_vault.py puppet/database/foo_database/prod/foo_pwd
#
# Example with length change:
#   python3 ./random_password_to_vault.py --lenth 20 puppet/common/appname/foo
#
#!/usr/bin/python

import os
import sys
import argparse
import string
import random
import subprocess

# Create the parser
my_parser = argparse.ArgumentParser(description='Create a random password string and save it to vault')

# Add the arguments
my_parser.add_argument('VaultPath',
                       metavar='vault_path',
                       type=str,
                       help='the vault path to list')
my_parser.add_argument('--length',
                        metavar='string_length',
                        type=int,
                        default=18,
                        required=False,
                        help='sets the lenght of random string; defaults to 18')

# Execute parse_args()
args = my_parser.parse_args()

vault_path = args.VaultPath

#if args.StringLength:
string_length = args.length
#else:
#   string_length = 18

def createRandomString(str_length):
    # create random string based on length
    global random_password
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join((random.choice(characters)) for i in range(str_length))
    return random_password

vault_import = subprocess.call(["vault","kv","put",vault_path,"content="+createRandomString(string_length)])
print("the random password was " + random_password)