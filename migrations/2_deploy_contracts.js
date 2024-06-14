const Voting = artifacts.require("Voting");

module.exports = function (deployer) {
  const candidateNames = ["Imran Khan", "Nawaz Sharif", "Asif Ali Zardari"];

  // Deploy the Voting contract with the list of candidate names
  deployer.deploy(Voting, candidateNames);
};