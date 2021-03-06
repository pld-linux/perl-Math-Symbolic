#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Symbolic
Summary:	Math::Symbolic - symbolic calculations
Summary(pl.UTF-8):	Math::Symbolic - obliczenia symboliczne
Name:		perl-Math-Symbolic
Version:	0.606
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6272de6bfc780ec1476e08d209816dcf
URL:		http://search.cpan.org/dist/Math-Symbolic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Memoize) >= 1.01
BuildRequires:	perl(Test::More)
BuildRequires:	perl-Parse-RecDescent >= 1.94
BuildRequires:	perl-Pod-Coverage >= 0.11
%endif
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

%description -l pl.UTF-8
Pakiet Math::Symbolic oferuje programistom perlowym możliwość obliczeń
symbolicznych bez używania zewnętrznych (i komercyjnych) bibliotek
i/lub aplikacji.

Drzewa Math::Symbolic można tworzyć na kilka sposobów. Nie ma
właściwych obiektów Math::Symbolic, zamiast nich używa się podklas
Math::Symbolic. Najbardziej ogólnym, ale niestety najmniej intuicyjnym
sposobem tworzenia drzew jest użycie konstruktorów klas
Math::Symbolic::Operator, Math::Symbolic::Variable i
Math::Symbolic::Constant do tworzenia (zagnieżdżonych) obiektów
odpowiednich typów.

Poza tym można używać interfejsu przeciążania, aby używać
standardowych operatorów (i funkcji) Perla na istniejących drzewach
Math::Symbolic i standardowych wyrażeniach perlowych.

Prawdopodobnie najwygodniejszym sposobem tworzenia drzew
Math::Symbolic jest używanie wbudowanego parsera do generowania drzew
z wyrażeń takich jak '2 * x^5'. Można do tego użyć metody klasy
Math::Symbolic->parse_from_string().

Oczywiście można łączyć interfejs przeciążania z parserem przy
generowaniu drzew w kodzie perlowym - na przykład "$term * 5 *
'sin(omega*t+fi)'" stworzy drzewo z istniejącego drzewa $term
pomnożonego przez 5 razy sinus omega razy t plus fi.

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

cp -p examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Math/Symbolic.pm
%{perl_vendorlib}/Math/Symbolic
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
