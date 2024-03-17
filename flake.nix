{
  description = "OCF etc configuration files";

  outputs = { self }:
    let
      overlay = (final: prev: {
        ocf-sync-etc = final.callPackage ./sync { };
      });
    in
    {
      overlays.ocf-sync-etc = overlay;
      overlays.default = overlay;
    };
}
