import pnrw

node = pnrw.Node("192.168.0.142",dontUseHTTPS=True) # Create a new node instance

print(node.block_count()) # Check node block count

balance = node.account_balance("nano_396phmigwi883hk4x3teedtjk1ejskckmqe7xz3ymfnhe58p9o8gzmkygx91") # Get balance of an account
myBalance = node.rai_from_raw(balance["balance"])
print(f"I currently have {myBalance} Nano!")
