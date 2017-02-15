import imaplib # Read more about this library
import urllib2


class EmailHandler(object):
    def __init__(self):
        self.connect_to_mail()

    def get_all_folders(self):
        response_code, response = self.mail_box.list()
        if response_code == 'OK':
            success_message = 'I was able to connect and reprieve data from ' \
                              'your folders!'
            user_created_folders = []
            system_created_folders = []
            separator = True
            for raw_folder_output in response:
                folder = raw_folder_output.split(' "/" ')[1]
                if '[Gmail]' in folder:
                    separator = True
                    folder = folder.split('[Gmail]')[1]
                if '"' in folder:
                    folder = folder.replace('"', '')
                if '/' in folder:
                    folder = folder.replace('/', '')
                if folder:
                    if not separator:
                        user_created_folders.append(folder)
                        continue
                    system_created_folders.append(folder)
                separator = False
            return user_created_folders, system_created_folders
        else:
            failure_message = 'I was not able to retrieve any data from your '\
                              'folders!'

    def get_status_for_all_folders(self):
        user_folders, system_folders = self.get_all_folders()
        for i in range(len(system_folders)):
            if system_folders[i].isupper():
                continue
            system_folders[i] = '[Gmail]/' + system_folders[i]

        all_folders = user_folders+system_folders
        for folder in all_folders:
            response_code, response = self.mail_box.status(
                folder, '(MESSAGES RECENT)')
            if response_code == 'OK':
                response = (response[0].split(' (')[1].replace(')', '')).split(
                    ' ')
                return response
            else:
                print 'Error reading the folder: %s!' % folder

    def get_status_for_specific_folder(self, folder):
        """
        Method to get the total number of messages in the folder and the
        number of unseen messages.
        :param folder: The folder to look into. Use the constants for the
        folders precrated by Google.
        :return:
        """
        response_code, response = self.mail_box.status(
            folder, '(MESSAGES UNSEEN)')

        if response_code == 'OK':
            response = (response[0].split(' (')[1].replace(')','')).split(' ')
            return response
        else:
            print 'Error reading the folder: %s!' % folder

    def get_mails_subject(self, folder):
        info_for_folder = self.get_status_for_specific_folder(folder)
        self.mail_box.select(folder, readonly=True)
        if int(info_for_folder[1]):
            subject_id_dict = {}
            for i in range(1, int(info_for_folder[1])+1):
                response_code, message_data = self.mail_box.fetch(
                    i, '(BODY[HEADER.FIELDS (SUBJECT)])')
                subject = message_data[0][1].replace(
                    '\r', '').replace('\n', '')
                subject_id_dict.update({i:subject})
            return subject_id_dict
        else:
            print 'There are no messages to read!'

    def read_mail_body_given_subject(self, folder, subject):
        subject = 'Subject: ' + subject
        all_mail_subjects_in_folder = self.get_mails_subject(folder)
        mail_id = None
        for mail in all_mail_subjects_in_folder:
            if all_mail_subjects_in_folder[mail] == subject:
                mail_id = mail
                break
        response_code, msg_data = self.mail_box.fetch(
            mail_id, '(BODY[1])')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                print response_part[1]

    def connect_to_mail(self):
        try:
            self.mail_box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
            self.mail_box.login('python.project.test.email', 'Pyt#onProject')
        except imaplib.IMAP4.error:
            print 'Invalid credentials!'


'''
https://developers.google.com/gmail/api/v1/reference/users/messages/list
'''