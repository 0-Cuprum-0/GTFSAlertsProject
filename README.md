# Systemd services and timers (in etc/nixos/configuration.nix)

``

systemd.timers.gtfs_fetcher = {
  wantedBy = [ "timers.target" ];
    timerConfig = {
      OnBootSec = "5m";
      OnUnitActiveSec = "6h";
      Persistent = true;
      Unit = "gtfs_fetcher.service";
    };
};

systemd.services.gtfs_fetcher = {
  script = ''
    cd /home/cuprum/GTFSAlertsProject/server/
    ${pkgs.python313.withPackages (python-pkgs: [
	python-pkgs.gtfs-realtime-bindings
	python-pkgs.requests

		
    ])



    }/bin/python ./parser.py
    ${pkgs.coreutils}/bin/python ./parser.py
  '';
  serviceConfig = {
    Type = "oneshot";
    User = "cuprum";
  };
};

systemd.services.gtfs_server= {
  description = "Server responsible for sending gtfs data to esp32 project ";
  serviceConfig = {
    User = "cuprum";
    Restart = "always";
  };
  script = ''

  ${pkgs.python313}/bin/python   /home/cuprum/GTFSAlertsProject/server/server_handler.py
  '';
  wantedBy = [ "multi-user.target" ]; # starts after login
};




``
