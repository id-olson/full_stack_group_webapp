# Git Cheat Sheet

Always `git pull` on master before you start editing if you plan on pushing very soon

#### Creating branches

`git checkout main && git checkout -b gs/12-NAME`

#### Commiting branches

`git add . && git commit -m "YOUR MESSAGE" && git push`

#### Many commits behind. Delete whatever I have and Fetch me the latest head

`git reset --hard && git fetch main`

#### Merge into Master (Might have to resolve conflicts)

`git checkout main && git merge gs/12-Name`

#### Pull all remote branches

```bash
git branch -r | grep -v '\->' | sed "s,\x1B\[[0-9;]*[a-zA-Z],,g" | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git fetch --all
git pull --all
```

#### WSL Cred Manager

`git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"`
