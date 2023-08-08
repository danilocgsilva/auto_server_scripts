# Generates the content for a new Apache virtual host

Just run:
```
aus --type apache_new_vhost --server-name my_server
```
**Note that** if you desire to use this option, you are require to provides the `--server-name` parameter as well to be the server name.

You can generate a file instead of just spiting the file:
```
aus --type apache_new_vhost --server-name my_server --generate-file
```

Also, to generate a file, you have the option to set a file to where the generated file should be saved. In this ways:
```
aus --type apache_new_vhost --server-name my_server --generate-file --to-directory /tmp
```

By default, the virtualhost file creates the document root path as
```
/var/www/html/<your_virtualhostname>/public
```
But, you may need to change this a litte. You have the option `--documentroot-suffix` to change this:
```
aus --type apache_new_vhost --server-name my_server --documentroot-suffix web
```
Then, the document path for the virtualhost file will be:
```
/var/www/html/<your_virtualhostname>/web
```

