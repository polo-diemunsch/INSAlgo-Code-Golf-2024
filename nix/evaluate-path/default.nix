{ lib
, python3Packages
}:

python3Packages.buildPythonApplication rec {
  pname = "evaluate-path";
  version = "1.0.0";

  format = "other";

  src = ./.;
  
  installPhase = ''
    install -Dm755 $src/evaluate-path.py $out/bin/evaluate-path
  '';

  doCheck = false;
}
