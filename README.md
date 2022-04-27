# url-shortener

## Description:
An application for shortening and saving the URLs you are interested in.

## Dependencies:

- python = "^3.9"
- Flask = "^2.1.1"
- Flask-SQLAlchemy = "^2.5.1"
- Flask-Migrate = "^3.1.0"
- gunicorn = "^20.1.0"
- hashids = "^1.3.1"

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