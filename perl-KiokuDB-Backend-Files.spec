%define upstream_name    KiokuDB-Backend-Files
Name:       perl-%{upstream_name}
Version:    0.06
Release:    3

Summary:    Deprecated, use L<KiokuDB::Backend::Files>
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/KiokuDB-Backend-Files
Source0:    https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/KiokuDB-Backend-Files-%{version}.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


