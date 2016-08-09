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

# Usage
To create a "BAAMessage" python object from the schema and set the sender_id, open python and type:
```
from baa_messages.messages.core.ttypes import BAAMessage
x=BAAMessage()
x.sender_id = "1234"
```
Also see [baa_messages.codec](./baa_messages/codec.py) for usage on the codec tools

## Building LZ4 library
The LZ4 library is required. We are going to need to build it out for Linux since the default Mac version
does not work in a linux env.
```
cd [repo_location] # Note there should be a file called VagrantFile at this level
vagrant up
vagrant ssh
cd /vagrant
sudo pip install -t baa_messages/vendored/ -r requirements.txt
```

>>>>>>> Try building vendor files locally.
