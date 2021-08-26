



# datasets = {
#      "transmitter": pd.read_csv(r"C:\vlcchanges\underwatervlc\logData\temperature_48c_30Hz_60fps_transmitter3.csv"),
#      "receiver": pd.read_csv(r"C:\vlcchanges\underwatervlc\logData\temperature_48c_30Hz_60fps_receiver3.csv")
#  }

def getTransmissionStart(recRatio, transmitter, receiver, precision):
   # print(recRatio)
    
    string = ""
    recRatio = int(recRatio)

    for i in range(0, precision, recRatio):
        for j in range(0, recRatio, 1):
            string += str(transmitter[i]) # transmitted Bit at i index
    
    startPattern = string
    string = ""

    for i in range(0, (precision * recRatio * 100), 1):
        string += str(receiver[i])

    receiverString = string
    found = receiverString.find(startPattern)
  
    return found if found else -1

    

def getBer(transmitterbits, receiverbits, transmission_rate, fps, precision):

    recRatio = int(fps / transmission_rate) 

    vecOverflow = False

    receiver_length = len(receiverbits)
    success = 0
    receiverStart = getTransmissionStart(recRatio, transmitterbits, receiverbits, precision)
    receivedBits = [None] * recRatio

    for bit in transmitterbits:
        tBit = bit
        iSucc = 0

        for r in range(0, recRatio, 1):
            if receiverStart + r < receiver_length:
                rBit = receiverbits[receiverStart + r]
                if (rBit):
                    if rBit == tBit:
                        iSucc += 1
                    receivedBits[r] = rBit
            else:
                vecOverflow = True
            
        receiverStart += recRatio

        if iSucc >= recRatio/2:
            success += 1

    return success/len(transmitterbits) * 100











