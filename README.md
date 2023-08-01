# auto-server-scripts

## To install:

```
pip install .
```

## To run:

```
aus --type php_composer
```
This will write in the terminal the command required to install the composer (from PHP) in a debian-like webserver.

You can type as well:
```
aus --type php_composer --docker
```
Then it will prefix the output with a `RUN`, so suitable to be written in a Dockerfile, so the composer can be installed in the container in the build time.

