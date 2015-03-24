%define beta alpha
%define qttarballdir qtdoc-opensource-src-%{version}%{?beta:-%{beta}}

Name:		qt5-qtdoc
Version:	5.5.0
Release:	%{?beta:0.%{beta}.}1
Source0:	http://download.qt.io/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/%{qttarballdir}.tar.xz
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	qt5-linguist-tools
BuildRequires:	qdoc5

BuildArch:	noarch


%description
Qt5 Documentation.

%files
# Need to be splitted ?
%doc %_qt5_docdir

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5
%make docs

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

mkdir -p %{buildroot}%{_qt5_docdir}
cp -fr doc/qtdoc* %{buildroot}%{_qt5_docdir}/
