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
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	qdoc5
BuildRequires:	findutils
BuildArch:	noarch


%description
Qt5 Documentation.

%files
# Need to be splitted ?
%doc %_qt5_docdir

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir
%apply_patches

%build
rpm -ql %{_lib}qt5core-devel
ls -l /usr/share/doc/qt5
ls -l /usr/share/doc/qt5/global
ls -l /usr/share/doc/qt5/global/template
find /usr/share/doc/qt5
rpm -V %{_lib}qt5core-devel
ls -l /usr/share/doc/qt5/global/qt-module-defaults.qdocconf
#find . -name "*.qdocconf"

%qmake_qt5
%make docs

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_qt5_docdir}
cp -fr doc/qtdoc* %{buildroot}%{_qt5_docdir}/
