%define upstream_name	 Module-Compile
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl Module Compilation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:  perl(Digest::SHA1)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a system for writing modules that compile other Perl
modules. Modules that use these compilation modules get compiled into some
altered form the first time they are run. The result is cached into .pmc files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
