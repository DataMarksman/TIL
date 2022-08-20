@echo off
git pull origin master
git add .
git commit -m '%date%_commit'
git push origin master