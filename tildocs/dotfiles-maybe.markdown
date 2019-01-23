# Dotfiles maybe

Stuff to add in dotfiles. Some time. Maybe.

## infinite undo in vim

Can I add something from .vimrc?

If you put the commands:

    set undofile
    set undodir=~/.vim/undodir

You get infinite undo in your files.

Now when you go into a file, delete or add some text and close your terminal
down, the next time you enter vim you can (re|un)do previous operations.

Has saved my ass more times than I care to mention over my career!

----

You can also delete old (older than 90 days) undo files with the following in your .vimrc:
	
    let s:undos = split(globpath(&undodir, '*'), "\n")
    call filter(s:undos, 'getftime(v:val) < localtime() - (60 * 60 * 24 * 90)')
    call map(s:undos, 'delete(v:val)')

[Source](https://news.ycombinator.com/item?id=18898523)
