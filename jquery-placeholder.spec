# TODO
# - paths and deps for demo
%define		plugin	placeholder
Summary:	jQuery HTML5 Placeholder Plugin
Name:		jquery-%{plugin}
Version:	0.1
Release:	1
License:	MIT, BSD, and GPL
Group:		Applications/WWW
Source0:	https://github.com/danielstocks/jQuery-Placeholder/tarball/master/%{name}-%{version}.tgz
# Source0-md5:	7b345a530a0424d29a364215c3578d18
URL:		http://webcloud.se/code/jQuery-Placeholder/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jquery >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
The HTML5 placeholder attribute is awesome, unfortunately only
supported by some browsers. This plugin replicates the placeholder
behavior for unsupported browsers.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv *-jQuery-Placeholder-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.%{plugin}.min.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p demo.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
