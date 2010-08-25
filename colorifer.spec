%define		subver	rc6
%define		rel		1
Summary:	Simple program output colorifer
Name:		colorifer
Version:	1.0.1
Release:	0.%{subver}.%{rel}
License:	GPL
Group:		Applications/Text
URL:		http://colorifer.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/colorifer/colorifer/%{version}%{subver}/%{name}-%{version}%{subver}.tar.bz2
# Source0-md5:	ff478e218d64dd37064dfc47a9429a76
BuildRequires:	boost-devel
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-c++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pcre-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains simple wrapper to colorize output from any
programs.

%prep
%setup -q -n %{name}-%{version}%{subver}

%{__sed} -i -e 's,pcre/pcreposix.h,pcreposix.h,' include/pcre_regex.hh
%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS='-DCONFIGDIR=\\\"%{_datadir}/%{name}/\\\"' \
	DEBUG_LDGLAGS= \
	DEBUG_LDGLAGS_UTILS=

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO NEWS
%attr(755,root,root) %{_bindir}/csed
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/pcolorize*
%attr(755,root,root) %{_libdir}/*.so.*
%dir %{_datadir}/%{name}
%{_mandir}/man1/csed.*
%{_mandir}/man1/pcolorize.*
