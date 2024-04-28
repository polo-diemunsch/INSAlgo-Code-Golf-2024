{ lib
, python3Packages
}:

python3Packages.buildPythonApplication rec {
  pname = "osabie-encode";
  version = "1.0.0";

  format = "other";

  src = ./.;
  
  installPhase = ''
    install -Dm755 $src/osabie-encode.py $out/bin/osabie-encode
  '';

  doCheck = false;
}
