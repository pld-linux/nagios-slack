Summary:	Nagios/Icinga Slack integration
Name:		nagios-slack
Version:	1.1
Release:	0.2
License:	Apache v2.0
Group:		Networking
Source0:	https://raw.github.com/tinyspeck/services-examples/master/nagios.pl
# Source0-md5:	cea400bfa840ceffea318e5fd8d7c6d5
Source1:	slack_nagios.cfg
URL:		https://slack.com/apps/A0F81R747-nagios
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios is an IT management system that organizations use to identify
and resolve IT infrastructure problems.

This integration will post Nagios alerts to a channel.

%prep
%setup -qcT
install -p %{SOURCE0} .
cp -p %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{_sysconfdir}}

install -p nagios.pl $RPM_BUILD_ROOT%{plugindir}/slack_nagios
cp -p slack_nagios.cfg $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/slack_nagios.cfg
%attr(755,root,root) %{plugindir}/slack_nagios
