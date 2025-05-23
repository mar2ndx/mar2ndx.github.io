---
title: "[Design] OOD Design of Elevator"
category: Design
tags: []
comments: true
date: 2014-08-26 00:00
---


### Question

[link](http://thought-works.blogspot.sg/2012/11/object-oriented-design-for-elevator-in.html)

> Object Oriented design for Elevator in a multi-storied apartment

### A Single Elevator

Use Case:

1. User
   1. press a button to summon the lift
   1. press a button to get to a specific floor
1. Button
   1. floor button and level button
   1. illuminates when pressed
   1. place an 'elevator request' when pressed
1. Elevator
   1. moves up/down
   1. open/close the door

![](/images/elevator-class-diagram.png)

**ElevatorRequests Class**

Each button press results in an elevator request which has to be served. Each of these requests is tracked at a global place. ElevatorRequests, the class which stores elevator requests can use different strategies to schedule the elevator requests.

**ElevatorController**

The elevator is controlled by a controller class which we call ElevatorController. The elevator controller instructs the elevator what to do and also can shutdown/start up the elevator of the building. The elevator controller reads the next elevator request to be processed and serves it.

**Button (Abstract) Class**

Button is abstract class defining common behavior like illuminate, doNotIlluminate. FloorButton, ElevatorButton extend Button type and define placeRequest() which is invoked when the button is pressed.

In conclusion, **ElevatorController** runs the show by reading the **ElevatorRequests** to process and instructing the **Elevator** what to do. User send request by pressing **Buttons**.

### Extend the answer to multiple elevators

1. Each elevator have 1 controller.

1. Floor based requests can be served by any elevator, thus these requests are added to a common area accessible by all controllers.

1. Each elevator controller runs as a separate thread and checks if it can process a floor request. Mind synchronization issues.
