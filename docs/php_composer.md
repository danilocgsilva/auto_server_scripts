# Generates a composer php installation command

To generate a script to install the php composer, run after the installation:

```
aus --type php_composer
```

To generate the script suitable for a Docker build stage, type:

```
aus --type php_composer --docker
```
Then it will prefix the output with a `RUN`, so suitable to be written in a Dockerfile, so the composer can be installed in the container in the build time.

