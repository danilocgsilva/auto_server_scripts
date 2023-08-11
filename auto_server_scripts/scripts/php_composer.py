class PhpComposer:
    
    def __init__(self):
        self.isDocker = None
    
    def setDocker(self, active: bool):
        self.isDocker = active

    def exec(self) -> str:
        if self.isDocker == None:
            self.isDocker = False
        base_string = "curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer"
        if self.isDocker:
            base_string = "RUN " + base_string

        return base_string