#!/usr/bin/env bash

API_KEY=$1
API_PSS=$2
GIT_USR=ppgodel
#GIT_REPO=$4

# curl -s "https://api.github.com/users/$GIT_USR/repos" | grep "^    \"url\"" |cut -d "\"" -f 4  | head -n 30 # |  xargs -I % curl -s "%" > archivo.txt

curl -s https://api.github.com/repos/ppGodel/data_mining
# curl -u $API_KEY:$API_PSS "https://api.twitter.com/1.1/search/tweets.json?q=%40${TW_SEARCH}"