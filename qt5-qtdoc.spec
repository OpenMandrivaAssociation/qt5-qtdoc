%define beta %nil

Name:		qt5-qtdoc
Version:	5.5.1
%if "%{beta}" != ""
Release:	1.%{beta}.1
%define qttarballdir qtdoc-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtdoc-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	qdoc5
BuildRequires:	qt5-assistant
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-macros
BuildRequires:	qmake5
BuildRequires:	findutils
BuildArch:	noarch


%description
Qt5 Documentation.

%files
%doc LICENSE.FDL
%{_qt5_docdir}/qtdoc.qch
%{_qt5_docdir}/qtdoc

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir
%apply_patches

%build
%qmake_qt5
%make docs

#------------------------------------------------------------------------------

%install
make install_docs INSTALL_ROOT=%{buildroot}
