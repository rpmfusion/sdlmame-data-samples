Name:           sdlmame-data-samples
Version:        0126
Release:        1%{?dist}
Summary:        Sound samples for the SDLMAME package

Group:          Amusements/Games
License:        Distributable
URL:            http://www.mameworld.net/samples
Source0:        sdlmame-samples.tar
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       sdlmame >= 0126

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
* Fri Jul 11 2008 Julian Sikorski <belegdol[at]gmail[dot]com> - 0126-1
- Removed dkongjr and mario
- Updated gorf

* Sun Oct 28 2007 Julian Sikorski <belegdol[at]gmail[dot]com> - 0120-1
- First attempt at breaking down the package into smaller pieces
