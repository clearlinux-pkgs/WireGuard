#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WireGuard
Version  : 1.0.20210914
Release  : 14
URL      : https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-1.0.20210914.tar.xz
Source0  : https://git.zx2c4.com/wireguard-tools/snapshot/wireguard-tools-1.0.20210914.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: WireGuard-bin = %{version}-%{release}
Requires: WireGuard-data = %{version}-%{release}
Requires: WireGuard-license = %{version}-%{release}
Requires: WireGuard-man = %{version}-%{release}
Requires: WireGuard-services = %{version}-%{release}
BuildRequires : buildreq-qmake

%description
These scripts should be modified according to your precise setup.
They provide a very simple way of tunneling synergy inside of a
WireGuard tunnel, to protect your data in transit.

%package bin
Summary: bin components for the WireGuard package.
Group: Binaries
Requires: WireGuard-data = %{version}-%{release}
Requires: WireGuard-license = %{version}-%{release}
Requires: WireGuard-services = %{version}-%{release}

%description bin
bin components for the WireGuard package.


%package data
Summary: data components for the WireGuard package.
Group: Data

%description data
data components for the WireGuard package.


%package license
Summary: license components for the WireGuard package.
Group: Default

%description license
license components for the WireGuard package.


%package man
Summary: man components for the WireGuard package.
Group: Default

%description man
man components for the WireGuard package.


%package services
Summary: services components for the WireGuard package.
Group: Systemd services

%description services
services components for the WireGuard package.


%prep
%setup -q -n wireguard-tools-1.0.20210914
cd %{_builddir}/wireguard-tools-1.0.20210914

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647627989
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
pushd src
make  %{?_smp_mflags}
popd


%install
export SOURCE_DATE_EPOCH=1647627989
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WireGuard
cp %{_builddir}/wireguard-tools-1.0.20210914/COPYING %{buildroot}/usr/share/package-licenses/WireGuard/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd src
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wg
/usr/bin/wg-quick

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/wg
/usr/share/bash-completion/completions/wg-quick

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WireGuard/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/wg-quick.8
/usr/share/man/man8/wg.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/wg-quick.target
/usr/lib/systemd/system/wg-quick@.service
