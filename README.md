
  <h3 align="center">Herogi Interview Runner Profile</h3>

  <p align="center">
     A fully fledged, production ready, microservice based application to list runners and their paces.
    <br />
    ·
    <a href="https://github.com/sodaliAyran/herogi-interview/issues">Report Bug</a>
    ·
    <a href="https://github.com/sodaliAyran/herogi-interview/issues">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Decisions](#decisions)
  * [Why Microservices?](#why-microservices)
  * [Why Postgresql?](#why-postgresl)
  * [Why Flask?](#why-flask)
  * [Why Docker, Docker Compose?](#why-docker-docker-compose)
* [Project Rundown](#project-rundown)
  * [Database](#database)
  * [Backend](#backend)
  * [Frontend](#frontend)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This is a single page including a backend, a frontend and a database. The problem was to create a single page web application with the provided data that does the following:
* Runners based on their average pace. (Time(minute) per kilometer)
* Provide sorting functionality based on average pace, distance and total time
* Also include username, age, gender in the UI

Also there was a Bonus Points Section with the following:
* An option to group users by their age group (group1: 20-30, group2: 30-40, group3: 40 - 60) -> Which I did
* Use React --> Which I also did
* Use Scala --> That is something I won't do for extra points.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Reactjs](https://reactjs.org/)
* [Postgresql](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* docker
* docker-compose

### Installation

1. Clone the repo
```sh
$ git clone https://github.com/sodaliayran/herogi-interview.git
```
3. Build the containers
```sh
$ docker-compose build
```
4. Run them
```sh
$ docker-compose up
```

Tests will run automatically when you build the image. (Not ideal because why should you download a testing library to you production system but I like seeing the dots.)
After that just hit http://localhost:3000 on your browser.

or

```sh
$ curl http://localhost:5000/get_values
```

for API access.


<!-- USAGE EXAMPLES -->
## Usage

Here is a quick demonstration of how to start up and use this project. 


<!-- DECISION EXPILAINING -->

## Decisions 

### Why Microservices?

It' simple, because they are scalable, easily managable, reusable, plugable... and much more.
To expand upon this, for example if you want to scale this system using Kubernetes or something similar, you can do it.
If you want to monitor different parts by using different applications, you can do it.
If you want to change the database to another one or get rid of SQL for some NOSQL database, you can do it.
If you want to replace backend with something like Scala without touching anything on the database and frontend, YOU CAN DO IT.
All it takes is just a little bit(or none) of code refactoring and some changes in the enviroment variables and voilà you are all set. That's the power of microservices

### Why Postgresql?

No reason. I could have used any other relational database or non relational database (Although the problem was more appropriate for a relational one.) and it still would have worked fine. I just like Postgresql.

### Why Flask?

There was a bonus for using Scala so why did I choose Flask for backend? That's because I'm used to it. I have developed many web services using Flask and I can definitely say that it gets the job done pretty well. To add more to this Flask is really easy to use and deploy, has many powerful community created plugins and written in Python. A language that get more popular day by day. Comparing Scala to Python one can say without a doubt that Scala lost it's popularity, and although it still has uses on Big Data, many companies abandoned Scala based web applications.

### Why Reactjs?

Ahhh React, the new thing Papa Facebook gave us. It's on everyone's minds and hands until it'll got replaced of course. You might be suprised but I used React not because I want the bonus points but because I recently started taking a React Native course and wanted have some practice with the real thing as well. Normally I would have used pure HTML, CSS and Javascript because that's what I'm used to but I believe it's time that I should embrace the future since HTML+CSS+Javascript combo has run it's time. Also it's pretty fast creating a React App from scratch.  

### Why Docker, Docker Compose?

I'm building a microservice architecture, of course I have to use some kind of containerization. Also I'm building severeal services that communicate with each. I have to use docker-compose so that I don't have to rebuild and deploy each one them everytime I make a change.

## Project Rundown

### Database

Here is the provided data fields

User:
- id (int, primary_key)
- username (string)
- age (integer)

Pace:
- user_id (foreign_key user)
- total_time_in_minutes (int)
- distance_in_meters (int)

Using these I created two tables. The problem didn't specify using a database but I did it just for the sake of it. Do I think it's an overkill. Yes, yes I do.
While I'm at it I should also mention that there were some missing information in the provided data. For example there was a Pace belonged to a User with the id 4 but there wasn't any User with the id 4 on the Users table. So I took to liberty to add myself as the User with id 4. Also, project requirements stated that in the end result User gender should be shown but the gender information wasn't included in the data. So again I filled in the information based on their usernames. (I know I'm in no place to assign gender roles to  people based on their names but I had to make a choice. And still I value represantation so I made user1 gender queer so that he/she/etc can be whatever he/she/etc. want. Also I'm pretty sure you can't have numbers in your name. Unless your father worths 93 billion USD)

### Backend

A simple overkill middleware app factory with different configurations for development and production environments. I used marshmallow to serialize database objects. If you check the schemas you can see that I'm calculating the age group and the average pace while serializing the data. I could have added that fields while seeding the database but I assumed the database already existed with the given fields and I had no permission to add or remove fields on the database.
There are also test that I wrote just do show you that I can actually write test and TDD is something I do occasionally. The tests themselves don't do much (They are just HTTP GET functions) but they are there. You can run the tests with `$ pytest` after you installed the requirements. Why I didn't use unittest for such simple tests you might ask. The answer is I thought I already overkilled everything might as well do the same thing to tests. Lastly I should also mention that the middleware runs with gunicorn, so it's production ready.

### Frontend

Well I'm not a frontend expert therefore it doesn't look good but then again maybe you should have used Excel for displaying data on a table. I used react table to display the data. It was interesting cause when using react table you do everything by using functions. So I'm pretty sure it's quite lightweight. But that didn't stop me from importing some heavy libraries that I only used two maybe three classes of. A small price for salvation. You can sort data by clicking the headers and filter age groups by selecting one. There is also pagination but it doesn't do anything since there isn't much data. Finally the app runs on production with nginx.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **appreciated**.

1. Fork the Project
2. Create your Feature Branch (`$ git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`$ git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`$ git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

İlke Elvan - [@ilkebey](https://instagram.com/ilkebey) - ilkeelvan@gmail.com

Project Link: [https://github.com/sodaliAyran/herogi-interview](https://github.com/sodaliAyran/herogi-interview)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [pytest](https://docs.pytest.org/en/stable/)
* [gunicorn](https://gunicorn.org/)
* [Postgresql](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)
* [Reactjs](https://reactjs.org/)
* [React Table](https://github.com/tannerlinsley/react-table)
* [nginx](https://www.nginx.com/)
