![GitHub](https://img.shields.io/github/license/curioo/emailpyspam)
![Build Status](https://img.shields.io/badge/Build-Passing-green)
![GitHub top language](https://img.shields.io/github/languages/top/curioo/emailpyspam)

# EmailPySpam

Python 3+ program to send emails to a list of users repetitively.


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
Or
```
python3 emailspam.py -i -t target@email.com -f youremail@gmail.com -d intervalbetweenemails -p passwordforyouremail -s subject -b body(\ before every space) -n numOfEmails
```

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
Or


## Usage

You have the ability to use the program in three ways.
* Simple
  * Type an email and password in at the beginning
* Extended
  * Have the program access a list of emails and passwords to access once an email has been locked
* Single Command
  * Run the program with options given by the user when the file is run. See your options with:
  ```
  python3 emailspam.py --help
  ```
  
  
### Webapp

This repo also contains code for a website where you can run the code in a user friendly interface. This code for the webserver has been tested on Manjaro and Debian, with apache running the webserver It uses php to execute the python and html and java for the webpage. To achieve this you will need to install php, apache and of course all the requirements for the python. 

* On debian
  Install the apache webserver as well as php
  ```
  sudo apt install apache && sudo apt install php
  ```
  Copy the html folder to the webserver location
  ```
  sudo cp -r html/. /var/www/html
  ```
  Enable php on apache2
  Open the apache2 config file with:
  ```
  sudo nano /etc/apache2/apache2.conf
  ```
  then add the following lines 
  ```
  <FilesMatch \.php$>
   SetHandler application/x-httpd-php
  </FilesMatch>
  ```
  Certain modules will need to be disabled for the apache webserver 
  ```
  sudo a2dismod mpm_event && sudo a2enmod mpm_prefork && sudo a2enmod php7.0
  ```
  Restart the webserver
  ```
  sudo service apache2 restart
  ```

* On manjaro
  Install apache2 and php 
  ```
  sudo pacman -S apache php php-apache
  ```
  Edit the configuration file for apache 
  ```
  sudo nano /etc/httpd/conf/httpd.conf
  ```
  and comment out this line
  ```
  #LoadModule mpm_event_module modules/mod_mpm_event.so
  ```
  un comment this line
  ```
  LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
  ```
  then add the following lines at the end
  ```
  LoadModule php7_module modules/libphp7.so
  AddHandler php7-script php
  Include conf/extra/php7_module.conf
  ```
  restart the apache webserver
  ```
  sudo systemctl restart httpd
  ```
  If the webserver was not already running start it with
  ```
  sudo systemctl start httpd
  ```
  ```
  sudo systemctl enable httpd
  ```
  
If you have anny issues or questions setting up the webserver please post them in the issues section of the repository and we will address them as soon as possible.

In the future you can expect intructions for setting up the webserver on MacOS and possibly windows, with the other possibility of scripts to automate the process for a more user friendly setup for a webserver

## Screenshots

Welcome message:


![Image of welcome message](https://i.imgur.com/G1X8r49.png)

Webserver:



## Built With

* [Python](https://www.python.org) - The language used
* [Atom](https://Atom.io) - Code editing

## Contributing

Please read [CONTRIBUTING.md](https://github.com/Curioo/emailpyspam/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Max Spitzer** - *Initial work* - [Curioo](https://github.com/Curioo)
* **Franco Aparicio** - *Main Contributor* - [NONAME1103](https://github.com/NONAME1103)

See also the list of [contributors](https://github.com/Curioo/emailpyspam/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Curioo/emailpyspam/blob/master/LICENSE) file for details
