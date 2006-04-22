#
# Conditional build:
%bcond_with	java		# with Java bindings
%bcond_without	perl		# without Perl bindings
%bcond_without	ruby		# without Ruby bindings
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Quick Database Manager
Summary(pl):	Quick Database Manager - szybki silnik bazy danych
Name:		qdbm
Version:	1.8.49
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://qdbm.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	0f7eb9a4bafafe7080c73980e38415e9
Patch0:		%{name}-am_ac.patch
URL:		http://qdbm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?with_java:BuildRequires:	jdk}
%if %{with perl}
BuildRequires:  perl-devel >= 1:5.8.0
BuildRequires:  rpm-perlprov >= 4.1-13
%endif
%{?with_ruby:BuildRequires:	ruby-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/qdbm

%description
QDBM is an embeded database library compatible with GDBM and NDBM. It
features hash database and B+ tree database and is developed referring
to GDBM for the purpose of the following three points: higher
processing speed, smaller size of a database file, and simpler API.
This package includes API for C; APIs for C++, Java and CGI scripts
are contained in appropriate subpackages. APIs for Perl and Ruby
should be installed with a source package.

%description -l pl
QDBM to biblioteka wbudowanej bazy danych kompatybilnej z GDBM i NDBM.
Obs³uguje bazy danych oparte na haszach oraz B+ drzewach; jest
tworzona na wzór GDBM-a maj±c na celu nastêpuj±ce trzy punkty: wy¿sz±
szybko¶æ przetwarzania, mniejszy rozmiar pliku bazy danych i prostsze
API. Ten pakiet zawiera API dla C; API dla C++ i Javy oraz skrypty CGI
znajduj± siê w odpowiednich podpakietach. API dla Perla i Ruby'ego
mo¿na doinstalowaæ z pakietu ¼ród³owego.

%package devel
Summary:	Header files, utilities and documentation for QDBM
Summary(pl):	Pliki nag³ówkowe, narzêdzia i dokumentacja dla QDBM-a
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files needed to develop programs using
the QDBM library. Some utility commands are also provided.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia programów z
u¿yciem biblioteki QDBM. Do³±czone jest tak¿e trochê programów
narzêdziowych.

%package static
Summary:	QDBM static library
Summary(pl):	Biblioteka statyczna QDBM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
QDBM static library.

%description static -l pl
Biblioteka statyczna QDBM.

%package plus
Summary:	C++ bindings for QDBM
Summary(pl):	Wi±zania C++ dla QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plus
QDBM C++ bindings.

%description plus -l pl
Wi±zania C++ dla QDBM-a.

%package plus-devel
Summary:	Header files for QDBM C++ bindings
Summary(pl):	Pliki nag³ówkowe wi±zañ C++ dla QDBM-a
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-plus = %{version}-%{release}
Requires:	libstdc++-devel

%description plus-devel
This package contains header files needed to develop programs using
the QDBM C++ bindings.

%description plus-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe potrzebne do tworzenia programów z
u¿yciem wi±zañ C++ QDBM-a.

%package plus-static
Summary:	C++ static library for QDBM
Summary(pl):	Statyczna biblioteka C++ QDBM-a
Group:		Development/Libraries
Requires:	%{name}-plus-devel = %{version}-%{release}

%description plus-static
This package contains static library to develop programs using the
QDBM C++ bindings.

%description plus-static -l pl
Ten pakiet zawiera bibliotekê statyczn± do tworzenia programów z
u¿yciem wi±zañ C++ QDBM-a.

%package cgi
Summary:	CGI scripts with QDBM
Summary(pl):	Skrypty CGI dla QDBM-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description cgi
This package contains CGI scripts with QDBM, for administration of
databases, file uploading, and full-text search.

%description cgi -l pl
Ten pakiet zawiera skrypty CGI dla QDBM-a s³u¿±ce do administrowania
bazami danych, przesy³ania plików i wyszukiwania pe³notekstowego.

%package java
Summary:	Java libraries for QDBM
Summary(pl):	Biblioteki Javy dla QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
QDBM Java bindings.

%description java -l pl
Biblioteki Javy dla QDBM-a.

%package java-devel
Summary:	Java development library for QDBM and documentation
Summary(pl):	Biblioteka programistyczna Javy dla QDBM-a i dokumentacja
Group:		Development/Libraries
Requires:	%{name}-java = %{version}-%{release}

%description java-devel
This package contains development library needed to develop programs
using the QDBM Java bindings.

%description java-devel -l pl
Ten pakiet zawiera bibliotekê programistyczn± potrzebn± do tworzenia
programów z u¿yciem wi±zañ Javy QDBM-a.

%package perl
Summary:	Perl libraries for QDBM
Summary(pl):	Biblioteki Perla dla QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
QDBM Perl bindings.

%description perl -l pl
Biblioteki Perla dla QDBM-a.

%package ruby
Summary:	Ruby libraries for QDBM
Summary(pl):	Biblioteki Ruby dla QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%ruby_ver_requires_eq

%description ruby
QDBM Ruby bindings.

%description ruby -l pl
Biblioteki Ruby dla QDBM-a.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

cd plus
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}
cd ..

