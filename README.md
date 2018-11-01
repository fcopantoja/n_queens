### Status
[![Build Status](https://travis-ci.com/fcopantoja/n_queens.png)](https://travis-ci.com/fcopantoja/n_queens)

## N Queens Problem

- Basic solution of n queen problem (https://en.wikipedia.org/wiki/Eight_queens_puzzle) that solves for N ≥ 8
- Iterate over N and store the solutions in postgres using SQLAlchemy
- Basic tests that verify the number of solutions for a given N match
- Dockerized solution
- Travis CI setup
 


#### Run tests with
```
docker-compose build
docker-compose up -d
docker-compose exec solution pytest tests.py
```
