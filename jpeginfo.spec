Summary:	Utility for testing JPEG files
Summary(pl):	Narzêdzie do testowania plików JPEG
Name:		jpeginfo
Version:	1.6.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://www.iki.fi/tjko/projects.html
Source0:	http://www.cc.jyu.fi/~tjko/src/%{name}-%{version}.tar.gz
# Source0-md5:	eda5b0d15d7373c9b0bc96bba4af61e0
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jpeginfo prints information and tests integrity of JPEG/JFIF files.
Program can generate informative listings of jpeg files, and can also
be used to test jpeg files for errors (optionally broken files can be
automatically deleted).

%description -l pl
Jpeginfo wypisuje informacje i testuje integralno¶æ plików JPEG/JFIF.
Program mo¿e generowaæ listê informacji na temat plików jpeg, a tak¿e
byæ u¿ywany do testowania plików na wypadek b³êdów(dodatkowo
uszkodzone pliki mog± byæ automatycznie kasowane).

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%doc README
