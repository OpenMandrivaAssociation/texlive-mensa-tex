Name:		texlive-mensa-tex
Version:	45997
Release:	2
Summary:	Typeset simple school cafeteria menus
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mensa-tex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mensa-tex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mensa-tex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a flexible LaTeX2e class for typesetting
school cafeteria menus consisting of two lunches (with
dessert), and dinner. It supports two different layouts: The
first layout is optimized for printing the menu on A4 paper.
The second layout is optimized for smartphone screens and uses
one (A6 sized) page per day. Supported localizations are
English (GB/US) and German. A way of defining additional
localizations is described in the documentation. The package
requires array, colortbl, datetime2, datetime2-calc, geometry,
graphicx, lmodern, textcomp, and xcolor.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mensa-tex
%doc %{_texmfdistdir}/doc/latex/mensa-tex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
