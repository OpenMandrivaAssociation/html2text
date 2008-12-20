Summary:	A command line utility to convert HTML document to plain text
Name:		html2text
Version:	1.3.2a
Release:	%mkrel 6
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


