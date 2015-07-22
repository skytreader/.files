# .files
My personal Linux config files. I am using this on the following platforms:

- Ubuntu 12.04 with bash 4.2.25(1)-release
- Ubuntu 14.04 with bash 4.3.11(1)-release

# bashrc set-up on a new machine

    cd ~/kode
    git clone https://github.com/skytreader/.files dotfiles
    cd dotfiles
    ./gobash
    source ~/.bashrc
    ./configit

## bashrc update

    ./gobash
    source ~/.bashrc

**Important:** Execute the two commands above in the directory of this repo. You
need to manually `source ~/.bashrc` (i.e., don't put those two lines in a script
anymore).

# vim set-up on a new machine
Assuming the repository has already been cloned as above, just copy the whole
`vim` directory in `/etc/vim`.

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
