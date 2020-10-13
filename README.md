
  <h3 align="center">Herogi Interview Runner Profile</h3>

  <p align="center">
     A fully fledged, production ready, micro service based application to list runners and their paces.
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
* [Roadmap](#roadmap)
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

Also there was a Bonus points section with the following:
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
git clone https://github.com/your_username_/Project-Name.git
```
3. Build the containers
```sh
docker-compose build
```
4. Run them
```sh
docker-compose up
```

Tests will run automatically.
After that just hit http://localhost:3000 

or

```sh
curl http://localhost:5000/get_values
```

for API access.


<!-- USAGE EXAMPLES -->
## Usage

Here is a quick rundown of how to start up and use this project. 


<!-- DECISION EXPILAINING -->

## Decisions 

### Why Microservices?

It' simple, because they are scalable, easily managable, reusable, plugable... and much more.
To expand upon this, for example if you want to scale this system using Kubernetes or something similar, you can do it.
If you want to monitor different parts by using different applications, you can do it.
If you want to change the database to another one or get rid of SQL for some NOSQL database, you can do it.
If you want to replace backend with something like Scala without touching anything on the database and frontend, YOU CAN DO IT.
All it takes is just a little bit(or none) of code refactoring and some changes in the enviroment variables and voilà you are all set. That's the power of microservices

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
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
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
