#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-AnyEvent-CacheDNS
Version  : 0.08
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/P/PO/POTYL/AnyEvent-CacheDNS-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PO/POTYL/AnyEvent-CacheDNS-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libanyevent-cachedns-perl/libanyevent-cachedns-perl_0.08-2.debian.tar.xz
Summary  : 'Simple DNS resolver with caching'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-AnyEvent-CacheDNS-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(AnyEvent)
BuildRequires : perl(Module::Build)

%description
AnyEvent::CacheDNS
==================
*******************************************************************************
This CPAN package provides a simple DNS resolver that caches the results for a
faster retrieval for subsequent calls.

%package dev
Summary: dev components for the perl-AnyEvent-CacheDNS package.
Group: Development
Provides: perl-AnyEvent-CacheDNS-devel = %{version}-%{release}

%description dev
dev components for the perl-AnyEvent-CacheDNS package.


%package license
Summary: license components for the perl-AnyEvent-CacheDNS package.
Group: Default

%description license
license components for the perl-AnyEvent-CacheDNS package.


%prep
%setup -q -n AnyEvent-CacheDNS-0.08
cd ..
%setup -q -T -D -n AnyEvent-CacheDNS-0.08 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/AnyEvent-CacheDNS-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-AnyEvent-CacheDNS
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-AnyEvent-CacheDNS/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/AnyEvent/CacheDNS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/AnyEvent::CacheDNS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-AnyEvent-CacheDNS/deblicense_copyright
