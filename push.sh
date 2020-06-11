#! /bin/bash
read -p 'commit girin: ' commit

git add .
git commit -m "$commit"
git push origin master
exec echo "burakgul01"