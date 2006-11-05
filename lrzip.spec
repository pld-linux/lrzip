Summary:	Long Range ZIP or Lzma RZIP
Summary(pl):	Long Range ZIP lub Lzma RZIP
Name:		lrzip
Version:	0.16
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
# Source0-md5:	d4371cd6b32398e95fb7ed704addf361
Patch0:		%{name}-lzma.patch
URL:		http://ck.kolivas.org/apps/lrzip/
BuildRequires:	bzip2-devel
BuildRequires:	lzma-devel >= 4.43-5
BuildRequires:	lzo-devel >= 2.02-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a compression program optimised for large files. The larger
the file and the more memory you have, the better the compression
advantage this will provide, especially once the files are larger than
100MB. The advantage can be chosen to be either size (much smaller
than bzip2) or speed (much faster than bzip2). Decompression is much
always faster than bzip2.

%description -l pl
LRZIP to program kompresuj±cy zoptymalizowany dla du¿ych plików. Im
wiêkszy jest plik i im wiêcej jest dostêpnej pamiêci, tym lepsz±
kompresjê mo¿na uzyskaæ, zw³aszcza dla plików wiêkszych ni¿ 100MB.
Mo¿na wybraæ kompresjê bardziej korzystn± pod wzglêdem rozmiaru (du¿o
mniejszy ni¿ bzip2) lub szybko¶ci (du¿o szybszy ni¿ bzip2).
Dekompresja jest zawsze du¿o szybsza ni¿ bzip2.

%prep
%setup -q
%{!?debug:rm -rf lzma}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/lrzip
%{_mandir}/man1/lrzip.1*
