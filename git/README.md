# Git

| Script           | Command or Description                                                         |
|:-----------------|:-------------------------------------------------------------------------------|
| --git-add        | `git add $@` or `git add -A` (If param is empty)                               |
| --git-b-stash    | Add currnet branch name to top of file `.git/info/bNameStash`                  |
| --git-b-stash-a  | Apply branch name from top of file `.git/info/bNameStash` or by pos param `$1` |
| --git-b-stash-c  | Clear branch name stash by removing `.git/info/bNameStash`                     |
| --git-b-stash-s  | `cat .git/info/bNameStash`                                                     |
| --git-co         | `git checkout $@`                                                              |
| --git-commit     | `git commit $@`                                                                |
| --git-dev        | `git checkout {dev branch}`                                                    |
| --git-main       | `git checkout {main branch}`                                                   |
| --git-mg         | `git merge $@`                                                                 |
| --git-mg-dev     | `git merge {dev branch}`                                                       |
| --git-mg-main    | `git merge {main branch}`                                                      |
| --git-pull       | `git pull origin {current branch}`                                             |
| --git-push       | `git push origin {current branch}`                                             |
| --git-reset      | `git reset --hard HEAD`                                                        |
| --git-stash      | `git stash $@`                                                                 |
| --git-stash-a    | `git stash apply $@`                                                           |
| --git-stash-c    | `git stash clear`                                                              |
| --git-sub-pull   | `git submodule update --init --recursive`                                      |
| --git-sub-update | `git submodule update --remote --merge`                                        |