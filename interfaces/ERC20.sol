// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

interface ERC20 {
    function totalSupply() external view returns (uint);
    function balanceOf(address account) external view returns (uint);
    function allowance(address owner, address spender) external view returns (uint);
    function transfer(address receiver, uint value) external returns (bool successful);
    function transferFrom(address sender, address receiver, uint value) external returns (bool successful);
    function approve(address spender, uint value) external returns (bool successful);
    event Transfer(address indexed sender, address indexed receiver, uint value);
    event Approval(address indexed owner, address indexed spender, uint value);
}
