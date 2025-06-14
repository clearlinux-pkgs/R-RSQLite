#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v27
# autospec commit: 65cf152
#
Name     : R-RSQLite
Version  : 2.4.1
Release  : 101
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/RSQLite_2.4.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/RSQLite_2.4.1.tar.gz
Summary  : SQLite Interface for R
Group    : Development/Tools
License  : LGPL-2.1+
Requires: R-RSQLite-lib = %{version}-%{release}
Requires: R-DBI
Requires: R-bit64
Requires: R-blob
Requires: R-cpp11
Requires: R-memoise
Requires: R-pkgconfig
Requires: R-plogr
Requires: R-rlang
BuildRequires : R-DBI
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-cpp11
BuildRequires : R-memoise
BuildRequires : R-pkgconfig
BuildRequires : R-plogr
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
interface compliant with the DBI package. The source for the SQLite
    engine and for various extensions in a recent version is included.
    System libraries will never be consulted because this package relies
    on static linking for the plugins it includes; this also ensures a
    consistent experience across all installations.

%package lib
Summary: lib components for the R-RSQLite package.
Group: Libraries

%description lib
lib components for the R-RSQLite package.


%prep
%setup -q -n RSQLite
pushd ..
cp -a RSQLite buildavx2
popd
pushd ..
cp -a RSQLite buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749574377

%install
export SOURCE_DATE_EPOCH=1749574377
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/RSQLite/tests/testthat/helper-reexport.R
/usr/lib64/R/library/RSQLite/tests/testthat/helper-tibble.R
/usr/lib64/R/library/RSQLite/tests/testthat/setup.R
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
/usr/lib64/R/library/RSQLite/tests/testthat/test-uuid.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/RSQLite/libs/RSQLite.so
/V4/usr/lib64/R/library/RSQLite/libs/RSQLite.so
/usr/lib64/R/library/RSQLite/libs/RSQLite.so
