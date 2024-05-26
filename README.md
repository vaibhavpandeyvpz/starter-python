# starter-python

Starter template for kick-starting [Python](https://www.python.org/) API projects.

## Prepare

Before running the project, go to [ngrok](https://ngrok.com/) and create a free account.
Once logged in, make note of the auth token.

## Usage

Run below commands in project folder:

```shell
# create .env file
cp .env.dist .env

# update values in .env file e.g., NGROK_AUTHTOKEN

# create ngrok config
cp ngrok.dist.yml ngrok.yml

# create app config
cp config.dist.ini config.ini

# start the services
docker compose up -d
```

Server should be up & running on [127.0.0.1:8000](http://127.0.0.1:8000/).

## Development

This project includes a cron job scheduled to run `index` command (see `app/cli.py`) every hour.
You can also use below command to run it on demand (or any added command) anytime.

```shell
# spawn a shell
docker compose exec cron bash

# run "add-user" command
poe add-user
```

You can test the API by calling `/` endpoint as below:

```shell
curl -X GET \
  -H "accept: application/json" \
  http://127.0.0.1:8000/
```

To get [ngrok](https://ngrok.com/) public URL from container, use below command (requires [jq](https://jqlang.github.io/jq/)):

```shell
curl --silent -X GET http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'
```