# TODO:
# Not packaged dirs:
# /usr/include/KF5
# /usr/lib/qt5/plugins/kf5/parts
# /usr/share/kf5/khtml/css
# /usr/share/kf5/khtml
# /usr/share/kf5/kjava
# /usr/share/khtml
# /usr/share/kservices5


%define         _state          stable
%define		orgname		kdelibs4support

Summary:	KDELibs 4 Support
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/portingAids/%{orgname}-%{version}.tar.xz
# Source0-md5:	1fe3fc10a31a2c123338c3a8ae82455a
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
BuildRequires:	kf5-kdesignerplugin-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
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
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
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
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	-D_IMPORT_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
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
%attr(755,root,root) %{_libdir}/kf5/fileshareset
%attr(755,root,root) %ghost %{_libdir}/libKF5KDELibs4Support.so.5
%attr(755,root,root) %{_libdir}/libKF5KDELibs4Support.so.5.0.0
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kf5deprecatedwidgets.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ssl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/networkstatus.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/metainfo.so
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.Inhibit.xml
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.PowerManagement.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.Solid.Networking.Client.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.Solid.PowerManagement.PolicyAgent.xml
%{_docdir}/HTML/en/kdebugdialog5/index.cache.bz2
%{_docdir}/HTML/en/kdebugdialog5/index.docbook
%{_datadir}/kf5/kdoctools/customization/catalog4.xml
%{_datadir}/kf5/kdoctools/customization/dtd/kdex.dtd
%{_datadir}/kf5/kssl/ca-bundle.crt
%{_datadir}/kf5/locale/countries/C/country.desktop
%{_datadir}/kf5/locale/countries/C/flag.png
%{_datadir}/kf5/locale/countries/ad/country.desktop
%{_datadir}/kf5/locale/countries/ad/flag.png
%{_datadir}/kf5/locale/countries/ae/country.desktop
%{_datadir}/kf5/locale/countries/ae/flag.png
%{_datadir}/kf5/locale/countries/af/country.desktop
%{_datadir}/kf5/locale/countries/af/flag.png
%{_datadir}/kf5/locale/countries/ag/country.desktop
%{_datadir}/kf5/locale/countries/ag/flag.png
%{_datadir}/kf5/locale/countries/ai/country.desktop
%{_datadir}/kf5/locale/countries/ai/flag.png
%{_datadir}/kf5/locale/countries/al/country.desktop
%{_datadir}/kf5/locale/countries/al/flag.png
%{_datadir}/kf5/locale/countries/am/country.desktop
%{_datadir}/kf5/locale/countries/am/flag.png
%{_datadir}/kf5/locale/countries/an/country.desktop
%{_datadir}/kf5/locale/countries/an/flag.png
%{_datadir}/kf5/locale/countries/ao/country.desktop
%{_datadir}/kf5/locale/countries/ao/flag.png
%{_datadir}/kf5/locale/countries/ar/country.desktop
%{_datadir}/kf5/locale/countries/ar/flag.png
%{_datadir}/kf5/locale/countries/as/country.desktop
%{_datadir}/kf5/locale/countries/as/flag.png
%{_datadir}/kf5/locale/countries/at/country.desktop
%{_datadir}/kf5/locale/countries/at/flag.png
%{_datadir}/kf5/locale/countries/au/country.desktop
%{_datadir}/kf5/locale/countries/au/flag.png
%{_datadir}/kf5/locale/countries/aw/country.desktop
%{_datadir}/kf5/locale/countries/aw/flag.png
%{_datadir}/kf5/locale/countries/ax/country.desktop
%{_datadir}/kf5/locale/countries/ax/flag.png
%{_datadir}/kf5/locale/countries/az/country.desktop
%{_datadir}/kf5/locale/countries/az/flag.png
%{_datadir}/kf5/locale/countries/ba/country.desktop
%{_datadir}/kf5/locale/countries/ba/flag.png
%{_datadir}/kf5/locale/countries/bb/country.desktop
%{_datadir}/kf5/locale/countries/bb/flag.png
%{_datadir}/kf5/locale/countries/bd/country.desktop
%{_datadir}/kf5/locale/countries/bd/flag.png
%{_datadir}/kf5/locale/countries/be/country.desktop
%{_datadir}/kf5/locale/countries/be/flag.png
%{_datadir}/kf5/locale/countries/bf/country.desktop
%{_datadir}/kf5/locale/countries/bf/flag.png
%{_datadir}/kf5/locale/countries/bg/country.desktop
%{_datadir}/kf5/locale/countries/bg/flag.png
%{_datadir}/kf5/locale/countries/bh/country.desktop
%{_datadir}/kf5/locale/countries/bh/flag.png
%{_datadir}/kf5/locale/countries/bi/country.desktop
%{_datadir}/kf5/locale/countries/bi/flag.png
%{_datadir}/kf5/locale/countries/bj/country.desktop
%{_datadir}/kf5/locale/countries/bj/flag.png
%{_datadir}/kf5/locale/countries/bl/country.desktop
%{_datadir}/kf5/locale/countries/bl/flag.png
%{_datadir}/kf5/locale/countries/bm/country.desktop
%{_datadir}/kf5/locale/countries/bm/flag.png
%{_datadir}/kf5/locale/countries/bn/country.desktop
%{_datadir}/kf5/locale/countries/bn/flag.png
%{_datadir}/kf5/locale/countries/bo/country.desktop
%{_datadir}/kf5/locale/countries/bo/flag.png
%{_datadir}/kf5/locale/countries/br/country.desktop
%{_datadir}/kf5/locale/countries/br/flag.png
%{_datadir}/kf5/locale/countries/bs/country.desktop
%{_datadir}/kf5/locale/countries/bs/flag.png
%{_datadir}/kf5/locale/countries/bt/country.desktop
%{_datadir}/kf5/locale/countries/bt/flag.png
%{_datadir}/kf5/locale/countries/bw/country.desktop
%{_datadir}/kf5/locale/countries/bw/flag.png
%{_datadir}/kf5/locale/countries/by/country.desktop
%{_datadir}/kf5/locale/countries/by/flag.png
%{_datadir}/kf5/locale/countries/bz/country.desktop
%{_datadir}/kf5/locale/countries/bz/flag.png
%{_datadir}/kf5/locale/countries/ca/country.desktop
%{_datadir}/kf5/locale/countries/ca/flag.png
%{_datadir}/kf5/locale/countries/caribbean.desktop
%{_datadir}/kf5/locale/countries/cc/country.desktop
%{_datadir}/kf5/locale/countries/cc/flag.png
%{_datadir}/kf5/locale/countries/cd/country.desktop
%{_datadir}/kf5/locale/countries/cd/flag.png
%{_datadir}/kf5/locale/countries/centralafrica.desktop
%{_datadir}/kf5/locale/countries/centralamerica.desktop
%{_datadir}/kf5/locale/countries/centralasia.desktop
%{_datadir}/kf5/locale/countries/centraleurope.desktop
%{_datadir}/kf5/locale/countries/cf/country.desktop
%{_datadir}/kf5/locale/countries/cf/flag.png
%{_datadir}/kf5/locale/countries/cg/country.desktop
%{_datadir}/kf5/locale/countries/cg/flag.png
%{_datadir}/kf5/locale/countries/ch/country.desktop
%{_datadir}/kf5/locale/countries/ch/flag.png
%{_datadir}/kf5/locale/countries/ci/country.desktop
%{_datadir}/kf5/locale/countries/ci/flag.png
%{_datadir}/kf5/locale/countries/ck/country.desktop
%{_datadir}/kf5/locale/countries/ck/flag.png
%{_datadir}/kf5/locale/countries/cl/country.desktop
%{_datadir}/kf5/locale/countries/cl/flag.png
%{_datadir}/kf5/locale/countries/cm/country.desktop
%{_datadir}/kf5/locale/countries/cm/flag.png
%{_datadir}/kf5/locale/countries/cn/country.desktop
%{_datadir}/kf5/locale/countries/cn/flag.png
%{_datadir}/kf5/locale/countries/co/country.desktop
%{_datadir}/kf5/locale/countries/co/flag.png
%{_datadir}/kf5/locale/countries/cr/country.desktop
%{_datadir}/kf5/locale/countries/cr/flag.png
%{_datadir}/kf5/locale/countries/cu/country.desktop
%{_datadir}/kf5/locale/countries/cu/flag.png
%{_datadir}/kf5/locale/countries/cv/country.desktop
%{_datadir}/kf5/locale/countries/cv/flag.png
%{_datadir}/kf5/locale/countries/cx/country.desktop
%{_datadir}/kf5/locale/countries/cx/flag.png
%{_datadir}/kf5/locale/countries/cy/country.desktop
%{_datadir}/kf5/locale/countries/cy/flag.png
%{_datadir}/kf5/locale/countries/cz/country.desktop
%{_datadir}/kf5/locale/countries/cz/flag.png
%{_datadir}/kf5/locale/countries/de/country.desktop
%{_datadir}/kf5/locale/countries/de/flag.png
%{_datadir}/kf5/locale/countries/dj/country.desktop
%{_datadir}/kf5/locale/countries/dj/flag.png
%{_datadir}/kf5/locale/countries/dk/country.desktop
%{_datadir}/kf5/locale/countries/dk/flag.png
%{_datadir}/kf5/locale/countries/dm/country.desktop
%{_datadir}/kf5/locale/countries/dm/flag.png
%{_datadir}/kf5/locale/countries/do/country.desktop
%{_datadir}/kf5/locale/countries/do/flag.png
%{_datadir}/kf5/locale/countries/dz/country.desktop
%{_datadir}/kf5/locale/countries/dz/flag.png
%{_datadir}/kf5/locale/countries/eastafrica.desktop
%{_datadir}/kf5/locale/countries/eastasia.desktop
%{_datadir}/kf5/locale/countries/easteurope.desktop
%{_datadir}/kf5/locale/countries/ec/country.desktop
%{_datadir}/kf5/locale/countries/ec/flag.png
%{_datadir}/kf5/locale/countries/ee/country.desktop
%{_datadir}/kf5/locale/countries/ee/flag.png
%{_datadir}/kf5/locale/countries/eg/country.desktop
%{_datadir}/kf5/locale/countries/eg/flag.png
%{_datadir}/kf5/locale/countries/eh/country.desktop
%{_datadir}/kf5/locale/countries/eh/flag.png
%{_datadir}/kf5/locale/countries/er/country.desktop
%{_datadir}/kf5/locale/countries/er/flag.png
%{_datadir}/kf5/locale/countries/es/country.desktop
%{_datadir}/kf5/locale/countries/es/flag.png
%{_datadir}/kf5/locale/countries/et/country.desktop
%{_datadir}/kf5/locale/countries/et/flag.png
%{_datadir}/kf5/locale/countries/fi/country.desktop
%{_datadir}/kf5/locale/countries/fi/flag.png
%{_datadir}/kf5/locale/countries/fj/country.desktop
%{_datadir}/kf5/locale/countries/fj/flag.png
%{_datadir}/kf5/locale/countries/fk/country.desktop
%{_datadir}/kf5/locale/countries/fk/flag.png
%{_datadir}/kf5/locale/countries/fm/country.desktop
%{_datadir}/kf5/locale/countries/fm/flag.png
%{_datadir}/kf5/locale/countries/fo/country.desktop
%{_datadir}/kf5/locale/countries/fo/flag.png
%{_datadir}/kf5/locale/countries/fr/country.desktop
%{_datadir}/kf5/locale/countries/fr/flag.png
%{_datadir}/kf5/locale/countries/ga/country.desktop
%{_datadir}/kf5/locale/countries/ga/flag.png
%{_datadir}/kf5/locale/countries/gb/country.desktop
%{_datadir}/kf5/locale/countries/gb/flag.png
%{_datadir}/kf5/locale/countries/gd/country.desktop
%{_datadir}/kf5/locale/countries/gd/flag.png
%{_datadir}/kf5/locale/countries/ge/country.desktop
%{_datadir}/kf5/locale/countries/ge/flag.png
%{_datadir}/kf5/locale/countries/gf/country.desktop
%{_datadir}/kf5/locale/countries/gf/flag.png
%{_datadir}/kf5/locale/countries/gg/country.desktop
%{_datadir}/kf5/locale/countries/gg/flag.png
%{_datadir}/kf5/locale/countries/gh/country.desktop
%{_datadir}/kf5/locale/countries/gh/flag.png
%{_datadir}/kf5/locale/countries/gi/country.desktop
%{_datadir}/kf5/locale/countries/gi/flag.png
%{_datadir}/kf5/locale/countries/gl/country.desktop
%{_datadir}/kf5/locale/countries/gl/flag.png
%{_datadir}/kf5/locale/countries/gm/country.desktop
%{_datadir}/kf5/locale/countries/gm/flag.png
%{_datadir}/kf5/locale/countries/gn/country.desktop
%{_datadir}/kf5/locale/countries/gn/flag.png
%{_datadir}/kf5/locale/countries/gp/country.desktop
%{_datadir}/kf5/locale/countries/gp/flag.png
%{_datadir}/kf5/locale/countries/gq/country.desktop
%{_datadir}/kf5/locale/countries/gq/flag.png
%{_datadir}/kf5/locale/countries/gr/country.desktop
%{_datadir}/kf5/locale/countries/gr/flag.png
%{_datadir}/kf5/locale/countries/gt/country.desktop
%{_datadir}/kf5/locale/countries/gt/flag.png
%{_datadir}/kf5/locale/countries/gu/country.desktop
%{_datadir}/kf5/locale/countries/gu/flag.png
%{_datadir}/kf5/locale/countries/gw/country.desktop
%{_datadir}/kf5/locale/countries/gw/flag.png
%{_datadir}/kf5/locale/countries/gy/country.desktop
%{_datadir}/kf5/locale/countries/gy/flag.png
%{_datadir}/kf5/locale/countries/hk/country.desktop
%{_datadir}/kf5/locale/countries/hk/flag.png
%{_datadir}/kf5/locale/countries/hn/country.desktop
%{_datadir}/kf5/locale/countries/hn/flag.png
%{_datadir}/kf5/locale/countries/hr/country.desktop
%{_datadir}/kf5/locale/countries/hr/flag.png
%{_datadir}/kf5/locale/countries/ht/country.desktop
%{_datadir}/kf5/locale/countries/ht/flag.png
%{_datadir}/kf5/locale/countries/hu/country.desktop
%{_datadir}/kf5/locale/countries/hu/flag.png
%{_datadir}/kf5/locale/countries/id/country.desktop
%{_datadir}/kf5/locale/countries/id/flag.png
%{_datadir}/kf5/locale/countries/ie/country.desktop
%{_datadir}/kf5/locale/countries/ie/flag.png
%{_datadir}/kf5/locale/countries/il/country.desktop
%{_datadir}/kf5/locale/countries/il/flag.png
%{_datadir}/kf5/locale/countries/im/country.desktop
%{_datadir}/kf5/locale/countries/im/flag.png
%{_datadir}/kf5/locale/countries/in/country.desktop
%{_datadir}/kf5/locale/countries/in/flag.png
%{_datadir}/kf5/locale/countries/iq/country.desktop
%{_datadir}/kf5/locale/countries/iq/flag.png
%{_datadir}/kf5/locale/countries/ir/country.desktop
%{_datadir}/kf5/locale/countries/ir/flag.png
%{_datadir}/kf5/locale/countries/is/country.desktop
%{_datadir}/kf5/locale/countries/is/flag.png
%{_datadir}/kf5/locale/countries/it/country.desktop
%{_datadir}/kf5/locale/countries/it/flag.png
%{_datadir}/kf5/locale/countries/je/country.desktop
%{_datadir}/kf5/locale/countries/je/flag.png
%{_datadir}/kf5/locale/countries/jm/country.desktop
%{_datadir}/kf5/locale/countries/jm/flag.png
%{_datadir}/kf5/locale/countries/jo/country.desktop
%{_datadir}/kf5/locale/countries/jo/flag.png
%{_datadir}/kf5/locale/countries/jp/country.desktop
%{_datadir}/kf5/locale/countries/jp/flag.png
%{_datadir}/kf5/locale/countries/ke/country.desktop
%{_datadir}/kf5/locale/countries/ke/flag.png
%{_datadir}/kf5/locale/countries/kg/country.desktop
%{_datadir}/kf5/locale/countries/kg/flag.png
%{_datadir}/kf5/locale/countries/kh/country.desktop
%{_datadir}/kf5/locale/countries/kh/flag.png
%{_datadir}/kf5/locale/countries/ki/country.desktop
%{_datadir}/kf5/locale/countries/ki/flag.png
%{_datadir}/kf5/locale/countries/km/country.desktop
%{_datadir}/kf5/locale/countries/km/flag.png
%{_datadir}/kf5/locale/countries/kn/country.desktop
%{_datadir}/kf5/locale/countries/kn/flag.png
%{_datadir}/kf5/locale/countries/kp/country.desktop
%{_datadir}/kf5/locale/countries/kp/flag.png
%{_datadir}/kf5/locale/countries/kr/country.desktop
%{_datadir}/kf5/locale/countries/kr/flag.png
%{_datadir}/kf5/locale/countries/kw/country.desktop
%{_datadir}/kf5/locale/countries/kw/flag.png
%{_datadir}/kf5/locale/countries/ky/country.desktop
%{_datadir}/kf5/locale/countries/ky/flag.png
%{_datadir}/kf5/locale/countries/kz/country.desktop
%{_datadir}/kf5/locale/countries/kz/flag.png
%{_datadir}/kf5/locale/countries/la/country.desktop
%{_datadir}/kf5/locale/countries/la/flag.png
%{_datadir}/kf5/locale/countries/lb/country.desktop
%{_datadir}/kf5/locale/countries/lb/flag.png
%{_datadir}/kf5/locale/countries/lc/country.desktop
%{_datadir}/kf5/locale/countries/lc/flag.png
%{_datadir}/kf5/locale/countries/li/country.desktop
%{_datadir}/kf5/locale/countries/li/flag.png
%{_datadir}/kf5/locale/countries/lk/country.desktop
%{_datadir}/kf5/locale/countries/lk/flag.png
%{_datadir}/kf5/locale/countries/lr/country.desktop
%{_datadir}/kf5/locale/countries/lr/flag.png
%{_datadir}/kf5/locale/countries/ls/country.desktop
%{_datadir}/kf5/locale/countries/ls/flag.png
%{_datadir}/kf5/locale/countries/lt/country.desktop
%{_datadir}/kf5/locale/countries/lt/flag.png
%{_datadir}/kf5/locale/countries/lu/country.desktop
%{_datadir}/kf5/locale/countries/lu/flag.png
%{_datadir}/kf5/locale/countries/lv/country.desktop
%{_datadir}/kf5/locale/countries/lv/flag.png
%{_datadir}/kf5/locale/countries/ly/country.desktop
%{_datadir}/kf5/locale/countries/ly/flag.png
%{_datadir}/kf5/locale/countries/ma/country.desktop
%{_datadir}/kf5/locale/countries/ma/flag.png
%{_datadir}/kf5/locale/countries/mc/country.desktop
%{_datadir}/kf5/locale/countries/mc/flag.png
%{_datadir}/kf5/locale/countries/md/country.desktop
%{_datadir}/kf5/locale/countries/md/flag.png
%{_datadir}/kf5/locale/countries/me/country.desktop
%{_datadir}/kf5/locale/countries/me/flag.png
%{_datadir}/kf5/locale/countries/mf/country.desktop
%{_datadir}/kf5/locale/countries/mf/flag.png
%{_datadir}/kf5/locale/countries/mg/country.desktop
%{_datadir}/kf5/locale/countries/mg/flag.png
%{_datadir}/kf5/locale/countries/mh/country.desktop
%{_datadir}/kf5/locale/countries/mh/flag.png
%{_datadir}/kf5/locale/countries/middleeast.desktop
%{_datadir}/kf5/locale/countries/mk/country.desktop
%{_datadir}/kf5/locale/countries/mk/flag.png
%{_datadir}/kf5/locale/countries/ml/country.desktop
%{_datadir}/kf5/locale/countries/ml/flag.png
%{_datadir}/kf5/locale/countries/mm/country.desktop
%{_datadir}/kf5/locale/countries/mm/flag.png
%{_datadir}/kf5/locale/countries/mn/country.desktop
%{_datadir}/kf5/locale/countries/mn/flag.png
%{_datadir}/kf5/locale/countries/mo/country.desktop
%{_datadir}/kf5/locale/countries/mo/flag.png
%{_datadir}/kf5/locale/countries/mp/country.desktop
%{_datadir}/kf5/locale/countries/mp/flag.png
%{_datadir}/kf5/locale/countries/mq/country.desktop
%{_datadir}/kf5/locale/countries/mq/flag.png
%{_datadir}/kf5/locale/countries/mr/country.desktop
%{_datadir}/kf5/locale/countries/mr/flag.png
%{_datadir}/kf5/locale/countries/ms/country.desktop
%{_datadir}/kf5/locale/countries/ms/flag.png
%{_datadir}/kf5/locale/countries/mt/country.desktop
%{_datadir}/kf5/locale/countries/mt/flag.png
%{_datadir}/kf5/locale/countries/mu/country.desktop
%{_datadir}/kf5/locale/countries/mu/flag.png
%{_datadir}/kf5/locale/countries/mv/country.desktop
%{_datadir}/kf5/locale/countries/mv/flag.png
%{_datadir}/kf5/locale/countries/mw/country.desktop
%{_datadir}/kf5/locale/countries/mw/flag.png
%{_datadir}/kf5/locale/countries/mx/country.desktop
%{_datadir}/kf5/locale/countries/mx/flag.png
%{_datadir}/kf5/locale/countries/my/country.desktop
%{_datadir}/kf5/locale/countries/my/flag.png
%{_datadir}/kf5/locale/countries/mz/country.desktop
%{_datadir}/kf5/locale/countries/mz/flag.png
%{_datadir}/kf5/locale/countries/na/country.desktop
%{_datadir}/kf5/locale/countries/na/flag.png
%{_datadir}/kf5/locale/countries/nc/country.desktop
%{_datadir}/kf5/locale/countries/nc/flag.png
%{_datadir}/kf5/locale/countries/ne/country.desktop
%{_datadir}/kf5/locale/countries/ne/flag.png
%{_datadir}/kf5/locale/countries/nf/country.desktop
%{_datadir}/kf5/locale/countries/nf/flag.png
%{_datadir}/kf5/locale/countries/ng/country.desktop
%{_datadir}/kf5/locale/countries/ng/flag.png
%{_datadir}/kf5/locale/countries/ni/country.desktop
%{_datadir}/kf5/locale/countries/ni/flag.png
%{_datadir}/kf5/locale/countries/nl/country.desktop
%{_datadir}/kf5/locale/countries/nl/flag.png
%{_datadir}/kf5/locale/countries/no/country.desktop
%{_datadir}/kf5/locale/countries/no/flag.png
%{_datadir}/kf5/locale/countries/northafrica.desktop
%{_datadir}/kf5/locale/countries/northamerica.desktop
%{_datadir}/kf5/locale/countries/northeurope.desktop
%{_datadir}/kf5/locale/countries/np/country.desktop
%{_datadir}/kf5/locale/countries/np/flag.png
%{_datadir}/kf5/locale/countries/nr/country.desktop
%{_datadir}/kf5/locale/countries/nr/flag.png
%{_datadir}/kf5/locale/countries/nu/country.desktop
%{_datadir}/kf5/locale/countries/nu/flag.png
%{_datadir}/kf5/locale/countries/nz/country.desktop
%{_datadir}/kf5/locale/countries/nz/flag.png
%{_datadir}/kf5/locale/countries/oceania.desktop
%{_datadir}/kf5/locale/countries/om/country.desktop
%{_datadir}/kf5/locale/countries/om/flag.png
%{_datadir}/kf5/locale/countries/pa/country.desktop
%{_datadir}/kf5/locale/countries/pa/flag.png
%{_datadir}/kf5/locale/countries/pe/country.desktop
%{_datadir}/kf5/locale/countries/pe/flag.png
%{_datadir}/kf5/locale/countries/pf/country.desktop
%{_datadir}/kf5/locale/countries/pf/flag.png
%{_datadir}/kf5/locale/countries/pg/country.desktop
%{_datadir}/kf5/locale/countries/pg/flag.png
%{_datadir}/kf5/locale/countries/ph/country.desktop
%{_datadir}/kf5/locale/countries/ph/flag.png
%{_datadir}/kf5/locale/countries/pk/country.desktop
%{_datadir}/kf5/locale/countries/pk/flag.png
%{_datadir}/kf5/locale/countries/pl/country.desktop
%{_datadir}/kf5/locale/countries/pl/flag.png
%{_datadir}/kf5/locale/countries/pm/country.desktop
%{_datadir}/kf5/locale/countries/pm/flag.png
%{_datadir}/kf5/locale/countries/pn/country.desktop
%{_datadir}/kf5/locale/countries/pn/flag.png
%{_datadir}/kf5/locale/countries/pr/country.desktop
%{_datadir}/kf5/locale/countries/pr/flag.png
%{_datadir}/kf5/locale/countries/ps/country.desktop
%{_datadir}/kf5/locale/countries/ps/flag.png
%{_datadir}/kf5/locale/countries/pt/country.desktop
%{_datadir}/kf5/locale/countries/pt/flag.png
%{_datadir}/kf5/locale/countries/pw/country.desktop
%{_datadir}/kf5/locale/countries/pw/flag.png
%{_datadir}/kf5/locale/countries/py/country.desktop
%{_datadir}/kf5/locale/countries/py/flag.png
%{_datadir}/kf5/locale/countries/qa/country.desktop
%{_datadir}/kf5/locale/countries/qa/flag.png
%{_datadir}/kf5/locale/countries/re/country.desktop
%{_datadir}/kf5/locale/countries/re/flag.png
%{_datadir}/kf5/locale/countries/ro/country.desktop
%{_datadir}/kf5/locale/countries/ro/flag.png
%{_datadir}/kf5/locale/countries/rs/country.desktop
%{_datadir}/kf5/locale/countries/rs/flag.png
%{_datadir}/kf5/locale/countries/ru/country.desktop
%{_datadir}/kf5/locale/countries/ru/flag.png
%{_datadir}/kf5/locale/countries/rw/country.desktop
%{_datadir}/kf5/locale/countries/rw/flag.png
%{_datadir}/kf5/locale/countries/sa/country.desktop
%{_datadir}/kf5/locale/countries/sa/flag.png
%{_datadir}/kf5/locale/countries/sb/country.desktop
%{_datadir}/kf5/locale/countries/sb/flag.png
%{_datadir}/kf5/locale/countries/sc/country.desktop
%{_datadir}/kf5/locale/countries/sc/flag.png
%{_datadir}/kf5/locale/countries/sd/country.desktop
%{_datadir}/kf5/locale/countries/sd/flag.png
%{_datadir}/kf5/locale/countries/se/country.desktop
%{_datadir}/kf5/locale/countries/se/flag.png
%{_datadir}/kf5/locale/countries/sg/country.desktop
%{_datadir}/kf5/locale/countries/sg/flag.png
%{_datadir}/kf5/locale/countries/sh/country.desktop
%{_datadir}/kf5/locale/countries/sh/flag.png
%{_datadir}/kf5/locale/countries/si/country.desktop
%{_datadir}/kf5/locale/countries/si/flag.png
%{_datadir}/kf5/locale/countries/sk/country.desktop
%{_datadir}/kf5/locale/countries/sk/flag.png
%{_datadir}/kf5/locale/countries/sl/country.desktop
%{_datadir}/kf5/locale/countries/sl/flag.png
%{_datadir}/kf5/locale/countries/sm/country.desktop
%{_datadir}/kf5/locale/countries/sm/flag.png
%{_datadir}/kf5/locale/countries/sn/country.desktop
%{_datadir}/kf5/locale/countries/sn/flag.png
%{_datadir}/kf5/locale/countries/so/country.desktop
%{_datadir}/kf5/locale/countries/so/flag.png
%{_datadir}/kf5/locale/countries/southafrica.desktop
%{_datadir}/kf5/locale/countries/southamerica.desktop
%{_datadir}/kf5/locale/countries/southasia.desktop
%{_datadir}/kf5/locale/countries/southeastasia.desktop
%{_datadir}/kf5/locale/countries/southeurope.desktop
%{_datadir}/kf5/locale/countries/sr/country.desktop
%{_datadir}/kf5/locale/countries/sr/flag.png
%{_datadir}/kf5/locale/countries/ss/country.desktop
%{_datadir}/kf5/locale/countries/ss/flag.png
%{_datadir}/kf5/locale/countries/st/country.desktop
%{_datadir}/kf5/locale/countries/st/flag.png
%{_datadir}/kf5/locale/countries/sv/country.desktop
%{_datadir}/kf5/locale/countries/sv/flag.png
%{_datadir}/kf5/locale/countries/sy/country.desktop
%{_datadir}/kf5/locale/countries/sy/flag.png
%{_datadir}/kf5/locale/countries/sz/country.desktop
%{_datadir}/kf5/locale/countries/sz/flag.png
%{_datadir}/kf5/locale/countries/tc/country.desktop
%{_datadir}/kf5/locale/countries/tc/flag.png
%{_datadir}/kf5/locale/countries/td/country.desktop
%{_datadir}/kf5/locale/countries/td/flag.png
%{_datadir}/kf5/locale/countries/tg/country.desktop
%{_datadir}/kf5/locale/countries/tg/flag.png
%{_datadir}/kf5/locale/countries/th/country.desktop
%{_datadir}/kf5/locale/countries/th/flag.png
%{_datadir}/kf5/locale/countries/tj/country.desktop
%{_datadir}/kf5/locale/countries/tj/flag.png
%{_datadir}/kf5/locale/countries/tk/country.desktop
%{_datadir}/kf5/locale/countries/tk/flag.png
%{_datadir}/kf5/locale/countries/tl/country.desktop
%{_datadir}/kf5/locale/countries/tl/flag.png
%{_datadir}/kf5/locale/countries/tm/country.desktop
%{_datadir}/kf5/locale/countries/tm/flag.png
%{_datadir}/kf5/locale/countries/tn/country.desktop
%{_datadir}/kf5/locale/countries/tn/flag.png
%{_datadir}/kf5/locale/countries/to/country.desktop
%{_datadir}/kf5/locale/countries/to/flag.png
%{_datadir}/kf5/locale/countries/tp/country.desktop
%{_datadir}/kf5/locale/countries/tp/flag.png
%{_datadir}/kf5/locale/countries/tr/country.desktop
%{_datadir}/kf5/locale/countries/tr/flag.png
%{_datadir}/kf5/locale/countries/tt/country.desktop
%{_datadir}/kf5/locale/countries/tt/flag.png
%{_datadir}/kf5/locale/countries/tv/country.desktop
%{_datadir}/kf5/locale/countries/tv/flag.png
%{_datadir}/kf5/locale/countries/tw/country.desktop
%{_datadir}/kf5/locale/countries/tw/flag.png
%{_datadir}/kf5/locale/countries/tz/country.desktop
%{_datadir}/kf5/locale/countries/tz/flag.png
%{_datadir}/kf5/locale/countries/ua/country.desktop
%{_datadir}/kf5/locale/countries/ua/flag.png
%{_datadir}/kf5/locale/countries/ug/country.desktop
%{_datadir}/kf5/locale/countries/ug/flag.png
%{_datadir}/kf5/locale/countries/us/country.desktop
%{_datadir}/kf5/locale/countries/us/flag.png
%{_datadir}/kf5/locale/countries/uy/country.desktop
%{_datadir}/kf5/locale/countries/uy/flag.png
%{_datadir}/kf5/locale/countries/uz/country.desktop
%{_datadir}/kf5/locale/countries/uz/flag.png
%{_datadir}/kf5/locale/countries/va/country.desktop
%{_datadir}/kf5/locale/countries/va/flag.png
%{_datadir}/kf5/locale/countries/vc/country.desktop
%{_datadir}/kf5/locale/countries/vc/flag.png
%{_datadir}/kf5/locale/countries/ve/country.desktop
%{_datadir}/kf5/locale/countries/ve/flag.png
%{_datadir}/kf5/locale/countries/vg/country.desktop
%{_datadir}/kf5/locale/countries/vg/flag.png
%{_datadir}/kf5/locale/countries/vi/country.desktop
%{_datadir}/kf5/locale/countries/vi/flag.png
%{_datadir}/kf5/locale/countries/vn/country.desktop
%{_datadir}/kf5/locale/countries/vn/flag.png
%{_datadir}/kf5/locale/countries/vu/country.desktop
%{_datadir}/kf5/locale/countries/vu/flag.png
%{_datadir}/kf5/locale/countries/westafrica.desktop
%{_datadir}/kf5/locale/countries/westeurope.desktop
%{_datadir}/kf5/locale/countries/wf/country.desktop
%{_datadir}/kf5/locale/countries/wf/flag.png
%{_datadir}/kf5/locale/countries/ws/country.desktop
%{_datadir}/kf5/locale/countries/ws/flag.png
%{_datadir}/kf5/locale/countries/ye/country.desktop
%{_datadir}/kf5/locale/countries/ye/flag.png
%{_datadir}/kf5/locale/countries/yt/country.desktop
%{_datadir}/kf5/locale/countries/yt/flag.png
%{_datadir}/kf5/locale/countries/za/country.desktop
%{_datadir}/kf5/locale/countries/za/flag.png
%{_datadir}/kf5/locale/countries/zm/country.desktop
%{_datadir}/kf5/locale/countries/zm/flag.png
%{_datadir}/kf5/locale/countries/zw/country.desktop
%{_datadir}/kf5/locale/countries/zw/flag.png
%{_datadir}/kf5/locale/currency/adf.desktop
%{_datadir}/kf5/locale/currency/adp.desktop
%{_datadir}/kf5/locale/currency/aed.desktop
%{_datadir}/kf5/locale/currency/afa.desktop
%{_datadir}/kf5/locale/currency/afn.desktop
%{_datadir}/kf5/locale/currency/all.desktop
%{_datadir}/kf5/locale/currency/amd.desktop
%{_datadir}/kf5/locale/currency/ang.desktop
%{_datadir}/kf5/locale/currency/aoa.desktop
%{_datadir}/kf5/locale/currency/aon.desktop
%{_datadir}/kf5/locale/currency/ars.desktop
%{_datadir}/kf5/locale/currency/ats.desktop
%{_datadir}/kf5/locale/currency/aud.desktop
%{_datadir}/kf5/locale/currency/awg.desktop
%{_datadir}/kf5/locale/currency/azm.desktop
%{_datadir}/kf5/locale/currency/azn.desktop
%{_datadir}/kf5/locale/currency/bam.desktop
%{_datadir}/kf5/locale/currency/bbd.desktop
%{_datadir}/kf5/locale/currency/bdt.desktop
%{_datadir}/kf5/locale/currency/bef.desktop
%{_datadir}/kf5/locale/currency/bgl.desktop
%{_datadir}/kf5/locale/currency/bgn.desktop
%{_datadir}/kf5/locale/currency/bhd.desktop
%{_datadir}/kf5/locale/currency/bif.desktop
%{_datadir}/kf5/locale/currency/bmd.desktop
%{_datadir}/kf5/locale/currency/bnd.desktop
%{_datadir}/kf5/locale/currency/bob.desktop
%{_datadir}/kf5/locale/currency/bov.desktop
%{_datadir}/kf5/locale/currency/brl.desktop
%{_datadir}/kf5/locale/currency/bsd.desktop
%{_datadir}/kf5/locale/currency/btn.desktop
%{_datadir}/kf5/locale/currency/bwp.desktop
%{_datadir}/kf5/locale/currency/byr.desktop
%{_datadir}/kf5/locale/currency/bzd.desktop
%{_datadir}/kf5/locale/currency/cad.desktop
%{_datadir}/kf5/locale/currency/cdf.desktop
%{_datadir}/kf5/locale/currency/chf.desktop
%{_datadir}/kf5/locale/currency/clf.desktop
%{_datadir}/kf5/locale/currency/clp.desktop
%{_datadir}/kf5/locale/currency/cny.desktop
%{_datadir}/kf5/locale/currency/cop.desktop
%{_datadir}/kf5/locale/currency/cou.desktop
%{_datadir}/kf5/locale/currency/crc.desktop
%{_datadir}/kf5/locale/currency/cuc.desktop
%{_datadir}/kf5/locale/currency/cup.desktop
%{_datadir}/kf5/locale/currency/cve.desktop
%{_datadir}/kf5/locale/currency/cyp.desktop
%{_datadir}/kf5/locale/currency/czk.desktop
%{_datadir}/kf5/locale/currency/dem.desktop
%{_datadir}/kf5/locale/currency/djf.desktop
%{_datadir}/kf5/locale/currency/dkk.desktop
%{_datadir}/kf5/locale/currency/dop.desktop
%{_datadir}/kf5/locale/currency/dzd.desktop
%{_datadir}/kf5/locale/currency/eek.desktop
%{_datadir}/kf5/locale/currency/egp.desktop
%{_datadir}/kf5/locale/currency/ern.desktop
%{_datadir}/kf5/locale/currency/esp.desktop
%{_datadir}/kf5/locale/currency/etb.desktop
%{_datadir}/kf5/locale/currency/eur.desktop
%{_datadir}/kf5/locale/currency/fim.desktop
%{_datadir}/kf5/locale/currency/fjd.desktop
%{_datadir}/kf5/locale/currency/fkp.desktop
%{_datadir}/kf5/locale/currency/frf.desktop
%{_datadir}/kf5/locale/currency/gbp.desktop
%{_datadir}/kf5/locale/currency/gel.desktop
%{_datadir}/kf5/locale/currency/ghc.desktop
%{_datadir}/kf5/locale/currency/ghs.desktop
%{_datadir}/kf5/locale/currency/gip.desktop
%{_datadir}/kf5/locale/currency/gmd.desktop
%{_datadir}/kf5/locale/currency/gnf.desktop
%{_datadir}/kf5/locale/currency/grd.desktop
%{_datadir}/kf5/locale/currency/gtq.desktop
%{_datadir}/kf5/locale/currency/gwp.desktop
%{_datadir}/kf5/locale/currency/gyd.desktop
%{_datadir}/kf5/locale/currency/hkd.desktop
%{_datadir}/kf5/locale/currency/hnl.desktop
%{_datadir}/kf5/locale/currency/hrk.desktop
%{_datadir}/kf5/locale/currency/htg.desktop
%{_datadir}/kf5/locale/currency/huf.desktop
%{_datadir}/kf5/locale/currency/idr.desktop
%{_datadir}/kf5/locale/currency/iep.desktop
%{_datadir}/kf5/locale/currency/ils.desktop
%{_datadir}/kf5/locale/currency/inr.desktop
%{_datadir}/kf5/locale/currency/iqd.desktop
%{_datadir}/kf5/locale/currency/irr.desktop
%{_datadir}/kf5/locale/currency/isk.desktop
%{_datadir}/kf5/locale/currency/itl.desktop
%{_datadir}/kf5/locale/currency/jmd.desktop
%{_datadir}/kf5/locale/currency/jod.desktop
%{_datadir}/kf5/locale/currency/jpy.desktop
%{_datadir}/kf5/locale/currency/kes.desktop
%{_datadir}/kf5/locale/currency/kgs.desktop
%{_datadir}/kf5/locale/currency/khr.desktop
%{_datadir}/kf5/locale/currency/kmf.desktop
%{_datadir}/kf5/locale/currency/kpw.desktop
%{_datadir}/kf5/locale/currency/krw.desktop
%{_datadir}/kf5/locale/currency/kwd.desktop
%{_datadir}/kf5/locale/currency/kyd.desktop
%{_datadir}/kf5/locale/currency/kzt.desktop
%{_datadir}/kf5/locale/currency/lak.desktop
%{_datadir}/kf5/locale/currency/lbp.desktop
%{_datadir}/kf5/locale/currency/lkr.desktop
%{_datadir}/kf5/locale/currency/lrd.desktop
%{_datadir}/kf5/locale/currency/lsl.desktop
%{_datadir}/kf5/locale/currency/ltl.desktop
%{_datadir}/kf5/locale/currency/luf.desktop
%{_datadir}/kf5/locale/currency/lvl.desktop
%{_datadir}/kf5/locale/currency/lyd.desktop
%{_datadir}/kf5/locale/currency/mad.desktop
%{_datadir}/kf5/locale/currency/mdl.desktop
%{_datadir}/kf5/locale/currency/mga.desktop
%{_datadir}/kf5/locale/currency/mgf.desktop
%{_datadir}/kf5/locale/currency/mkd.desktop
%{_datadir}/kf5/locale/currency/mlf.desktop
%{_datadir}/kf5/locale/currency/mmk.desktop
%{_datadir}/kf5/locale/currency/mnt.desktop
%{_datadir}/kf5/locale/currency/mop.desktop
%{_datadir}/kf5/locale/currency/mro.desktop
%{_datadir}/kf5/locale/currency/mtl.desktop
%{_datadir}/kf5/locale/currency/mur.desktop
%{_datadir}/kf5/locale/currency/mvr.desktop
%{_datadir}/kf5/locale/currency/mwk.desktop
%{_datadir}/kf5/locale/currency/mxn.desktop
%{_datadir}/kf5/locale/currency/mxv.desktop
%{_datadir}/kf5/locale/currency/myr.desktop
%{_datadir}/kf5/locale/currency/mzm.desktop
%{_datadir}/kf5/locale/currency/mzn.desktop
%{_datadir}/kf5/locale/currency/nad.desktop
%{_datadir}/kf5/locale/currency/ngn.desktop
%{_datadir}/kf5/locale/currency/nio.desktop
%{_datadir}/kf5/locale/currency/nlg.desktop
%{_datadir}/kf5/locale/currency/nok.desktop
%{_datadir}/kf5/locale/currency/npr.desktop
%{_datadir}/kf5/locale/currency/nzd.desktop
%{_datadir}/kf5/locale/currency/omr.desktop
%{_datadir}/kf5/locale/currency/pab.desktop
%{_datadir}/kf5/locale/currency/pen.desktop
%{_datadir}/kf5/locale/currency/pgk.desktop
%{_datadir}/kf5/locale/currency/php.desktop
%{_datadir}/kf5/locale/currency/pkr.desktop
%{_datadir}/kf5/locale/currency/pln.desktop
%{_datadir}/kf5/locale/currency/pte.desktop
%{_datadir}/kf5/locale/currency/pyg.desktop
%{_datadir}/kf5/locale/currency/qar.desktop
%{_datadir}/kf5/locale/currency/rol.desktop
%{_datadir}/kf5/locale/currency/ron.desktop
%{_datadir}/kf5/locale/currency/rsd.desktop
%{_datadir}/kf5/locale/currency/rub.desktop
%{_datadir}/kf5/locale/currency/rur.desktop
%{_datadir}/kf5/locale/currency/rwf.desktop
%{_datadir}/kf5/locale/currency/sar.desktop
%{_datadir}/kf5/locale/currency/sbd.desktop
%{_datadir}/kf5/locale/currency/scr.desktop
%{_datadir}/kf5/locale/currency/sdd.desktop
%{_datadir}/kf5/locale/currency/sdg.desktop
%{_datadir}/kf5/locale/currency/sek.desktop
%{_datadir}/kf5/locale/currency/sgd.desktop
%{_datadir}/kf5/locale/currency/shp.desktop
%{_datadir}/kf5/locale/currency/sit.desktop
%{_datadir}/kf5/locale/currency/skk.desktop
%{_datadir}/kf5/locale/currency/sll.desktop
%{_datadir}/kf5/locale/currency/sos.desktop
%{_datadir}/kf5/locale/currency/srd.desktop
%{_datadir}/kf5/locale/currency/srg.desktop
%{_datadir}/kf5/locale/currency/ssp.desktop
%{_datadir}/kf5/locale/currency/std.desktop
%{_datadir}/kf5/locale/currency/svc.desktop
%{_datadir}/kf5/locale/currency/syp.desktop
%{_datadir}/kf5/locale/currency/szl.desktop
%{_datadir}/kf5/locale/currency/thb.desktop
%{_datadir}/kf5/locale/currency/tjs.desktop
%{_datadir}/kf5/locale/currency/tmm.desktop
%{_datadir}/kf5/locale/currency/tmt.desktop
%{_datadir}/kf5/locale/currency/tnd.desktop
%{_datadir}/kf5/locale/currency/top.desktop
%{_datadir}/kf5/locale/currency/tpe.desktop
%{_datadir}/kf5/locale/currency/trl.desktop
%{_datadir}/kf5/locale/currency/try.desktop
%{_datadir}/kf5/locale/currency/ttd.desktop
%{_datadir}/kf5/locale/currency/twd.desktop
%{_datadir}/kf5/locale/currency/tzs.desktop
%{_datadir}/kf5/locale/currency/uah.desktop
%{_datadir}/kf5/locale/currency/ugx.desktop
%{_datadir}/kf5/locale/currency/usd.desktop
%{_datadir}/kf5/locale/currency/usn.desktop
%{_datadir}/kf5/locale/currency/uss.desktop
%{_datadir}/kf5/locale/currency/uyu.desktop
%{_datadir}/kf5/locale/currency/uzs.desktop
%{_datadir}/kf5/locale/currency/veb.desktop
%{_datadir}/kf5/locale/currency/vnd.desktop
%{_datadir}/kf5/locale/currency/vuv.desktop
%{_datadir}/kf5/locale/currency/wst.desktop
%{_datadir}/kf5/locale/currency/xaf.desktop
%{_datadir}/kf5/locale/currency/xag.desktop
%{_datadir}/kf5/locale/currency/xau.desktop
%{_datadir}/kf5/locale/currency/xcd.desktop
%{_datadir}/kf5/locale/currency/xof.desktop
%{_datadir}/kf5/locale/currency/xpd.desktop
%{_datadir}/kf5/locale/currency/xpf.desktop
%{_datadir}/kf5/locale/currency/xpt.desktop
%{_datadir}/kf5/locale/currency/yer.desktop
%{_datadir}/kf5/locale/currency/yum.desktop
%{_datadir}/kf5/locale/currency/zar.desktop
%{_datadir}/kf5/locale/currency/zmk.desktop
%{_datadir}/kf5/locale/currency/zwd.desktop
%{_datadir}/kf5/locale/currency/zwl.desktop
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
%{_datadir}/kservices5/kded/networkstatus.desktop
%{_datadir}/kservices5/metainfo.protocol
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
%{_localedir}/en_US/kf5_entry.desktop
%{_localedir}/kf5_all_languages
%{_mandir}/man1/kf5-config.1*


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDELibs4Support
%{_includedir}/KF5/kdelibs4support_version.h
%{_libdir}/cmake/KDELibs4
%{_libdir}/cmake/KF5KDE4Support
%{_libdir}/cmake/KF5KDELibs4Support
%attr(755,root,root) %{_libdir}/libKF5KDELibs4Support.so