%if %{with java}
cd java
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}
cd ..
%endif

%if %{with perl}
cd perl
%{__autoconf}
%configure
%{__make} \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
cd ..
%endif

%if %{with ruby}
cd ruby
%{__autoconf}
%configure
%{__make}
cd ..
%endif

cd cgi
%{__aclocal}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C plus install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C cgi install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with java}
%{__make} -C java install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with perl}
%{__make} -C perl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with ruby}
%{__make} -C ruby install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	plus -p /sbin/ldconfig
%postun	plus -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/libqdbm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc spex.html
%lang(ja) %doc spex-ja.html
%attr(755,root,root) %{_bindir}/dpmgr
%attr(755,root,root) %{_bindir}/dptest
%attr(755,root,root) %{_bindir}/dptsv
%attr(755,root,root) %{_bindir}/crmgr
%attr(755,root,root) %{_bindir}/crtest
%attr(755,root,root) %{_bindir}/crtsv
%attr(755,root,root) %{_bindir}/rlmgr
%attr(755,root,root) %{_bindir}/rltest
%attr(755,root,root) %{_bindir}/hvmgr
%attr(755,root,root) %{_bindir}/hvtest
%attr(755,root,root) %{_bindir}/cbtest
%attr(755,root,root) %{_bindir}/cbcodec
%attr(755,root,root) %{_bindir}/vlmgr
%attr(755,root,root) %{_bindir}/vltest
%attr(755,root,root) %{_bindir}/vltsv
%attr(755,root,root) %{_bindir}/odmgr
%attr(755,root,root) %{_bindir}/odtest
%attr(755,root,root) %{_bindir}/odidx
%attr(755,root,root) %{_libdir}/libqdbm.so
%{_libdir}/libqdbm.la
%{_includedir}/depot.h
%{_includedir}/curia.h
%{_includedir}/relic.h
%{_includedir}/hovel.h
%{_includedir}/cabin.h
%{_includedir}/villa.h
%{_includedir}/vista.h
%{_includedir}/odeum.h
%{_pkgconfigdir}/qdbm.pc
%{_mandir}/man1/dpmgr.1*
%{_mandir}/man1/dptest.1*
%{_mandir}/man1/dptsv.1*
%{_mandir}/man1/crmgr.1*
%{_mandir}/man1/crtest.1*
%{_mandir}/man1/crtsv.1*
%{_mandir}/man1/rlmgr.1*
%{_mandir}/man1/rltest.1*
%{_mandir}/man1/hvmgr.1*
%{_mandir}/man1/hvtest.1*
%{_mandir}/man1/cbtest.1*
%{_mandir}/man1/cbcodec.1*
%{_mandir}/man1/vlmgr.1*
%{_mandir}/man1/vltest.1*
%{_mandir}/man1/vltsv.1*
%{_mandir}/man1/odmgr.1*
%{_mandir}/man1/odtest.1*
%{_mandir}/man1/odidx.1*
%{_mandir}/man3/qdbm.3*
%{_mandir}/man3/depot.3*
%{_mandir}/man3/dpopen.3*
%{_mandir}/man3/curia.3*
%{_mandir}/man3/cropen.3*
%{_mandir}/man3/relic.3*
%{_mandir}/man3/hovel.3*
%{_mandir}/man3/cabin.3*
%{_mandir}/man3/villa.3*
%{_mandir}/man3/vlopen.3*
%{_mandir}/man3/vista.3*
%{_mandir}/man3/odeum.3*
%{_mandir}/man3/odopen.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libqdbm.a
%endif

