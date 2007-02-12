%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Session
Summary:	Apache::Session - a persistence framework for session data
Summary(pl.UTF-8):   Apache::Session - szkielet trwałości dla danych w sesji
Name:		perl-Apache-Session
Version:	1.81
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	942788df6c5e743333cae5816551f203
URL:		http://search.cpan.org/dist/Apache-Session/
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
