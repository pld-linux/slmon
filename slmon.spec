Summary:	A simple S-Lang based system performance monitor
Summary(pl):	Prosty monitor obci±¿enia systemu oparty na bibliotece S-Lang
Name:		slmon
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://slmon.sourceforge.net/download/%{name}-%{version}.tar.gz
URL:		http://slmon.sourceforge.net
BuildRequires:	slang-devel >= 1.2.2
BuildRequires:	popt-devel >= 1.1.3
BuildRequires:	autoconf
BuildRequires:	automake
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
oraz liczbê zalogowanych uzytkowników.

%prep
%setup  -q

%build
autoconf
automake -a -c
%configure \
	--enable-strip \
	--with-libgtop=no
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/slmonrc doc/slmon.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
