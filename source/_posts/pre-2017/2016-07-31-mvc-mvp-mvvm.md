---
title: "[Design] MVC, MVP and MVVM"
category: Design
tags: []
comments: true
date: 2016-07-31 00:00
---


# MVC Pattern

Model-View-Controller.

The model and controller logic are **decoupled from user interface (view)**.

![](/images/mvc-pattern.png)

1. Model

   business model + **data access operations** (i.e. data model)

2. View

   **only for displaying data** (received from the controller, transforms the model into UI)

3. Controller **(IMPORTANT)**

   **process incoming requests**. It receives input from users via the View, then process the user's data with the help of Model and passing the results back to the View. Typically, it acts as the coordinator between the View and the Model.

## example

Ruby on Rails, Spring Framework, Apple iOS Development and ASP.NET MVC.

Softwares (not web apps).

# MVP pattern

separate the presentation layer from the logic

The Presenter is responsible for handling all UI events on behalf of the view.

![](/images/mvp-pattern.png)

Unlike view and controller, view and presenter are completely decoupled from each other’s and communicate to each other’s by an interface.

Also, presenter does not manage the incoming request traffic as controller.

## Key Points about MVP

1. User interacts with the View.

1. There is one-to-one relationship between View and Presenter means one View is mapped to only one Presenter.

1. View has a reference to Presenter but View has not reference to Model.

1. Provides two way communication between View and Presenter.

## example

Android, ASP.NET Web Forms applications

# MVVM pattern

This pattern supports two-way data binding between view and View model.

This enables automatic propagation of changes, within the state of view model to the View.

Typically, **the view model uses the observer pattern** to notify changes in the view model to model.

![](/images/mvvm-pattern.png)

## details

The View Model is responsible for exposing methods, commands, and other properties that helps to maintain the state of the view, manipulate the model as the result of actions on the view, and trigger events in the view itself.

## Key Points about MVVM

1. User interacts with the View.

1. There is many-to-one relationship between View and ViewModel means many View can be mapped to one ViewModel.

1. View has a reference to ViewModel but View Model has no information about the View.

1. Supports two-way data binding between View and ViewModel.

## example

Ember.js, WPF, Silverlight

# Ref

Main: http://www.dotnet-tricks.com/Tutorial/designpatterns/2FMM060314-Understanding-MVC,-MVP-and-MVVM-Design-Patterns.html

TLDR: http://www.beyondjava.net/blog/model-view-whatever/
