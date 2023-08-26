# Useful Bin

Just a collection of useful script I use for my work, nothing more nothing less.
I prefer not to have to much clutter in my rc files (.zshrc), I'd rather have shell script
in $PATH rather than too much alias.

# Script Documentation

 * [Git](git/README.md)

# Note

To use the script you need to have dash shell installed, alternativly you can just symlink dash
to sh.

```sh
cd /usr/bin; ln -s sh dash
```

My script are posix compliant it should work with most shells.

## Direnv

I use it in conjuntion with [Direnv](https://direnv.net/), you should check it out,
it really useful. Can be used to version SDK (Node, deno and go).

### Exmaple

`direnv edit .`
```
PATH_add /path/to/git/bin
```