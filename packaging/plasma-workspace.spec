# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       plasma-workspace

# >> macros
%bcond_with plasma-activities
# << macros

Summary:    Plasma 5 workspace applications and applets
Version:    5.1.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source1:    kde.pam
Source100:  plasma-workspace.yaml
Source101:  plasma-workspace-rpmlintrc
Patch0:     0001-Don-t-override-default-font-configuration.patch
Patch1:     0002-Show-activities-action-only-when-the-service-is-runn.patch
Patch2:     0003-Fix-interactive-console-build-when-KF5TextEditor-is-.patch
Patch3:     0004-Rename-InteractiveConsoleItem-to-InteractiveConsoleW.patch
Requires:   kf5-filesystem
Requires:   kinit
Requires:   kded
Requires:   kdoctools
Requires:   qt5-qtquickcontrols
Requires:   qt5-qttools-paths
Requires:   qt5-qttools-qdbus
Requires:   coreutils
Requires:   dbus-x11
Requires:   xorg-x11-apps
Requires:   xorg-x11-utils
Requires:   xorg-x11-server-utils
Requires:   socat
Requires:   systemd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-screensaver)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xevie)
BuildRequires:  pkgconfig(xcb-xf86dri)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xprint)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-xv)
BuildRequires:  pkgconfig(xcb-xvmc)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  libGL-devel
BuildRequires:  boost-devel
BuildRequires:  pam-devel
BuildRequires:  phonon-qt5-devel
BuildRequires:  plasma-devel
BuildRequires:  kdoctools-devel
BuildRequires:  krunner-devel
BuildRequires:  kjsembed-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kdesu-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kwallet-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kidletime-devel
BuildRequires:  threadweaver-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  plasma-devel
BuildRequires:  kdewebkit-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  baloo-devel
BuildRequires:  libksysguard-devel
BuildRequires:  libkscreen-devel
BuildRequires:  kwin-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

%description
Plasma 5 libraries and runtime components.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%package shell
Summary:    Plasma shell autostart entry
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description shell
Autostart entry that brings the Plasma desktop up.


%package lookandfeel
Summary:    Plasma look and feel
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description lookandfeel
Plasma look and feel.


%package plasmoids
Summary:    Widgets for Plasma
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description plasmoids
Widgets for Plasma.


%package wallpaper-color
Summary:    Color wallpaper plugin for Plasma
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description wallpaper-color
Color wallpaper plugins for Plasma.


%package wallpaper-image
Summary:    Image wallpaper plugin for Plasma
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description wallpaper-image
Image wallpaper plugin for Plasma.


%package wallpaper-slideshow
Summary:    Slideshow wallpaper plugin for Plasma
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description wallpaper-slideshow
Slideshow wallpaper plugin for Plasma.


%package session
Summary:    Plasma session entry
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-shell = %{version}-%{release}

%description session
Plasma session entry for display managers.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%package -n sddm-theme-breeze
Summary:    SDDM "Breeze" theme
Group:      System/GUI/Other
BuildArch:  noarch
Requires:   sddm
Requires:   oxygen-icon-theme

%description -n sddm-theme-breeze
This package contains the "Breeze" theme for SDDM.


%prep
%setup -q -n %{name}-%{version}

# 0001-Don-t-override-default-font-configuration.patch
%patch0 -p1
# 0002-Show-activities-action-only-when-the-service-is-runn.patch
%patch1 -p1
# 0003-Fix-interactive-console-build-when-KF5TextEditor-is-.patch
%patch2 -p1
# 0004-Rename-InteractiveConsoleItem-to-InteractiveConsoleW.patch
%patch3 -p1
# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
mkdir -p %{buildroot}%{_kf5_sysconfdir}/profile.d
cat > %{buildroot}%{_kf5_sysconfdir}/profile.d/plasma5.sh <<EOF
export LIBEXEC_PATH="%{_libexecdir}:%{_libdir}/libexec:%{_kf5_libexecdir}"
EOF

chrpath --delete %{buildroot}%{_kf5_plugindir}/phonon_platform/kde.so

# Makes kcheckpass work
install -m455 -p -D %{SOURCE1} %{buildroot}%{_kf5_sysconfdir}/pam.d/kde

