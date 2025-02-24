---
layout: post
title: "[Design] Strategy design pattern "
comments: true
category: Design
tags: []
---

# Overview

**[Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern)** (also known as the policy pattern) is a design pattern that **enables an algorithm's behavior to be selected** at runtime.

For instance, a class that performs **validation on incoming data** may use a strategy pattern to select a validation algorithm **based on the type of data**, the source of the data, user choice... These factors are not known **until run-time**...

## A car example

Since accelerate and brake behaviors change frequently between models, **a common approach is to implement these behaviors in subclasses**. This approach has significant drawbacks: accelerate and brake behaviors **must be declared in each new Car model**.

![](/images/600px-StrategyPattern_IBrakeBehavior.png)

The strategy pattern uses **composition** instead of inheritance. This allows:

1. better **decoupling between the behavior** and the class that uses it. (i.e. behavior can be changed without breaking the classes that use it)

1. classes can switch between behaviors by changing the specific implementation used without requiring any significant code changes.

Code:

    /* Encapsulated family of Algorithms
     * Interface and its implementations
     */
    public interface IBrakeBehavior {
        public void brake();
    }

    public class BrakeWithABS implements IBrakeBehavior {
        public void brake() {
            System.out.println("Brake with ABS applied");
        }
    }

    public class Brake implements IBrakeBehavior {
        public void brake() {
            System.out.println("Simple Brake applied");
        }
    }


    /* Client which can use the algorithms above interchangeably */
    public abstract class Car {
        protected IBrakeBehavior brakeBehavior;

        public void applyBrake() {
            brakeBehavior.brake();
        }

        public void setBrakeBehavior(IBrakeBehavior brakeType) {
            this.brakeBehavior = brakeType;
        }
    }

    /* Client 1 uses one algorithm (Brake) in the constructor */
    public class Sedan extends Car {
        public Sedan() {
            this.brakeBehavior = new Brake();
        }
    }

    /* Client 2 uses another algorithm (BrakeWithABS) in the constructor */
    public class SUV extends Car {
        public SUV() {
            this.brakeBehavior = new BrakeWithABS();
        }
    }


    /* Using the Car Example */
    public class CarExample {
        public static void main(String[] args) {
            Car sedanCar = new Sedan();
            sedanCar.applyBrake();  // This will invoke class "Brake"

            Car suvCar = new SUV();
            suvCar.applyBrake();    // This will invoke class "BrakeWithABS"

            // set brake behavior dynamically
            suvCar.setBrakeBehavior( new Brake() );
            suvCar.applyBrake();    // This will invoke class "Brake"
        }
    }

This gives greater flexibility in design and is in harmony with the **[Open/closed principle](https://en.wikipedia.org/wiki/Open/closed_principle)** (OCP) that states that **classes should be open for extension but closed for modification**.
