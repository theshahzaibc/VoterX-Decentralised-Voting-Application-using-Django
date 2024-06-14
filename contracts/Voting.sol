// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    struct Voter {
        bool voted;
        uint vote;
        bool isRegistered;
    }

    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    address public admin;
    mapping(address => Voter) public voters;
    Candidate[] public candidates;
    bool public votingStarted;

    event VoterRegistered(address voter);
    event VoteCast(address voter, uint candidateId);

    constructor(string[] memory candidateNames) {
        admin = msg.sender;
        for (uint i = 0; i < candidateNames.length; i++) {
            candidates.push(Candidate({
                id: i,
                name: candidateNames[i],
                voteCount: 0
            }));
        }
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    modifier hasNotVoted() {
        require(!voters[msg.sender].voted, "You have already voted");
        _;
    }

    modifier isRegisteredVoter() {
        require(voters[msg.sender].isRegistered, "You are not a registered voter");
        _;
    }

    function registerVoter(address voter) public onlyAdmin {
        require(!voters[voter].isRegistered, "Voter is already registered");
        voters[voter].isRegistered = true;
        emit VoterRegistered(voter);
    }

    function startVoting() public onlyAdmin {
        votingStarted = true;
    }
    function endVoting() public onlyAdmin {
        votingStarted = false;
    }

    function vote(uint candidateId) public isRegisteredVoter hasNotVoted {
        require(votingStarted, "Voting has not started yet");
        voters[msg.sender].voted = true;
        voters[msg.sender].vote = candidateId;
        candidates[candidateId].voteCount += 1;
        emit VoteCast(msg.sender, candidateId);
    }

    function getCandidates() public view returns (Candidate[] memory) {
        return candidates;
    }

    function getVoter(address voter) public view returns (Voter memory) {
        return voters[voter];
    }
}
