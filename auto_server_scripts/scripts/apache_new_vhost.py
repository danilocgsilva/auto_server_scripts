class ApacheNewVhost:
    
    def __init__(self):
        self.vhostName = None
        self.documentRoot = None
    
    def setVhostName(self, vhostName):
        self.vhostName = vhostName
        self.documentRoot = "/var/www/html/" + vhostName + "/public"

    def exec(self) -> str:
        
        base_string = '''<VirtualHost {0}:80>
        ServerName {0}

        ServerAdmin webmaster@localhost
        DocumentRoot {1}

        ErrorLog {2}/error.log
        CustomLog {2}/access.log combined

</VirtualHost>
'''

        return base_string.format(self.vhostName, self.documentRoot, "${APACHE_LOG_DIR}")
