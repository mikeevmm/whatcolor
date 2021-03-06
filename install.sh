#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo -e "This script will add a symlink from"
echo -e "$HOME/bin/"
echo -e "to"
echo -e "$DIR/whatcolor"
echo -e "so that you can call whatcolor from any directory."
read -p $'\033[33mIs this ok [N/y]?\033[0m ' -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

if [ ! -d $HOME/bin ]; then
    echo -e "$HOME/bin does not exist, creating that directory."
    read -p "Is this ok [N/y]? " -n 1 -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]
    then
        [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
    fi
    mkdir $HOME/bin
    export PATH="$HOME/bin:$PATH"
    echo -e "\033[32mCreated $HOME/bin\033[0m"
fi

if ln -s "$DIR/whatcolor.py" "$HOME/bin/whatcolor"
then
    echo -e "\033[32mDone.\033[0m"
    echo -e "Call \`whatcolor RGB\` to try it out."
else
    echo -e "\033[91mSomething went wrong.\033[0m"
fi
