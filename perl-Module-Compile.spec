%define module	Module-Compile
%define name	perl-%{module}
%define version 0.20
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl Module Compilation
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Digest::SHA1)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides a system for writing modules that compile other Perl
modules. Modules that use these compilation modules get compiled into some
altered form the first time they are run. The result is cached into .pmc files.

%prep
%setup -q -n %{module}-%{version}
# upstream packaging bug
rm -f lib/Module/._Compile.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc DESIGN Changes
%{perl_vendorlib}/Module
%{_mandir}/*/*


