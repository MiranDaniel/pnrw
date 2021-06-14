
# PNRW: Python Nanocurrency RPC Wrapper

***PNRW is a Python Wrapper for the Nano RPC protocol.***

---

![badge](https://img.shields.io/pypi/dm/pnrw?style=for-the-badge)
![badge](https://img.shields.io/pypi/pyversions/pnrw?style=for-the-badge)

## Documentation

PNRW uses the same variable and function names as the RPC Protocol, this means that you can use the official documentation for this library.

(There are some differences, please check the difference guide below)

---
<!-- markdownlint-disable -->
### pnrw.**Node**
<!-- markdownlint-restore -->
*The node class handles all node connections.*

```py
import pnrw

node = pnrw.Node("nodeIp") # Create a new node instance
```

#### **Arguments**

`ip` (str): The node IP address

#### **Optional arguments**

`port` (int): The node's RPC port, default value is 7076

`dontUseHTTPS` (bool): Disables HTTPS, default value if False

`headers` (dict): Custom headers that are sent with each request, default value is "Default"


## Examples

#### Starting code

```py
import pnrw

node = pnrw.Node("mynano.ninja/api/node") # Create a new node instance
```

#### Getting basic node information

```py
import pnrw

node = pnrw.Node("mynano.ninja/api/node") # Create a new node instance

print(node.block_count()) # Check node block count
print(node.version()["protocol_version"]) # Print protocol version of node
print(node.uptime()) # Print node uptime in seconds
```

#### Showing current account balance

```py
import pnrw

node = pnrw.Node("mynano.ninja/api/node") # Create a new node instance

balance = node.account_balance("nano_396phmigwi883hk4x3teedtjk1ejskckmqe7xz3ymfnhe58p9o8gzmkygx91") # Get balance of an account
myBalance = node.rai_from_raw(balance["balance"]) # Convert from raw to Nano

print(f"I currently have {myBalance} Nano!")
```
---

## Differences from official commands


### Node.**sign**

*Official documentation: <https://docs.nano.org/commands/rpc-protocol/#sign>*

Changed to: `sign_private()` & `sign_acount()` & `sign_block_hash()`

#### **Changes**

Use `sign_private()` when signing a block with a private key, `sign_account()` when signing a block with an account from wallet and `sign_block_hash()` when signing a block hash.

---

## Donations

### All donations and contributions are welcome! <3

Nano: `nano_396phmigwi883hk4x3teedtjk1ejskckmqe7xz3ymfnhe58p9o8gzmkygx91`

Banano: `ban_1aws637mb3qnuf9j8swzufq3nj3fttuzkixbd817nmmhyms6a6kt1zyptq87`