%define module  Sub-Install

Summary:	Install subroutines into packages easily
Name:		perl-%{module}
Version:	0.925
Release:	12
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description 
This module makes it easy to install subroutines into packages without the
unslightly mess of no strict or typeglobs lying about where just anyone can see
them.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Sub
%{_mandir}/man3/*

