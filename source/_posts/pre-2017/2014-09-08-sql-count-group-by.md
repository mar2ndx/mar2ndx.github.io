---
title: "[CC150v4] 15.1 SQL count and group by statement "
category: CC150v4
tags: []
comments: true
date: 2014-09-08 00:00
---


### Question

> Write a method to find the number of employees in each department.

### Answer

    select
        Dept_Name,
        Departments.Dept_ID,
        count(*) as ‘num_employees’
    from
        Departments
    left join
        Employees
    on
        Employees.Dept_ID = Departments.Dept_ID
    group by
        Departments.Dept_ID, Dept_Name
