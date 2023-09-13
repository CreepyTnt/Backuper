import utils as api
from win10toast import ToastNotifier

if api.days_since_last_backup() > int(api.get_options()['frequency']):
    api.backup_all()
    
    toaster = ToastNotifier()

    try:
        toaster.show_toast("Backuper", f"Backup completed {api.get_options()['backup_to']}", duration=10)
    except:
        print('notification sent')


