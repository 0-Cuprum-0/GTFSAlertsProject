{
  description = "Dev env for python";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-26.05";
  };

  outputs = { self , nixpkgs ,... }: let
    # system should match the system you are running on
    system = "x86_64-linux";

  in {
    devShells."${system}".default = let
      pkgs = import nixpkgs { inherit system; };
    in pkgs.mkShell {
      packages = with pkgs; [
      cowsay
      mpremote
      picocom
      lsof
          (python314.withPackages (ps: with ps; [
	      gtfs-realtime-bindings
	      requests
	      micropython
	      esptool

	
    ]))  


      ];

      shellHook = ''
      echo "Welcome  to dev enviroment for python + micropython "
      '';
    };
  };
}
