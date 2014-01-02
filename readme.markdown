# .files
My personal Linux config files. My current set-up is Ubuntu 12.04 and bash
4.2.25(1)-release.

# bashrc set-up on a new machine

    cd ~/kode
    git clone https://github.com/skytreader/.files dotfiles
    cd dotfiles
    ./gobash
    source ~/.bashrc
    ./configit

# vim set-up on a new machine
Assuming the repository has already been cloned as above, just copy the whole
`vim` directory in `/etc/vim`.

    cd vim
    sudo cp -r . /etc/vim

Or just use the included `vimsetup` script.
