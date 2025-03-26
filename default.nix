{ pkgs ? import <nixpkgs> {} }:
pkgs.python3Packages.buildPythonPackage {
  name = "pydoto";
  src = pkgs.lib.sourceByRegex ./. [".*\.py$"];
  propagatedBuildInputs = [
    pkgs.python3Packages.pydot
  ];
}
