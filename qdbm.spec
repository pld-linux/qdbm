# 
# Conditional build:
%bcond_with	java	# with java bindings
#
Summary:	Quick Database Manager
Name:		qdbm
Version:	1.8.48
Release:	0.1
Source0:	http://qdbm.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	ac59de1fd23478edcb906612fe48f3b8
License:	LGPL
Group:		Development/Libraries
Url:		http://qdbm.sourceforge.net/
%{?with_java:BuildRequires:	jdk}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_libexecdir	/usr/lib/qdbm

%description
QDBM is an embeded database library compatible with GDBM and NDBM. It
features hash database and B+ tree database and is developed referring
to GDBM for the purpose of the following three points: higher
processing speed, smaller size of a database file, and simpler API.
This package includes APIs for C, C++, and Java. CGI scripts are also
contained. APIs for Perl and Ruby should be installed with a source
package.

%package devel
Summary:	Headers, libraries, utilities and documentation for QDBM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and libraries needed to develop
programs using the QDBM library. Some utility commands are also
provided.

%package static
Summary:	QDBM static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
QDBM static libraries.

%package plus
Summary:	C++ bindings for QDBM
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plus
QDBM C++ bindings.

%package plus-devel
Summary:	C++ libraries for QDBM
Group:		Development/Libraries
Requires:	%{name}-plus = %{version}-%{release}

%description plus-devel
This package contains libraries needed to develop and run programs
using the QDBM C++ bindings.

%package plus-static
Summary:	C++ static libraries for QDBM
Group:		Development/Libraries
Requires:	%{name}-plus-devel = %{version}-%{release}

%description plus-static
This package contains static libraries needed to develop and run programs
using the QDBM C++ bindings.

%package java
Summary:	Java libraries for QDBM
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
QDBM Java bindings.

%package java-devel
Summary:	Java libraries for QDBM
Group:		Development/Libraries
Requires:	%{name}-java = %{version}-%{release}

%description java-devel
This package contains libraries needed to develop and run programs
using the QDBM Java bindings.

%package cgi
Summary:	CGI scripts with QDBM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description cgi
This package contains CGI scripts with QDBM, for administration of
databases, file uploading, and full-text search.

%prep
%setup -q

%build
%configure
%{__make}

cd plus
%configure
%{__make}
cd ..

%if %{with java}
cd java
%configure
%{__make}
cd ..
%endif

cd cgi
%configure
%{__make} 
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

cd plus
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ..

%if %{with java}
cd java
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ..
%endif

cd cgi
%{__make} install DESTDIR=$RPM_BUILD_ROOT
cd ..

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	plus -p /sbin/ldconfig
%postun	plus -p /sbin/ldconfig

%post	java -p /sbin/ldconfig
%postun	java -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/libqdbm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_libdir}/libqdbm.so
%{_includedir}/depot.h
%{_includedir}/curia.h
%{_includedir}/relic.h
%{_includedir}/hovel.h
%{_includedir}/cabin.h
%{_includedir}/villa.h
%{_includedir}/vista.h
%{_includedir}/odeum.h
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
%{_pkgconfigdir}/qdbm.pc
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libqdbm.a

%files plus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxqdbm.so.*.*.*

%files plus-devel
%defattr(644,root,root,755)
%doc plus/*.html plus/xapidoc
%{_includedir}/xqdbm.h
%{_includedir}/xadbm.h
%{_includedir}/xdepot.h
%{_includedir}/xcuria.h
%{_includedir}/xvilla.h
%attr(755,root,root) %{_libdir}/libxqdbm.so
%attr(755,root,root) %{_bindir}/xdptest
%attr(755,root,root) %{_bindir}/xcrtest
%attr(755,root,root) %{_bindir}/xvltest

%files plus-static
%defattr(644,root,root,755)
%{_libdir}/libxqdbm.a

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjqdbm.so.*.*.*
%{_libdir}/qdbm.jar

%files java-devel
%defattr(644,root,root,755)
%doc java/*.html java/japidoc
%attr(755,root,root) %{_libdir}/libjqdbm.so
%endif

%files cgi
%defattr(644,root,root,755)
%doc cgi/*.html
# don't move it to /usr/lib/cgi-bin - write your wrapper (sh script),
# utilize SCRIPT_NAME env. var. and put into your cgi-bin directory
%{_libexecdir}/qadm.cgi
%{_libexecdir}/qupl.cgi
%{_libexecdir}/qfts.cgi
# config templates - don't add to %%config, don't move it to /etc
%{_datadir}/qdbm/cgi/qadm.conf
%{_datadir}/qdbm/cgi/qupl.conf
%{_datadir}/qdbm/cgi/qfts.conf
