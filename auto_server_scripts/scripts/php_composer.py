def exec(docker):

    base_string = "curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer"
    if docker:
        base_string = "RUN " + base_string

    return base_string