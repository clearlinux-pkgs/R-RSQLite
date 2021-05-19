#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RSQLite
Version  : 2.2.7
Release  : 55
URL      : https://cran.r-project.org/src/contrib/RSQLite_2.2.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RSQLite_2.2.7.tar.gz
Summary  : 'SQLite' Interface for R
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-RSQLite-lib = %{version}-%{release}
Requires: R-DBI
Requires: R-Rcpp
Requires: R-bit64
Requires: R-blob
Requires: R-memoise
Requires: R-pkgconfig
Requires: R-plogr
BuildRequires : R-DBI
BuildRequires : R-Rcpp
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-memoise
BuildRequires : R-pkgconfig
BuildRequires : R-plogr
BuildRequires : buildreq-R

%description
provides an interface compliant with the 'DBI' package. The source for
    the 'SQLite' engine is included.

%package lib
Summary: lib components for the R-RSQLite package.
Group: Libraries

%description lib
lib components for the R-RSQLite package.


%prep
%setup -q -c -n RSQLite
cd %{_builddir}/RSQLite

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619145615

%install
export SOURCE_DATE_EPOCH=1619145615
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RSQLite || :


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
/usr/lib64/R/library/RSQLite/WORDLIST
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
/usr/lib64/R/library/RSQLite/tests/testthat.R
/usr/lib64/R/library/RSQLite/tests/testthat/dat-n.txt
/usr/lib64/R/library/RSQLite/tests/testthat/dat-rn.txt
/usr/lib64/R/library/RSQLite/tests/testthat/helper-DBItest.R
/usr/lib64/R/library/RSQLite/tests/testthat/helper-astyle.R
/usr/lib64/R/library/RSQLite/tests/testthat/helper-memdb.R
/usr/lib64/R/library/RSQLite/tests/testthat/helper-tibble.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-DBItest.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-affinity.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-astyle.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-basic-types.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-blob.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-column-info.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-data-type.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-dbClearResult.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-dbConnect.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-dbSendQuery.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-dbWriteTable.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-dbWriteTableAutoincrement.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-encoding.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-error.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-exception.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-extendedTypes.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-field-types.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-json.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-readonly.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-regularExpressions.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-sd.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-sqliteCopyDatabase.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-sqliteQuickColumn.R
/usr/lib64/R/library/RSQLite/tests/testthat/test-transactions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RSQLite/libs/RSQLite.so
/usr/lib64/R/library/RSQLite/libs/RSQLite.so.avx2
/usr/lib64/R/library/RSQLite/libs/RSQLite.so.avx512
