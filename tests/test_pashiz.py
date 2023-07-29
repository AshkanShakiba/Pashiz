from brownie import Pashiz, accounts
from brownie.exceptions import VirtualMachineError


def test_deploy():
    account = accounts[0]
    initial_supply = 324 * 10**18
    pashiz = Pashiz.deploy(initial_supply, {"from": account})
    name = pashiz.name({"from": account})
    symbol = pashiz.symbol({"from": account})
    decimals = pashiz.decimals({"from": account})
    total_supply = pashiz.totalSupply({"from": account})
    assert name == "Pashiz"
    assert symbol == "PSZ"
    assert decimals == 18
    assert total_supply == initial_supply
    return pashiz


def test_transfer():
    pashiz = test_deploy()
    transfer_value = 4 * 10**18
    sender, receiver = accounts[0], accounts[1]
    sender_initial_balance = pashiz.balanceOf(sender, {"from": sender})
    receiver_initial_balance = pashiz.balanceOf(receiver, {"from": receiver})
    pashiz.transfer(receiver, transfer_value, {"from": sender})
    assert pashiz.balanceOf(sender, {"from": sender}) == sender_initial_balance - transfer_value
    assert pashiz.balanceOf(receiver, {"from": receiver}) == receiver_initial_balance + transfer_value


def test_approve():
    pashiz = test_deploy()
    approve_value = 20 * 10**18
    owner, spender, receiver = accounts[0], accounts[1], accounts[2]
    owner_initial_balance = pashiz.balanceOf(owner, {"from": owner})
    spender_initial_balance = pashiz.balanceOf(spender, {"from": spender})
    receiver_initial_balance = pashiz.balanceOf(receiver, {"from": receiver})
    pashiz.approve(spender, approve_value, {"from": owner})
    assert pashiz.allowance(owner, spender, {"from": spender}) == approve_value
    pashiz.transferFrom(owner, receiver, approve_value, {"from": spender})
    assert pashiz.balanceOf(owner, {"from": owner}) == owner_initial_balance - approve_value
    assert pashiz.balanceOf(receiver, {"from": receiver}) == receiver_initial_balance + approve_value


def test_transfer_burn():
    pashiz = test_deploy()
    transfer_value = 4 * 10**18
    sender, receiver = accounts[0], "0x0000000000000000000000000000000000000000"
    sender_initial_balance = pashiz.balanceOf(sender, {"from": sender})
    try:
        pashiz.transfer(receiver, transfer_value, {"from": sender})
    except VirtualMachineError:
        pass
    assert pashiz.balanceOf(sender, {"from": sender}) == sender_initial_balance


def test_transfer_not_enough_credit():
    pashiz = test_deploy()
    transfer_value = 4 * 10**18
    sender, receiver = accounts[1], accounts[0]
    sender_initial_balance = pashiz.balanceOf(sender, {"from": sender})
    receiver_initial_balance = pashiz.balanceOf(receiver, {"from": receiver})
    try:
        pashiz.transfer(receiver, transfer_value, {"from": sender})
    except VirtualMachineError:
        pass
    assert pashiz.balanceOf(sender, {"from": sender}) == sender_initial_balance
    assert pashiz.balanceOf(receiver, {"from": receiver}) == receiver_initial_balance


def test_not_enough_allowance():
    pashiz = test_deploy()
    approve_value = 20 * 10**18
    owner, spender, receiver = accounts[0], accounts[1], accounts[2]
    owner_initial_balance = pashiz.balanceOf(owner, {"from": owner})
    spender_initial_balance = pashiz.balanceOf(spender, {"from": spender})
    receiver_initial_balance = pashiz.balanceOf(receiver, {"from": receiver})
    pashiz.approve(spender, approve_value, {"from": owner})
    assert pashiz.allowance(owner, spender, {"from": spender}) == approve_value
    try:
        pashiz.transferFrom(owner, receiver, approve_value + 1, {"from": spender})
    except VirtualMachineError:
        pass
    assert pashiz.balanceOf(owner, {"from": owner}) == owner_initial_balance
    assert pashiz.balanceOf(receiver, {"from": receiver}) == receiver_initial_balance
