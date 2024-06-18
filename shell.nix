{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.gcc
    pkgs.pkg-config
    pkgs.openssl
    pkgs.zlib
    pkgs.python3
    pkgs.python3Packages.virtualenv
    pkgs.cargo
  ];
}
