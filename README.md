BAA Messaging Library
====================
This Repo is designed to facilitate the sending/receiving of BAA messages, both over local
and cloud based networks. There are two main users of this repo, those you want to be able to send
data to the cloud and those who want to contribute to the development.  In general the setup of your
environment is different for these different options so please choose from the below options to setup.

Note:  If you want to both send to the cloud and develop, see [contributing.md](contributing.md)

## For Clients
This section describes how to setup your machine to use the baa_messages package to send
data to the BAA Cloud.  This setup is unique for the client usage and will conflict with the
development environment.  If you would to be able to contribute to the development of the baa_messages
package please seesee [contributing.md](contributing.md)

To install this package simply type:
```bash
sudo pip install baa_messages git+https://github.com/berkeleyapplied/baa_messages#branch
```
where branch is the branch you want to work against.
Branches are as follows:
  * master or no # - stable current release
  * stage - tested release, may contain breaking changes
  * dev - under heavy development, not for the feint of heart.

Now you are ready to use the package to create messages and send them to the BAA Cloud
### Usage
The baa_messages library is intended to provide an interface to the Message Schema used in the BAA Cloud.
At the base level, for every message structure, there is an associated schema, and therefore python Object.
These objects are grouped, by there nature into components.

Much of the creation of these objects has been abstracted away from you. All data that is being passed to
will be done via a SensorUnit -> Sensor abstraction layer. You begin by creating a SensorUnit which maps to a
SensorUnit you have setup on the BAA dashboard. This SensorUnit will need an ID and credentials, by default it will
use the credentials that were emailed to you when you setup the unit, please place this un-zipped folder at the root
of your device in a folder called .baa_credentials.

Once you have your credentials on the device, you can setup your unit's object:
```
from baa_messages.components.sensor_unit import SensorUnit
unit = SensorUnit(id={Your id here})
```

This will be the main interface into the system. You can add your sensors and get them as follows:
```
unit.add_sensor(type="gps", id={Your sensor's id})
unit.get_sensor({Your sensor's id})
```
The sensor types available map to the different sensor families in the [sensor schema folder](baa_messages/schema/sensor/).
The type past in is the string segment at the end of the namespace, ie. gamma, gps, nuetron etc... as annotated in the top of each schema file
```
namespace py baa_messages.messages.sensor.gps
```

## Creating messages:
Once you have a sensor you can create different types of messages.
```
sensor.create_reading(timestamp=time, latitude=lat, longitude=long)
sensor.create_setting(poll_frequency=1)
```
These messages will be added as the latest reading and setting to the sensor.
When creating a message you can pass in any attributes for the Thrift type associated with the factory's type. You can also check what these are in the schema folder [sensor schema folder](baa_messages/schema/sensor/).


## Publishing Messages:
Once you have built up a latest reading and setting on all the sensors you can publish.
To do so simply call the publish method on the unit, it will publish all the associated sensors which have latest reading or settings available.
```
unit.publish()
```
Publishing flushes the latest reading and setting from the sensor once completed.

When you publish a message, we will create two pieces of metadata associated with your data.
  1. A [BaaMessage](baa_messages/schema/core.thrift)
  2. A [BaaContext](baa_messages/schema/core.thrift)
This meta data is useful for understand where a message came from and when actions occured. We will include the sensor unit id, sensor id, sensor unit lat/long, and published time, you can also pass in a timestamp for synchronization. Read more about [time formatting here](#Time Formating)

## Unit Location:
You can keep track of the unit's location by setting it on the unit object. When you publish, the lat long will be included
as part of the meta data passed by the system.
```
unit.set_latitude(lat)
unit.set_longitude(lng)
```

### Disable publishing
If you wish to not publish and simply run in test mode, you can set the publishing flag on the unit to False. You can also disable cloud publishing only and allow custom publishers to run with a flag.

# Setup our listner to listen to messages being sent to the cloud.
# The cloud based pubsub system will allow you to listen to topics you have
# access to.
subscriber = sb.Mqtt(topic="test")


# Custom Publishers
TODO...

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

# Time Formatting
ADD THIS

