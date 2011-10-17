
#
# compile and run:
#
# clear; python setup.py py2app -A && dist/gitbox.app/Contents/MacOS/gitbox
#
# TODO build and dist can only be removed as root!? :(
#

import objc
from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper

# For now just a test!!!! ;)

class MyApp(NSApplication):
    
    def __new__(cls):
        return cls.alloc().init()
    
    # NOT CALLED :((((
    def applicationDidFinishLaunching_(self, notification):
        print('did finish')
        
        systemTray = NSStatusBar.systemStatusBar()
        
        textInputItem = NSMenuItem.alloc().init()
        textInputItem.setTitle_('test')
        #action:@selector(menuItemSelected:)
        #keyEquivalent:@"Q"];
        textInputItem.setTarget_(textInputItem);
        textInputItem.setEnabled_(True);
        
        systemTrayMenu = NSMenu.alloc().init();
        systemTrayMenu.addItem_(textInputItem);
        
        systemTrayIcon = systemTray.statusItemWithLength_(NSVariableStatusItemLength)
        systemTrayIcon.setMenu_(systemTrayMenu);
        #does not work: systemTrayIcon.setImage_(NSImage.imageNamed("git.png"));
        systemTrayIcon.setTitle_("git-autosync");
        systemTrayIcon.setToolTip_("git-autosync");
        systemTrayIcon.setHighlightMode_(True);


if __name__ == "__main__":
    print(1)
    app = MyApp()
    print(2)
    #    app.run()
    print(3)
    AppHelper.runEventLoop()
    print(2)

