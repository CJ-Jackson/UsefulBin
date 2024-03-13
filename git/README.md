# Git

| Script        | Command or Description                                                         |
|:--------------|:-------------------------------------------------------------------------------|
| _gitAdd       | `git add $@` or `git add -A` (If param is empty)                               |
| _gitBStash    | Add currnet branch name to top of file `.git/info/bNameStash`                  |
| _gitBStashA   | Apply branch name from top of file `.git/info/bNameStash` or by pos param `$1` |
| _gitBStashC   | Clear branch name stash by removing `.git/info/bNameStash`                     |
| _gitBStashS   | `cat .git/info/bNameStash`                                                     |
| _gitCo        | `git checkout $@`                                                              |
| _gitCommit    | `git commit $@`                                                                |
| _gitDev       | `git checkout {dev branch}`                                                    |
| _gitMain      | `git checkout {main branch}`                                                   |
| _gitMg        | `git merge $@`                                                                 |
| _gitMgDev     | `git merge {dev branch}`                                                       |
| _gitMgMain    | `git merge {main branch}`                                                      |
| _gitPull      | `git pull origin {current branch}`                                             |
| _gitPush      | `git push origin {current branch}`                                             |
| _gitReset     | `git reset --hard HEAD`                                                        |
| _gitStash     | `git stash $@`                                                                 |
| _gitStashA    | `git stash apply $@`                                                           |
| _gitStashC    | `git stash clear`                                                              |
| _gitSubPull   | `git submodule update --init --recursive`                                      |
| _gitSubUpdate | `git submodule update --remote --merge`                                        |