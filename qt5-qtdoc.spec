# (tpg) just disobey --excludedocs if passed to allow succesful rpm build
%global _excludedocs 0

%define beta %{nil}

Name:		qt5-qtdoc
Version:	5.15.15
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtdoc-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtdoc-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		https://www.qt.io
# From KDE
%(P=1001; cd %{_sourcedir}; for i in [0-9][0-9][0-9][0-9]-*.patch; do echo -e "Patch$P:\t$i"; P=$((P+1)); done)

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
%autosetup -n %(echo %{qttarballdir} |sed -e 's,-opensource,,') -p1
%{_qt5_bindir}/syncqt.pl -version %{version}

%build
%qmake_qt5
%make_build docs

#------------------------------------------------------------------------------

%install
%make_install install_docs INSTALL_ROOT=%{buildroot}
