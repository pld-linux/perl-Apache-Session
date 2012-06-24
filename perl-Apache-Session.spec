%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Session
Summary:	Apache::Session Perl module
Summary(cs):	Modul Apache::Session pro Perl
Summary(da):	Perlmodul Apache::Session
Summary(de):	Apache::Session Perl Modul
Summary(es):	M�dulo de Perl Apache::Session
Summary(fr):	Module Perl Apache::Session
Summary(it):	Modulo di Perl Apache::Session
Summary(ja):	Apache::Session Perl �⥸�塼��
Summary(ko):	Apache::Session �� ����
Summary(nb):	Perlmodul Apache::Session
Summary(pl):	Modu� Perla Apache::Session
Summary(pt):	M�dulo de Perl Apache::Session
Summary(pt_BR):	M�dulo Perl Apache::Session
Summary(ru):	������ ��� Perl Apache::Session
Summary(sv):	Apache::Session Perlmodul
Summary(uk):	������ ��� Perl Apache::Session
Summary(zh_CN):	Apache::Session Perl ģ��
Name:		perl-Apache-Session
Version:	1.6
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a373102e3ba49f93a76994c6599e1ff
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Apache)'

%description
Apache::Session is a persistence framework, particularly useful for
tracking session data between httpd requests.  Apache::Session is
designed to work with Apache and mod_perl, but it should work under
CGI and other web servers, and it also works outside of a web server
altogether.

%description -l pl
Apache::Session jest szkieletem trwa�o�ci szczeg�lnie przydatnym przy
przekazywaniu danych pomi�dzy zapytaniami HTTP. Apache::Session
zosta� zaprojektowany do pracy z Apache i mod_perl, ale dzia�a
r�wnie� z CGI, z innymi serwerami HTTP, a tak�e zupe�nie poza
serwerem HTTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/example.perl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES TODO
%{perl_vendorlib}/Apache/Session
%{perl_vendorlib}/Apache/Session.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
