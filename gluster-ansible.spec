%global docdir %{_datadir}/doc/gluster.ansible

Name:      gluster-ansible
Version:   0.5
Release:   1
Summary:   Ansible roles for GlusterFS deployment and management

URL:       https://github.com/gluster/gluster-ansible
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible >= 2.6
Requires:  gluster-ansible-infra >= 0.3
Requires:  gluster-ansible-features >= 0.3
Requires:  gluster-ansible-cluster >= 0.1
Requires:  gluster-ansible-repositories >= 0.2
Requires:  gluster-ansible-maintenance >= 0.1

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{docdir}
install -p -m 644 README.md %{buildroot}/%{docdir}

%files
%doc %{docdir}

%license LICENSE

%changelog
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

