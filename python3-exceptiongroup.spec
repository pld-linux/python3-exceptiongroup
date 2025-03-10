#
# Conditional build:
%bcond_with	tests	# unit tests (missing in sdist)

Summary:	Backport of PEP 654 (exception groups)
Summary(pl.UTF-8):	Backport PEP 654 (grup wyjątków)
Name:		python3-exceptiongroup
Version:	1.1.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/exceptiongroup/
Source0:	https://files.pythonhosted.org/packages/source/e/exceptiongroup/exceptiongroup-%{version}.tar.gz
# Source0-md5:	2a5d49d1c727e2895b8f58893446d8fa
URL:		https://pypi.org/project/exceptiongroup/
# TODO
#BuildRequires:	python3-flit_scm
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a backport of the BaseExceptionGroup and ExceptionGroup
classes from Python 3.11.

%description -l pl.UTF-8
Ten pakiet to backport klas BaseExceptionGroup i ExceptionGroup z
Pythona 3.11.

%prep
%setup -q -n exceptiongroup-%{version}

cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/exceptiongroup
%{py3_sitescriptdir}/exceptiongroup-%{version}-py*.egg-info
