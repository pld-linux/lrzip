# TODO
# - lrzip should link to shared lrzip library
#
# Conditional build:
%bcond_with	system_lzma	# use system lzma instead of internal
%bcond_without	asm	# Enable native Assembly code (ia32 only)
%bcond_without	jit	# JIT in bundled libzpaq
%bcond_without	tests		# build without tests

%ifnarch %{ix86} %{x8664}
%undefine	with_jit
%endif

%ifnarch %{ix86}
%undefine	with_asm
%endif

Summary:	Long Range ZIP or Lzma RZIP
Summary(pl.UTF-8):	Long Range ZIP lub Lzma RZIP
Name:		lrzip
Version:	0.621
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
# Source0-md5:	53a12cc4d19aa030d0ab7f0a21db2cfe
Patch0:		%{name}-lzma.patch
URL:		http://ck.kolivas.org/apps/lrzip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
%{?with_system_lzma:BuildRequires:	lzma-devel >= 4.43-5}
BuildRequires:	lzo-devel >= 2.02-1
%{?with_asm:BuildRequires:	nasm}
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a compression program optimised for large files. The larger
the file and the more memory you have, the better the compression
advantage this will provide, especially once the files are larger than
100MB. The advantage can be chosen to be either size (much smaller
than bzip2) or speed (much faster than bzip2). Decompression is much
always faster than bzip2.

%description -l pl.UTF-8
LRZIP to program kompresujący zoptymalizowany dla dużych plików. Im
większy jest plik i im więcej jest dostępnej pamięci, tym lepszą
kompresję można uzyskać, zwłaszcza dla plików większych niż 100MB.
Można wybrać kompresję bardziej korzystną pod względem rozmiaru (dużo
mniejszy niż bzip2) lub szybkości (dużo szybszy niż bzip2).
Dekompresja jest zawsze dużo szybsza niż bzip2.

%package libs
Summary:	Libraries for decoding LZMA compression
License:	LGPL v2+

%description    libs
Libraries for decoding LZMA compression.

%package devel
Summary:	Devel libraries & headers for liblzmadec
License:	LGPL v2+
Requires:	%{name}-libs = %{version}-%{release}

%description    devel
Devel libraries & headers for liblzmadec.

%prep
%setup -q
%if %{with system_lzma}
rm -rf lzma
%patch0 -p1
%endif

%build
%{__aclocal} -I m4
%{__autoconf}
%{!?with_jit:CPPFLAGS="%{rpmcppflags} -DNOJIT"}
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-static-bin \
	--enable-shared \
	%{__enable_disable asm}
%{__make}

%if %{with tests}
./lrzip -z COPYING
./lrzip --info COPYING.lrz
./lrzip -d -o COPYING.new COPYING.lrz
cmp COPYING COPYING.new
rm COPYING.new
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblrzip.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README* README-NOT-BACKWARD-COMPATIBLE TODO WHATS-NEW
%attr(755,root,root) %{_bindir}/lrunzip
%attr(755,root,root) %{_bindir}/lrzcat
%attr(755,root,root) %{_bindir}/lrzip
%attr(755,root,root) %{_bindir}/lrztar
%attr(755,root,root) %{_bindir}/lrzuntar
%{_mandir}/man1/lrunzip.1*
%{_mandir}/man1/lrzcat.1*
%{_mandir}/man1/lrzip.1*
%{_mandir}/man1/lrztar.1*
%{_mandir}/man1/lrzuntar.1*
%{_mandir}/man5/lrzip.conf.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblrzip.so.*.*.*
%ghost %{_libdir}/liblrzip.so.0

%files devel
%defattr(644,root,root,755)
%doc lzma/7zC.txt lzma/7zFormat.txt lzma/Methods.txt lzma/README lzma/README-Alloc lzma/history.txt lzma/lzma.txt
%doc doc/magic.header.txt doc/lrzip.conf.example doc/README.lzo_compresses.test.txt doc/README.benchmarks
%{_includedir}/Lrzip.h
%{_libdir}/liblrzip.so
%{_pkgconfigdir}/lrzip.pc
