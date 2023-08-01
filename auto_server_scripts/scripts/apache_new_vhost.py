class ApacheNewVhost:
    
    def __init__(self):
        self.vhostName = None
        self.documentRootSuffix = "public"
    
    def setVhostName(self, vhostName: str):
        self.vhostName = vhostName

    def setDocumentRootSuffix(self, documentRootPrefix: str):
        self.documentRootSuffix = documentRootPrefix

    def exec(self) -> str:

        documentRoot = "/var/www/html/" + self.vhostName + "/" + self.documentRootSuffix
        
        base_string = '''<VirtualHost {0}:80>
        ServerName {0}

        ServerAdmin webmaster@localhost
        DocumentRoot {1}

        ErrorLog {2}/error.log
        CustomLog {2}/access.log combined
</VirtualHost>
'''

        return base_string.format(self.vhostName, documentRoot, "${APACHE_LOG_DIR}")
