import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime



GPIO.setmode(GPIO.BCM)  # for using the names of the pins
GPIO.setwarnings(True)  # set to false if the warnings bother you, helps troubleshooting

class Relay:
    """
    Turns GPIO pins from LOW(on) to HIGH(off) and back again.  Remember: relays are inverted.
    3.3v turns the relay off.

    this class pretty much works for any device connected to a single GPIO pin
    as instances of Relays are created, their names are added as keys in the Relay.dictionary
    """
    dictionary = {}  # a dictionary will all created Pin instances' names as keys

    # state = None
    def __init__(self, pin, name):
        self.pin = int(pin)  # this is the GPIO pin number (will depend on GPIO config)
        self.name = name
        GPIO.setup(pin, GPIO.OUT, initial=1)
        Relay.dictionary[name] = self  # auto adds every instance of Relay to the dictionary

    @property
    def state(self):
        self._state = GPIO.input(self.pin)
        return self._state

    def on(self):
        """switches GPIO pin to LOW/0 - in open state relays, this turns the relay ON."""
        GPIO.output(self.pin, GPIO.LOW)

    def off(self):
        """ switches GPIO pin to HIGH/1 - in open state relays, this turns the relay OFF."""
        GPIO.output(self.pin, GPIO.HIGH)

    def blink(self, *args):
        """this should not be used for actual relays, just LEDs"""
        # print (len(args))          #troubleshooting print statement
        # print args                 # another
        try:
            repeat = int(args[0])   # if arguments are included, use the first one to mean number of blinks
        except:
            repeat = 1              # default is 1 blink
        try:
            speed = (float(args[1])) / 2    # second argument is the speed of blinks
        except:
            speed = .5              # default is .5 seconds
        # print repeat               #troubleshooting print statement
        # print speed                # another
        # color: uncomment below for color export to terminal.
        # print("%s Relay is" % self.name + bcolors.BOLD + bcolors.PURPLE + " blinking." + bcolors.END)
        while repeat > 0:
            GPIO.output(self.pin, GPIO.LOW)
            time.sleep(speed)
            GPIO.output(self.pin, GPIO.HIGH)
            time.sleep(speed)
            repeat -= 1





class Sensor:
    array = []
    def __init__(self, pin, sens_type, name):
        self.sens_type = sens_type
        self.pin = int(pin)  # this is the GPIO pin number (will depend on GPIO config)$
        self.name = name  #
        Sensor.array.append(self)

    @property
    def read(self):
        humidity, temp = Adafruit_DHT.read(self.sens_type, self.pin)

        #print 'Temperature: {0:0.1f} C'.format(temp)       #prints Temp formated
        #print 'Humidity:    {0:0.1f} %'.format(humidity)   #prints Humidity formatted

        #print temp         #prints temp unformated
        #print humidity     #prints humidity unformated

        # Sometimes the sensor will return "None"
        # This might happen if the CPU is under a lot of load and the sensor$
        # can't be reliably read (timing is critical to read the sensor).$
        # the following loop will read the sensor every 2 seconds until both temp and humidity are not "None"

        while humidity is None or temp is None:  #this should prevent errors when rounding, but could cause a hang-up...
            time.sleep(2)
            humidity, temp = Adafruit_DHT.read(self.sens_type, self.pin)

        return {"%s"%self.name: {"temp": round(float(temp),1), "humidity": round(float(humidity),1), "timestamp": datetime.datetime.utcnow().isoformat()}}
