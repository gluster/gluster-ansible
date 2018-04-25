%global docdir %{_datadir}/doc/gluster.ansible

Name:      gluster-ansible
Version:   0.1
Release:   1%{?dist}
Summary:   Ansible roles for GlusterFS deployment and management

URL:       https://github.com/gluster/gluster-ansible
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible >= 2.5
Requires:  gluster-ansible-infra >= 0.1
Requires:  gluster-ansible-features >= 0.1
# Requires:  gluster-ansible-cluster >= 0.1

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/%{docdir}
install -p -m 644 README.md %{buildroot}/%{docdir}

%files
%doc %{docdir}/README.md

%license LICENSE

%changelog
* Tue Apr 24 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release.

