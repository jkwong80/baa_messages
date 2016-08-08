BAA Messaging Library
====================
This Repo is designed to facilitate the sending/receiving of BAA messages, both over local
and cloud based networks.

# Setting up this module
To setup this module, we will need to install dependencies, install the main package, and test
the installation.  First, though, we will need to clone the repo to an appropriate location on your computer
```bash
git clone git@github.com:berkeleyapplied/baa_messages.git
```
## Install Dependencies and Main Package
Now we will need to go into that directory (herein referred to as [repo_location]) and run the setup
baa_messages:
```bash
cd [repo_location]
./bin/setup.sh
```
This will install all the necessary dependencies for the library and install the module in
your python site-packages.  Now to test the installation
## Testing the Installation
To test the installation run:
```bash
cd [repo_location]
python setup.py test
```
