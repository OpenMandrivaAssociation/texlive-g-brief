# revision 21140
# category Package
# catalog-ctan /macros/latex/contrib/g-brief
# catalog-date 2009-01-23 15:11:09 +0100
# catalog-license lppl
# catalog-version 4.0.2
Name:		texlive-g-brief
Version:	4.0.2
Release:	1
Summary:	Letter document class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/g-brief
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Designed for formatting formless letters in German; can also be
used for English (by those who can read the documentation).
There are LaTeX 2.09 documentstyle and LaTeX 2e class files for
both an 'old' and a 'new' version of g-brief.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
