%define module  Sub-Install
%define upstream_version 0.926

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:	Install subroutines into packages easily
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Sub/Sub-Install-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
This module makes it easy to install subroutines into packages without the
unslightly mess of no strict or typeglobs lying about where just anyone can see
them.

%prep
%setup -q -n %{module}-%{upstream_version}

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
