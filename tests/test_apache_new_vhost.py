import unittest
from auto_server_scripts.scripts.apache_new_vhost import ApacheNewVhost

class test_apache_new_vhost(unittest.TestCase):

    def test_basic(self):
        apache_new_vhost = ApacheNewVhost()
        apache_new_vhost.setVhostName("marilia")
        
        expected_content = '''<VirtualHost marilia:80>
        ServerName marilia

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/marilia/public

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
'''

        self.assertEqual(expected_content, apache_new_vhost.exec())

    def test_change_document_root_suffix(self):

        apache_new_vhost = ApacheNewVhost()
        apache_new_vhost.setVhostName("juca")
        apache_new_vhost.setDocumentRootSuffix("web")
        
        expected_content = '''<VirtualHost juca:80>
        ServerName juca

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/juca/web

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
'''

        self.assertEqual(expected_content, apache_new_vhost.exec())
