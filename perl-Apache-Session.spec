%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Session
Summary:	Apache::Session Perl module
Summary(cs):	Modul Apache::Session pro Perl
Summary(da):	Perlmodul Apache::Session
Summary(de):	Apache::Session Perl Modul
Summary(es):	Módulo de Perl Apache::Session
Summary(fr):	Module Perl Apache::Session
Summary(it):	Modulo di Perl Apache::Session
Summary(ja):	Apache::Session Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Apache::Session ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Apache::Session
Summary(pl):	Modu³ Perla Apache::Session
Summary(pt):	Módulo de Perl Apache::Session
Summary(pt_BR):	Módulo Perl Apache::Session
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Apache::Session
Summary(sv):	Apache::Session Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Apache::Session
Summary(zh_CN):	Apache::Session Perl Ä£¿é
Name:		perl-Apache-Session
Version:	1.54
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(Apache)"

%description
Apache::Session Perl module.

%description -l cs
Modul Apache::Session pro Perl.

%description -l da
Perlmodul Apache::Session.

%description -l de
Apache::Session Perl Modul.

%description -l es
Módulo de Perl Apache::Session.

%description -l fr
Module Perl Apache::Session.

%description -l it
Modulo di Perl Apache::Session.

%description -l ja
Apache::Session Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Apache::Session ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Apache::Session.

%description -l pl
Modu³ perla Apache::Session.

%description -l pt
Módulo de Perl Apache::Session.

%description -l pt_BR
Módulo Perl Apache::Session.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Apache::Session.

%description -l sv
Apache::Session Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Apache::Session.

%description -l zh_CN
Apache::Session Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install eg/example.perl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{perl_sitelib}/Apache/Session
%{perl_sitelib}/Apache/Session.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
