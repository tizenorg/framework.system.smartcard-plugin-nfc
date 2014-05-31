Name:             smartcard-plugin-nfc
Summary:          Smartcard plugin nfc
Version:          0.0.3
Release:          0
Group:            libs
License:          Apache License, Version 2.0
Source0:          %{name}-%{version}.tar.gz
BuildRequires:    pkgconfig(glib-2.0)
BuildRequires:    pkgconfig(dlog)
BuildRequires:    pkgconfig(nfc)
BuildRequires:    pkgconfig(smartcard-service-common)
BuildRequires:    cmake
BuildRequires:    gettext-tools
Requires(post):   /sbin/ldconfig
Requires(post):   /usr/bin/vconftool
requires(postun): /sbin/ldconfig
%description
Smartcard Service plugin nfc

%prep
%setup -q


%package    devel
Summary:    smartcard service
Group:      Development/Libraries
Requires:   %{name} = %{version}

%description devel
smartcard service.


%build
%cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
#make %{?jobs:-j%jobs}


%install
mkdir -p %{buildroot}/usr/share/license
cp -af LICENSE.APLv2 %{buildroot}/usr/share/license/%{name}

%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest smartcard-plugin-nfc.manifest
%defattr(-,root,root,-)
/usr/lib/se/lib*.so
/usr/share/license/%{name}