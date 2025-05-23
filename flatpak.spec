#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : flatpak
Version  : 1.14.10
Release  : 106
URL      : https://github.com/flatpak/flatpak/releases/download/1.14.10/flatpak-1.14.10.tar.xz
Source0  : https://github.com/flatpak/flatpak/releases/download/1.14.10/flatpak-1.14.10.tar.xz
Source1  : flatpak-init.service
Source2  : flatpak.tmpfiles
Source3  : https://github.com/flatpak/flatpak/releases/download/1.14.10/flatpak-1.14.10.tar.xz.asc
Source4  : E05AE1478F814C4F.pkey
Summary  : Application sandboxing framework
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: flatpak-autostart = %{version}-%{release}
Requires: flatpak-bin = %{version}-%{release}
Requires: flatpak-config = %{version}-%{release}
Requires: flatpak-data = %{version}-%{release}
Requires: flatpak-lib = %{version}-%{release}
Requires: flatpak-libexec = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}
Requires: flatpak-locales = %{version}-%{release}
Requires: flatpak-services = %{version}-%{release}
Requires: glib-networking
Requires: gnupg
Requires: gsettings-desktop-schemas
Requires: xdg-desktop-portal-gtk
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : file
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libarchive-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(appstream)
BuildRequires : pkgconfig(dconf)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gpgme)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libgsystem)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libzstd)
BuildRequires : pkgconfig(ostree-1)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(xau)
BuildRequires : pypi(pyparsing)
BuildRequires : sed
BuildRequires : valgrind
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-add-cleanup-helpers.patch

%description
<p align="center">
<img src="https://github.com/flatpak/flatpak/blob/main/flatpak.png?raw=true" alt="Flatpak icon"/>
</p>

%package autostart
Summary: autostart components for the flatpak package.
Group: Default

%description autostart
autostart components for the flatpak package.


%package bin
Summary: bin components for the flatpak package.
Group: Binaries
Requires: flatpak-data = %{version}-%{release}
Requires: flatpak-libexec = %{version}-%{release}
Requires: flatpak-config = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}
Requires: flatpak-services = %{version}-%{release}

%description bin
bin components for the flatpak package.


%package config
Summary: config components for the flatpak package.
Group: Default

%description config
config components for the flatpak package.


%package data
Summary: data components for the flatpak package.
Group: Data

%description data
data components for the flatpak package.


%package dev
Summary: dev components for the flatpak package.
Group: Development
Requires: flatpak-lib = %{version}-%{release}
Requires: flatpak-bin = %{version}-%{release}
Requires: flatpak-data = %{version}-%{release}
Provides: flatpak-devel = %{version}-%{release}
Requires: flatpak = %{version}-%{release}

%description dev
dev components for the flatpak package.


%package lib
Summary: lib components for the flatpak package.
Group: Libraries
Requires: flatpak-data = %{version}-%{release}
Requires: flatpak-libexec = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}

%description lib
lib components for the flatpak package.


%package libexec
Summary: libexec components for the flatpak package.
Group: Default
Requires: flatpak-config = %{version}-%{release}
Requires: flatpak-license = %{version}-%{release}

%description libexec
libexec components for the flatpak package.


%package license
Summary: license components for the flatpak package.
Group: Default

%description license
license components for the flatpak package.


%package locales
Summary: locales components for the flatpak package.
Group: Default

%description locales
locales components for the flatpak package.


%package services
Summary: services components for the flatpak package.
Group: Systemd services
Requires: systemd

%description services
services components for the flatpak package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE4}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE3} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) E05AE1478F814C4F' gpg.status
%setup -q -n flatpak-1.14.10
cd %{_builddir}/flatpak-1.14.10
%patch -P 1 -p1
pushd ..
cp -a flatpak-1.14.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724169367
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-documentation \
--with-profile-dir=/usr/share/defaults/etc/profile.d \
--disable-seccomp \
--enable-gdm-env-file
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-documentation \
--with-profile-dir=/usr/share/defaults/etc/profile.d \
--disable-seccomp \
--enable-gdm-env-file
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724169367
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flatpak
cp %{_builddir}/flatpak-%{version}/COPYING %{buildroot}/usr/share/package-licenses/flatpak/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/flatpak-%{version}/subprojects/libglnx/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/flatpak/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/flatpak-%{version}/subprojects/libglnx/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/flatpak/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang flatpak
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/flatpak-init.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/flatpak.conf
## Remove excluded files
rm -f %{buildroot}*/usr/share/gdm/env.d/flatpak.env
## install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
mv system-helper/org.freedesktop.Flatpak.SystemHelper.conf %{buildroot}/usr/share/dbus-1/system.d/

