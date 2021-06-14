"""
    Copyright (C) 2021 MiranDaniel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import requests
import json

def _validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False

    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

class Node:
    def __init__(self, ip, port=7076, dontUseHTTPS=False, headers="Default"):
        self.ip = ip
        self.port = port
        self.secure = "s" if dontUseHTTPS == False else ""
        if _validate_ip(self.ip) == True:
            self.target = f"http{self.secure}://{self.ip}:{self.port}"
        else:
            self.target = f"http{self.secure}://{self.ip}"
        if headers != "Default":
            self.headers = {'Content-type': 'application/json', 'Accept': '*/*',"Accept-Encoding":"gzip, deflate, br","Connection":"keep-alive"}
        else:
            self.headers = headers

    def _request(self, data):
        response = requests.post(self.target, data=json.dumps(data), headers=self.headers).text
        return json.loads(response)

    def account_balance(self, account):
        response = self._request(
            {"action": "account_balance", "account": account})
        return {"balance": int(response["balance"]), "pending": int(response["pending"])}

    def account_block_count(self, account):
        response = self._request(
            {"action": "account_block_count", "account": account})
        return int(response["block_count"])

    def account_get(self, key):
        response = self._request({"action": "account_get", "key": key})
        return response["account"]

    def account_history(self, account, count):
        response = self._request(
            {"action": "account_history", "account": account, "count": count})
        ret = {
            "account": response["account"],
            "history": [],
            "previous": response["previous"]
        }
        for i in response["history"]:
            ret["history"].append(
                {
                    "type": i["type"],
                    "account": i["account"],
                    "amount": int(i["amount"]),
                    "local_timestamp": int(i["local_timestamp"]),
                    "height": int(i["height"]),
                    "hash": i["hash"]
                }
            )
        return ret

    def account_info(self, account):
        response = self._request(
            {"action": "account_info", "account": account})
        return {
            "frontier": response["frontier"],
            "open_block": response["open_block"],
            "representative_block": response["representative_block"],
            "balance": int(response["balance"]),
            "modified_timestamp": int(response["modified_timestamp"]),
            "block_count": int(response["block_count"]),
            "account_version": int(response["account_version"]),
            "confirmation_height": int(response["confirmation_height"]),
            "confirmation_height_frontier": response["confirmation_height_frontier"],
        }

    def account_key(self, account):
        response = self._request({"action": "account_key", "account": account})
        return response["key"]

    def account_representative(self, account):
        response = self._request(
            {"action": "account_representative", "account": account})
        return response["representative"]

    def account_weight(self, account):
        response = self._request(
            {"action": "account_weight", "account": account})
        return int(response["weight"])

    def accounts_balances(self, accounts):
        response = self._request(
            {"action": "accounts_balances", "accounts": accounts})
        ret = {}
        for i in response["balances"]:
            ret[i] = {"balance": int(response["balances"][i]["balance"]), "pending": int(
                response["balances"][i]["pending"])}

        return ret

    def accounts_frontiers(self, accounts):
        response = self._request(
            {"action": "accounts_frontiers", "accounts": accounts})
        ret = {}
        for i in response["frontiers"]:
            ret[i] = response["frontiers"][i]

        return ret

    def account_pending(self, accounts, count):
        response = self._request(
            {"action": "account_pending", "accounts": accounts, "count": count})
        ret = {}
        for i in response["blocks"]:
            ret[i] = response["blocks"][i]

        return ret

    def available_supply(self):
        response = self._request({"action": "available_supply"})
        return int(response["available"])

    def block_account(self, Hash):
        response = self._request({"action": "available_supply", "hash": Hash})
        return response["account"]

    def block_confirm(self, Hash):
        response = self._request({"action": "available_supply", "hash": Hash})
        return int(response["started"])

    def block_count(self):
        response = self._request({"action": "block_count"})
        if "count" in response:
            return {"count": int(response["count"]), "unchecked": int(response["unchecked"]), "cemented": int(response["cemented"])}

    def block_create(self, json_block, Type, balance, key, representative, link, previous):
        response = self._request({"action": "block_create", "json_block": json_block, "type": Type,
                                 "balance": balance, "key": key, "representative": representative, "link": link, "previous": previous})
        return {
            "hash": response["hash"],
            "difficulty": response["difficulty"],
            "block": {
                "type": response["type"],
                "account": response["account"],
                "previous": response["previous"],
                "representative": response["representative"],
                "balance": int(response["balance"]),
                "link": response["link"],
                "link_as_account": response["link_as_account"],
                "signature": response["signature"],
                "work": response["work"],
            }
        }

    def block_hash(self, json_block, block):
        response = self._request(
            {"action": "block_create", "json_block": json_block, "block": block})
        return response["hash"]

    def block_info(self, json_block, Hash):
        response = self._request(
            {"action": "block_create", "json_block": json_block, "hash": Hash})
        return {
            "block_account": response["block_account"],
            "amount": int(response["amount"]),
            "balance": int(response["balance"]),
            "height": int(response["height"]),
            "local_timestamp": response["local_timestamp"],
            "confirmed": response["confirmed"],
            "contents": {
                "type": response["type"],
                "account": response["account"],
                "previous": response["previous"],
                "representative": response["representative"],
                "balance": int(response["balance"]),
                "link": response["link"],
                "link_as_account": response["link_as_account"],
                "signature": response["signature"],
                "work": response["work"],
            },
            "subtype": response["subtype"],
        }

    # blocks
    # blocks_info

    def bootstrap(self, address, port):
        response = self._request(
            {"action": "bootstrap", "address": address, "port": port})
        return response["success"]

    def bootstrap_any(self):
        response = self._request({"action": "bootstrap_any"})
        return response["success"]

    def bootstrap_lazy(self, Hash):
        response = self._request({"action": "bootstrap_lazy", "hash": Hash})
        return {
            "started": response["started"],
            "key_inserted": response["key_inserted"]
        }

    def bootstrap_status(self):
        response = self._request({"action": "bootstrap_status"})
        ret = {
            "bootstrap_threads": int(response["bootstrap_threads"]),
            "running_attempts_count": int(response["running_attempts_count"]),
            "total_attempts_count": int(response["total_attempts_count"]),
            "connections": {
                "clients": int(response["clients"]),
                "connections": int(response["connections"]),
                "idle": int(response["idle"]),
                "target_connections": int(response["target_connections"]),
                "pulls": int(response["pulls"])
            },
            "attempts": []
        }
        for i in response["attempts"]:
            ret["attempts"].append(i)  # WORK ON DATATYPE CONVERSION

        return ret

    def chain(self, block, count):
        response = self._request(
            {"action": "chain", "block": block, "count": count})
        return response["blocks"]

    def confirmation_active(self):
        response = self._request(
            {"action": "confirmation_active"})
        ret = {
            "confirmations": [],
            "unconfirmed": int(response["unconfirmed"]),
            "confirmed": int(response["confirmed"])
        }
        for i in response["confirmations"]:
            ret["confirmations"].append(i)

        return response["blocks"]

    def confirmation_height_currently_processing(self):
        response = self._request(
            {"action": "confirmation_height_currently_processing"})
        return response["hash"]

    def confirmation_history(self):
        response = self._request(
            {"action": "confirmation_history"})
        ret = {
            "confirmation_stats": {
                "count": int(response["confirmation_stats"]["count"]),
                "average": int(response["confirtmation_stats"]["count"])
            },
            "confirmations": []
        }
        for i in response["confirmations"]:
            ret["confirmations"].append({
                "hash": i["hash"],
                "duration": int(i["duration"]),
                "time": int(i["time"]),
                "tally": int(i["tally"]),
                "blocks": int(i["blocks"]),
                "voters": int(i["voters"]),
                "request_count": int(i["request_count"])
            })
        return ret

    # confirmation_info
    # confirmation_quorum
    # database_txn_tracker

    def delegators(self):
        response = self._request(
            {"action": "delegators"})
        ret = {}
        for i in response["delegators"]:
            ret[i] = int(response["delegators"][i])

        return ret

    def delegators_count(self, account):
        response = self._request(
            {"action": "delegators_count", "account": account})
        return int(response["count"])

    def deterministic_key(self, seed, index):
        response = self._request(
            {"action": "deterministic_key", "seed":seed,"index":index})
        return response

    def epoch_upgrade(self, epoch, key):
        response = self._request(
            {"action": "epoch_upgrade", "epoch": epoch, "key": key})
        return int(response["started"])

    def frontier_count(self):
        response = self._request({"action": "frontier_count"})
        return int(response["count"])

    def frontiers(self,account,count):
        response = self._request({"action": "frontiers","account":account,"count":count})
        return response["frontiers"]

    def keepalive(self, address, port):
        response = self._request(
            {"action": "keepalive", "address": address, "port": port})
        return int(response["started"])

    def key_create(self):
        response = self._request({"action": "key_create"})
        return response

    def key_expand(self, key):
        response = self._request({"action": "key_expand", "key": key})
        return response

    def ledger(self, account, count):
        response = self._request({"action": "ledger", "account":account,"count":count})
        ret = {}
        for i in response["accounts"]:
            ret[i] = {
                "frontier": response["accounts"][i]["frontier"],
                "open_block": response["accounts"][i]["open_block"],
                "representative_block": response["accounts"][i]["representative_block"],
                "balance": int(response["accounts"][i]["balance"]),
                "modified_timestamp": int(response["accounts"][i]["modified_timestamp"]),
                "block_count": int(response["accounts"][i]["block_count"])
            }
        return ret

    def node_id(self):
        response = self._request({"action": "node_id"})
        return response

    def node_id_delete(self):
        response = self._request({"action": "node_id_delete"})
        return response["deprecated"]

    def peers(self):
        response = self._request({"action": "peers"})
        ret = {}
        for i in response["peers"]:
            ret[i] = int(response["peers"][i])
        return ret

    def pending(self, account, count):
        response = self._request(
            {"action": "pending", "account": account, "count": count})
        return response["blocks"]

    def pending_exists(self, Hash):
        response = self._request({"action": "pending_exists", "hash": Hash})
        return int(response["exists"])

    def process(self, json_block, subtype, block):
        response = self._request({"action": "process", "json_block":json_block,"subtype":subtype, "block":block})
        return response["hash"]

    def representatives(self):
        response = self._request({"action": "representatives"})
        ret = {}
        for i in response["representatives"]:
            ret[i] = int(response["representatives"][i])
        return ret

    def representatives_online(self):
        response = self._request({"action": "representatives_online"})
        return response["representatives"]

    def republish(self, Hash):
        response = self._request({"action": "republish", "hash": Hash})
        return {
            "success": response["success"],
            "blocks": response["blocks"]
        }

    # sign

    def stats(self, Type):
        response = self._request({"action": "stats", "type": Type})
        return response

    def stats_clear(self):
        response = self._request({"action": "stats_clear"})
        return response["success"]

    def stop(self):
        response = self._request({"action": "stop"})
        return response["success"]

    def successors(self, block, count):
        response = self._request(
            {"action": "successors", "block": block, "count": count})
        return response["blocks"]

    def telemetry(self):
        response = self._request({"action": "telemetry"})
        return {
            "block_count": int(response["block_count"]),
            "cemented_count": int(response["cemented_count"]),
            "unchecked_count": int(response["unchecked_count"]),
            "account_count": int(response["account_count"]),
            "bandwidth_cap": int(response["bandwidth_cap"]),
            "peer_count": int(response["peer_count"]),
            "protocol_version": int(response["protocol_version"]),
            "uptime": int(response["uptime"]),
            "genesis_block": response["genesis_block"],
            "major_version": int(response["major_version"]),
            "minor_version": int(response["minor_version"]),
            "patch_version": int(response["patch_version"]),
            "pre_release_version": int(response["pre_release_version"]),
            "maker": int(response["maker"]),
            "timestamp": int(response["timestamp"]),
            "active_difficulty": response["active_difficulty"]
        }

    def validate_account_number(self, account):
        response = self._request(
            {"action": "validate_account_number", "account": account})
        return int(response["valid"])

    def version(self, account):
        response = self._request(
            {"action": "version"})
        return {
            "rpc_version": int(response["rpc_version"]),
            "store_version": int(response["store_version"]),
            "protocol_version": int(response["protocol_version"]),
            "node_vendor": response["node_vendor"],
            "store_vendor": response["store_vendor"],
            "network": response["network"],
            "network_identifier": response["network_identifier"],
            "build_info": response["build_info"]
        }

    # unchecked

    def unchecked_clear(self):
        response = self._request({"action": "unchecked_clear"})
        return response["success"]

    # unchecked_get
    # unchecked_keys
    # unopened

    def uptime(self):
        response = self._request({"action": "uptime"})
        return int(response["seconds"])

    def work_cancel(self, Hash):
        response = self._request({"action": "work_cancel", "hash": Hash})
        return response

    # work_generate

    def work_peer_add(self, address, port):
        response = self._request(
            {"action": "work_peer_add", "address": address, "port": port})
        return response["success"]

    def work_peers(self):
        response = self._request({"action": "work_peers"})
        return response["work_peers"]

    def work_peers_clear(self):
        response = self._request({"action": "work_peer_add"})
        return response["success"]

    # work validate

    def account_create(self, wallet):
        response = self._request(
            {"action": "account_create", "wallet": wallet})
        return response["account"]

    def account_list(self, wallet):
        response = self._request({"action": "account_list", "wallet": wallet})
        return response["accounts"]

    def account_move(self, wallet, source, accounts):
        response = self._request(
            {"action": "account_move", "wallet": wallet, "source": source, "accounts": accounts})
        return int(response["moved"])

    def account_remove(self, wallet, account):
        response = self._request(
            {"action": "account_remove", "wallet": wallet, "account": account})
        return int(response["removed"])

    def account_representative_set(self, wallet, account, representative):
        response = self._request({"action": "account_representative_set",
                                 "wallet": wallet, "account": account, "representative": representative})
        return response["block"]

    def accounts_create(self, wallet, count):
        response = self._request(
            {"action": "accounts_create", "wallet": wallet, "count": count})
        return response["accounts"]

    def password_change(self, wallet, password):
        response = self._request(
            {"action": "password_change", "wallet": wallet, "password": password})
        return int(response["changed"])

    def password_enter(self, wallet, password):
        response = self._request(
            {"action": "password_enter", "wallet": wallet, "password": password})
        return int(response["valid"])

    def password_valid(self, wallet):
        response = self._request(
            {"action": "password_valid", "wallet": wallet})
        return int(response["valid"])

    def receive(self, wallet, account, block):
        response = self._request(
            {"action": "password_valid", "wallet": wallet, "account": account, "block": block})
        return response["block"]

    def receive_minimum(self):
        response = self._request(
            {"action": "receive_minimum"})
        return int(response["amount"])

    def receive_minimum_set(self, amount):
        response = self._request(
            {"action": "receive_minimum_set", "amount": amount})
        return response["success"]

    def search_pending(self, wallet):
        response = self._request(
            {"action": "search_pending", "wallet": wallet})
        return int(response["started"])

    def search_pending_all(self):
        response = self._request(
            {"action": "search_pending_all"})
        return response["success"]

    def send(self, wallet, source, destination, amount, Id=None):
        if Id != None:
            response = self._request(
                {"action": "send", "wallet": wallet, "source": source, "destination": destination, "amount": amount, "id": Id})
        else:
            response = self._request(
                {"action": "send", "wallet": wallet, "source": source, "destination": destination, "amount": amount})

        return response["block"]

    def wallet_add(self, wallet, key):
        response = self._request(
            {"action": "wallet_add", "wallet": wallet, "key": key})
        return response["account"]

    def wallet_add_watch(self, wallet, accounts):
        response = self._request(
            {"action": "wallet_add_watch", "wallet": wallet, "accounts": accounts})
        return response["success"]

    def wallet_balances(self, wallet):
        response = self._request(
            {"action": "wallet_balances", "wallet": wallet})
        ret = {}
        for i in response["balances"]:
            ret[i] = int(response["balances"][i])
        return ret

    def wallet_change_seed(self, wallet, seed):
        response = self._request(
            {"action": "wallet_change_seed", "wallet": wallet, "seed": seed})
        return {
            "success": response["success"],
            "last_restored_account": response["last_restored_account"],
            "restored_count": int(response["restored_count"])
        }

    def wallet_contains(self, wallet, account):
        response = self._request(
            {"action": "wallet_contains", "wallet": wallet, "account": account})
        return int(response["exists"])

    def wallet_create(self):
        response = self._request(
            {"action": "wallet_create"})
        return response["wallet"]

    def wallet_destroy(self, wallet):
        response = self._request(
            {"action": "wallet_destroy", "wallet": wallet})
        return int(response["destroyed"])

    # wallet_export

    def wallet_frontiers(self, wallet):
        response = self._request(
            {"action": "wallet_frontiers", "wallet": wallet})
        return response["frontiers"]

    def wallet_history(self, wallet):
        response = self._request({"wallet_history": "peers", "wallet": wallet})
        ret = []
        for i in response["history"]:
            ret.append(
                {
                    "type": response[i]["type"],
                    "account": response[i]["account"],
                    "amount": int(response[i]["amount"]),
                    "block_account": response[i]["block_account"],
                    "hash": response[i]["hash"],
                    "local_timestamp": int(response[i]["local_timestamp"]),
                }
            )
        return ret

    def wallet_info(self, wallet):
        response = self._request(
            {"action": "wallet_info", "wallet": wallet})
        ret = {}
        for i in response:
            ret[i] = int(i)
        return ret

    def wallet_ledger(self, wallet):
        response = self._request(
            {"action": "wallet_ledger", "wallet": wallet})
        ret = {}
        for i in response["accounts"]:
            ret[i] = {
                "frontier": response["accounts"][i]["frontier"],
                "open_block": response["accounts"][i]["open_block"],
                "representative_block": response["accounts"][i]["representative_block"],
                "balance": int(response["accounts"][i]["balance"]),
                "modified_timestamp": int(response["accounts"][i]["modified_timestamp"]),
                "block_count": int(response["accounts"][i]["block_count"])
            }
        return ret

    def wallet_lock(self, wallet):
        response = self._request(
            {"action": "wallet_lock", "wallet": wallet})
        return int(response["locked"])

    def wallet_locked(self, wallet):
        response = self._request(
            {"action": "wallet_locked", "wallet": wallet})
        return int(response["locked"])

    def wallet_pending(self, wallet, count):
        response = self._request(
            {"action": "wallet_pending", "wallet": wallet, "count": count})
        return response["blocks"]

    def wallet_representative(self, wallet):
        response = self._request(
            {"action": "wallet_representative", "wallet": wallet})
        return response["representative"]

    def wallet_representative_set(self, wallet, representative):
        response = self._request(
            {"action": "wallet_representative_set", "wallet": wallet, "representative": representative})
        return int(response["set"])

    def wallet_republish(self, wallet, count):
        response = self._request(
            {"action": "wallet_republish", "wallet": wallet, "count": count})
        return response["blocks"]

    def wallet_work_get(self, wallet):
        response = self._request(
            {"action": "wallet_work_get", "wallet": wallet})
        return response["works"]

    def work_get(self, wallet, account):
        response = self._request(
            {"action": "work_get", "wallet": wallet, "account": account})
        return response["work"]

    def work_set(self, wallet, account, work):
        response = self._request(
            {"action": "work_set", "wallet": wallet, "account": account, "work": work})
        return response["success"]

    """ UNIT CONVERSION RPCS """

    def krai_from_raw(self, amount):
        response = self._request(
            {"action": "krai_from_raw", "amount": amount})
        return int(response["amount"])

    def krai_to_raw(self, amount):
        response = self._request(
            {"action": "krai_to_raw", "amount": amount})
        return int(response["amount"])

    def mrai_from_raw(self, amount):
        response = self._request(
            {"action": "mrai_from_raw", "amount": amount})
        return int(response["amount"])

    def mrai_to_raw(self, amount):
        response = self._request(
            {"action": "mrai_to_raw", "amount": amount})
        return int(response["amount"])

    def rai_from_raw(self, amount):
        response = self._request(
            {"action": "rai_from_raw", "amount": amount})
        return int(response["amount"])

    def rai_to_raw(self, amount):
        response = self._request(
            {"action": "rai_to_raw", "amount": amount})
        return int(response["amount"])
