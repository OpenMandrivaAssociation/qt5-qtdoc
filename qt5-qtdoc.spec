%define api 5
%define qtminor 4
%define qtsubminor 0

%define qtversion %{api}.%{qtminor}.%{qtsubminor}
%define qttarballdir qtdoc-opensource-src-%{qtversion}

Name:		qt5-qtdoc
Version:	%{qtversion}
Release:	1
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
Source0:	http://download.qt-project.org/official_releases/qt/%{api}.%{qtminor}/%{version}/submodules/%{qttarballdir}.tar.xz
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5XmlPatterns)
BuildRequires:	qt5-qttools-assistant
BuildRequires:	qdoc5

BuildArch:	noarch


%description
Qt5 Documentation

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
