# gitbox

Simple and automatically sync deamon for git repositories. A dropbox alternative.

## Install

   pip install gitbox

## Try

Start gitbox

    gitbox -p ./

where "./" is your local repositorie where "git add .", "git commit -am test", "git push" and "git pull" works.

or 

    gitbox --help

for more information 

## Troubleshooting

### Too many open files

For MacOSX it's required to install the python library watchdog from source
repository because the pip version does not contains the FSEvent library:
http://packages.python.org/watchdog/installation.html#installing-from-source-tarballs
