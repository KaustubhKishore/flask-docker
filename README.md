# flask-docker

> docker build --tag dockerflask:1 . 
>
> docker run -d -p 5001:5000 dockerflask:1
>
> localhost:5001 on browser


## Deploy on docker swarm
> docker-machine create --driver virtualbox manager
>
> docker-machine create --driver virtualbox worker1
>
> docker-machine create --driver virtualbox worker2

*Note: A registry is required to create a service with custom image. We can either use a docker registry container or just upload it on docker hub*

#### Create docker service from the image we created in this sample project.
- docker service create --replicas 3 -p 5004:5000 --name flaskservice lordrevolta/dockerflask:1
    - Takes a lot of time. It will look like it's stuck
- Open \<manager\> ip:5004
    - Refresh multiple times and random numbers will appear starting from 1. This means requests are split between the workers(or containers to be precise.)
    - If we scale up you will see the counters at the same position for containers that already exist but the new containers that are created because of scaling up start from 1 as expected.
    
    
### Notes (IGNORE THESE)
##### Upload a docker image on docker hub
- docker login
- docker tag \<image id\> \<dockerhub username\>/imagename:tag
- docker push \<dockerhub username\>/imagename:tag
