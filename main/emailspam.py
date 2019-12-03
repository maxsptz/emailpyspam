def gmailInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Gmail has a limit of 500 emails per day per account" + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in gmail.txt and gmailpass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Yahoo DISCLAIMER

def yahooInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Yahoo has a limit of 100 recipients per email (this cannot be exceeded)." + bcolors.ENDC)
    print(bcolors.FAIL + "\nYahoo also has a limit of 500 emails per day per account." + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in yahoo.txt and yahoopass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple

# Outlook DISCLAIMER

def outlookInstruct():
    print(bcolors.FAIL + "\nDISCLAIMER: Outlook has a limit of 100 recipients per email (this cannot be exceeded)." + bcolors.ENDC)
    print(bcolors.FAIL + "\nOutlook also has a limit of 300 emails per day per account (limit also depends on reputation of email address)." + bcolors.ENDC)
    print(bcolors.FAIL + "\nKeep in mind, each recipient of the same email adds to the email count." + bcolors.ENDC)
    print(bcolors.WARNING + "The email limit can be surpassed by using multiple emails."\
    "\nDo you wish to surpass the limit using multiple emails?"\
    "\n(Emails and passwords must be predefined in yahoo.txt and yahoopass.txt)"\
    "\n1) Yes"\
    "\n2) No"\
    + bcolors.ENDC)
    multiple = input(bcolors.OKGREEN + '\nNumber: ' + bcolors.ENDC)
    return multiple
