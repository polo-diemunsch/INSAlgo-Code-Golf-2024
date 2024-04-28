{ lib
, python3Packages
, fetchFromGitHub
}:

python3Packages.buildPythonApplication rec {
  pname = "osabie";
  version = "legacy";

  format = "other";

  src = fetchFromGitHub {
    owner = "Adriandmen";
    repo = "05AB1E";
    rev = "fb4a2ce2bce6660e1a680a74dd61b72c945e6c3b";
    hash = "sha256-sSDHJNnXqclp9P2IP/j108hFk0VLtH1GvrEhdJQVHxQ=";
  };
  
  installPhase = ''
    mkdir -p $out/lib $out/behaviour
    cp -r lib $out/lib
    cp -r behaviour $out/behaviour

    sed -i '1i#!/usr/bin/env python3' osabie.py
    install -Dm755 osabie.py $out/bin/osabie

    makeWrapperArgs+=( --prefix PYTHONPATH : "$out/lib:$out/behaviour" )
  '';

  doCheck = false;
}
