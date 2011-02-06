%define 	srcname	perl-modes
Summary:	XEmacs modes for Perl
Summary(pl.UTF-8):	XEmacsowe tryby do jezyka Perl
Name:		xemacs-%{srcname}-pkg
Version:	1.06
Release:	0.1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	75651f6590cef4d11217f5ea0edf41a4
URL:		http://www.xemacs.org/
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs modes for Perl.

%description -l pl.UTF-8
XEmacsowe tryby do Perla.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/perl-modes/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
