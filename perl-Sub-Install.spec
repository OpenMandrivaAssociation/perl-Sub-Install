%define module  Sub-Install

Name:		perl-%{module}
Version:	0.925
Release:	9
Summary:	Install subroutines into packages easily
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Sub/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
This module makes it easy to install subroutines into packages without the
unslightly mess of no strict or typeglobs lying about where just anyone can see
them.

%prep
%setup -q -n %{module}-%{version}

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

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.925-6mdv2012.0
+ Revision: 765663
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.925-5
+ Revision: 764174
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.925-4
+ Revision: 667316
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.925-3mdv2011.0
+ Revision: 609166
- rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.925-2mdv2010.0
+ Revision: 440669
- rebuild

* Sat Jan 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.925-1mdv2009.1
+ Revision: 330402
- update to new version 0.925

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.924-3mdv2009.0
+ Revision: 241909
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.924-1mdv2008.0
+ Revision: 74474
- import perl-Sub-Install


* Wed Aug 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.924-1mdv2008.0
- first mdv release
