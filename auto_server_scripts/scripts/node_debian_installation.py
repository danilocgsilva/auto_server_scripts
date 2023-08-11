class NodeDebianInstallation:

    def __init__(self):
        self.isDocker = False

    def setDocker(self, active: bool):
        self.isDocker = active

    def exec(self) -> str:

        if self.isDocker == None:
            self.isDocker = False
        
        code_lines = [
            "curl -sL https://deb.nodesource.com/setup_20.x | bash -",
            "apt-get update",
            "apt-get install nodejs",
        ]

        return_string = ""
        for code_line in code_lines:
            if self.isDocker:
                return_string += "RUN " + code_line + "\n"
            else:
                return_string += code_line + "\n"
        return return_string
