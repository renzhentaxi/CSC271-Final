import os

def send(to, subject, attachment):
    '''
    sends an email
    to: the recipient of the mail
    subject: the subject of the mail
    attachment: path to the attachment file (in this case it should be the workbook)
    '''
    os.system("mutt -s \"{subject}\" -a {attachment} < /dev/null -- {to}".format(**locals()))
