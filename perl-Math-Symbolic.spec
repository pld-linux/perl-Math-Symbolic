#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Symbolic
Summary:	Math::Symbolic - symbolic calculations
Summary(pl):	Math::Symbolic - obliczenia symboliczne
Name:		perl-Math-Symbolic
Version:	0.125
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83b0bc6886e61b8e8bf52223712f9be8
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Memoize) >= 1.01
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-Pod-Coverage
BuildRequires:	perl(Test::More)
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Symbolic is intended to offer symbolic calculation capabilities
to the Perl programmer without using external (and commercial)
libraries and/or applications.

There are several ways to construct Math::Symbolic trees. There are no
actual Math::Symbolic objects, but rather trees of objects of
subclasses of Math::Symbolic. The most general but unfortunately also
the least intuitive way of constructing trees is to use the
constructors of the Math::Symbolic::Operator,
Math::Symbolic::Variable, and Math::Symbolic::Constant classes to
create (nested) objects of the corresponding types.

Furthermore, you may use the overloaded interface to apply the
standard Perl operators (and functions) to existing Math::Symbolic
trees and standard Perl expressions.

Possibly the most convenient way of constructing Math::Symbolic trees
is using the builtin parser to generate trees from expressions such as
'2 * x^5'. You may use the Math::Symbolic->parse_from_string() class
method for this.

Of course, you may combine the overloaded interface with the parser to
generate trees with Perl code such as "$term * 5 * 'sin(omega*t+phi)'"
which will create a tree of the existing tree $term times 5 times the
sine of the vars omega times t plus phi.

%description -l pl
Pakiet Math::Symbolic oferuje programistom perlowym mo¿liwo¶æ obliczeñ
symbolicznych bez u¿ywania zewnêtrznych (i komercyjnych) bibliotek
i/lub aplikacji.

Drzewa Math::Symbolic mo¿na tworzyæ na kilka sposobów. Nie ma
w³a¶ciwych obiektów Math::Symbolic, zamiast nich u¿ywa siê podklas
Math::Symbolic. Najbardziej ogólnym, ale niestety najmniej intuicyjnym
sposobem tworzenia drzew jest u¿ycie konstruktorów klas
Math::Symbolic::Operator, Math::Symbolic::Variable i
Math::Symbolic::Constant do tworzenia (zagnie¿d¿onych) obiektów
odpowiednich typów.

Poza tym mo¿na u¿ywaæ interfejsu przeci±¿ania, aby u¿ywaæ
standardowych operatorów (i funkcji) Perla na istniej±cych drzewach
Math::Symbolic i standardowych wyra¿eniach perlowych.

Prawdopodobnie najwygodniejszym sposobem tworzenia drzew
Math::Symbolic jest u¿ywanie wbudowanego parsera do generowania drzew
z wyra¿eñ takich jak '2 * x^5'. Mo¿na do tego u¿yæ metody klasy
Math::Symbolic->parse_from_string().

Oczywi¶cie mo¿na ³±czyæ interfejs przeci±¿anai z parserem przy
generowaniu drzew w kodzie perlowym - na przyk³ad
"$term * 5 * 'sin(omega*t+fi)'" stworzy drzewo z istniej±cego
drzewa $term pomno¿onego przez 5 razy sinus omega razy t plus fi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Math/Symbolic.pm
%{perl_vendorlib}/Math/Symbolic
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
