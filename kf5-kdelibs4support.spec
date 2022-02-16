%define		kdeframever	5.91
%define		qtver		5.9.0
%define		kfname		kdelibs4support
#
Summary:	KDELibs 4 Support
Name:		kf5-%{kfname}
Version:	5.91.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	c366867d52842fa7b720dafb5fb76b40
URL:		http://www.kde.org/
BuildRequires:	NetworkManager-devel >= 0.7.0
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel >= 5.2.0
BuildRequires:	Qt5Xml-devel >= 5.3.1
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kcrash-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kded-devel >= %{version}
BuildRequires:	kf5-kdesignerplugin-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kemoticons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kinit-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemmodels-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kparts-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kunitconversion-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This framework provides code and utilities to ease the transition from
kdelibs 4 to KDE Frameworks 5. This includes CMake macros and C++
classes whose functionality has been replaced by code in CMake, Qt and
other frameworks.

Code should aim to port away from this framework eventually. The API
documentation of the classes in this framework and the notes at
<http://community.kde.org/Frameworks/Porting_Notes> should help with
this.

Note that some of the classes in this framework, especially
KStandardDirs, may not work correctly unless any libraries and other
software using the KDELibs 4 Support framework are installed to the
same location as KDELibs4Support, although it may be sufficient to set
the KDEDIRS environment variable correctly.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf5-kcrash-devel >= %{version}
Requires:	kf5-kdesignerplugin-devel >= %{version}
Requires:	kf5-kemoticons-devel >= %{version}
Requires:	kf5-kguiaddons-devel >= %{version}
Requires:	kf5-kiconthemes-devel >= %{version}
Requires:	kf5-kinit-devel >= %{version}
Requires:	kf5-kitemmodels-devel >= %{version}
Requires:	kf5-kparts-devel >= %{version}
Requires:	kf5-kunitconversion-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

ln -sf /etc/certs/ca-certificates.crt $RPM_BUILD_ROOT%{_datadir}/kf5/kssl/ca-bundle.crt
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr@latin

%find_lang kdelibs4support --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdelibs4support.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/colors/40.colors
/etc/xdg/colors/Oxygen.colors
/etc/xdg/colors/Rainbow.colors
/etc/xdg/colors/Royal.colors
/etc/xdg/colors/Web.colors
/etc/xdg/kdebug.areas
/etc/xdg/kdebugrc
/etc/xdg/ksslcalist
%attr(755,root,root) %{_bindir}/kdebugdialog5
%attr(755,root,root) %{_bindir}/kf5-config
%attr(755,root,root) %{_libexecdir}/kf5/fileshareset
%ghost %{_libdir}/libKF5KDELibs4Support.so.5
%attr(755,root,root) %{_libdir}/libKF5KDELibs4Support.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kf5deprecatedwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ssl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/networkstatus.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/metainfo.so
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.Inhibit.xml
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.Solid.Networking.Client.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.Solid.PowerManagement.PolicyAgent.xml
%{_datadir}/kf5/kdoctools/customization/catalog4.xml
%{_datadir}/kf5/kdoctools/customization/dtd/kdex.dtd
%dir %{_datadir}/kf5/kssl
%{_datadir}/kf5/kssl/ca-bundle.crt
%{_datadir}/kf5/locale/countries
%{_datadir}/kf5/locale/currency
%{_datadir}/kf5/widgets/pics/kdatetimewidget.png
%{_datadir}/kf5/widgets/pics/kdatewidget.png
%{_datadir}/kf5/widgets/pics/kdialog.png
%{_datadir}/kf5/widgets/pics/kdoublenuminput.png
%{_datadir}/kf5/widgets/pics/keditlistbox.png
%{_datadir}/kf5/widgets/pics/kintnuminput.png
%{_datadir}/kf5/widgets/pics/kintspinbox.png
%{_datadir}/kf5/widgets/pics/kpushbutton.png
%{_datadir}/kf5/widgets/pics/krestrictedline.png
%{_datadir}/kf5/widgets/pics/ktextbrowser.png
%{_datadir}/kservices5/kcm_ssl.desktop
%{_datadir}/kservices5/qimageioplugins/bmp.desktop
%{_datadir}/kservices5/qimageioplugins/gif.desktop
%{_datadir}/kservices5/qimageioplugins/ico.desktop
%{_datadir}/kservices5/qimageioplugins/jpeg.desktop
%{_datadir}/kservices5/qimageioplugins/mng.desktop
%{_datadir}/kservices5/qimageioplugins/pbm.desktop
%{_datadir}/kservices5/qimageioplugins/pgm.desktop
%{_datadir}/kservices5/qimageioplugins/png.desktop
%{_datadir}/kservices5/qimageioplugins/ppm.desktop
%{_datadir}/kservices5/qimageioplugins/svg+xml-compressed.desktop
%{_datadir}/kservices5/qimageioplugins/svg+xml.desktop
%{_datadir}/kservices5/qimageioplugins/tiff.desktop
%{_datadir}/kservices5/qimageioplugins/wbmp.desktop
%{_datadir}/kservices5/qimageioplugins/webp.desktop
%{_datadir}/kservices5/qimageioplugins/xbm.desktop
%{_datadir}/kservices5/qimageioplugins/xpm.desktop
%{_datadir}/kservicetypes5/kdatatool.desktop
%{_datadir}/kservicetypes5/kfilewrite.desktop
%{_datadir}/kservicetypes5/kscan.desktop
%{_datadir}/kservicetypes5/qimageio_plugin.desktop
%{_localedir}/kf5_all_languages
%{_mandir}/man1/kf5-config.1*
%lang(ca) %{_mandir}/ca/man1/kf5-config.1*
%lang(de) %{_mandir}/de/man1/kf5-config.1*
%lang(es) %{_mandir}/es/man1/kf5-config.1*
%lang(fr) %{_mandir}/fr/man1/kf5-config.1*
%lang(it) %{_mandir}/it/man1/kf5-config.1*
%lang(nl) %{_mandir}/nl/man1/kf5-config.1*
%lang(pt) %{_mandir}/pt/man1/kf5-config.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kf5-config.1*
%lang(sv) %{_mandir}/sv/man1/kf5-config.1*
%lang(uk) %{_mandir}/uk/man1/kf5-config.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDELibs4Support
%{_libdir}/cmake/KDELibs4
%{_libdir}/cmake/KF5KDE4Support
%{_libdir}/cmake/KF5KDELibs4Support
%{_libdir}/libKF5KDELibs4Support.so
