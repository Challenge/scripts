from pfsense import *
import string
import random

# Load ticket ids
with open('brugernavne.csv') as f:
    ticket_ids = f.read().strip().split('\n')[1:]


def gen_pw(length = 6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

pws = [gen_pw() for _ in range(len(ticket_ids))]

# add users
f = open('passwords.txt', 'a')
f.write('Brugernavn, password\n')
for i,pw in zip(ticket_ids, pws):
    pfsense.add_user(i,pw)
    f.write('%s, %s\n' % (i,pw))
