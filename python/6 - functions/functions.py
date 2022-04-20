

applicant_list = []
hired_list = []


def ResetApplications():
    applicant_list.extend(["Rico", "Francine", "Rodney", "Franny", "Richard", "Franklin", "Rodrick", "Flourance"])
    hired_list.clear()


ResetApplications()

removed_applicant = applicant_list.pop(4)
removed_applicant = removed_applicant + " - HIRED"
hired_list.append(removed_applicant)

removed_applicant = applicant_list.pop(3)
removed_applicant = removed_applicant + " - HIRED"
hired_list.append(removed_applicant)

removed_applicant = applicant_list.pop(1)
removed_applicant = removed_applicant + " - HIRED"
hired_list.append(removed_applicant)



ResetApplications()

def HireApplicant(app_index):
    removed_applicant = applicant_list.pop(app_index)
    removed_applicant = removed_applicant + " - HIRED"
    hired_list.append(removed_applicant)

HireApplicant(4)
HireApplicant(3)
HireApplicant(1)




# ----------------------------------------------------------------




mailbox_mail = []


new_mail = {}
new_mail["date"] = "04-18-2022"
new_mail["header"] = "Happy Birthday!"
new_mail["content"] = "Wishing you a very happy birthday."
new_mail["stamp"] = "cake"
mailbox_mail.append(new_mail)


new_mail = {}
new_mail["date"] = "04-18-2022"
new_mail["header"] = "Thanks for your feedback!"
new_mail["content"] = "We've received your review of the 'giant metal fan' and appreciate your positive feedback."
new_mail["stamp"] = "smile"
mailbox_mail.append(new_mail)


new_mail = {}
new_mail["date"] = "04-18-2022"
new_mail["header"] = "Jury Duty"
new_mail["content"] = "You've been summoned to report to jury duty on 06-20-2022."
new_mail["stamp"] = "flag"
mailbox_mail.append(new_mail)



def CreateNewMail(date, header, content, stamp):
    new_mail = {}

    new_mail["date"] = date
    new_mail["header"] = header
    new_mail["content"] = content
    new_mail["stamp"] = stamp

    mailbox_mail.append(new_mail)


CreateNewMail("04-18-2022", "Happy Birthday!", "Wishing you a very happy birthday.", "cake")
CreateNewMail("04-18-2022", "Thanks for your feedback!", "We've received your review of the 'giant metal fan' and appreciate your positive feedback.", "smile")
CreateNewMail("04-18-2022", "Jury Duty", "You've been summoned to report to jury duty on 06-20-2022.", "flag")




# ----------------------------------------------------------------



def AddSpaceBetweenLetters(word):
    return " ".join(list(word))


test_1 = AddSpaceBetweenLetters('word')
test_2 = AddSpaceBetweenLetters('sample')