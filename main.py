from OAuth.credential import usermail,password
from utils import *
from features import *

def main():
    """
    Main function that handles primary choices
    """

    if usermail != "" and password != "":

        SpeakText("Choose and speak out the option number for the task you want to perform. Say 1 to send a mail. Say 2 to get your mailbox status. Say 3 to search a mail. Say 4 to get the last 3 mails.")
        choice = speech_to_text()
        
        if choice == '1' or choice.lower() == 'one':
            composeMail()
        elif choice == '2' or choice.lower() == 'too' or choice.lower() == 'two' or choice.lower() == 'to' or choice.lower() == 'tu':
            getMailBoxStatus()
        elif choice == '3' or choice.lower() == 'tree' or choice.lower() == 'three':
            searchMail()
        elif choice == '4' or choice.lower() == 'four' or choice.lower() == 'for':
            getLatestMails()
        else:
            SpeakText("Wrong choice. Please say only the number")

    else:
        SpeakText("Both Email ID and Password should be present")



if __name__ == '__main__':
    flag = True
    while(flag):
        main()
        SpeakText("Do you want to perform more operations? (Say yes/no)")
        choice = speech_to_text()
        flag = False
        if choice == "yes":
            flag = True
        