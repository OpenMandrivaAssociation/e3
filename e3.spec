%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Tiny editor, well suited for rescue disks
Name:		e3
Version:	2.8
Release:	1
License:	GPLv2+
Group:		Editors
Url:		https://sites.google.com/site/e3editor/
Source0:	https://sites.google.com/site/e3editor/Home/%{name}-%{version}.tgz
# mark the stack as non-executable and disable tiny/crippled elf on 32
# bit linux so that stack can be marked as non-executable on it too
# http://www.gentoo.org/proj/en/hardened/gnu-stack.xml
Patch0:		e3-gnu-stack.patch
BuildRequires:	nasm
ExclusiveArch:	%{ix86} x86_64

%description
E3 is teeny tiny editor that doesn't depend on any libs.
e3 uses subset of wordstar|emacs|pico|vi|nedit commands.

%files
%doc README ChangeLog e3.html
%{_bindir}/e3
%{_bindir}/e3em
%{_bindir}/e3ne
%{_bindir}/e3pi
%{_bindir}/e3vi
%{_bindir}/e3ws
%{_mandir}/man1/e3*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
rm -rf bin

%build
%ifarch x86_64
make PREFIX=%{_prefix} MANDIR=%{_mandir}/man1 EXMODE=SED 64
%else
make PREFIX=%{_prefix} MANDIR=%{_mandir}/man1 EXMODE=SED 32
%endif

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 e3 %{buildroot}%{_bindir}/e3
install -m644 e3.man %{buildroot}%{_mandir}/man1/e3.1

# fix those softlinks
pushd %{buildroot}%{_bindir}
    for i in e3em e3ne e3pi e3vi e3ws; do
	ln -snf e3 ${i}
    done
popd

