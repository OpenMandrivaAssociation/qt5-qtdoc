%define beta %{nil}

Name:		qt5-qtdoc
Version:	5.15.3
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtdoc-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtdoc-everywhere-src-5.15.2
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/5.15.2/submodules/%{qttarballdir}.tar.xz
%endif
# From KDE
Patch1000:	0001-Bump-version.patch
Patch1001:	0002-EGLFS-document-that-desktop-centric-APIs-are-not-sup.patch
Patch1002:	0003-Move-Qt-Wayland-Compositor-to-Commercial-GPLv3-secti.patch
Patch1004:	0005-wasm-link-to-platform-notes-page-instead-of-wiki.patch
Patch1005:	0006-wasm-move-supported-modules-list-to-front-page.patch
Patch1006:	0007-wasm-remove-some-incorrect-information.patch
Patch1009:	0010-Android-keep-only-mandatory-arguments-for-configure-.patch
Patch1010:	0011-Doc-update-some-packages-for-Linux.patch
Patch1011:	0012-Android-update-linux-package-dependencies.patch
Patch1012:	0013-Remove-unneeded-italic-decoration.patch
Patch1013:	0014-Linux-Fix-library-xcb-spelling-errors.patch
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	pkgconfig(Qt5Concurrent) >= %{version}
BuildRequires:	pkgconfig(Qt5Gui) >= %{version}
BuildRequires:	pkgconfig(Qt5Multimedia) >= %{version}
BuildRequires:	pkgconfig(Qt5Script) >= %{version}
BuildRequires:	pkgconfig(Qt5Widgets) >= %{version}
BuildRequires:	pkgconfig(Qt5Qml) >= %{version}
BuildRequires:	qt5-assistant
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-macros
BuildRequires:	qt5-qttools >= 5.11.0-0
BuildRequires:	qdoc5
BuildRequires:	qmake5 >= %{version}
BuildRequires:	findutils
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt5 Documentation.

%files
%{_qt5_docdir}/qtdoc.qch
%{_qt5_docdir}/qtdoc
%{_qt5_docdir}/qtcmake.qch
%{_qt5_docdir}/qtcmake
%{_libdir}/qt5/examples

#------------------------------------------------------------------------------

%prep
%autosetup -n %qttarballdir -p1
%{_qt5_bindir}/syncqt.pl -version %{version}

%build
%qmake_qt5
%make_build docs

#------------------------------------------------------------------------------

%install
%make_install install_docs INSTALL_ROOT=%{buildroot}
