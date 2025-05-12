%global debug_package %{nil}
%define ver %(curl -s https://api.github.com/repos/starship/starship/releases/latest | grep tag_name | sed -E 's/.*v(.*?)".*/\1/')

Name:    starship
Version: %{ver}
Release: %autorelease
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell!
License: ISC License
URL:     https://github.com/starship/%{name}
Source:  https://github.com/starship/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!
- Fast: it's fast – really really fast! 🚀
- Customizable: configure every aspect of your prompt.
- Universal: works on any shell, on any operating system.
- Intelligent: shows relevant information at a glance.
- Feature rich: support for all your favorite tools.
- Easy: quick to install – start using it in minutes.

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

%files
%license LICENSE LICENSE.summary LICENSE.dependencies
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
%autochangelog
