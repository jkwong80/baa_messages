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
If this works then the build works in a clean environment and you can move on to committing your changes.


To exit the virtual environment, inside the venv type:
```bash
deactivate
```
Once you are done making changes, and you have deactivated the venv session, you can simply remove the
my_venv directory to blow away that virtual environment.  (Please be sure not to check in
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
The baa_messages library is intended to provide an interface to the Message Schema used in the BAA Cloud.
At the base level, for every message structure, there is an associated schema, and therefore python Object.
These objects are grouped, by there nature into components.  At this time, the baa_messages library supports
the following components:
- Sensor - a system that primarily publishes its data to the cloud and, whose settings, can be set through a cloud subscription
- Algorithm - A process that takes in values (primarily from sensors) and publishes its results to the cloud

For each component there is a concept of a **"Reading"** and a **"Setting"**.  The **Reading** is used to report
the information coming out of the component while the **Setting** is used to interact with the component and change
its state.

Equipped with this knowledge, the easiest way to interact with the library is to use the Component factories
as shown below:
#### Access via Component Factories
To build out a sensor you can use the sensor factory:
```python
from baa_messages.components.sensor import SensorFactory
sf = SensorFactory()

gps_reading = sf.create_sensor_reading("gps")
gps_reading.reading.latitude=10
gps_reading.reading.longitude=20
```

Alternatively, you can provide the arguments of the context and the reading as arguments to ```create_sensor_reading``` like:
```python
import time
from baa_messages.components.sensor import SensorFactory
sf = SensorFactory()

gps_reading = sf.create_sensor_reading("gps",timestamp=time.time(), latitude=38, longitude=-73)
```

The same can be done using ```create_sensor_setting``` and if you would like a collection
of settings and readings you can use ```create_sensor_report```.

#### Access via base schema

To create a "BAAMessage" python object from the schema and set the sender_id, open python and type:
```
from baa_messages.messages.core.ttypes import BAAMessage
x=BAAMessage()
x.sender_id = "1234"
```

If you wanted to create a gps_reading you would use:
```python
from baa_messages.messages.sensor.gps.ttypes import Reading as GPSReading
gps_reading = GPSReading(latitude=10, longitude=10)
```
Note that there are several issues with doing this.  First, if you want to package that into a
sensor reading it will require something like the following:
```python
from baa_messages.messages.sensor.ttypes import Reading,SensorReading
from baa_messages.messages.core.ttypes import BAAContext
ctx = BAAContext()
r = Reading(gps=gps_reading)
sr = SensorReading(ctx,r)
```

Please make sure you understand the paradigm before attempting this level of interaction.  When in doubt,
you should use the Factories to access schema objects

####Encoding your data
see [baa_messages.codec](./baa_messages/codec.py) for usage on the codec tools

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

