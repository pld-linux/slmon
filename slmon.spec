Summary:	A simple S-Lang based system performance monitor
Summary(pl):	Prosty monitor obci±¿enia systemu oparty na bibliotece S-Lang
Name:		slmon
Version:	0.5.13
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/slmon/%{name}-%{version}.tar.gz
# Source0-md5:	9907c53e26b8dfb5d33af6da32ed89e3
URL:		http://slmon.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	libgtop-devel
BuildRequires:	popt-devel >= 1.1.3
BuildRequires:	slang-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLmon is a tool for monitoring system's performance. It displays
results using nice and (hopefully) readable text-based UI. Currently
monitored are: CPU load (SMP is supported), memory (including swap),
uptime, date and time, number of logged in users.

%description -l pl
SLmon jest aplikacj± monitoruj±c± obci±¿enie systemu. Do wy¶wietlania
wyników u¿ywa ³adnego i (tak± mamy nadziejê) czytelnego tekstowego
interfejsu u¿ytkownika. Obecnie slmon pokazuje: obci±¿enie procesora
(lub procesorów), zajêto¶æ pamiêci (tak¿e swapa), uptime, datê i czas
oraz liczbê zalogowanych u¿ytkowników.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--enable-strip \
	--with-libgtop=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS TODO slmonrc slmon.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
