Name:		texlive-g-brief
Version:	50415
Release:	2
Summary:	Letter document class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/g-brief
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/g-brief
%doc %{_texmfdistdir}/doc/latex/g-brief
#- source
%doc %{_texmfdistdir}/source/latex/g-brief

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
