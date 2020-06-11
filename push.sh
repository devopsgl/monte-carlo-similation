#! /bin/bash
read -p 'commit girin: ' commit

git add .
git commit -m "$commit"
git push origin master
expect "Username"
send "burakgul01"
expect "password"
send "Burak137."
echo ""

