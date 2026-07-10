%global tl_name g-brief
%global tl_revision 77050

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0.3
Release:	%{tl_revision}.1
Summary:	Letter document class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/g-brief
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/g-brief.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Designed for formatting formless letters in German; can also be used for
English (by those who can read the documentation). There are LaTeX 2.09
documentstyle and LaTeX2e class files for both an 'old' and a 'new'
version of g-brief.

