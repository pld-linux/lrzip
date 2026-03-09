# Conditional build:
%bcond_without	asm	# native Assembly code (x86/x86_64)
%bcond_without	tests	# build without tests

%ifnarch %{ix86} %{x8664}
%undefine	with_asm
%endif

Summary:	Long Range ZIP or Lzma RZIP
Summary(pl.UTF-8):	Long Range ZIP lub Lzma RZIP
Name:		lrzip
Version:	0.660
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	https://github.com/ckolivas/lrzip/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b4163b9bb9ed03d5cb858cdbe465f793
URL:		https://github.com/ckolivas/lrzip
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lz4-devel
BuildRequires:	lzo-devel >= 2.02
%{?with_asm:BuildRequires:	nasm}
BuildRequires:	perl-tools-pod
BuildRequires:	zlib-devel
Provides:	bundled(zpaq)
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static-bin \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README.md README-NOT-BACKWARD-COMPATIBLE TODO WHATS-NEW
%doc doc/magic.header.txt doc/lrzip.conf.example doc/README.lzo_compresses.test.txt doc/README.benchmarks doc/README.Assembler
%doc lzma/7zC.txt lzma/7zFormat.txt lzma/Methods.txt lzma/README lzma/README-Alloc lzma/history.txt lzma/lzma.txt
%attr(755,root,root) %{_bindir}/lrunzip
%attr(755,root,root) %{_bindir}/lrz
%attr(755,root,root) %{_bindir}/lrzcat
%attr(755,root,root) %{_bindir}/lrzip
%attr(755,root,root) %{_bindir}/lrztar
%attr(755,root,root) %{_bindir}/lrzuntar
%{_mandir}/man1/lrunzip.1*
%{_mandir}/man1/lrz.1*
%{_mandir}/man1/lrzcat.1*
%{_mandir}/man1/lrzip.1*
%{_mandir}/man1/lrztar.1*
%{_mandir}/man1/lrzuntar.1*
%{_mandir}/man5/lrzip.conf.5*
