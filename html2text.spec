Summary:	A command line utility to convert HTML document to plain text
Name:		html2text
Version:	1.3.2a
Release:	26
Group:		File tools
License:	GPLv2
Url:    https://github.com/grobian/html2text
# Previous (old) url:
#Url:		http://www.mbayer.de/html2text/
Source0:        http://www.mbayer.de/html2text/downloads/%{name}-%{version}.tar.bz2

%description
html2text is a command line utility, written in C++, that converts HTML
documents into plain text.

%prep
%autosetup -p1

%build
%configure
%make_build DEBUG="%{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/{man1,man5}}

gunzip %{name}.1.gz %{name}rc.5.gz

install -m755 %{name} %{buildroot}%{_bindir}
install -m644 %{name}.1  %{buildroot}%{_mandir}/man1/
install -m644 %{name}rc.5 %{buildroot}%{_mandir}/man5/

%files
%doc CHANGES COPYING CREDITS INSTALL KNOWN_BUGS RELEASE_NOTES README TODO
%{_bindir}/*
%{_mandir}/man?/*
