%include	/usr/lib/rpm/macros.perl
Summary:	Apache-Session perl module
Summary(pl):	Modu³ perla Apache-Session
Name:		perl-Apache-Session
Version:	1.54
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/Apache-Session-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache-Session perl module.

%description -l pl
Modu³ perla Apache-Session.

%prep
%setup -q -n Apache-Session-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install eg/example.perl $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Apache/Session
%{perl_sitelib}/Apache/Session.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}/example.perl
