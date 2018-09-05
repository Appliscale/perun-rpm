%define debug_package %{nil}
Name:           perun-linux-amd64
Version:        latest
Release:        1
Summary:        A Swiss army knife for AWS CloudFormation templates

License:        ASL 2.0
URL:            http://perun-for-aws.appliscale.io/
Source0:        %{version}/%{name}.tar.gz

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
install -m 0644 LICENSE $RPM_BUILD_ROOT/%{name}/LICENSE

%files  
%license //%{name}/LICENSE
//%{name}/%{name}
%doc

%changelog
* Thu Jun  7 2018 Sylwia Gargula sylwia.gargula@npspace.pl latest
-Initial package
