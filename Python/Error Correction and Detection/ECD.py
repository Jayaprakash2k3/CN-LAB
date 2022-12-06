#ORIGINAL_DATA="01101001"
RECIVED_DATA="01101101"
def Detect(data):
    p1=data[1]
    p2=data[2]
    p4=data[4]    
    calP1=str((p1+data[3]+data[5]+data[7]).count("1")%2)
    calP2=str((p2+data[3]+data[6]+data[7]).count("1")%2)
    calP4=str((p4+data[5]+data[6]+data[7]).count("1")%2)
    print("Actual Parity Bit:",calP4,calP2,calP1)
    print("Recived Parity Bit:",p4,p2,p1)
    return (calP1+calP2+calP4)

def Correct(data,index):
    base=0
    value=0
    for each in range(len(index)):
        base=2**each
        value=(base*int(index[each]))+value
    print("Error is Detected at Index:",value)
    data[value]="0" if data[value]=="1"  else "1"
    print("Corrected Data:","".join(data))
    return index

a=Detect(RECIVED_DATA)
b=Correct(list(RECIVED_DATA),a)