%define debug_package %{nil}
Name:           perun
Version:        1.1.1
Release:        1
Summary:        A swiss army knife for AWS CloudFormation templates - validation, conversion, generators and other various stuff.

License:        Apache Liceunse 2.0
URL:            http://perun-for-aws.appliscale.io/
Source0:        perun-1.1.1.tar.gz

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
install -m 0755 -d $RPM_BUILD_ROOT/etc/perun
install -m 0755 perun-1.1.1 $RPM_BUILD_ROOT/etc/perun/perun-1.1.1

%files
/etc/perun/perun-1.1.1


%changelog
* Thu Jun  7 2018 Sylwia Gargula sylwia.gargula@npspace.pl 1.1.1-1
-Initial package
