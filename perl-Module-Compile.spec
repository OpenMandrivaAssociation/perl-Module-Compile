%define upstream_name	 Module-Compile
%define upstream_version 0.23

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl Module Compilation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::SHA1)
BuildArch:	noarch

%description
This module provides a system for writing modules that compile other Perl
modules. Modules that use these compilation modules get compiled into some
altered form the first time they are run. The result is cached into .pmc files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# upstream packaging bug
rm -f lib/Module/._Compile.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc DESIGN Changes
%{perl_vendorlib}/Module
%{_mandir}/*/*

%changelog
* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1mdv2011.0
+ Revision: 685330
- update to new version 0.23

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1
+ Revision: 684774
- update to new version 0.22

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 407805
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.20-5mdv2009.0
+ Revision: 257852
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.20-4mdv2009.0
+ Revision: 245883
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-2mdv2008.1
+ Revision: 137000
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 0.20-1mdv2007.0
+ Revision: 95144
- 0.20
- 0.18
- Import perl-Module-Compile

* Mon Jul 10 2006 Emmanuel Andry <eandry@mandriva.org> 0.17-1mdv2007.0
- New version 0.17

* Wed Jun 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2007.0
- New version 0.16

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-4mdk
- Fix According to perl Policy
	- BuildRequires

* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-3mdk
- Add Buildrequires

* Tue Apr 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-2mdk
- oops, really rpmbuildupdate aware

* Tue Apr 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdk
- new version
- rpmbuildupdate aware
- fix directory ownership
- spec cleanup

* Wed Mar 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.13-1mdk
- 0.13

* Mon Mar 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- Initial MDV release

