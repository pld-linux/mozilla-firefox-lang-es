%define		_lang		es
Summary:	Spanish resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols per Firefox
Summary(es.UTF-8):	Recursos españoles para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa
Name:		mozilla-firefox-lang-%{_lang}
Version:	3.0.5
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source0-md5:	49c588c089e4d28d0dfc92a0e19182e0
URL:		http://www.mozilla.org/
BuildRequires:	unzip
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_datadir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Spanish resources for Firefox.

%description -l ca.UTF-8
Recursos espanyols per Firefox.

%description -l es.UTF-8
Recursos españoles para Firefox.

%description -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa.

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
