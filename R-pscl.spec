%global packname  pscl
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.04.1
Release:          1
Summary:          Political Science Computational Laboratory, Stanford University
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-MASS R-stats R-mvtnorm R-coda R-gam R-vcd 
Requires:         R-lattice 
Requires:         R-MCMCpack R-car R-lmtest R-sandwich R-zoo 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-stats R-mvtnorm R-coda R-gam R-vcd
BuildRequires:    R-lattice 
BuildRequires:    R-MCMCpack R-car R-lmtest R-sandwich R-zoo 
BuildRequires:    blas-devel
BuildRequires:    lapack-devel

%description
Bayesian analysis of item-response theory (IRT) models, roll call
analysis; computing highest density regions; maximum likelihood estimation
of zero-inflated and hurdle models for count data; goodness-of-fit
measures for GLMs; data sets used in writing and teaching at the Political
Science Computational Laboratory; seats-votes curves.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
