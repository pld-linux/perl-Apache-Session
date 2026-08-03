#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Apache
%define		pnam	Session
Summary:	Apache::Session - a persistence framework for session data
Summary(pl.UTF-8):	Apache::Session - szkielet trwałości dla danych w sesji
Name:		perl-Apache-Session
Version:	1.94
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	122b69a50cda8a22cb407d56c51a39ba
Patch0:		%{name}-CVE-2025-40931.patch
Patch1:		%{name}-CVE-2013-10075.patch
Patch2:		%{name}-mysql-lock-result.patch
URL:		https://metacpan.org/dist/Apache-Session
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
%if %{with tests}
BuildRequires:	perl-Crypt-URandom
BuildRequires:	perl-DB_File
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Apache)'

%description
Apache::Session is a persistence framework, particularly useful for
tracking session data between httpd requests. Apache::Session is
designed to work with Apache and mod_perl, but it should work under
CGI and other web servers, and it also works outside of a web server
altogether.

%description -l pl.UTF-8
Apache::Session jest szkieletem trwałości szczególnie przydatnym przy
przekazywaniu danych pomiędzy zapytaniami HTTP. Apache::Session został
zaprojektowany do pracy z Apache i mod_perl, ale działa również z CGI,
z innymi serwerami HTTP, a także zupełnie poza serwerem HTTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
