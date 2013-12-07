# revision 23252
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/mpcolornames
# catalog-date 2011-07-18 09:05:38 +0200
# catalog-license lppl
# catalog-version 0.20
Name:		texlive-mpcolornames
Version:	0.20
Release:	5
Summary:	XXXX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/mpcolornames
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpcolornames.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpcolornames.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mpcolornames.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The MetaPost format plain.mp provides only five built-in colour
names (variables), all of which are defined in the RGB model:
red, green and blue for the primary colours and black and
white. The package makes more than 500 colour names from
different colour sets in different colour models available to
MetaPost. Colour sets include X11, SVG, DVIPS and xcolor
specifications.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/mpcolornames/mpcolornames-spec-dvipsnam-def.mp
%{_texmfdistdir}/metapost/mpcolornames/mpcolornames-spec-plain-mp.mp
%{_texmfdistdir}/metapost/mpcolornames/mpcolornames-spec-svgnam-def.mp
%{_texmfdistdir}/metapost/mpcolornames/mpcolornames-spec-x11nam-def.mp
%{_texmfdistdir}/metapost/mpcolornames/mpcolornames-spec-xcolor-sty.mp
%{_texmfdistdir}/metapost/mpcolornames/mpcolornames.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/CHANGES
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/LICENSE
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/README
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/expl-array-index.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/fig-clash-svg-dvips.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/mpcolornames.pdf
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/mpcolornames.tex
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/proof-mpcolornames.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/proof-spec-dvipsnam-def.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/proof-spec-plain-mp.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/proof-spec-svgnam-def.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/proof-spec-x11nam-def.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/proof-spec-xcolor-sty.mp
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/tab-clash-svg-dvips.tex
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/tab-spec-dvipsnam-def.tex
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/tab-spec-plain-mp.tex
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/tab-spec-svgnam-def.tex
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/tab-spec-x11nam-def.tex
%doc %{_texmfdistdir}/doc/metapost/mpcolornames/tab-spec-xcolor-sty.tex
#- source
%doc %{_texmfdistdir}/source/metapost/mpcolornames/Makefile
%doc %{_texmfdistdir}/source/metapost/mpcolornames/spec-dvipsnam-def.awk
%doc %{_texmfdistdir}/source/metapost/mpcolornames/spec-plain-mp.awk
%doc %{_texmfdistdir}/source/metapost/mpcolornames/spec-svgnam-def.awk
%doc %{_texmfdistdir}/source/metapost/mpcolornames/spec-x11nam-def.awk
%doc %{_texmfdistdir}/source/metapost/mpcolornames/spec-xcolor-sty.awk
%doc %{_texmfdistdir}/source/metapost/mpcolornames/tab-clash-svg-dvips.awk

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.20-2
+ Revision: 754115
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.20-1
+ Revision: 719069
- texlive-mpcolornames
- texlive-mpcolornames
- texlive-mpcolornames
- texlive-mpcolornames

