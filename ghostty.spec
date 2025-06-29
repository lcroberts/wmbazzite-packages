%global debug_package %{nil}
%define ver %(curl -s https://api.github.com/repos/ghostty-org/ghostty/git/refs/tags | grep '"ref"' | cut -d '"' -f4 | cut -d '/' -f3 | cut -d 'v' -f2 | sort -V | tail -n 2 | head -n 1)
%define tip %(curl -s https://api.github.com/repos/ghostty-org/ghostty/git/refs/tags | grep "sha" | head -n 1 | cut -d '"' -f4)

Name:    ghostty
Version: %{ver}+%{tip}
Release: %autorelease
Summary:  Fast, native, feature-rich terminal emulator pushing modern features.
License: MIT
URL:     https://github.com/ghostty-org/%{name}
# Source0:  https://github.com/ghostty-org/%{name}/archive/refs/tags/v%{version}.tar.gz
Source0:  https://github.com/ghostty-org/%{name}/archive/refs/tags/tip.tar.gz

BuildRequires: gtk4-devel
BuildRequires: zig
BuildRequires: libadwaita-devel
BuildRequires: blueprint-compiler
BuildRequires: gettext

%description
Ghostty is a terminal emulator that differentiates itself by being fast,
feature-rich, and native. While there are many excellent terminal emulators
available, they all force you to choose between speed, features, or native UIs.
Ghostty provides all three.

%prep
%autosetup -n %{name}-tip

%build
ZIG_GLOBAL_CACHE_DIR=/tmp/offline-cache ./nix/build-support/fetch-zig-cache.sh
zig build \
    --summary all \
    --prefix "%{buildroot}%{_prefix}" \
    --system /tmp/offline-cache/p \
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
%{_prefix}/share/dbus-1/services/com.mitchellh.ghostty.service
%{_prefix}/share/locale/ca_ES.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/de_DE.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/es_BO.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/fr_FR.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/id_ID.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/ja_JP.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/mk_MK.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/nb_NO.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/nl_NL.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/pl_PL.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/pt_BR.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/ru_RU.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/tr_TR.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/uk_UA.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/locale/zh_CN.UTF-8/LC_MESSAGES/com.mitchellh.ghostty.mo
%{_prefix}/share/metainfo/com.mitchellh.ghostty.metainfo.xml
%{_prefix}/share/systemd/user/com.mitchellh.ghostty.service

%changelog
%autochangelog
