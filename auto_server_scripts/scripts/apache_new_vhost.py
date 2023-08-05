import os

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
    
    def injectInDockerReceipt(
        self, 
        fileOperations, 
        file_name,
        path_provided_by_cli
    ):
        folder_to_write = os.path.join(path_provided_by_cli, "configure", "vhosts")
        if not os.path.exists(folder_to_write):
            os.makedirs(folder_to_write)
        full_file_vhost_path = os.path.join(folder_to_write, file_name)
        fileOperations.generate_file(full_file_vhost_path, full_file_vhost_path)
        print("Great! A new virtualhost configuration file has been created. Check the file in " + full_file_vhost_path + ".")
        fileOperations.insert_line_in_file(
            file_path=os.path.join(path_provided_by_cli,"Dockerfile"),
            inserting_line_number=3, 
            line_content="COPY ./configure/vhosts/" + file_name + " /etc/apache2/sites-available/" + file_name
        )
    
    def checkReceipt(self, files_listed: list) -> bool:
        if not self._doesHaveDockerFile(files_listed):
            raise Exception('The provided folder does not have a Dockerfile')
        return True
        
    def _doesHaveDockerFile(self, files_listed: str) -> bool:
        validFolder = False
        for entry in files_listed:
            if entry == "Dockerfile":
                validFolder = True
        return validFolder
                