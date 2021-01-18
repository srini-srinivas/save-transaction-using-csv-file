from web3 import Web3
import csv

w3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/de662f5e6a1c44d08f153937a514fcb3'))
block = w3.eth.getBlock(9450580)
val = block.number

address = "0x4f829596FB9541a3aeC8ff78406EF635f650e93c"

if block != None and block.transactions != None:
    print()
    print("Difficulty -" ,block.difficulty)
    print()

for txHash in block.transactions:
    tx = w3.eth.getTransaction(txHash)
    send = (tx['from'])
    receiver = (tx['to'])
    ether = tx['value']
    if(receiver == address):
        print("Transaction is found on block -",val)
        print("Transaction Id -",block.hash.hex())
        print("TimeStamp -",block.timestamp)
        print("From: "+send+" To: "+receiver)
        print("Ether value -",w3.fromWei(ether, "ether"))
    #else:
        #print("Transaction Not Found")    
    
    with open('Transaction.csv', mode='w') as csv_file:
        fieldnames = ['Block','Block_Id','From','To','Ether Value']      
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Block': val, 'Block_Id': block.hash.hex(), 'From': send , "To": receiver , "Ether Value" : w3.fromWei(ether, "ether")})
        