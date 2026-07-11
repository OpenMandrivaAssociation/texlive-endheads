%global tl_name endheads
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Running headers of the form Notes to pp.xx-yy
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/endheads
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endheads.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endheads.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endheads.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides running headers of the form "Notes to pp. xx-yy"
for endnotes sections. It also enables one to reset the endnotes
counter, and put a line marking the chapter change in the endnotes, at
the beginning of every chapter. Endheads requires the fancyhdr,
needspace, ifthen, and endnotes packages.

