%define name	e3
%define version	2.7.1
%define release %mkrel 10

Summary:	Tiny editor, well suited for rescue disks
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Editors 
URL:	    	http://mitglied.lycos.de/albkleine/
Source0:	http://mitglied.lycos.de/albkleine/%{name}-%{version}.tar.gz
Provides:	editor
BuildRequires:	nasm
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
#ExclusiveArch:  %ix86
%description
E3 is teeny tiny editor that doesn't depend on any libs.
e3 uses subset of wordstar|emacs|pico|vi|nedit commands.

%prep

%setup -q -n %{name}-%{version}

%build

%ifarch x86_64
%make nasm64
%else
%make nasm32
%endif

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.7.1-10mdv2011.0
+ Revision: 617948
- the mass rebuild of 2010.0 packages

* Wed May 27 2009 Jérôme Brenier <incubusss@mandriva.org> 2.7.1-9mdv2010.0
+ Revision: 380087
- fix build with x86_64 arch

* Sun May 17 2009 Jérôme Brenier <incubusss@mandriva.org> 2.7.1-8mdv2010.0
+ Revision: 376686
- fix license (GPLv2+)

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.1-7mdv2009.1
+ Revision: 354751
- rebuild

* Mon Mar 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.7.1-6mdv2009.1
+ Revision: 347456
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.7.1-5mdv2009.0
+ Revision: 244602
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.7.1-3mdv2008.1
+ Revision: 170805
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sun Feb 17 2008 Michael Scherer <misc@mandriva.org> 2.7.1-2mdv2008.1
+ Revision: 169840
- bump release for submitting
- restrict to x86, soft in assembly, and it doesn't compil on x86_64
- update to latest version
- change url, new page
- remove the email of developer, as it likely changed at the same time than the homepage

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode bz2 extension


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 2.7.0-1mdv2007.0
+ Revision: 101721
- Import e3

* Fri Apr 07 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.7.0-1mdk
- New release 2.7.0
- use mkrel

* Tue Feb 22 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.6.2-1mdk
- 2.6.2
- make it compile...
- run the tests

* Fri Jan 07 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.6.1-2mdk
- rpmlint fixes

* Fri Jan 07 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.6.1-1mdk
- 2.6.1

* Fri Aug 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.6.0-1mdk
- 2.6.0

