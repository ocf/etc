{ stdenvNoCC, python3, git, rsync }:

stdenvNoCC.mkDerivation {
  pname = "ocf-sync-etc";
  version = "2024-03-16";

  dontUnpack = true;

  installPhase = ''
    install -Dm755 ${./sync-etc} $out/bin/sync-etc
  '';

  propagatedBuildInputs = [
    python3
    git
    rsync
  ];

  meta = {
    description = "OCF etc configuration files";
    homepage = "https://github.com/ocf/etc";
  };
}
