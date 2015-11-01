# open chat file
f = open('vgchat.txt', 'r')

# place to store all lists
msgs = []  # list of all messages
afzs = []  # list of all senders


# function definitions
def avgLength(afz, output=True):
    """Calculate the average length of all messages by one sender in number of characters"""
    count = 0
    length = 0
    for msg in msgs:
        if msg.afz == afz:
            count = count + 1
            length = length + len(msg.msg)
    avg = length/count
    if output:
        print afz, 'heeft', count, 'berichten verzonden met een gemiddelde lengte van', avg, 'tekens.'
        return avg
    else:
        return avg


def usedWord(afz, word, output=True):
    """Calculate how many times a sender has used a word"""
    count = 0
    for msg in msgs:
        if msg.afz == afz:
            if word.lower() in msg.msg.lower():
                count = count + 1
    print afz, 'heeft', count, 'keer het woord', word, 'gebruikt.'

def countWord(afz, word, output=True):
    """Calculated how many times a sender has said a word"""
    count = 0
    for msg in msgs:
        if msg.afz == afz:
            count = count + msg.msg.lower().count(word.lower())
    print afz, 'heeft', count, 'keer', word, 'gezegd.'


# message class
class Msg:
    def __init__(self, date, time, afz, msg):
        self.date = date  # date the message was sent
        self.time = time  # time the message was sent
        self.afz = afz  # sender of the message 
        self.msg = msg  # message itself

# process the file
for line in f:
    date = line[0:line.find(',')]
    if len(date) is not 10:
        continue
    res = line[line.find(',')+2:-1]

    time = res[0:res.find(' ')]
    res = res[res.find(' ')+1::]

    if res.find(':') is not -1:
        afz = res[2:res.find(':')]
        msg = res[res.find(':')+2::]

        msg = Msg(date, time, afz, msg)
        msgs.append(msg)
    else:  # skip if status update
        continue

# close file
f.close()

# make a list of all participants (afzs)
for msg in msgs:
    if msg.afz in afzs:
        continue
    else:
        afzs.append(msg.afz)


for afz in afzs:
    # count how many everyone has said the word 'slik'
    countWord(afz, 'slik')

    # write average lengths
    avgLength(afz)
