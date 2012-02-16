# Generated from cgi_multipart_eof_fix-2.5.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	cgi_multipart_eof_fix

Summary:	Fix an exploitable bug in CGI multipart parsing
Name:		rubygem-%{rbname}

Version:	2.5.0
Release:	2
Group:		Development/Ruby
License:	AFL
URL:		http://blog.evanweaver.com/pages/code#cgi_multipart_eof_fix
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

