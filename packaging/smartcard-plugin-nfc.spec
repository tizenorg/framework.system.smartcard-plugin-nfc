Name:             smartcard-plugin-nfc
Summary:          Smartcard plugin nfc
Version:          0.0.12
Release:          0
Group:            libs
License:          Apache License, Version 2.0
Source0:          %{name}-%{version}.tar.gz
BuildRequires:    cmake
BuildRequires:    pkgconfig(glib-2.0)
BuildRequires:    pkgconfig(dlog)
BuildRequires:    pkgconfig(smartcard-service-common)
BuildRequires:    pkgconfig(capi-network-nfc)
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Smartcard Service plugin nfc


%prep
%setup -q


%package    devel
Summary:    smartcard service nfc
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}


%description devel
smartcard service.


%build
%if 0%{?sec_build_binary_debug_enable}
export CFLAGS="$CFLAGS -DTIZEN_DEBUG_ENABLE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_DEBUG_ENABLE"
export FFLAGS="$FFLAGS -DTIZEN_DEBUG_ENABLE"
%endif
mkdir obj-arm-limux-qnueabi
cd obj-arm-limux-qnueabi
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix}
#make %{?jobs:-j%jobs}


%install
cd obj-arm-limux-qnueabi
%make_install
mkdir -p %{buildroot}/usr/share/license
cp -af %{_builddir}/%{name}-%{version}/packaging/%{name} %{buildroot}/usr/share/license/


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/se/lib*.so
%{_datadir}/license/%{name}
