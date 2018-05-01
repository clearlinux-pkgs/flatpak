#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flatpak
Version  : 0.11.3
Release  : 26
URL      : https://github.com/flatpak/flatpak/releases/download/0.11.3/flatpak-0.11.3.tar.xz
Source0  : https://github.com/flatpak/flatpak/releases/download/0.11.3/flatpak-0.11.3.tar.xz
Summary  : Application sandboxing framework
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: flatpak-bin
Requires: flatpak-config
Requires: flatpak-lib
Requires: flatpak-data
Requires: flatpak-locales
Requires: gnupg
Requires: xdg-desktop-portal
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libarchive-dev
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libgsystem)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(ostree-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xdg-desktop-portal)
BuildRequires : sed
BuildRequires : valgrind
BuildRequires : xdg-desktop-portal
BuildRequires : xmlto

%description
These are completely random keys, which include the secret key.
Use these for testing gpg signing, do *NOT* ever use these for any
real application.

%package bin
Summary: bin components for the flatpak package.
Group: Binaries
Requires: flatpak-data
Requires: flatpak-config

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
Requires: flatpak-lib
Requires: flatpak-bin
Requires: flatpak-data
Provides: flatpak-devel

%description dev
dev components for the flatpak package.


%package lib
Summary: lib components for the flatpak package.
Group: Libraries
Requires: flatpak-data

%description lib
lib components for the flatpak package.


%package locales
Summary: locales components for the flatpak package.
Group: Default

%description locales
locales components for the flatpak package.


%prep
%setup -q -n flatpak-0.11.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525199677
%configure --disable-static --disable-documentation
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:

%install
export SOURCE_DATE_EPOCH=1525199677
rm -rf %{buildroot}
%make_install
%find_lang flatpak

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flatpak
/usr/bin/flatpak-bisect
/usr/libexec/flatpak-bwrap
/usr/libexec/flatpak-dbus-proxy
/usr/libexec/flatpak-session-helper
/usr/libexec/flatpak-system-helper

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/flatpak-system-helper.service
/usr/lib/systemd/user/dbus.service.d/flatpak.conf
/usr/lib/systemd/user/flatpak-session-helper.service

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Flatpak-1.0.typelib
/usr/share/bash-completion/completions/flatpak
/usr/share/dbus-1/interfaces/org.freedesktop.Flatpak.xml
/usr/share/dbus-1/services/org.freedesktop.Flatpak.service
/usr/share/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
/usr/share/flatpak/triggers/desktop-database.trigger
/usr/share/flatpak/triggers/gtk-icon-cache.trigger
/usr/share/flatpak/triggers/mime-database.trigger
/usr/share/gdm/env.d/flatpak.env
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.Flatpak.policy
/usr/share/polkit-1/rules.d/org.freedesktop.Flatpak.rules

%files dev
%defattr(-,root,root,-)
/usr/include/flatpak/flatpak-bundle-ref.h
/usr/include/flatpak/flatpak-enum-types.h
/usr/include/flatpak/flatpak-error.h
/usr/include/flatpak/flatpak-installation.h
/usr/include/flatpak/flatpak-installed-ref.h
/usr/include/flatpak/flatpak-ref.h
/usr/include/flatpak/flatpak-related-ref.h
/usr/include/flatpak/flatpak-remote-ref.h
/usr/include/flatpak/flatpak-remote.h
/usr/include/flatpak/flatpak-version-macros.h
/usr/include/flatpak/flatpak.h
/usr/lib64/libflatpak.so
/usr/lib64/pkgconfig/flatpak.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libflatpak.so.0
/usr/lib64/libflatpak.so.0.1103.0

%files locales -f flatpak.lang
%defattr(-,root,root,-)

