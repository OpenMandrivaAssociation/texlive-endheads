# revision 24992
# category Package
# catalog-ctan /macros/latex/contrib/endheads
# catalog-date 2011-12-31 23:12:05 +0100
# catalog-license lppl
# catalog-version v1.5
Name:		texlive-endheads
Epoch:		1
Version:	v1.5
Release:	1
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
%doc %{_texmfdistdir}/doc/latex/endheads/README
%doc %{_texmfdistdir}/doc/latex/endheads/endheads.pdf
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


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:v1.5-1
+ Revision: 758879
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.53-2
+ Revision: 751418
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.53-1
+ Revision: 718332
- texlive-endheads
- texlive-endheads
- texlive-endheads
- texlive-endheads

