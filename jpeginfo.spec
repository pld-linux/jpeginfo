Summary:	Utility for testing JPEG files
Summary(pl.UTF-8):	Narzędzie do testowania plików JPEG
Name:		jpeginfo
Version:	1.7.1
Release:	1
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://www.kokkonen.net/tjko/src/%{name}-%{version}.tar.gz
# Source0-md5:	74c8acf55b35670bf475e701e49843c9
URL:		https://www.kokkonen.net/tjko/projects.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jpeginfo prints information and tests integrity of JPEG/JFIF files.
Program can generate informative listings of jpeg files, and can also
be used to test jpeg files for errors (optionally broken files can be
automatically deleted).

%description -l pl.UTF-8
Jpeginfo wypisuje informacje i testuje integralność plików JPEG/JFIF.
Program może generować listę informacji na temat plików jpeg, a także
być używany do testowania plików na wypadek błędów (dodatkowo
uszkodzone pliki mogą być automatycznie kasowane).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub aux
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README
%attr(755,root,root) %{_bindir}/jpeginfo
%{_mandir}/man1/jpeginfo.1*
