# Flask APP

This repo can be used as a based for a Flask application monitored with grafana, prometheus and node exporter

## 1- Prerequisite

- Docker : 20.10.22, build 3a2c30b
- Docker Compose : v2.15.1
- Python : 3.9.6

## 2- Launch the app

- _Note_ :
  - You must be in the repo folder
  - **The ports 9090, 9100, 5000, 3000 must not be in use**

```cmd
docker-compose up
```

## 3- Useful information

- prometheus user metrics implemented for the flask app :
  - by_end_counter_total : count the amount of connection on <http:localhost:5000>

- Path :
  - Flask app : <http://localhost:5000>
  - Grafana : <http://localhost:3000>
  - Prometheus : <http://localhost:9090>
  - Node Exporter : <http://localhost:9100>

Note : Add /metrics to the path above to access the metrics for flask app, prometheus and node exporter

- Grafana
  - Default user login informations : (it will ask to change the password at the first connection)
    - login : admin
    - password : admin
  - Add a data source :
    - Login with the grafana path (see above)
    - From the left menu navigate to Configuration/Data Source -> Add data source
    - Select Prometheus from the list
    - Enter <http://prometheus:9090> as the URL
    - Click Save & Test
  - Create a dashboard
    - From the left menu navigate to dashboard -> + New Dashboard
    - Add a graph and select Prometheus data source
