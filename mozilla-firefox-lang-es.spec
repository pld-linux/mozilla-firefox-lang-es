Summary:	Spanish resources for Mozilla-firefox
Summary(ca.UTF-8):	Recursos espanyols per Mozilla-firefox
Summary(es.UTF-8):	Recursos españoles para Mozilla-firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-es
Version:	2.0.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source0-md5:	ab6db020c1e97f593b81caf5ff3f3284
URL:		http://www.mozilla.org/
BuildRequires:	unzip
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_datadir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Spanish resources for Mozilla-firefox.

%description -l ca.UTF-8
Recursos espanyols per Mozilla-firefox.

%description -l es.UTF-8
Recursos españoles para Mozilla-firefox.

%description -l pl.UTF-8
Hiszpańskie pliki językowe dla Mozilli-firefox.

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
