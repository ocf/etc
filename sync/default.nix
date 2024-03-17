{ python3Packages, python3, git, rsync }:

python3Packages.buildPythonApplication {
  pname = "ocf-sync-etc";
  version = "2024-03-16";
  format = "other";

  dontUnpack = true;

  installPhase = ''
    mkdir -p $out/bin
    cp ${./sync-etc} $out/bin/sync-etc
  '';

  propagatedBuildInputs = [
    git
    rsync
  ];

  meta = {
    description = "OCF etc configuration files";
    homepage = "https://github.com/ocf/etc";
  };
}
