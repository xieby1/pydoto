let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  name = "test-pydoto";
  packages = [
    (import ./. { inherit pkgs; })
    pkgs.graphviz
  ];
}
