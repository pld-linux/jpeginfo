Summary:	Utility for testing JPEG files
Summary(pl):	Narz�dzie do testowania plik�w JPEG
Name:		jpeginfo
Version:	1.6.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.cc.jyu.fi/~tjko/src/%{name}-%{version}.tar.gz
# Source0-md5:	eda5b0d15d7373c9b0bc96bba4af61e0
URL:		http://www.iki.fi/tjko/projects.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jpeginfo prints information and tests integrity of JPEG/JFIF files.
Program can generate informative listings of jpeg files, and can also
be used to test jpeg files for errors (optionally broken files can be
automatically deleted).

%description -l pl
Jpeginfo wypisuje informacje i testuje integralno�� plik�w JPEG/JFIF.
Program mo�e generowa� list� informacji na temat plik�w jpeg, a tak�e
by� u�ywany do testowania plik�w na wypadek b��d�w (dodatkowo
uszkodzone pliki mog� by� automatycznie kasowane).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub aux
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
