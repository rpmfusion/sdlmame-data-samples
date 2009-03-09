Name:           sdlmame-data-samples
Version:        0129
Release:        1%{?dist}
Summary:        Sound samples for the SDLMAME package

Group:          Amusements/Games
License:        Distributable
URL:            http://samples.mameworld.info
Source0:        sdlmame-samples.tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       sdlmame >= 0129

%description
%{summary}.

%prep
%setup -qcT


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mame/samples
tar --extract --directory $RPM_BUILD_ROOT%{_datadir}/mame/samples \
    --file %{SOURCE0}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/mame


%changelog
* Mon Mar 09 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0129-1
- Added cosmica
- Updated the URL

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0126-2
- rebuild for buildsys cflags issue

* Fri Jul 11 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0126-1
- Removed dkongjr and mario
- Updated gorf

* Sun Oct 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0120-1
- First attempt at breaking down the package into smaller pieces
