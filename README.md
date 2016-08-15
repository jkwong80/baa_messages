BAA Messaging Library
====================
This Repo is designed to facilitate the sending/receiving of BAA messages, both over local
and cloud based networks.  For those who plan to participate in the development of this project,
please see the [For Developers](#For Developers)

# Setting up this module
To setup this module, we will need to install dependencies, install the main package, and test
the installation.  First, though, we will need to clone the repo to an appropriate location on your computer
```bash
git clone git@github.com:berkeleyapplied/baa_messages.git
```
## For Developers
Its best to use a virtual environment to contribute to the development of this library.  If you are unfamiliar
with virtual environments, see [Virtual Environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Before you commit your code, setup a blank virtual environment and install the package to
make sure that nothing you have done has broken the install:
```bash
virtualenv my_venv
source my_env/bin/activate
sudo pip install -r requirements.txt
sudo pip install .
./bin/run_tests.sh
```
If that works, then you can ...

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

## Using MQTT to Publish and subscribe to the cloud
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
