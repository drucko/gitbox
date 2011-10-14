# gitbox (alpha state, feel free to constribute via github)

Simple and automatically sync deamon for git repositories. A dropbox alternative.


## Requirements

* python2 (2.6-2.7 tested)
* git
* A remote git repository!
* A [PubNub](http://pubnub.com) account if you want push notifications to your other clients!
* [Growl](http://growl.info/) on Mac OS X
* an libnotify client on Linux (included in KDE, Gnome, Unity and XFCE. Minimal WM users should try [statnot](https://github.com/halhen/statnot).)

## Installation

gitbox is available via python package management system [pypi](http://pypi.python.org/pypi/gitbox) :)

    sudo pip install gitbox

If your system does not contain the pip command, just install it with this command:

    sudo easy_install pip


## Configuration

Check out your git repository via git clone!

Make sure "git add .", "git commit -am test", "git push" and "git pull" works in your local repository.


### Enable push notifications

For pushing updates to your other clients we use [PubNub](http://pubnub.com). There is a free account with 5000 messages a day.

Just add a hooks/post-update file with the following content.

    #!/bin/sh
    curl http://pubsub.pubnub.com/publish/<pub-key>/0/<project id>/0/%22update%22

Replace "pub-key" with your pubnub publishing-key and set "project id" to a unique value.

In some git hosting solutions you can set a web hook to the URL above.


## Try

Start gitbox

    gitbox -i <project id> -p <repositori path> -k <pupnub subscription key>

    gitbox -i gb-test -p ../gb-test/ -k sub-xyz-xyz-xyz

for more information try 

    gitbox --help


## Changelog

0.1.3 auto pull and messaging through pubnub

0.1.2 push to remote

0.1.1 monitoring and notifications

## Troubleshooting

### Too many open files

For MacOSX it's required to install the python library watchdog from source
repository because the pip version does not contains the FSEvent library:
http://packages.python.org/watchdog/installation.html#installing-from-source-tarballs
