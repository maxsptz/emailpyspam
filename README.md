![GitHub](https://img.shields.io/github/license/curioo/emailpyspam)
![Build Status](https://img.shields.io/badge/Build-Passing-green)
![GitHub top language](https://img.shields.io/github/languages/top/curioo/emailpyspam)

# EmailPySpam

Python 3+ program to send emails to a list of users repetitively.

**WARNING**: This project will be rewritten soon. Fork the repository if you wish to keep our current iteration of the program. Thanks!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

[Python 3+](https://www.python.org/downloads/) (made on python 3.8)

### Installing

A step by step series of examples that tell you how to get a development env running
#### Linux (Bash)
Clone the repository

```
git clone https://github.com/Curioo/emailpyspam.git
```

Install required libraries

```
pip3 install -r requirements.txt
```

Navigate into main directory

```
cd emailspam/
```

Navigate into sub-directory

```
cd main/
```

Start the program

```
python3 emailspam.py
```
There is also a non interactive mode, you can see the options for running it in non interactive mode with
```
python3 emailspam.py -h
```

Which creates the following output

```
Usage: emailspam.py [options]

Options:
  -h, --help            show this help message and exit
  -i, --interactive     this choice negates interactive mode
  -t TO_ADDRESS, --to=TO_ADDRESS
                        the email address you are spamming e.x.: email@gmail
                        (cannot contain .com)
  -f FROM_ADDRESS, --from=FROM_ADDRESS
                        the email you are spamming from
  -d SENDSPEED, --interval=SENDSPEED
                        the interval in seconds in which you want to send the
                        emails
  -p PASSWORD, --password=PASSWORD
                        the password for the email account you are spamming
                        from
  -s SUBJECT, --subject=SUBJECT
                        the subject of the email you want to spam
  -b BODY, --body=BODY  the actual message inside the email you wish to spam
  -e RECIPIENTNUM, --num-of-emails=RECIPIENTNUM
                        the number of email addresses you want to send from
  -n SEND, --num=SEND   the number of emails you wish to send

```
=======

#### Windows (Command Prompt)
Clone the repository

```
git clone https://github.com/Curioo/emailpyspam.git
```

Install required libraries

```
pip install -r requirements.txt
```

Navigate into main directory

```
cd emailspam/
```

Navigate into sub-directory

```
cd main/
```

Start the program

```
python emailspam
```

## Usage

You have the ability to use the program in two ways.
* Simple
  * Type an email and password in at the beginning
* Extended
  * Have the program access a list of emails and passwords to access once an email has been locked
  
## Screenshots

Welcome message:


![Image of welcome message](https://i.imgur.com/G1X8r49.png)

## Built With

* [Python](https://www.python.org) - The language used
* [Atom](https://Atom.io) - Code editing

## Contributing

Please read [CONTRIBUTING.md](https://github.com/Curioo/emailpyspam/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Max Spitzer** - *Initial work* - [Curioo](https://github.com/Curioo)
* **Franco Aparicio** - *Main Contributor* - [NONAME1103](https://github.com/NONAME1103)
* **Ethan Moore** - *Web Design and additional features* - [quarksrcool](https://github.com/quarksrcool)

See also the list of [contributors](https://github.com/Curioo/emailpyspam/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Curioo/emailpyspam/blob/master/LICENSE) file for details
