import json
import os
import shutil
from datetime import datetime
from datetime import date
def set_options_backuplocation(location):
    with open ('./config.json', 'r') as f:
        options_file = json.loads(f.read())
    with open ('./config.json', 'w') as f:
        #options_file = json.loads(f.read())
        options_file['backup_to'] = location
        f.write(json.dumps(options_file))

def get_options():
    with open('./config.json', 'r') as f:
        return json.loads(f.read())

    # with open(os.path.join(dir_path, 'config.json'), 'r') as f:
    #     backup_to = json.loads(f.read())['backup_to']

    # with open(os.path.join(dir_path, 'last_backup.json'), 'r') as f:
    #     last_backup = f.read()


    # with open(os.path.join(dir_path, 'config.json'), 'r') as f :
    #     days = json.loads(f.read())['frequency']


def set_options_backup_frequency(frequency):
    with open ('./config.json', 'r') as f:
        options_file = json.loads(f.read())
    with open ('./config.json', 'w') as f:
        options_file['frequency'] = frequency
        f.write(json.dumps(options_file))

def set_last_backup(year, month, day):
    with open ('./last_backup.json', 'w') as f:
        f.write(json.dumps([year, month, day]))

def backup(item):
    with open ('./folders.json', 'r') as f:
        backup_from = json.loads(f.read())[item]
    
    if os.path.exists(os.path.join(get_options()['backup_to'], f'{item} {os.path.basename(backup_from)}')):
        print ('true')
        shutil.rmtree(os.path.join(get_options()['backup_to'], f'{item} {os.path.basename(backup_from)}'))

    print (backup_from)
    print (get_options()['backup_to'], f'{item} {os.path.basename(backup_from)}')
    shutil.copytree(backup_from, os.path.join(get_options()['backup_to'], f'{item} {os.path.basename(backup_from)}'))

    set_last_backup(datetime.now().year, datetime.now().month, datetime.now().day)

def days_since_last_backup():
    with open('./last_backup.json', 'r') as f:
        d0 = json.loads(f.read())
    d0 = date(d0[0], d0[1], d0[2])
    
    d0 = date(d0.year, d0.month, d0.day)
    now = datetime.now()
    d1 = date(now.year, now.month, now.day)
    delta = d1 - d0
    #print (delta.days)
    return delta.days



def backup_all():
    with open('./folders.json', 'r') as f:
        folders = json.loads(f.read())
    i = 0
    while i < 5:
        if os.path.exists(folders[i]):
            backup(i)
        i += 1

# backup_all()
# set_last_backup(2023, 9, 13)
print (days_since_last_backup())