%global docdir %{_datadir}/doc/gluster.ansible
%global buildnum 1

Name:      gluster-ansible-roles
Version:   1.0.0
Release:   1%{?dist}
Summary:   Ansible roles for GlusterFS deployment and management

URL:       https://github.com/gluster/gluster-ansible
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible >= 2.6
Requires:  gluster-ansible-infra >= 1.0
Requires:  gluster-ansible-features >= 1.0
Requires:  gluster-ansible-cluster >= 1.0
Requires:  gluster-ansible-repositories >= 1.0
Requires:  gluster-ansible-maintenance >= 1.0

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{docdir}
install -p -m 644 README.md %{buildroot}/%{docdir}
cp -a playbooks/ %{buildroot}/%{docdir}

%files
%doc %{docdir}

%license LICENSE

%changelog
* Thu Feb 21 2019 Sachidananda Urs <sac@redhat.com> 1.0.0-1
- Bump the version number, stable enought to call 1.0.0

* Thu Jan 03 2019 Sachidananda Urs <sac@redhat.com> 0.6
- Add documentation to /usr add new playbooks/ directory

* Tue Oct 23 2018 Sachidananda Urs <sac@redhat.com> 0.5
- Address the security concerns regarding plaintext passwords

* Fri Oct 12 2018 Sachidnanda Urs <sac@redhat.com> 0.4
- Enhancements to examples

* Mon Sep 24 2018 Sachidananda Urs <sac@redhat.com> 0.3
- Added playbooks to illustrate end-to-end deployment

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.2
- Added gluster-maintenance. Bug fixes across the roles

* Tue Apr 24 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release.

