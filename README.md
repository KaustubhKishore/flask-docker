# flask-docker

> docker build --tag dockerflask:1 . 
>
> docker run -d -p 5001:5000 dockerflask:1
>
> localhost:5001 on browser


## Deploy on docker machine
> docker-machine create --driver virtualbox manager
>
> docker-machine create --driver virtualbox worker1
>
> docker-machine create --driver virtualbox worker2

*Note: A registry is required to create a service with custom image. We can either use a docker registry container or just upload it on docker hub*

#### Upload a docker image on docker hub
- docker login
- docker tag <image id> <dockerhub username>/imagename:tag
- docker push <dockerhub username>/imagename:tag

#### Create docker service from the image we created
- docker service create --replicas 3 -p 5004:5000 --name flaskservice <dockerhub username>/imagename:tag
    - Takes a lot of time. It will look like it's stuck
- Open <manager ip>:5004
    - Refresh multiple times and random numbers will appear starting from 1. This means requests are split between the workers(or containers to be precise.)
