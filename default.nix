{ lib
, buildPythonPackage
, pydot
}: buildPythonPackage {
  name = "pydoto";
  src = lib.sourceByRegex ./. [".*\.py$"];
  propagatedBuildInputs = [ pydot ];
}
