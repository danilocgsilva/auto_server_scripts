# Generates the content for a new Apache virtual host

Just run:
```
aus aus --type apache_new_vhost --server-name my_server
```
**Note that** if you desire to use this option, you are require to provides the `--server-name` parameter as well to be the server name.

You can generate a file instead of just spiting the file:
```
aus aus --type apache_new_vhost --server-name my_server --generate-file
```

Also, to generate a file, you have the option to set a file to where the generated file should be saved. In this ways:
```
aus aus --type apache_new_vhost --server-name my_server --generate-file --to-directory /tmp
```
