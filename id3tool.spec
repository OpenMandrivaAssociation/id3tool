%define name 	id3tool
%define version 1.2a
%define release  %mkrel 5

Summary:	: program for manipulating mp3 ID3 Tags
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	BSD
Group:		Sound
Url:		http://kitsumi.xware.cx/id3tool/
Source0:	http://kitsumi.xware.cx/id3tool/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
id3tool: a program for manipulating mp3 ID3 Tags 

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make 

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGELOG COPYING INSTALL README* 
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2a-5mdv2011.0
+ Revision: 619599
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2a-4mdv2010.0
+ Revision: 429494
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2a-3mdv2009.0
+ Revision: 247198
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.2a-1mdv2008.1
+ Revision: 126981
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import id3tool


* Mon Jul 11 2005 Götz Waschk <waschk@mandriva.org> 1.2a-1mdk
- New release 1.2a

* Wed Apr 20 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.2-5mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2-4mdk
- rebuild

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2-3mdk
- rebuild

* Tue Nov  5 2002 Götz Waschk <waschk@linux-mandrake.com> 1.2-2mdk
- drop obsolete patch
- license is BSD

* Tue Nov 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- 1.2

* Thu Oct 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1f-3mdk
- merge patch to enable track support from Dave MacKenzie <djm@pix.net>

* Wed Aug 01 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1f-2mdk
- rebuild

* Mon Feb 19 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1f-1mdk
- used srpm from Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- new package





