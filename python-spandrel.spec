Name:		python-spandrel
Version:	0.4.2
Release:	2
Summary:	PyTorch architecture support for loading many upscaler models
License:	MIT
Group:		Development/Python
URL:		https://github.com/chaiNNer-org/spandrel
Source0:	https://files.pythonhosted.org/packages/source/s/spandrel/spandrel-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(einops)

%description
Spandrel auto-detects and loads a wide range of PyTorch upscaler
and restoration architectures from .pth files. Used by ComfyUI
for extra model loaders.

%files
%doc README.md
%{py_sitedir}/spandrel
%{py_sitedir}/spandrel-*.*-info
