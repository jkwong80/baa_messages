from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os, time, yaml, logging
from random import randint

logging.basicConfig()

home = os.curdir

if 'HOME' in os.environ:
    home = os.environ['HOME']
elif os.name == 'posix':
    home = os.path.expanduser("~/")
elif os.name == 'nt':
    if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
        home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
else:
    home = os.environ['HOMEPATH']

class AWSIoTSetup():
    def __aws_setup__(self, credentials_dir=False):
        if credentials_dir == False:
            credentials_dir = os.path.join(home, ".baa_credentials")
        self.__config__(credentials_dir)
        self.__setup_mqtt_client__()
        self.__setup_credentials__(credentials_dir)
        self.__setup_endpoint__()
        self.__configure_queue__()

    def __config__(self, path):
        credentials_dir = os.path.abspath(path)
        configs = yaml.load(file(os.path.join(credentials_dir, "configs.yaml"), "r"))
        self.sensor_unit_id = configs['sensor_unit_id']
        print('config ran')

    def __setup_mqtt_client__(self):
        name = "sensor_unit-" + str(self.sensor_unit_id) + "-" + str(int(time.time())) + str(randint(0, 100))
        self.mqClient = AWSIoTMQTTClient(name)
        print('created ' + name)

    def __setup_credentials__(self, path):
        credentials_dir = os.path.abspath(path)
        self.mqClient.configureCredentials(os.path.join(credentials_dir,"root.pem"),
                                           os.path.join(credentials_dir,"privateKey.pem"),
                                           os.path.join(credentials_dir,"cert.pem"))
        print('setup creds')

    def __setup_endpoint__(self):
        # setup endpoint
        endpoint = 'a39dt04vx5u2zp.iot.us-east-1.amazonaws.com'
        self.mqClient.configureEndpoint(endpoint,8883)
        print('endpoint')
        self.mqClient.connect()
        print('connected')

    def __configure_queue__(self):
        self.mqClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.mqClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.mqClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.mqClient.configureMQTTOperationTimeout(5)  # 5 sec
        print('queue config')

