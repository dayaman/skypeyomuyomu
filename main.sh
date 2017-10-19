#!/bin/sh
cd $(dirname $0)
pwd

FILE_NAME="name.txt"

if [ -f $FILE_NAME ]; then
   name=$(cat $FILE_NAME)
else
    echo "What is your Skype ID? :\c"
    read name
    ls ~/Library/Application\ Support/Skype/$name
    if [ $? = 0 ]; then
        echo $name > $FILE_NAME
        ln -s ~/Library/Application\ Support/Skype/$name skdir
    else
        echo "そのようなアカウントはありません。"
        exit
    fi
fi

#cp ~/Library/Application\ Support/Skype/$name/main.db main.db
cd src
watch -n 4 "cp ../skdir/main.db main.db && python3 skype.py"
