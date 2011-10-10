import sys

if sys.platform.startswith('darwin'): pass
elif sys.platform.startswith('win32'): pass
elif sys.platform.startswith('linux'): 
    from pynotify import init, Notification
    init("GitBox")


def notify_on_darwin(title, msg='', msgtype="info", timeout=10000):
    return True

def notify_on_windows(title, msg='', msgtype="info", timeout=10000):
    return True

def notify_on_linux(title, msg, msgtype="info", timeout=10000):
    n = Notification(title, msg)
    n.set_timeout(timeout)
    return n.show()
