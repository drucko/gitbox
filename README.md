# gitbox

Simple and automatically sync deamon for git repositories. A dropbox alternative.

## Install

Setup virtual env:
    
    virtualenv --no-site-packages -p python2 --distribute env 

Install required libraries:

    pip install -E env -r requirements.txt


## Try

Activate Virtualenv
    
    . env/bin/activate

Start gitbox

    gbcli -p ./

or 

    gbcli --help

for more information 

## Troubleshooting

### Too many open files

For MacOSX it's required to install the python library watchdog from source
repository because the pip version does not contains the FSEvent library:
http://packages.python.org/watchdog/installation.html#installing-from-source-tarballs
