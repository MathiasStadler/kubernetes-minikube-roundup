# code extension via cli

## list installed plugins

```bash
> /usr/local/bin/code --list-extensions
```

## install extensions

```bash
> code --install-extension {extension id}
```

## uninstall extensions

```bash
> code --uninstall-extension {extension id}
```

## save and export extension to another vscode installation

- [from here](https://stackoverflow.com/questions/35773299/how-can-you-export-vs-code-extension-list) all credits goes to [Benny](https://stackoverflow.com/users/2243665/benny)

```bash
> code --list-extensions | xargs -L 1 echo code --install-extension
code --install-extension eamodio.gitlens
code --install-extension eg2.tslint
code --install-extension eg2.vscode-npm-script
code --install-extension msjsdiag.debugger-for-chrome
code --install-extension redhat.vscode-yaml
code --install-extension steoates.autoimport
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension wix.vscode-import-cost

> code --list-extensions | xargs -L 1 echo code --install-extension > vscode-extension-install.sh
```

- copy the script to another instance and install all extension at all

## reload plugins via cli

```bash
> code --install-extension timonwong.shellcheck
```
