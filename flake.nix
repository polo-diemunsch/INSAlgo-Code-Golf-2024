{
  description = "Dev environment to run my solutions for INSAlgo 2024 code golf contest";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };
  outputs = { self, nixpkgs, systems }:
    let
      forAllSystems = nixpkgs.lib.genAttrs (import systems);
      pkgsFor = nixpkgs.legacyPackages;
    in {
      devShells = forAllSystems (system: {
        default = pkgsFor.${system}.callPackage ./nix/shell.nix { };
      });
    };
}