%files plus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxqdbm.so.*.*.*

%files plus-devel
%defattr(644,root,root,755)
%doc plus/*.html plus/xapidoc
%attr(755,root,root) %{_bindir}/xdptest
%attr(755,root,root) %{_bindir}/xcrtest
%attr(755,root,root) %{_bindir}/xvltest
%attr(755,root,root) %{_libdir}/libxqdbm.so
%{_libdir}/libxqdbm.la
%{_includedir}/xqdbm.h
%{_includedir}/xadbm.h
%{_includedir}/xdepot.h
%{_includedir}/xcuria.h
%{_includedir}/xvilla.h

%if %{with static_libs}
%files plus-static
%defattr(644,root,root,755)
%{_libdir}/libxqdbm.a
%endif

%files cgi
%defattr(644,root,root,755)
%doc cgi/*.html
# don't move cgi binaries to /usr/lib/cgi-bin - write your own wrapper
# (shell script) instead, utilize SCRIPT_NAME env. var. and put into
# your cgi-bin directory
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/qadm.cgi
%attr(755,root,root) %{_libexecdir}/qupl.cgi
%attr(755,root,root) %{_libexecdir}/qfts.cgi
%dir %{_datadir}/qdbm
%dir %{_datadir}/qdbm/cgi
# *.conf are config templates not real configs - don't mark them with
# %%config, don't move it to /etc
%{_datadir}/qdbm/cgi/qadm.conf
%{_datadir}/qdbm/cgi/qupl.conf
%{_datadir}/qdbm/cgi/qfts.conf

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjqdbm.so.*.*.*
%{_libdir}/qdbm.jar

%files java-devel
%defattr(644,root,root,755)
%doc java/jspex.html java/japidoc
%lang(ja) %doc java/jspex-ja.html
%attr(755,root,root) %{_libdir}/libjqdbm.so
%endif

%if %{with perl}
%files perl
%defattr(644,root,root,755)
%doc perl/plspex.html perl/plapidoc
%lang(ja) %doc perl/plspex-ja.html
%attr(755,root,root) %{_bindir}/plcrtest
%attr(755,root,root) %{_bindir}/pldptest
%attr(755,root,root) %{_bindir}/plvltest
%{perl_vendorarch}/Curia.pm
%{perl_vendorarch}/Depot.pm
%{perl_vendorarch}/Villa.pm
%dir %{perl_vendorarch}/auto/Curia
%{perl_vendorarch}/auto/Curia/Curia.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Curia/Curia.so
%dir %{perl_vendorarch}/auto/Depot
%{perl_vendorarch}/auto/Depot/Depot.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Depot/Depot.so
%dir %{perl_vendorarch}/auto/Villa
%{perl_vendorarch}/auto/Villa/Villa.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Villa/Villa.so
%endif

%if %{with ruby}
%files ruby
%defattr(644,root,root,755)
%doc ruby/rbspex.html ruby/rbapidoc
%lang(ja) %doc ruby/rbspex-ja.html
%attr(755,root,root) %{_bindir}/rbcrtest
%attr(755,root,root) %{_bindir}/rbdptest
%attr(755,root,root) %{_bindir}/rbvltest
%{ruby_sitelibdir}/curia.rb
%{ruby_sitelibdir}/depot.rb
%{ruby_sitelibdir}/villa.rb
%attr(755,root,root) %{ruby_sitearchdir}/mod_curia.so
%attr(755,root,root) %{ruby_sitearchdir}/mod_depot.so
%attr(755,root,root) %{ruby_sitearchdir}/mod_villa.so
%endif
