#mqtt paho
import sys
import paho.mqtt.client as mqtt
import requests as req

#subscribe to topic = "/is4151-is5451/Hamza/NUS/19_04/great"

def on_message(client, userdata, message):
    print("Message received: ", str(message.payload.decode("utf-8")))

def main():

    #Topic
    topic = "/is4151-is5451/Hamza/NUS/19_04/great"

    # Create a new MQTT client instance
    client = mqtt.Client()

    client.connect("broker.emqx.io", 1883, 60)

    

    print("Starting control application...")
    # get argument from command line
    n = len(sys.argv)
    if n > 1:
        arg = sys.argv[1]        
        
        response = req.get(f'http://localhost:5000/api/lightclustertwo?brightness={arg}')

        # its a json
        #format as json
        result = int(response.json()['result'])

        if result == 0:
            smartlight = 'on'
        else:
            smartlight = 'off'

        client.publish(topic, smartlight)

        print("Response from server: ", result)
        
        # if cluster_label == '0':       
        #     smartlight = 'on'
    # #Topic
    # topic = "/is4151-is5451/Hamza/NUS/19_04/great"

    # # Create a new MQTT client instance
    # client = mqtt.Client()
    
    # # Set the on_message callback function
    # client.on_message = on_message
    
    # # Connect to the MQTT broker
    # client.connect("broker.emqx.io", 1883, 60)
    
    # # Subscribe to the topic
    # client.subscribe(topic)
    
    # # Start the loop to process incoming messages
    # client.loop_forever()>
    client.loop_forever()

#init main
if __name__ == "__main__":
    main()
