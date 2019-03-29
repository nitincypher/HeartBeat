#Imports
import socket
import psutil
from datetime import datetime
import json
import requests

#Payload Class
class Payload:
    machineId         = ""
    cpuUtilization    = ""
    totalRam          = ""
    ramPercentageUsed = ""
    utc_time          = ""

    #JSON conversion helper
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

#Heartbeat Class
class HeartBeat:

    timestamp = ""

    def getMachineId(self):
        return socket.getfqdn()

    def getCpuUtilization(self):
        return psutil.cpu_percent(interval=1)

    def getRamUtilization(self):
        return psutil.virtual_memory()

    def sendData(self, data, endpoint):
        #Use requests to send data
        return ""    

    #Aggregates all Machine Data to be sent
    def aggregateData(self):

        #Get Data to Populate Payload
        machineId      = self.getMachineId()
        cpuUtilization = self.getCpuUtilization()
        ramUtilization = self.getRamUtilization()
        utc_time       = self.getTimestamp()

        #Create the Payload Object
        payload = Payload()
        payload.machineId = machineId
        payload.cpuUtilization = cpuUtilization
        payload.totalRam = ramUtilization[0]/1024/1024
        payload.ramPercentageUsed = ramUtilization[2]
        payload.utc_time = utc_time
        return payload

    
    #Gives a unified timestamp for atomic run
    def getTimestamp(self):
        if self.timestamp == "":
            self.timestamp = datetime.utcnow()
            return self.timestamp.strftime("%m%d%YT%H%M%S")
        else:
            return self.timestamp.strftime("%m%d%YT%H%M%S")


heartBeat = HeartBeat()
payload = heartBeat.aggregateData().toJSON()

print(payload)




