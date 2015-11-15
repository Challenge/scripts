import requests
import re

SITE = 'http://10.0.0.1'

##### Login #######
s = requests.session()

def find_csrf(action):
    res = s.get(SITE + action)
    csrf = re.search("name='__csrf_magic' value=\"(.*)\"", str(res.text))
    return csrf.group(1)

action = '/index.php'
login_data = { 'usernamefld'  : 'admin'
             , 'passwordfld'  :  'admin'
             , 'login'        : 'Login'
             , '__csrf_magic' : find_csrf(action)
             }
res = s.post(SITE + action, login_data)
assert 'Dashboard' in res.text
##################

USERIDS = {}

def get_users():
    """Scrape all user data and populate the global USERIDS dict"""
    global USERS
    action = '/system_usermanager.php'
    res = s.get(SITE + action)
    usernames = map(lambda u: u.strip(), re.findall('<td align="left" valign="middle">([a-zA-Z0-9\s_-]*)</td>', res.text))

    # id's should be [0..max_id], but get them just in case
    ids = re.findall('act=edit&amp;id=(\d+)"', res.text)
    assert len(ids) == len(usernames)

    groups = re.findall('<td class="listbg">([\s\w,]*)', res.text)

    for (u,i,g) in zip(usernames,ids,groups):
        USERIDS[u] = { 'id' : int(i), 'group' : g.strip() }

def adduser(name, passwd):
    """Add a user under the 'user' group"""
    action = '/system_usermanager.php?act=new'
    form = { 'usernamefld' : name
           , 'passwordfld1' : passwd
           , 'passwordfld2' : passwd
           , 'groups[]'  : ['user']
           , '__csrf_magic' : find_csrf(action)
           , 'save' : 'Save'
           , 'utype' : 'user'
           }


    s.post(SITE + action, form)

def deluser(name):
    """Delete all members of the 'user' group"""
    userid = USERIDS[name]['id']
    assert userid >= 0
    s.get(SITE + '/system_usermanager.php?act=deluser&id=%d' % userid)

def del_all_users_in_group():
    for 

get_users()
print USERIDS
adduser('test3', 'asdf')
