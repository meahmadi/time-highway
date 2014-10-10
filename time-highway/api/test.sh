#!/bin/bash

#OPTIONS="-H \"Content-Type: application/json\" -i -b cook -c cook"
OPTIONS="-i -b cook -c cook"

if [[ -z "$2" ]]; then
  BASEURL=http://localhost:5000
else
  BASEURL=$2
fi
echo $BASEURL

case "$1" in
  test)
    curl $OPTIONS -X GET $BASEURL/test
    ;;
  signup)
    curl -H "Content-Type: application/json" $OPTIONS -X POST -d '{"email": "example@gmail.com", "password": "testtest"}' $BASEURL/users/signup
    ;;
  login)
    curl -H "Content-Type: application/json" $OPTIONS -X POST -d '{"email": "vahid@kharazi.net", "password": "123qwe"}' $BASEURL/users/login
    ;;
  logout)
    curl -H "Content-Type: application/json" $OPTIONS -X POST $BASEURL/users/logout
    ;;
  userstory_g)
    curl -H "Content-Type: application/json" $OPTIONS -X GET $BASEURL/user/stories
    ;;
  userstory_p)
    curl -H "Content-Type: application/json" $OPTIONS -X POST -d '{"story_id": "54383442b0b7080641a808da", "events": ["54383442b0b7080641a808da", "54383442b0b7080641a808db"]}' $BASEURL/story
    ;;
esac
