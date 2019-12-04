#
# TODO:
# - build requires jni.h (from package compatible with installed jdk)
#
# Conditional build:
%bcond_without	java		# with Java bindings
%bcond_without	perl		# without Perl bindings
%bcond_without	ruby		# without Ruby bindings
%bcond_without	static_libs	# don't build static libraries
#
%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine with_java
%endif
#
%include	/usr/lib/rpm/macros.perl
#
Summary:	Quick Database Manager
Summary(pl.UTF-8):	Quick Database Manager - szybki silnik bazy danych
Name:		qdbm
Version:	1.8.78
Release:	18
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://fallabs.com/qdbm/%{name}-%{version}.tar.gz
# Source0-md5:	66b3bd69a651316b8d6adc2f21cf3225
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-ruby1.9.patch
URL:		http://fallabs.com/qdbm/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
%if %{with perl}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%endif
%{?with_ruby:BuildRequires:	ruby-devel}
%{?with_ruby:BuildConflicts:	qdbm-devel}
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

%description -l pl.UTF-8
QDBM to biblioteka wbudowanej bazy danych kompatybilnej z GDBM i NDBM.
Obsługuje bazy danych oparte na haszach oraz B+ drzewach; jest
tworzona na wzór GDBM-a mając na celu następujące trzy punkty: wyższą
szybkość przetwarzania, mniejszy rozmiar pliku bazy danych i prostsze
API. Ten pakiet zawiera API dla C; API dla C++ i Javy oraz skrypty CGI
znajdują się w odpowiednich podpakietach. API dla Perla i Ruby'ego
można doinstalować z pakietu źródłowego.

%package devel
Summary:	Header files, utilities and documentation for QDBM
Summary(pl.UTF-8):	Pliki nagłówkowe, narzędzia i dokumentacja dla QDBM-a
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files needed to develop programs using
the QDBM library. Some utility commands are also provided.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem biblioteki QDBM. Dołączone jest także trochę programów
narzędziowych.

%package static
Summary:	QDBM static library
Summary(pl.UTF-8):	Biblioteka statyczna QDBM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
QDBM static library.

%description static -l pl.UTF-8
Biblioteka statyczna QDBM.

%package plus
Summary:	C++ bindings for QDBM
Summary(pl.UTF-8):	Wiązania C++ dla QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plus
QDBM C++ bindings.

%description plus -l pl.UTF-8
Wiązania C++ dla QDBM-a.

%package plus-devel
Summary:	Header files for QDBM C++ bindings
Summary(pl.UTF-8):	Pliki nagłówkowe wiązań C++ dla QDBM-a
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-plus = %{version}-%{release}
Requires:	libstdc++-devel

%description plus-devel
This package contains header files needed to develop programs using
the QDBM C++ bindings.

%description plus-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem wiązań C++ QDBM-a.

%package plus-static
Summary:	C++ static library for QDBM
Summary(pl.UTF-8):	Statyczna biblioteka C++ QDBM-a
Group:		Development/Libraries
Requires:	%{name}-plus-devel = %{version}-%{release}

%description plus-static
This package contains static library to develop programs using the
QDBM C++ bindings.

%description plus-static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną do tworzenia programów z
użyciem wiązań C++ QDBM-a.

%package cgi
Summary:	CGI scripts with QDBM
Summary(pl.UTF-8):	Skrypty CGI dla QDBM-a
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}

%description cgi
This package contains CGI scripts with QDBM, for administration of
databases, file uploading, and full-text search.

%description cgi -l pl.UTF-8
Ten pakiet zawiera skrypty CGI dla QDBM-a służące do administrowania
bazami danych, przesyłania plików i wyszukiwania pełnotekstowego.

%package java
Summary:	Java libraries for QDBM
Summary(pl.UTF-8):	Wiązania Javy do QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
QDBM Java bindings.

%description java -l pl.UTF-8
Wiązania Javy do QDBM-a.

%package java-devel
Summary:	Java development library for QDBM and documentation
Summary(pl.UTF-8):	Biblioteka programistyczna Javy dla QDBM-a i dokumentacja
Group:		Development/Libraries
Requires:	%{name}-java = %{version}-%{release}

%description java-devel
This package contains development library needed to develop programs
using the QDBM Java bindings.

%description java-devel -l pl.UTF-8
Ten pakiet zawiera bibliotekę programistyczną potrzebną do tworzenia
programów z użyciem wiązań Javy QDBM-a.

%package perl
Summary:	Perl libraries for QDBM
Summary(pl.UTF-8):	Wiązania Perla do QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
QDBM Perl bindings.

%description perl -l pl.UTF-8
Wiązania Perla do QDBM-a.

%package ruby
Summary:	Ruby libraries for QDBM
Summary(pl.UTF-8):	Wiązania języka Ruby do QDBM-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ruby
QDBM Ruby bindings.

%description ruby -l pl.UTF-8
Wiązania języka Ruby do QDBM-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static%{!?with_static_libs:=no}
%{__make} -j1

cd plus
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static%{!?with_static_libs:=no}
%{__make} -j1
cd ..

%if %{with java}
cd java
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make} -j1
cd ..
%endif

%if %{with perl}
cd perl
%{__autoconf}
%configure
%{__make} -j1 \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
cd ..
%endif

%if %{with ruby}
cd ruby
%{__autoconf}
%configure
%{__make} -j1
cd ..
%endif

cd cgi
%{__aclocal}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -j1 -C plus install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -j1 -C cgi install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with java}
%{__make} -j1 -C java install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with perl}
%{__make} -j1 -C perl install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with ruby}
%{__make} -j1 -C ruby install \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_vendorarchdir} \
	RUBYLIBDIR=$RPM_BUILD_ROOT%{ruby_vendorlibdir} \
	DESTDIR=$RPM_BUILD_ROOT
%endif

# packaged as %doc
%if %{with perl}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/qdbm/perl/{plapidoc,*.html}
%endif
%if %{with ruby}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/qdbm/ruby/{rbapidoc,*.html}
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
%attr(755,root,root) %ghost %{_libdir}/libqdbm.so.13

%files devel
%defattr(644,root,root,755)
%doc doc/spex.html
%lang(ja) %doc doc/spex-ja.html
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
%attr(755,root,root) %{_bindir}/qmttest
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
%{_mandir}/man1/qmttest.1*
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
%attr(755,root,root) %ghost %{_libdir}/libxqdbm.so.3

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
%attr(755,root,root) %ghost %{_libdir}/libjqdbm.so.1
%{_libdir}/qdbm.jar

%files java-devel
%defattr(644,root,root,755)
%doc java/jspex.html java/japidoc
%lang(ja) %doc java/jspex-ja.html
%attr(755,root,root) %{_libdir}/libjqdbm.so
%{_libdir}/libjqdbm.la
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
%attr(755,root,root) %{perl_vendorarch}/auto/Curia/Curia.so
%dir %{perl_vendorarch}/auto/Depot
%attr(755,root,root) %{perl_vendorarch}/auto/Depot/Depot.so
%dir %{perl_vendorarch}/auto/Villa
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
%{ruby_vendorlibdir}/curia.rb
%{ruby_vendorlibdir}/depot.rb
%{ruby_vendorlibdir}/villa.rb
%attr(755,root,root) %{ruby_vendorarchdir}/mod_curia.so
%attr(755,root,root) %{ruby_vendorarchdir}/mod_depot.so
%attr(755,root,root) %{ruby_vendorarchdir}/mod_villa.so
%endif
