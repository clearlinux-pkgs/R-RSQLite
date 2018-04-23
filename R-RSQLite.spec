#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RSQLite
Version  : 2.1.0
Release  : 6
URL      : https://cran.r-project.org/src/contrib/RSQLite_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RSQLite_2.1.0.tar.gz
Summary  : 'SQLite' Interface for R
Group    : Development/Tools
License  : LGPL-2.0+
Requires: R-RSQLite-lib
Requires: R-BH
Requires: R-DBI
Requires: R-Rcpp
Requires: R-bit64
Requires: R-blob
Requires: R-memoise
Requires: R-pkgconfig
Requires: R-plogr
BuildRequires : R-BH
BuildRequires : R-DBI
BuildRequires : R-Rcpp
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-memoise
BuildRequires : R-pkgconfig
BuildRequires : R-plogr
BuildRequires : clr-R-helpers

%description
provides an interface compliant with the 'DBI' package. The
    source for the 'SQLite' engine is included.

%package lib
Summary: lib components for the R-RSQLite package.
Group: Libraries

%description lib
lib components for the R-RSQLite package.


%prep
%setup -q -c -n RSQLite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522687694

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522687694
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RSQLite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RSQLite
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RSQLite
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library RSQLite|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RSQLite/DESCRIPTION
/usr/lib64/R/library/RSQLite/INDEX
/usr/lib64/R/library/RSQLite/Meta/Rd.rds
/usr/lib64/R/library/RSQLite/Meta/features.rds
/usr/lib64/R/library/RSQLite/Meta/hsearch.rds
/usr/lib64/R/library/RSQLite/Meta/links.rds
/usr/lib64/R/library/RSQLite/Meta/nsInfo.rds
/usr/lib64/R/library/RSQLite/Meta/package.rds
/usr/lib64/R/library/RSQLite/Meta/vignette.rds
/usr/lib64/R/library/RSQLite/NAMESPACE
/usr/lib64/R/library/RSQLite/NEWS.md
/usr/lib64/R/library/RSQLite/R/RSQLite
/usr/lib64/R/library/RSQLite/R/RSQLite.rdb
/usr/lib64/R/library/RSQLite/R/RSQLite.rdx
/usr/lib64/R/library/RSQLite/db/datasets.sqlite
/usr/lib64/R/library/RSQLite/doc/RSQLite.R
/usr/lib64/R/library/RSQLite/doc/RSQLite.Rmd
/usr/lib64/R/library/RSQLite/doc/RSQLite.html
/usr/lib64/R/library/RSQLite/doc/index.html
/usr/lib64/R/library/RSQLite/help/AnIndex
/usr/lib64/R/library/RSQLite/help/RSQLite.rdb
/usr/lib64/R/library/RSQLite/help/RSQLite.rdx
/usr/lib64/R/library/RSQLite/help/aliases.rds
/usr/lib64/R/library/RSQLite/help/paths.rds
/usr/lib64/R/library/RSQLite/html/00Index.html
/usr/lib64/R/library/RSQLite/html/R.css
/usr/lib64/R/library/RSQLite/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RSQLite/libs/RSQLite.so
/usr/lib64/R/library/RSQLite/libs/RSQLite.so.avx2
/usr/lib64/R/library/RSQLite/libs/RSQLite.so.avx512
