BAA Messaging Library
====================
This Repo is designed to facilitate the sending/receiving of BAA messages, both over local
and cloud based networks. There are two main users of this repo, those you want to be able to send
data to the cloud and those who want to contribute to the development.  In general the setup of your
environment is different for these different options so please choose from the below options to setup.

Note:  If you want to both send to the cloud and develop, choose [For Developers](#For Developers)
  - [For Clients](#For Clients)
  - [For Developers](#For Developers)


## For Developers
The first thing you are going to need to do is get the package, install the dependencies, and then setup
a virtual environment to be able to test the build.

### Git Package
Move to an appropriate location on your computer (I recommend using a directory as a workspace for your
development projects e.g., ~/workspace/) and run:
```bash
git clone git@github.com:berkeleyapplied/baa_messages.git
```
###Install Dependencies
Now we will need to go into that directory (herein referred to as [repo_location]) and run the setup
baa_messages:
```bash
cd [repo_location]
./bin/setup.sh
```
Note, this setup script is currently setup for Mac computers.  if you are running on a different OS, please
see the setup.sh script and install the appropriate packages

### Setting up a Virtual Environment for Build Testing
Its best to use a virtual environment to contribute to the development of this library.  If you are unfamiliar
with virtual environments, see [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Before you commit your code, setup a blank virtual environment and install the package to
make sure that nothing you have done has broken the install:
```bash
virtualenv my_venv
source my_venv/bin/activate
sudo pip install -r requirements.txt
sudo pip install .
./bin/run_tests.sh
```
If that works, then you can you know that the build worked and you can commit your code changes. Once you are done,
you can simply remove the my_venv directory to blow away that virtual environment.  (Please be sure not to check in
that directory as it will be different for different development environments)

## Testing the Installation
If you would like to run the unit tests, separate from the commit, you can do the following:
```bash
cd [repo_location]
python setup.py test
```
Note: When you commit your code git will run a few tests to ensure that everything meets the specs required to contribute,
if you find bugs in this process, please add a bug report [here](https://github.com/berkeleyapplied/baa_messages)

## For Clients
This section describes how to setup your machine to use the baa_messages package to send
data to the BAA Cloud.  This setup is unique for the client usage and will conflict with the
development environment.  If you would to be able to contribute to the development of the baa_messages
package please see [For Developers](#For Developers)

To install this package simply type:
```bash
sudo pip install baa_messages
```

Now you are ready to use the package to create messages and send them to the BAA Cloud
### Usage
To create a "BAAMessage" python object from the schema and set the sender_id, open python and type:
```
from baa_messages.messages.core.ttypes import BAAMessage
x=BAAMessage()
x.sender_id = "1234"
```
Also see [baa_messages.codec](./baa_messages/codec.py) for usage on the codec tools

### Using MQTT to Publish and subscribe to the cloud
```python
import baa_messages.publisher.mqtt as b
import baa_messages.subscriber.mqtt as sb

# Setup our publisher to send messages to the cloud
pub = b.Mqtt(topic="test", sensor_id="test")

# Setup our listner to listen to messages being sent to the cloud.
# The cloud based pubsub system will allow you to listen to topics you have
# access to.
subscriber = sb.Mqtt(topic="test")

# Create some callbacks to work with the data.
def custom_callback(message=""):
  # do something
  print(message)

def callback2(message=""):
  pass

# Add callbacks to the subscriber, you can add many callbacks here.
subscriber.add_callback(custom_callback)
subscriber.add_callback(callback2)

# Publish hello to the test topic.
pub.publish("hello")
```

