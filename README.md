# url-shortener
<a href="https://codeclimate.com/github/emp7yhead/url-shortener/maintainability"><img src="https://api.codeclimate.com/v1/badges/10815e33b70070f3ca07/maintainability" /></a>
<a href="https://codeclimate.com/github/emp7yhead/url-shortener/test_coverage"><img src="https://api.codeclimate.com/v1/badges/10815e33b70070f3ca07/test_coverage" /></a>
[![Check lint](https://github.com/emp7yhead/url-shortener/actions/workflows/check-lint.yml/badge.svg)](https://github.com/emp7yhead/url-shortener/actions/workflows/check-lint.yml)
## Description:
An application for shortening and saving the URLs you are interested in.

https://flask-url-shortener.onrender.com/

## Screenshots (click to watch fullscreen):
<a href="https://i.imgur.com/kGbdnOl.png"><img  src="https://i.imgur.com/kGbdnOl.png" alt="main page" width="320"></a>
<a href="https://i.imgur.com/gpy3opM.png"><img  src="https://i.imgur.com/gpy3opM.png" alt="statictics page" width="320"></a>

## Dependencies:

- python = "^3.9"
- Flask = "^2.1.1"
- Flask-SQLAlchemy = "^2.5.1"
- Flask-Migrate = "^3.1.0"
- gunicorn = "^20.1.0"
- hashids = "^1.3.1"
- psycopg2-binary = "^2.9.3"
- python-dotenv = "^0.20.0"

## Installation:
### via poetry:
- clone repo:
```
git clone https://github.com/emp7yhead/url-shortener.git
cd url-shortener
```
- install dependencies:
```
make install
```
- initialize migrations:
```
make migration
```
- run app:
```
make run
```

### via Docker:
- clone repo:
```
git clone https://github.com/emp7yhead/url-shortener.git
cd url-shortener
```
- install dependencies:
```
docker-compose build
```
- run app:
```
docker-compose up
```
