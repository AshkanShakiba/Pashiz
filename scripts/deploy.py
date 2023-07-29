from brownie import Pashiz, accounts, network


def deploy_pashiz():
    account = get_account()
    initial_supply = 324 * 10**18
    pashiz = Pashiz.deploy(initial_supply, {"from": account})


def get_account():
    active_network = network.show_active()
    if active_network in ["development", "ganache-local"]:
        return accounts[0]
    else:
        return accounts.load("5Bd")


def main():
    deploy_pashiz()
