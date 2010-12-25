%define upstream_name    KiokuDB-Backend-Files
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Deprecated, use L<KiokuDB::Backend::Files>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/KiokuDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Directory::Transactional)
BuildRequires: perl(File::Path)
BuildRequires: perl(IO)
BuildRequires: perl(KiokuDB)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(Test::TempDir)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This backend provides a file based backend using the
Directory::Transactional manpage to provide ACID semantics.

This is one of the slower backends, and the support for searching is very
limited (only a linear scan is supported), but it is suitable for small,
simple projects.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


