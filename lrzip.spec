#
# Conditional build:
%bcond_with	system_lzma	# use system lzma instead of internal
#
Summary:	Long Range ZIP or Lzma RZIP
Summary(pl.UTF-8):	Long Range ZIP lub Lzma RZIP
Name:		lrzip
Version:	0.570
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
# Source0-md5:	644d28896d78ffaca88ea59bb8e72053
Patch0:		%{name}-lzma.patch
URL:		http://ck.kolivas.org/apps/lrzip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
%{?with_system_lzma:BuildRequires:	lzma-devel >= 4.43-5}
BuildRequires:	lzo-devel >= 2.02-1
BuildRequires:	nasm
BuildRequires:	perl-tools-pod
BuildRequires:	zlib-devel
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
%if %{with system_lzma}
rm -rf lzma
%patch0 -p1
%endif

%build
%{__aclocal}
%{__autoconf}
%configure \
	--enable-asm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%doc AUTHORS BUGS ChangeLog README README-NOT-BACKWARD-COMPATIBLE TODO WHATS-NEW
%doc lzma/7zC.txt lzma/7zFormat.txt lzma/Methods.txt lzma/README lzma/README-Alloc lzma/history.txt lzma/lzma.txt
%doc doc/magic.header.txt doc/lrzip.conf.example doc/README.lzo_compresses.test.txt doc/README.benchmarks
%attr(755,root,root) %{_bindir}/lrunzip
%attr(755,root,root) %{_bindir}/lrzip
%attr(755,root,root) %{_bindir}/lrztar
%attr(755,root,root) %{_bindir}/lrzuntar
%{_mandir}/man1/lrunzip.1*
%{_mandir}/man1/lrzip.1*
%{_mandir}/man1/lrztar.1*
%{_mandir}/man1/lrzuntar.1*
%{_mandir}/man5/lrzip.conf.5*
