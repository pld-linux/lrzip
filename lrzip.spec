Summary:	Long Range ZIP or Lzma RZIP
Name:		lrzip
Version:	0.16
Release:	0.2
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
# Source0-md5:	d4371cd6b32398e95fb7ed704addf361
#Patch0:	%{name}-lzolib.patch
#Patch2:	%{name}-lzma.patch
URL:		http://ck.kolivas.org/apps/lrzip/
BuildRequires:	bzip2-devel
#BuildRequires:	lzma-devel >= 4.43-2
BuildRequires:	lzo-devel >= 2.02-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a compression program optimised for large files. The larger
the file and the more memory you have, the better the compression
advantage this will provide, especially once the files are larger than
100MB. The advantage can be chosen to be either size (much smaller
than bzip2) or speed (much faster than bzip2). Decompression is much
always faster than bzip2.

%prep
%setup -q
#patch0 -p1
#patch2 -p1

# local copy has some changes. TODO: patch our lzma
#%{!?debug:rm -rf lzma} # lzma 4.43

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
