#! /bin/bash
read -p 'commit girin: ' commit

git add .
git commit -m "$commit"
git push origin master
expect "Username for 'https://github.com'"
send "burakgul01"
expect "password"
send "Burak137."
echo ""

