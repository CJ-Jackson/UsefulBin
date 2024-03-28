#!/usr/bin/env sh
filename=$(pr_gen_create_template)
nvim $filename
if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    pr_gen_create_pr $filename
else
    pr_gen_create_pr $filename | wl-copy
    wl-paste
fi
rm $filename