%if !%{with plasma-activities}
# Remove activities stuff
rm -f %{buildroot}%{_kf5_servicesdir}/plasma-runner-activityrunner.desktop
rm -f %{buildroot}%{_qt5_plugindir}/krunner_activities.so
rm -f %{buildroot}%{_qt5_plugindir}/plasma/dataengine/plasma_engine_activities.so
rm -f %{buildroot}%{_qt5_plugindir}/plasma_containmentactions_switchactivity.so
rm -f %{buildroot}%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.activitybar.desktop
rm -f %{buildroot}%{_kf5_servicesdir}/plasma-containmentactions-switchactivity.desktop
rm -f %{buildroot}%{_kf5_servicesdir}/plasma-engine-activities.desktop
rm -f %{buildroot}%{_kf5_servicesdir}/plasma-runner-activityrunner.desktop
%endif
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%dir %{_kf5_sharedir}/plasma/plasmoids
%dir %{_kf5_sharedir}/plasma/services
%dir %{_kf5_sharedir}/plasma/shareprovider
%dir %{_kf5_sharedir}/plasma/wallpapers
%dir %{_kf5_sharedir}/plasma/look-and-feel
%{_kf5_sysconfdir}/profile.d/plasma5.sh
%{_kf5_bindir}/*
%{_kf5_libdir}/*.so.*
%{_kf5_libdir}/libkdeinit5_*.so
%{_kf5_plugindir}/*
%{_kf5_qmldir}/org/kde/*
%exclude %{_kf5_qmldir}/org/kde/plasma/wallpapers/*
%{_kf5_libdir}/libexec/*
%{_kf5_sharedir}/ksmserver
%{_kf5_sharedir}/ksplash
%{_kf5_sharedir}/plasma/services/*
%{_kf5_sharedir}/plasma/shareprovider/*
%{_kf5_sharedir}/solid
%{_kf5_sharedir}/kstyle
%{_kf5_sharedir}/drkonqi/debuggers/external/*
%{_kf5_sharedir}/drkonqi/debuggers/internal/*
%{_kf5_sharedir}/drkonqi/mappings
%{_kf5_sharedir}/drkonqi/pics/*.png
%{_kf5_configdir}/*.knsrc
%{_kf5_configdir}/autostart/*.desktop
%exclude %{_kf5_configdir}/autostart/plasmashell.desktop
%{_kf5_sysconfdir}/pam.d/kde
%{_kf5_servicesdir}/*
%exclude %{_kf5_servicesdir}/plasma-wallpaper-*
%{_kf5_servicetypesdir}/*
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/applications/*.desktop
%{_datadir}/config.kcfg
%{_kf5_sharedir}/plasma/kcms/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/libplasma-geolocation-interface.so
%{_includedir}/*
%{_kf5_cmakedir}/KRunnerAppDBusInterface
%{_kf5_cmakedir}/KSMServerDBusInterface
%{_kf5_cmakedir}/LibKWorkspace
%{_kf5_cmakedir}/LibTaskManager
%{_kf5_cmakedir}/ScreenSaverDBusInterface
%{_kf5_dbusinterfacesdir}/*.xml
# >> files devel
# << files devel

%files shell
%defattr(-,root,root,-)
%{_kf5_configdir}/autostart/plasmashell.desktop
# >> files shell
# << files shell

%files lookandfeel
%defattr(-,root,root,-)
%{_kf5_sharedir}/plasma/look-and-feel/*
# >> files lookandfeel
# << files lookandfeel

%files plasmoids
%defattr(-,root,root,-)
%{_kf5_sharedir}/plasma/plasmoids/*
# >> files plasmoids
# << files plasmoids

%files wallpaper-color
%defattr(-,root,root,-)
%dir %{_kf5_sharedir}/plasma/wallpapers/org.kde.color
%{_kf5_sharedir}/plasma/wallpapers/org.kde.color/*
%{_kf5_servicesdir}/plasma-wallpaper-org.kde.color.desktop
# >> files wallpaper-color
# << files wallpaper-color

%files wallpaper-image
%defattr(-,root,root,-)
%dir %{_kf5_sharedir}/plasma/wallpapers/org.kde.image
%{_kf5_sharedir}/plasma/wallpapers/org.kde.image/*
%{_kf5_qmldir}/org/kde/plasma/wallpapers/*
%{_kf5_servicesdir}/plasma-wallpaper-org.kde.image.desktop
# >> files wallpaper-image
# << files wallpaper-image

%files wallpaper-slideshow
%defattr(-,root,root,-)
%dir %{_kf5_sharedir}/plasma/wallpapers/org.kde.slideshow
%{_kf5_sharedir}/plasma/wallpapers/org.kde.slideshow/*
%{_kf5_servicesdir}/plasma-wallpaper-org.kde.slideshow.desktop
# >> files wallpaper-slideshow
# << files wallpaper-slideshow

%files session
%defattr(-,root,root,-)
%{_datadir}/xsessions/plasma.desktop
# >> files session
# << files session

%files doc
%defattr(-,root,root,-)
%{_kf5_htmldir}/en/*
# >> files doc
# << files doc

%files -n sddm-theme-breeze
%defattr(-,root,root,-)
%{_datadir}/sddm/themes/breeze
# >> files sddm-theme-breeze
# << files sddm-theme-breeze
