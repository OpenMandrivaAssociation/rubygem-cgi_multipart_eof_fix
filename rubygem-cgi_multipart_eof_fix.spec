# Generated from cgi_multipart_eof_fix-2.5.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	cgi_multipart_eof_fix

Summary:	Fix an exploitable bug in CGI multipart parsing
Name:		rubygem-%{rbname}

Version:	2.5.0
Release:	3
Group:		Development/Ruby
License:	AFL
URL:		https://blog.evanweaver.com/pages/code#cgi_multipart_eof_fix
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Patch0:		cgi_multipart_eof_fix-2.5.0-add-licenses-tag-to-metadata.patch
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Fix an exploitable bug in CGI multipart parsing.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q
gunzip metadata.gz
%patch0 -p1 -b .licenses~
gzip metadata

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}



%changelog
* Thu Feb 16 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.5.0-2
+ Revision: 774704
- initial release..
- imported package rubygem-cgi_multipart_eof_fix

* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 2.5.0-1mdv2011.0
+ Revision: 623458
- import rubygem-cgi_multipart_eof_fix


