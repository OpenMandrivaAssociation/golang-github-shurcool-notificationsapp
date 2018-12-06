# Run tests in check section
%bcond_with check

%global goipath         github.com/shurcooL/notificationsapp
%global commit          1e3e09827ba4327f324e3ea826f00db21ad93ecd

%global common_description %{expand:
Web frontend for a notifications service.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Web frontend for a notifications service
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/dustin/go-humanize)
BuildRequires: golang(github.com/shurcooL/go/ctxhttp)
BuildRequires: golang(github.com/shurcooL/go/gopherjs_http)
BuildRequires: golang(github.com/shurcooL/htmlg)
BuildRequires: golang(github.com/shurcooL/httperror)
BuildRequires: golang(github.com/shurcooL/httpfs/union)
BuildRequires: golang(github.com/shurcooL/httpfs/vfsutil)
BuildRequires: golang(github.com/shurcooL/httpgzip)
BuildRequires: golang(github.com/shurcooL/notifications)
BuildRequires: golang(github.com/shurcooL/octicon)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(golang.org/x/net/html)
BuildRequires: golang(golang.org/x/net/html/atom)

%if %{with check}
BuildRequires: golang(golang.org/x/oauth2)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181026git1e3e098
- Bump to commit 1e3e09827ba4327f324e3ea826f00db21ad93ecd

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitcd3feaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitcd3feaf
- First package for Fedora

