#!/bin/bash

#OPTIONS="-H \"Content-Type: application/json\" -i -b cook -c cook"
OPTIONS="-i -b cook -c cook"

if [[ -z "$2" ]]; then
  BASEURL='localhost:5000'
else
  BASEURL=$2
fi

case "$1" in
  test)
    curl $OPTIONS -X GET $BASEURL/test
    ;;
  signup)
    curl -H "Content-Type: application/json" $OPTIONS -X POST -d '{"email": "example@gmail.com", "password": "testtest"}' $BASEURL/users/signup
    ;;
  login)
    curl -H "Content-Type: application/json" $OPTIONS -X POST -d '{"email": "example@gmail.com", "password": "testtest"}' $BASEURL/users/login
    ;;
  logout)
    curl -H "Content-Type: application/json" $OPTIONS -X POST $BASEURL/users/logout
    ;;
esac
