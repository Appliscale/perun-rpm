%define debug_package %{nil}
Name:           perun-linux-amd64
Version:        1.2.0
Release:        1
Summary:        A Swiss army knife for AWS CloudFormation templates

License:        ASL 2.0
URL:            http://perun-for-aws.appliscale.io/
Source0:        https://github.com/Appliscale/perun/releases/download/%{version}/%{name}.tar.gz

%description
Perun was created to support work with CloudFormation templates.
CloudFormation works in a way that it runs template online in AWS
infrastructure and fails after first error - in many cases it is
related with particular name length (e.g. maximum length is 64
characters). Instead of doing a round-trip, we would like
to detect such cases locally.

%prep
%setup -q -c
%build
%install LDFLAGS+=--build-id
install -m 0755 -d $RPM_BUILD_ROOT/%{name}
install -m 0755 %{name} $RPM_BUILD_ROOT/%{name}/%{name}
install -m 0644 main.yaml $RPM_BUILD_ROOT/%{name}/main.yaml
install -m 0644 LICENSE $RPM_BUILD_ROOT/%{name}/LICENSE

%post
mkdir -m 777 %{getenv:HOME}/.config/perun
cp $RPM_BUILD_ROOT/%{name}/main.yaml %{getenv:HOME}/.config/perun/

%files  
%license //%{name}/LICENSE
//%{name}/%{name}
//%{name}/main.yaml
%doc

%changelog
* Thu Jun  7 2018 Sylwia Gargula sylwia.gargula@npspace.pl 1.2.0-1
-Initial package
