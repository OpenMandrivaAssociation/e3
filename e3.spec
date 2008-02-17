%define name	e3
%define version	2.7.1
%define release %mkrel 2

Summary:	E3 is a tiny editor, well suited for rescue disks
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Editors 
URL:	    http://mitglied.lycos.de/albkleine/
Source0:	http://mitglied.lycos.de/albkleine/%{name}-%{version}.tar.gz
Provides:	editor
BuildRequires:	nasm
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
ExclusiveArch:  %ix86
%description
E3 is teeny tiny editor that doesn't depend on any libs.
e3 uses subset of wordstar|emacs|pico|vi|nedit commands.

%prep

%setup -q -n %{name}-%{version}

%build

# this was the only way i was able to compile it...
%make debug

# run the tests
#make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README ChangeLog e3.html
%{_bindir}/e3
%{_bindir}/e3em
%{_bindir}/e3ne
%{_bindir}/e3pi
%{_bindir}/e3vi
%{_bindir}/e3ws 
%{_mandir}/man1/e3*


