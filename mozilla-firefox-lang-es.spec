Summary:	Spanish resources for Mozilla-firefox
Summary(ca):	Recursos espanyols per Mozilla-firefox
Summary(es):	Recursos españoles para Mozilla-firefox
Summary(pl):	Hiszpañskie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-es
Version:	1.5.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source0-md5:	e2cf3de192754243674fbb2a1600004b
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
sed -e 's@chrome/es-ES\.jar@es-ES.jar@' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest \
	> $RPM_BUILD_ROOT%{_chromedir}/es-ES.manifest
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/es-ES.jar
%{_chromedir}/es-ES.manifest
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
