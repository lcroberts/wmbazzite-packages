%global debug_package %{nil}
%define ver %(curl -s https://api.github.com/repos/ghostty-org/ghostty/git/refs/tags | grep '"ref"' | tail -n 1 | cut -d '"' -f4 | cut -d '/' -f3 | cut -d 'v' -f2)

Name:    ghostty
Version: %{ver}
Release: %autorelease
Summary:  Fast, native, feature-rich terminal emulator pushing modern features.
License: MIT
URL:     https://github.com/ghostty-org/%{name}
Source0:  https://github.com/ghostty-org/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib2-devel
BuildRequires: gtk4-devel
BuildRequires: harfbuzz-devel
BuildRequires: libadwaita-devel
BuildRequires: libpng-devel
BuildRequires: oniguruma-devel
BuildRequires: pandoc-cli
BuildRequires: pixman-devel
BuildRequires: pkg-config
BuildRequires: zig
BuildRequires: zlib-ng-devel


Requires: fontconfig
Requires: freetype
Requires: glib2
Requires: gtk4
Requires: harfbuzz
Requires: libadwaita
Requires: libpng
Requires: oniguruma
Requires: pixman
Requires: zlib-ng
Requires: ncurses-term

%description
Ghostty is a terminal emulator that differentiates itself by being fast,
feature-rich, and native. While there are many excellent terminal emulators
available, they all force you to choose between speed, features, or native UIs.
Ghostty provides all three.

%prep
%autosetup -n %{name}-%{version}

%build
ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache ./nix/build-support/fetch-zig-cache.sh
zig build \
    --summary all \
    --prefix "%{buildroot}%{_prefix}" \
    --system "/tmp/offline-cache/p" \
    -Dversion-string=%{version}-%{release} \
    -Doptimize=ReleaseFast \
    -Dcpu=baseline \
    -Dpie=true \
    -Demit-docs
rm %{buildroot}%{_prefix}/share/terminfo/g/ghostty

%files
%license LICENSE
%{_bindir}/ghostty
%{_prefix}/share/applications/com.mitchellh.ghostty.desktop
%{_prefix}/share/bash-completion/completions/ghostty.bash
%{_prefix}/share/bat/syntaxes/ghostty.sublime-syntax
%{_prefix}/share/fish/vendor_completions.d/ghostty.fish
%{_prefix}/share/ghostty
%{_prefix}/share/icons/hicolor/1024x1024/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/128x128/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/128x128@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/16x16/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/16x16@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/256x256/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/256x256@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/32x32/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/32x32@2/apps/com.mitchellh.ghostty.png
%{_prefix}/share/icons/hicolor/512x512/apps/com.mitchellh.ghostty.png
%{_prefix}/share/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_prefix}/share/man/man1/ghostty.1
%{_prefix}/share/man/man5/ghostty.5
%{_prefix}/share/nautilus-python/extensions/ghostty.py
%{_prefix}/share/nvim/site/compiler/ghostty.vim
%{_prefix}/share/nvim/site/ftdetect/ghostty.vim
%{_prefix}/share/nvim/site/ftplugin/ghostty.vim
%{_prefix}/share/nvim/site/syntax/ghostty.vim
%{_prefix}/share/terminfo/x/xterm-ghostty
%{_prefix}/share/vim/vimfiles/compiler/ghostty.vim
%{_prefix}/share/vim/vimfiles/ftdetect/ghostty.vim
%{_prefix}/share/vim/vimfiles/ftplugin/ghostty.vim
%{_prefix}/share/vim/vimfiles/syntax/ghostty.vim
%{_prefix}/share/zsh/site-functions/_ghostty

%changelog
%autochangelog
