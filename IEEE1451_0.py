
# Import Statements
import struct # https://docs.python.org/3/library/struct.html




class NCAP:

    def __init__ (self, ncapID, ncapName, addressType, ncapAddress):
        self.ncapID = ncapID
        self.ncapName = ncapName
        self.addressType = addressType
        self.ncapAddress = ncapAddress



def generateNCAPAnnouncementMessage(NCAPObject):
    '''
    NetSvcType netSvcType // network service type (value = 1)
    NetSvcId netSvcId // network service Id (value = 1)
    MsgType msgType // Message type (value = 3)
    UInt16 msgLength // message length (2 bytes)
    UUID ncapId // NCAP Identifier (UUID)
    _String ncapName // NCAP name (length = 16)
    AddressType addressType // Address type (1-IPv4, 2-IPv6)
    UInt8Array ncapAddress // Address values (length = 4 or 16 bytes)
    '''
    if (NCAPObject.addressType == 1):   # If IPv4
        msgLength = 38+4
    elif (NCAPObject.addressType == 2): #if IPv6
        msgLength = 38+16
    return "1,1,3," + str(msgLength) + "," + NCAPObject.ncapName + "," + str(NCAPObject.addressType) + "," + str(NCAPObject.ncapAddress)

def generateNCAPDiscoveryMessage(NCAPObject):
    '''
    NetSvcType netSvcType
    NetSvcId netSvcId
    MsgType msgType
    UInt16 msgLength
    UInt16 errorCode
    UUID appId
    UUIDArray ncapIds
    StringArray ncapNames
    UInt8Array addressTypes
    UInt8Array ncapAddresses
    '''
