%global octpkg outliers

%global commit 551e891a09a9cdbba83d293841cf4cf89a0a05a1

Summary:	Grubbs, Dixon and Cochran tests for outlier detection and p-value approximating
Name:		octave-outliers
Version:	0.13.9
Release:	2
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/outliers/
Source0:	https://downloads.sourceforge.net/octave//outliers-%{version}.tar.gz

BuildRequires:  octave-devel >= 2.9.9

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Grubbs, Dixon and Cochran tests for outlier detection and p-value 
approximating routines.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

