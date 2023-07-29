// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

import "../interfaces/ERC20.sol";

contract Pashiz is ERC20 {
    address owner;

    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping (address => uint256)) public allowance;

    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        name = "Pashiz";
        symbol = "PSZ";
        decimals = 18;
        totalSupply = _initialSupply;
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    function internal_transfer(address sender, address receiver, uint256 value) internal {
        require(receiver != address(0x0), "burning is not allowed");
        require(balanceOf[sender] >= value, "not enough credit");
        require(balanceOf[receiver] + value >= balanceOf[receiver], "overflow occurred");
        uint256 previousBalances = balanceOf[sender] + balanceOf[receiver];
        balanceOf[sender] -= value;
        balanceOf[receiver] += value;
        emit Transfer(sender, receiver, value);
        assert (previousBalances == balanceOf[sender] + balanceOf[receiver]);
    }

    function transfer(address receiver, uint256 value) public returns (bool successful) {
        internal_transfer(msg.sender, receiver, value);
        return true;
    }

    function transferFrom(address sender, address receiver, uint256 value) public returns(bool successful) {
        require(allowance[sender][msg.sender] >= value, "not approved to transfer");
        internal_transfer(sender, receiver, value);
        allowance[sender][msg.sender] -= value;
        return true;
    }

    function approve(address spender, uint value) public returns (bool successful) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }
}
