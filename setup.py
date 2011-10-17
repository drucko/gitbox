#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages
import py2app

plist = dict(
    # TODO add other macosx plist values like an icon!
    
    # A MainNib file (and main menu) is required for any desktop app
    NSMainNibFile="MainMenu",
    # LSUIElement=True hide the application from macosx dock and process list (=service app)
    LSUIElement=False,
)

setup(
    name = 'gitbox',
    version = '0.1.3',
    description =
        'Simple and automatically sync deamon for git repositories. A dropbox alternative.',
    author = 'Christoph Jerolimov & Daniel Nuemm',
    author_email = 'jerolimov@googlemail.com, daniel.nuemm@googlemail.com',
    url = 'https://github.com/monocult/gitbox',

    install_requires = ['distribute', 'urllib3', 'py-notify>=0.1.1','watchdog>=0.5.4'],
    
    # py2app
    #setup_requires = ['py2app'],
    # TODO evtl. in ein extra verzeichnis schieben? es fehlen noch die normalen gitbox dateien.
    app = ['MacMain.py'],
    data_files = ['MainMenu.nib'],
    options=dict(py2app=dict(plist=plist)),

    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'gitbox  = gitbox.cli:main',
            'gitboxd = gitbox.deamon:main',
        ],
        'gui_scripts': []
    }
)
