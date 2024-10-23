%define module  Sub-Install

Name:		perl-%{module}
Version:	0.929
Release:	2
Summary:	Install subroutines into packages easily
License:	GPL or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Sub::Install
Source0:	http://www.cpan.org/modules/by-module/Sub/Sub-Install-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:  perl(Test::More)
BuildArch:	noarch

%description 
This module makes it easy to install subroutines into packages without the
unslightly mess of no strict or typeglobs lying about where just anyone can see
them.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Sub
%{_mandir}/*/*
