Summary:	A command line utility to convert HTML document to plain text
Name:		html2text
Version:	2.3.0
Release:	1
Group:		File tools
License:	GPLv2
Url:		https://github.com/grobian/html2text
Source0:	https://github.com/grobian/html2text/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel

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

install -m755 %{name} %{buildroot}%{_bindir}
install -m644 %{name}.1  %{buildroot}%{_mandir}/man1/
install -m644 %{name}rc.5 %{buildroot}%{_mandir}/man5/

%files
%doc ChangeLog.md COPYING CREDITS INSTALL KNOWN_BUGS README.md
%{_bindir}/*
%{_mandir}/man?/*
