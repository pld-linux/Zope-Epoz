%include        /usr/lib/rpm/macros.python
%define 	zope_subname	Epoz
Summary:	Epoz allows you to edit Zope or Plone-objects with a wysiwyg-editor.
Summary(pl):	Dodatek do Zope lub Plone umo¿liwiaj±cy manipulacje na obiektach w trybie WYSIWYG.
Name:		Zope-%{zope_subname}
Version:	0.6.1
Release:	1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://zope.org/Members/mjablonski/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	2f9a6bbf37c414db92045fc41eeca4a1
URL:		http://zope.org/Members/mjablonski/Epoz/
%pyrequires_eq  python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epoz allows you to edit Zope or Plone-objects with a wysiwyg-editor.

%description -l pl
Dodatek do Zope lub Plone umo¿liwiaj±cy manipulacje na obiektach w
trybie WYSIWYG.

%prep
%setup -q -n %{zope_subname}

%build
mkdir docs
mv -f {CHANGES.txt,README.txt,TODO.txt} docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -af * $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

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
%doc docs/*
%{_datadir}/%{name}
