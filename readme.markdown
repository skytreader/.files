# .files
My personal Linux config files. I am using this on the following platforms:

- Ubuntu 16.04 with bash 4.3.46(1)-release
- Ubuntu 20.04 with bash 5.0.17(1)-release

# bashrc set-up on a new machine

## Pre-set-up set-up

Some gotcha's for complete user-friendliness.

    ~$ sudo apt-get install git
    ~$ mkdir kode

Optionally, install virtualenv via [virtualenv-burrito](https://github.com/skytreader/virtualenv-burrito). Not needed but some
errors might occur during set-up because some aliases are for virtualenvs.

    curl -sL https://raw.githubusercontent.com/skytreader/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

## Actual set-up

    cd ~/kode
    git clone https://github.com/skytreader/.files dotfiles
    cd dotfiles
    ./gobash
    source ~/.bashrc
    ./configit

Additionally, you can set-up some of the additional tools I use by invoking the
scripts at `setup/`. Each script is named for the distro for which it can be
used (currently only `ubuntu`).

## bashrc update

    ./gobash
    source ~/.bashrc

**Important:** Execute the two commands above in the directory of this repo. You
need to manually `source ~/.bashrc` (i.e., don't put those two lines in a script
anymore).

For a quick check on possibly-outdated bash functions, the `dfiles_ver` command
is provided.

# vim set-up on a new machine
Assuming setup script for your distro has been run (it should install `vim` if
it is not included by default), just copy the whole `vim` directory in
`/etc/vim`.

    cd vim
    sudo cp -r . /etc/vim

Or just use the included `vimsetup` script.

## ...on not-new machines
If you update anything in the `vim` directory, use the included `vimsetup`
script.

If you need to install other vim syntax stuff not in the `vim` directory, you
may use the `vip` command defined (assuming bash has been set-up).

## vim files credit

I could've just `git submodule`d them from their respective repositories but I
figured that might take more work/hack scripts for the simple and pain-free
new-machine set-up that is the purpose of this repo so I'll just credit them here.

- [Arduino syntax](https://bitbucket.org/johannes/arduino-vim-syntax) by Johannes Hoff
- [Jinja2 syntax](https://github.com/Glench/Vim-Jinja2-Syntax) by Glench

# Miscellaneous Notes

## Installing Packages
Some packages only require you to uncompress a ZIP or TAR file then add the
uncompressed path to your `PATH` environment variable. To install such packages,
just use `anywhere` and `anyscript`, defined in `bash_personal`.

`anywhere` moves a file/directory to `/opt/bin` to keep binaries organized.
However, if it is a directory, it is not directly invokable yet. So use...

`anyscript` creates an executable script in `/opt/bin`. In this script, invoke
whatever needs to be invoked in the directory you just moved to `/opt/bin`.

## On `JAVA_HOME`
Android Studio and Apache Maven has conflicting ideas on where `JAVA_HOME` should
be. Android Studio wants it to contain the directory where the JDK (i.e., `javac`)
can be found. Maven, on the other hand, wants it where `bin/javac` can be found.

To remedy this, my set-up of Android Studio (see note above) creates a script
with its own `export JAVA_HOME` directive just before firing up the IDE.

Maven takes precedence in my `bashrc` since I use it more often.

## Configs
The files in the `config` directory are meant to be sent to the default
`~/.config` directory. After adding/modifying config files, do

    cp -r config/* ~/.config

Notice the form of the invocation: this ensures that both directories are "merged".
