import kivy
kivy.require('1.5.2')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from ftplib import FTP


#########################################################
#MAIN WINDOW
#########################################################
class Controller(FloatLayout):
    ftp = None

    #FTP Client Connect
    def ftp_client_connect(self, button_id):
        ftp_server_address = self.ids.ftp_server_address_text.text
        port = int(self.ids.ftp_client_port_text.text)
        self.ftp = FTP(ftp_server_address)
        self.ftp.login()


    #FTP Client get welcome message
    def ftp_client_getwelcome(self, button_id):
        self.print_message("There is no function yet")

    #FTP Client return lines
    def ftp_client_retrlines(self, button_id):
        file_list = []
        self.ftp.retrlines('NLST', file_list.append)
        for index, value in enumerate(file_list):
            self.ids.ftp_client_message_text.text += str(index + 1) + "_" + value + "\n"


    #FTP Client return binary
    def ftp_client_rtrbinary(self, button_id):
        file_name = self.ids.download_file_name_text.text
        command = "RETR " + file_name
        self.ftp.retrbinary(command, open(file_name, 'wb').write)

    #FTP Client quit
    def ftp_client_quit(self, button_id):
        self.ftp.quit()

    #FTP Client dir
    def ftp_client_dir(self, button_id):
        self.print_message("There is no function yet")

    #FTP Client cwd
    def ftp_client_cwd(self, button_id):
        file_name = self.ids.file_name_text.text
        self.ftp.cwd(file_name)
        self.ftp_client_retrlines(button_id)

    #Print Message
    def print_message(self, message):
        self.ids.ftp_client_message_text.text += message + "\n"



#########################################################
#APP START
#########################################################
#App
class ControllerApp(App):
    def build(self):
        return Controller()


#Run App
if __name__ == '__main__':
    ControllerApp().run()