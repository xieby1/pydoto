let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  name = "test-pydoto";
  packages = [
    (pkgs.python3Packages.callPackage ./. {})
    pkgs.graphviz
  ];
}
