#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	InKey
Summary:	Term::InKey - Perl extension for clearing the screen and receiving a keystroke
Summary(pl):	Term::InKey - rozszerzenie Perla do czyszczenia ekranu i odczytu klawisza
Name:		perl-Term-InKey
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2b31a6bb2f1b48123e6bc8f7a2f72147
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements Clear() to clear screen and ReadKey() to
receive a keystroke, on UNIX and Win32 platforms. As opposed to
Term::ReadKey, it does not contain XSUB code.

%description -l pl
Ten modu³ implementuje funkcjê Clear() do czyszczenia ekranu i
ReadKey() do odczytywania klawisza na platformach uniksowych i Win32.
W przeciwieñstwie do Term::ReadKey nie zawiera kodu XSUB.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Term/InKey.pm
%{_mandir}/man3/*
