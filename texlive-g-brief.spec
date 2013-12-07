# revision 21140
# category Package
# catalog-ctan /macros/latex/contrib/g-brief
# catalog-date 2009-01-23 15:11:09 +0100
# catalog-license lppl
# catalog-version 4.0.2
Name:		texlive-g-brief
Version:	4.0.2
Release:	6
Summary:	Letter document class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/g-brief
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Designed for formatting formless letters in German; can also be
used for English (by those who can read the documentation).
There are LaTeX 2.09 documentstyle and LaTeX 2e class files for
both an 'old' and a 'new' version of g-brief.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/g-brief/g-brief.cls
%{_texmfdistdir}/tex/latex/g-brief/g-brief.sty
%{_texmfdistdir}/tex/latex/g-brief/g-brief2.cls
%{_texmfdistdir}/tex/latex/g-brief/g-brief2.sty
%doc %{_texmfdistdir}/doc/latex/g-brief/beispiel.pdf
%doc %{_texmfdistdir}/doc/latex/g-brief/beispiel.tex
%doc %{_texmfdistdir}/doc/latex/g-brief/beispiel2.pdf
%doc %{_texmfdistdir}/doc/latex/g-brief/beispiel2.tex
%doc %{_texmfdistdir}/doc/latex/g-brief/g-brief.pdf
#- source
%doc %{_texmfdistdir}/source/latex/g-brief/g-brief.drv
%doc %{_texmfdistdir}/source/latex/g-brief/g-brief.dtx
%doc %{_texmfdistdir}/source/latex/g-brief/g-brief.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.0.2-2
+ Revision: 752189
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.0.2-1
+ Revision: 718525
- texlive-g-brief
- texlive-g-brief
- texlive-g-brief
- texlive-g-brief

