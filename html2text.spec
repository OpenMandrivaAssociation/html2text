Summary:	A command line utility to convert HTML document to plain text
Name:		html2text
Version:	1.3.2a
Release:	%mkrel 11
Group:		File tools
License:	GPL
URL:		http://userpage.fu-berlin.de/~mbayer/tools/html2text.html
Source0:        http://userpage.fu-berlin.de/%7Embayer/tools/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
html2text is a command line utility, written in C++, that converts HTML
documents into plain text.

%prep

%setup -q

%build
%configure2_5x
%make DEBUG="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/{man1,man5}}

gunzip %{name}.1.gz %{name}rc.5.gz

install -m755 %{name} %{buildroot}%{_bindir}
install -m644 %{name}.1  %{buildroot}%{_mandir}/man1/
install -m644 %{name}rc.5 %{buildroot}%{_mandir}/man5/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING CREDITS INSTALL KNOWN_BUGS RELEASE_NOTES README TODO
%{_bindir}/*
%{_mandir}/man?/*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.2a-10mdv2011.0
+ Revision: 665484
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2a-9mdv2011.0
+ Revision: 605883
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2a-8mdv2010.1
+ Revision: 520122
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.2a-7mdv2010.0
+ Revision: 425166
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.2a-6mdv2009.1
+ Revision: 316763
- use %%{optflags} and %%{ldflags}

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2a-5mdv2009.0
+ Revision: 221347
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.3.2a-4mdv2008.1
+ Revision: 126857
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.2a-4mdv2007.1
+ Revision: 145396
- Import html2text

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.2a-4mdv2007.1
- use the %%mrel macro
- bunzip patches

* Sat Aug 06 2005 Michael Scherer <misc@mandriva.org> 1.3.2a-3mdk
- Rebuild

* Mon Jun 07 2004 Michael Scherer <misc@mandrake.org> 1.3.2a-2mdk 
- rebuild for new gcc

* Thu May 06 2004 Michael Scherer <misc@mandrake.org> 1.3.2a-1mdk
- First version

