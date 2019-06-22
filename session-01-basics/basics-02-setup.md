## Basics > Setup

#### python3
First, we obviously need to install Python on our system.
 - Download Python [here](https://www.python.org/downloads/)

#### cmdr
Cmdr is a shell that works much better than the default cmd or powershell
 - Download cmdr [here](https://cmder.net/)

#### ipython
Ipython is a python interpreter that has some very nice built-in documentation, auto-complete, formatting, and colors.
 - Download ipython with the following command: ```pip install ipython```
 
#### vscode
Visual Studio Code (aka vscode) is a text editor with lots of easy to use plug-ins that makes programming easier.
 - Download vscode [here](https://code.visualstudio.com/)

 The first time you open a python file in vscode it will prompt you to install the correct plug-ins.

#### git
Git is a version control software. It is useful to make "snapshots" of your code so you can revert back if anything goes wrong.
It also enables multiple people to work on the same code project and easily merge their changes together.
 - Download git [here]()

 We will also be using a service called GitHub to store our code online so we can access it anywhere or share it with others.
 - Create a GitHub account [here](https://github.com/)
 - Create an ssh key with ```ssh-keygen -b 4096```, answer the questions, you can leave the password blank.
 - Add ssh key to GitHub account
 - Create a new code-camp-2019 repository in GitHub and copy the clone URL (green button)
 - Clone the repository to your computer with ```git clone <CLONE_URL>```

 After cloning your code repository, here is how it works.
  - Whenever you change a file you can ```git add``` it to the commit
  - After adding all the changes you want to include in the commit, type a commit message ```git commit -m "message"```
  - Once you've commit you can ```git push``` the changes to your GitHub repository


### Done!
That was a lot of setup, and a lot of new tools. Let's dive into some coding so we can learn how they all work together and help us create Python programs.
