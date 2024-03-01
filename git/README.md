# Git

| Script         | Command or Description                                                            |
| :------------- | :-------------------------------------------------------------------------------- |
| gitxAdd        | `git add $@` or `git add -A` (If param is empty)                                  |
| gitxBStash     | Add currnet branch name to top of file `.git/info/bNameStash`                     |
| gitxBStashA    | Apply branch name from top of file `.git/info/bNameStash` or by pos param `$1`    |
| gitxBStashC    | Clear branch name stash by removing `.git/info/bNameStash`                        |
| gitxBStashS    | `cat .git/info/bNameStash`                                                        |
| gitxCo         | `git checkout $@`                                                                 |
| gitxCommit     | `git commit $@`                                                                   |
| gitxDev        | `git checkout {dev branch}`                                                       |
| gitxMain       | `git checkout {main branch}`                                                      |
| gitxMg         | `git merge $@`                                                                    |
| gitxMgDev      | `git merge {dev branch}`                                                          |
| gitxMgMain     | `git merge {main branch}`                                                         |
| gitxPull       | `git pull origin {current branch}`                                                |
| gitxPush       | `git push origin {current branch}`                                                |
| gitxReset      | `git reset --hard HEAD`                                                           |
| gitxStash      | `git stash $@`                                                                    |
| gitxStashA     | `git stash apply $@`                                                              |
| gitxStashC     | `git stash clear`                                                                 |
| gitxSubPull    | `git submodule update --init --recursive`                                         |
| gitxSubUpdate  | `git submodule update --remote --merge`                                           |