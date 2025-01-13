import pkglite as pkg

dirs = ["path/to/pkg"]
txt = "path/to/pkg.txt"
pkg.use_pkglite(dirs)
pkg.pack(dirs, output_file=txt)
pkg.unpack(txt, output_dir="path/to/output")

dirs = ["path/to/pkg1", "path/to/pkg2"]
txt = "path/to/pkgs.txt"
pkg.use_pkglite(dirs)
pkg.pack(dirs, output_file=txt)
pkg.unpack(txt, output_dir="path/to/output")
