Name:           sdlmame-data-samples
Version:        0137
Release:        1%{?dist}
Summary:        Sound samples for the SDLMAME package

Group:          Amusements/Games
License:        Distributable
URL:            http://samples.mameworld.info
Source01:       armora.zip
Source02:       astrob.zip
Source03:       astrof.zip
Source04:       barrier.zip
Source05:       battles.zip
Source06:       blockade.zip
Source07:       buckrog.zip
Source08:       carnival.zip
Source09:       circus.zip
Source10:       congo.zip
Source11:       cosmica.zip
Source12:       cosmicg.zip
Source13:       depthch.zip
Source14:       elim2.zip
Source15:       fantasy.zip
Source16:       frogs.zip
Source17:       gaplus.zip
Source18:       gorf.zip
Source19:       gridlee.zip
Source20:       invaders.zip
Source21:       invinco.zip
Source22:       journey.zip
Source23:       lrescue.zip
Source24:       monsterb.zip
Source25:       natodef.zip
Source26:       panic.zip
Source27:       pulsar.zip
Source28:       qbert.zip
Source29:       rallyx.zip
Source30:       reactor.zip
Source31:       ripoff.zip
Source32:       safarir.zip
Source33:       sasuke.zip
Source34:       seawolf.zip
Source35:       sharkatt.zip
Source36:       solarq.zip
Source37:       spacefb.zip
Source38:       spaceod.zip
Source39:       spacewar.zip
Source40:       spacfury.zip
Source41:       starcas.zip
Source42:       starcrus.zip
Source43:       starhawk.zip
Source44:       subroc3d.zip
Source45:       sundance.zip
Source46:       tailg.zip
Source47:       tankbatt.zip
Source48:       targ.zip
Source49:       thehand.zip
Source50:       thief.zip
Source51:       triplhnt.zip
Source52:       turbo.zip
Source53:       vanguard.zip
Source54:       warrior.zip
Source55:       wow.zip
Source56:       zaxxon.zip
Source57:       zektor.zip
Source58:       speedfrk.zip
Source59:       wotw.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       sdlmame >= 0133

%description
%{summary}.

%prep
%setup -qcT


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mame/samples
install -pm 644 %{sources} $RPM_BUILD_ROOT%{_datadir}/mame/samples


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/mame


%changelog
* Thu Mar 25 2010 Julian Sikorski <belegdol[at]gmail[dot]com> - 0137-1
- Added speedfrk and wotw

* Tue Sep 22 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0134-1
- Updated safarir

* Wed Jul 22 2009 Julian Sikorski <belegdol[at]gmail[dot]com> - 0133-1
- Added barrier, safarir and starhawk
- Split the source into individual files in order to make updating easier

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0129-2
- rebuild for new F11 features

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
