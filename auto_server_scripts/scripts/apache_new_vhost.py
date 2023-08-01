class ApacheNewVhost:
    
    def __init__(self):
        self.vhostName = None
    
    def setVhostName(self, vhostName):
        self.vhostName = vhostName

    def exec(self) -> str:
        
        vhostName = "myVHost"
        documentRoot = "/var/www/html/" + vhostName + "/public"
        
        base_string = '''<VirtualHost {0}:80>
        ServerName {0}

        ServerAdmin webmaster@localhost
        DocumentRoot {1}

        ErrorLog {2}/error.log
        CustomLog {2}/access.log combined

</VirtualHost>
'''

        return base_string.format(vhostName, documentRoot, "${APACHE_LOG_DIR}")
