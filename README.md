## Players-backend service
This service is a REST API which saves players and their scores to mysql database.

## Setup
In projects directory run:

- `vagrant up` to launch vagrant with `armada` installed.
- `vagrant ssh` to enter vagrant.

In vagrant:

- armada run mysql --env dev to start `mysql` service.
- `cd /opt/players-backend` to enter projects directory.
- `armada build` to build service.
- `armada run --env dev` to run service.

`players-backend` should run on port 4999.

You also need to create mysql database:


    CREATE DATABASE `players`;
    CREATE TABLE `players`.`players` (
     `player_name` varchar(50) NOT NULL,
     `best_score` int(11) DEFAULT '0',
     PRIMARY KEY (`player_name`)
    )

## Usage
`curl localhost:4999/player/somedude -X POST` to add new player.

`curl localhost:4999/players` to get a list of players.

## Notices
This service uses `hermes`, which loads courier-provided configurations depending on `--env` passed to microservice.