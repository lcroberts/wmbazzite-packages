%global debug_package %{nil}
%define ver %(curl -s https://api.github.com/repos/sxyazi/yazi/releases/latest | grep tag_name | cut -d '"' -f4 | cut -d 'v' -f2)

Name:    yazi
Version: %{ver}
Release: %autorelease
Summary: Blazing fast terminal file manager written in Rust, based on async I/O. 
License: MIT License
URL:     https://github.com/sxyazi/%{name}
Source:  https://github.com/sxyazi/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description
Blazing fast terminal file manager written in Rust, based on async I/O. 
- Full Asynchronous Support
- Powerful Async Task Scheduling and Management
- Built-in Support for Multiple Image Protocols
- Built-in Code Highlighting and Image Encoding

%prep
%autosetup -n %{name}-%{version}

%build
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked

# Generate license documentation
cargo tree --workspace --edges no-build,no-dev,no-proc-macro --no-dedupe --prefix none --format '{l}' | sort -u > LICENSE.summary
cargo tree --workspace --edges no-build,no-dev,no-proc-macro --no-dedupe --prefix none --format '{l}: {p}' | sort -u > LICENSE.dependencies

%install
install -Dpm 0755 target/release/%{name} -t %{buildroot}%{_bindir}/
install -Dpm 0755 target/release/ya -t %{buildroot}%{_bindir}/

%files
%license LICENSE LICENSE.summary LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_bindir}/ya

%changelog
%autochangelog
