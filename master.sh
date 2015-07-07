content=$@
git status
git add --all
git commit -m "$content"
git pull origin master
git push origin master
