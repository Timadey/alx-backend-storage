#!/usr/bin/bash
# Transfer files from local to remote container
# Remote container has MongoDb
sshpass -p "$1" scp ./* b93355090d2c@b93355090d2c.a2c3e90c.alx-cod.online:/tmp/alx
