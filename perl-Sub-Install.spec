%define module  Sub-Install
%define	name	perl-%{module}
%define version 0.925
%define release %mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Install subroutines into packages easily
License: 	GPL or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description 
This module makes it easy to install subroutines into packages without the
unslightly mess of no strict or typeglobs lying about where just anyone can see
them.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%check
%{__make} test

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Sub
%{_mandir}/*/*

