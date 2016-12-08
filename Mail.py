import os
def send_mail(to, subject, attachment):
    os.system("mutt -s \"{subject}\" -a {attachment} < /dev/null -- {to}".format(**locals()))
