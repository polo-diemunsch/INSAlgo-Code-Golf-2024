{ pkgs ? import <nixpkgs> { } }:
  pkgs.mkShell {
    buildInputs = with pkgs; [
      python3
      (pkgs.callPackage ./05AB1E { })
      (pkgs.callPackage ./05AB1E-encode { })
      (pkgs.callPackage ./evaluate-path { })
    ];
}