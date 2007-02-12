Summary:	Long Range ZIP or Lzma RZIP
Summary(pl.UTF-8):	Long Range ZIP lub Lzma RZIP
Name:		lrzip
Version:	0.18
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
# Source0-md5:	285c995f6d861c4125f6164ab0ab2368
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

%description -l pl.UTF-8
LRZIP to program kompresujący zoptymalizowany dla dużych plików. Im
większy jest plik i im więcej jest dostępnej pamięci, tym lepszą
kompresję można uzyskać, zwłaszcza dla plików większych niż 100MB.
Można wybrać kompresję bardziej korzystną pod względem rozmiaru (dużo
mniejszy niż bzip2) lub szybkości (dużo szybszy niż bzip2).
Dekompresja jest zawsze dużo szybsza niż bzip2.

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
