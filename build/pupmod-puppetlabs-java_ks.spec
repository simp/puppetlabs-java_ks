%global short_name java_ks

Summary: Java Keystore Puppet Module
Name: pupmod-puppetlabs-java_ks
Version: 1.4.0
Release: 0
License: ASL 2.0
URL: https://github.com/puppetlabs/puppetlabs-java_ks
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch

Prefix: /etc/puppet/environments/simp/modules/%{short_name}

%description
A module to install Puppetlab's Java Keystore library

%prep
%setup -q

%build

%install

[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}

dirs='lib'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}
done

cp README.md %{buildroot}/%{prefix}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}

%files
%defattr(0640,root,puppet,0750)
%{prefix}

%changelog
* Tue Jan 19 2016 Nick Markowski <nmarkowski@keywcorp.com> - 1.4.0-0
- Updated module to the latest version.

* Mon Feb 09 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 1.2.0-1
- Update to relocate to the new default simp environment.

* Wed Oct 23 2013 Nick Markowski <nmarkowski@keywcorp.com> - 1.2.0-0
- Initial build.
