%global tl_name mensa-tex
%global tl_revision 45997

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset simple school cafeteria menus
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mensa-tex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mensa-tex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mensa-tex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a flexible LaTeX2e class for typesetting school
cafeteria menus consisting of two lunches (with dessert), and dinner. It
supports two different layouts: The first layout is optimized for
printing the menu on A4 paper. The second layout is optimized for
smartphone screens and uses one (A6 sized) page per day. Supported
localizations are English (GB/US) and German. A way of defining
additional localizations is described in the documentation. The package
requires array, colortbl, datetime2, datetime2-calc, geometry, graphicx,
lmodern, textcomp, and xcolor.