mkdir -p %{buildroot}/usr/lib/systemd/system/graphical.target.wants
ln -sf ../flatpak-init.service %{buildroot}/usr/lib/systemd/system/graphical.target.wants/flatpak-init.service

cp flatpak-cleanup.service %{buildroot}/usr/lib/systemd/system/flatpak-cleanup.service
mkdir -p %{buildroot}/usr/libexec
cp clr-flatpak-cleanup %{buildroot}/usr/libexec/clr-flatpak-cleanup

## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system-environment-generators/60-flatpak-system-only
/usr/lib/systemd/user-environment-generators/60-flatpak

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/graphical.target.wants/flatpak-init.service

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/flatpak
/usr/bin/flatpak
/usr/bin/flatpak-bisect
/usr/bin/flatpak-coredumpctl

%files config
%defattr(-,root,root,-)
/usr/lib/sysusers.d/flatpak.conf
/usr/lib/tmpfiles.d/flatpak.conf

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Flatpak-1.0.typelib
/usr/share/bash-completion/completions/flatpak
/usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.Authenticator.xml
/usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.xml
/usr/share/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
/usr/share/dbus-1/services/org.flatpak.Authenticator.Oci.service
/usr/share/dbus-1/services/org.freedesktop.Flatpak.service
/usr/share/dbus-1/services/org.freedesktop.portal.Flatpak.service
/usr/share/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
/usr/share/dbus-1/system.d/org.freedesktop.Flatpak.SystemHelper.conf
/usr/share/defaults/etc/profile.d/flatpak.sh
/usr/share/fish/vendor_completions.d/flatpak.fish
/usr/share/fish/vendor_conf.d/flatpak.fish
/usr/share/flatpak/triggers/desktop-database.trigger
/usr/share/flatpak/triggers/gtk-icon-cache.trigger
/usr/share/flatpak/triggers/mime-database.trigger
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.Flatpak.policy
/usr/share/polkit-1/rules.d/org.freedesktop.Flatpak.rules
/usr/share/zsh/site-functions/_flatpak

%files dev
%defattr(-,root,root,-)
/usr/include/flatpak/flatpak-bundle-ref.h
/usr/include/flatpak/flatpak-enum-types.h
/usr/include/flatpak/flatpak-error.h
/usr/include/flatpak/flatpak-installation.h
/usr/include/flatpak/flatpak-installed-ref.h
/usr/include/flatpak/flatpak-instance.h
/usr/include/flatpak/flatpak-portal-error.h
/usr/include/flatpak/flatpak-ref.h
/usr/include/flatpak/flatpak-related-ref.h
/usr/include/flatpak/flatpak-remote-ref.h
/usr/include/flatpak/flatpak-remote.h
/usr/include/flatpak/flatpak-transaction.h
/usr/include/flatpak/flatpak-version-macros.h
/usr/include/flatpak/flatpak.h
/usr/lib64/libflatpak.so
/usr/lib64/pkgconfig/flatpak.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libflatpak.so.0.11410.0
/usr/lib64/libflatpak.so.0
/usr/lib64/libflatpak.so.0.11410.0

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/flatpak-bwrap
/V3/usr/libexec/flatpak-dbus-proxy
/V3/usr/libexec/flatpak-oci-authenticator
/V3/usr/libexec/flatpak-portal
/V3/usr/libexec/flatpak-session-helper
/V3/usr/libexec/flatpak-system-helper
/V3/usr/libexec/flatpak-validate-icon
/V3/usr/libexec/revokefs-fuse
/usr/libexec/clr-flatpak-cleanup
/usr/libexec/flatpak-bwrap
/usr/libexec/flatpak-dbus-proxy
/usr/libexec/flatpak-oci-authenticator
/usr/libexec/flatpak-portal
/usr/libexec/flatpak-session-helper
/usr/libexec/flatpak-system-helper
/usr/libexec/flatpak-validate-icon
/usr/libexec/revokefs-fuse

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flatpak/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/flatpak/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/graphical.target.wants/flatpak-init.service
/usr/lib/systemd/system/flatpak-cleanup.service
/usr/lib/systemd/system/flatpak-init.service
/usr/lib/systemd/system/flatpak-system-helper.service
/usr/lib/systemd/user/flatpak-oci-authenticator.service
/usr/lib/systemd/user/flatpak-portal.service
/usr/lib/systemd/user/flatpak-session-helper.service

%files locales -f flatpak.lang
%defattr(-,root,root,-)

