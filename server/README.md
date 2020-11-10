# Belote server

this project is here to create a game server for the 32 cards game : Belote


## how to build the docker image


to build an arm image from an x86 computer:

'''
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
'''

then:

'''
docker build -t samsja/belote-api:dev-latest .
'''

## NEW:
```
docker buildx build --platform linux/arm/v7,linux/arm64/v8,linux/amd64  -t samsja/belote-api:latest .
```
