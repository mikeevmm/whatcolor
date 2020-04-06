#!/bin/bash

echo "Removing whatcolor link..."
if rm "$HOME/bin/whatcolor"; then
    echo -e "\033[32mDone.\033[0m"
else
    echo "Something went wrong."
fi
