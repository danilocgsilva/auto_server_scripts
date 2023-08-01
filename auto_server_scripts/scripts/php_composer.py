class PhpComposer:
    
    def __init__(self):
        self.isDocker = None
    
    def setDocker(self: bool):
        self.isDocker = None

    def exec(self) -> str:
        base_string = "curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer"
        if self.isDocker:
            base_string = "RUN " + base_string

        return base_string