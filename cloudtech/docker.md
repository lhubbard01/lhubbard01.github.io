---
title: Docker
description: going further than virtualization and solving the problem of containerized computing
layout: post
image: assets/images/infra.png
show_tile_home: false
tile_id: cloudtech
---


Docker is a solution that attends to a few issues relevant to cloud hosted infrastructure.

Virtualization allows for the creation of unqiue operating systems launched at will, that potentially share the same underlying hardware. 

Docker extends the abilities of virtualization through something called an image.
A *Docker Image* is many things. It is a collection of software that is used to execute a specific desired runtime. 

In practice, a Docker image *contains* a specification of software requirements associated with a desired virtualized runtime
This specification is used to build an environment containing all of the necessary requirements to execute our desired runtime.
Notably, it is built by the host OS, so the description constitutes a set of instructions that the host can execute to build our runtime.
Docker runtimes are behaviorally distinct enough to have their own name.
These are termed *Docker Containers*. 
A single Docker image can map to many *Docker containers*. 
This should follow as a natural consequence of the instructive, descriptive nature of the *image*, as instructions can be used many times over to create unique products.
At any rate, a container is a built instance of an image. 
Typically, this consistency is used to create replicas of compute instances, so as to maintain application availability.
This is important to acknowledge, as compute instances can fail for a number of instances in the real world. 
Because business operations typically require a consistent state of those operations (consider financial transactions or instant messaging), maintaining a shared consistency of these data can sometimes be business critical.
In case it isn't obvious, Docker containers aren't the only software that are employed or even built to maintain such consistency. 
The prevailing term in database jargon is "sharding", which is an action performed during state change of a database in a "cluster" of database instances.
As soon as an action of some sort updates a database, this update is shared across the others belonging to the cluster. 
This in effect aims to maintain clones of the overall database entity, so should one of them go down, the database itself is maintained as operational and relatively consistent.
In fact, the use of clusters (which are composed of these distinct entities, sharing the same data individually) is so common practice that it is almost implied in the modern understanding of what a database is.
As such, the instances, which run on different hardware ( perhaps even in different availability zones (covered later)), strive to maintain a shared state of business operational data. 

ASIDE:
You may be wondering why I opted to term its consistency "relative".
This is a highly important idea of distributed computing, but most specifically and importantly in database management.
This idea is the CAP theorem. CAP stands for consistent, available, and partitioned, and the theorem states it is impossible to have a distributed database that provides guarantees of all three components.
If you mull it over, you may find it is consequential from the conflicts that arise between the three components. 
To have something readily available, it must be able to distribute the data it contains from read requests from services or applications using this database.
However, in order to be consistent, the database must always be updating the nodes comprising its network, so the network would have to run a check during each update to know all databases are in the same state.
The partition portion is perhaps more alien, and is technically partition tolerance.
Should data in transit fail, due to networks effects or compute failures, the system must still be able to operate. 
And herein lies the dilemma:
Should we still provide data perhaps being in an inconsistent state with the rest of the network?
Or should we reject read requests until we once again become consistent with the rest of the network?

In the real world, this decision is nuanced by levels of availability and consistency a business entity may determine to be the best compromise for operations.


Docker containers allow for a streamline elastic scaling maintained through a consistent interface, instead of an internal tool or a proprietary solution, as it is open source.
As cloud hosted businesses, services, and applications scale up and down elastically, having
In some cases, containers can also be used to hot swap application versions, effectively providing a seamless transition across an update. 
This is appealing as it minimizes downtime and user frustration. 
This can also be a useful tool for A/B testing 

One of the relatively new features added (within the last few years), was the ability to easily handle multiple containers.
This was one of, if not the primary, use case of Kubernetes.
However Kubernetes has an expansive ecosystem and a relatively loyal following at this point, so a side by side comparison of their benefits is in order.
