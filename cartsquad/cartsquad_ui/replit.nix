{ pkgs }: {
	deps = [
		pkgs.python39Packages.django
  pkgs.nodejs-18_x
		pkgs.nodePackages.typescript-language-server
		pkgs.yarn
		pkgs.replitPackages.jest
	];
}