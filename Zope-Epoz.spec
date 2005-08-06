%define 	zope_subname	Epoz
Summary:	epoz allows you to edit Zope or Plone-objects with a WYSIWYG-editor (primary ver.)
Summary(pl):	Dodatek do Zope lub Plone umo¿liwiaj±cy manipulacje na obiektach w trybie WYSIWYG
Name:		Zope-%{zope_subname}
Version:	2.0.1
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://mjablonski.zope.de/Epoz/releases/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	2c796e323db156ae03876919c4db1e0a
URL:		http://mjablonski.zope.de/Epoz/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
Obsoletes:	Zope-epoz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
epoz allows you to edit Zope or Plone-objects with a WYSIWYG-editor.
(primary version)

%description -l pl
Dodatek do Zope lub Plone umo¿liwiaj±cy manipulacje na obiektach w
trybie WYSIWYG - (wersja pierwotna).

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af %{zope_subname}/{Extensions,epoz,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/{CHANGES.txt,HISTORY.txt,README.txt,TODO.txt,FAQ.txt,mx*.txt}
%{_datadir}/%{name}
