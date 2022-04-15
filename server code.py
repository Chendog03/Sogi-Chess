from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    def __init__(self, clientNumber):
        self.clientNumber = clientNumber

    def connectionMade(self):
        self.factory.users.append(self)

    def dataReceived(self, data):

        data = data.decode('ascii')
            
        if data.startswith('!JOIN'):
            text = '[MESSAGE] Hello {name}. Your client number is {data}.'.format(name = data[6::], data = self.clientNumber).encode('ascii')
            self.transport.write(text)
            return

        if data.startswith('!MOVE'):
            textList = data.split(' ')

            prv = [textList[1], textList[2]]
            nxt = [textList[3], textList[4]]
            moveNum = int(textList[5])
            piece = textList[6]

            print('move number {num} from {prv} to {nxt}'.format(prv = prv, nxt = nxt, num = moveNum))
            
            # TELL EVERYONE TO MOVE
            
            byteText = '[MOVE] {prev0} {prev1} {nxt0} {nxt1} {p}'.format(prev0 = prv[0], prev1 = prv[1], nxt0 = nxt[0], nxt1 = nxt[1], p = piece).encode('ascii')

            if moveNum%2 == 0:
                self.factory.users[1].transport.write(byteText)
            else:
                self.factory.users[0].transport.write(byteText)

    def connectionLost(self, reason):
        self.factory.clientCount -= 1
        self.factory.users.remove(self)
        
            


class serverFactory(protocol.Factory):
    maxConnections = 2

    def __init__(self):
        self.users = []
        self.clientCount = 0

    def buildProtocol(self, *args, **kwargs):
        if self.clientCount >= self.maxConnections:
            return None

        self.clientCount += 1

        p = Echo(self.clientCount)
        p.factory = self
        return p



def main():
    """This runs the protocol on port 25565"""
    
    reactor.listenTCP(25565, serverFactory())
    reactor.run()




# this only runs if the module was *not* imported
if __name__ == "__main__":
    main()










