Name:		texlive-endheads
Epoch:		1
Version:	1.6
Release:	2
Summary:	Running headers of the form "Notes to pp.xx-yy"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endheads
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endheads.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endheads.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endheads.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Endheads provides running headers of the form "Notes to pp. xx-
yy" for endnotes sections. It also enables one to reset the
endnotes counter, and put a line marking the chapter change in
the endnotes, at the beginning of every chapter. Endheads
requires the fancyhdr, needspace, ifthen, and endnotes
packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/endheads/endheads.sty
%doc %{_texmfdistdir}/doc/latex/endheads/endheads.pdf
%doc %{_texmfdistdir}/doc/latex/endheads/README.md
#- source
%doc %{_texmfdistdir}/source/latex/endheads/endheads.dtx
%doc %{_texmfdistdir}/source/latex/endheads/endheads.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
