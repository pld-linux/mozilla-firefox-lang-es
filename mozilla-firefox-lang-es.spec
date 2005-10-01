Summary:	Spanish resources for Mozilla-firefox
Summary(ca):	Recursos espanyols per Mozilla-firefox
Summary(es):	Recursos españoles para Mozilla-firefox
Summary(pl):	Hiszpañskie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-es
Version:	1.0.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source0-md5:	b3cd62069c703f388fd63bc633c0bc5a
Source1:	%{name}-installed-chrome.txt
URL:		http://www.mozilla.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox >= %{version}
Requires(post,postun):	textutils
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_libdir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Spanish resources for Mozilla-firefox.

%description -l ca
Recursos espanyols per Mozilla-firefox.

%description -l es
Recursos españoles para Mozilla-firefox.

%description -l pl
Hiszpañskie pliki jêzykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_firefoxdir}/chrome/*-installed-chrome.txt >%{_firefoxdir}/chrome/installed-chrome.txt

%postun
umask 022
cat %{_firefoxdir}/chrome/*-installed-chrome.txt >%{_firefoxdir}/chrome/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/es-ES.jar
%{_chromedir}/%{name}-installed-chrome.txt
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
