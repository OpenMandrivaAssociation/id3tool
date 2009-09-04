%define name 	id3tool
%define version 1.2a
%define release  %mkrel 4

Summary:	Id3tool: program for manipulating mp3 ID3 Tags
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


