# Project Title: Event Listeners (Signals), ORM & Advanced ORM Techniques

## About The Project
In modern web applications, **performance, modularity** and **clean architecture** are essential. Django provides powerful tools that help developers build robust and maintainable backend systems. 3 core concepts that support these goals are:
	- 1. **Event Listeners using Django Signals**
	     Signals allow decoupled parts of an application to communicate by emitting and		and listening to events. This enables actions like sending confirmation emails		   or logging activities whenever a specific model action(like saving or
	     deleting occurs—without tightly coupling that logic to your views or models.
	- 2. **Django ORM & Advanced ORM Techniques**
	     Django’s Object-Relational Mapper (ORM) enables developers to interact with
	     the database using Python code instead of SQL. It also provides advanced tools		to optimize performance—like `select_related`, `prefetch_related` and query
	     annotations helping avoid common issues like the N+1 query problem.
	- 3. **Basic Caching**
	     Caching stores frequently accessed data so it can be retrieved faster. Django 		supports various caching strategies (view-level, template fragment, low-level 		   caching), which can drastically reduce page load time and database load
Together, these techniques improve **application responsiveness**, **database efficiency** & **code scalability** making them crucial tools for Django backend developers.

## Learning Objectives
By the end of this module, learners will be able to:
- Explain and implement Django **Signals** to build event-driven features
- Use Django **ORM** to perform CRUD operations and write efficient queries.
- Apply **advanced ORM** techniques for optimizing database access.
- Implement **basic caching** strategies to enhance performance.
- Follow **best practices** to ensure maintainable, decoupled, and performant backend code.
