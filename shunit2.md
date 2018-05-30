# [shunit2](https://github.com/kward/shunit2)

## install on mac

- [brew](https://brew.sh/index_de) should already installed

```bash
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```bash
> brew install shunit2
```

## TL;DR

```bash
brew uninstall shunit2
if !  which shunit2 >/dev/null; then
 echo "install shunit2";
 brew install shunit2 ;
fi
if !  which shunit2 >/dev/null; then
 echo "install shunit2 goes wrong";
 echo "Please check manually" ;
exit 1
fi
test_subfolder="tests_workdir"
script_name="equality_test.sh"
mkdir -p ${test_subfolder}
cat > ./${test_subfolder}/${script_name} << 'EOL'
#! /bin/sh
# file: examples/equality_test.sh
testDryRunShUnit2() {
  assertEquals 1 1
}
EOL
# flag execute
chmod +x ./${test_subfolder}/${script_name}
#run test
shunit2 ./${test_subfolder}/${script_name}
# delete test
rm -f ./${test_subfolder}/${script_name}
# delete test_subfolder only if empty
rmdir ./${test_subfolder}
```

> [silent command](https://medium.freecodecamp.org/sh-silence-your-bash-scripts-by-coding-your-own-silent-flag-c7e9f8b668a4)

## test with line numbers

```bash
test_subfolder="tests_workdir"
script_name="test_LineNumbers.sh"
mkdir -p ${test_subfolder}
cat > ./${test_subfolder}/${script_name} << 'EOL'
#! /bin/sh
# file: ${test_subfolder}/${script_name}
testLineNo() {
  # This assert will have line numbers included (e.g. "ASSERT:[123] ...") if
  # they are supported.
  echo "_ASSERT_EQUALS_ macro value: ${_ASSERT_EQUALS_}"
  ${_ASSERT_EQUALS_} '"not equal (you see LINE numbers)"' 1 2
  # This assert will not have line numbers included (e.g. "ASSERT: ...").
  assertEquals 'not equal (you see NO line numbers)' 1 2
}
EOL
# flag execute
chmod +x ./${test_subfolder}/${script_name}
#run test
shunit2 ./${test_subfolder}/${script_name}
# delete test
rm -f ./${test_subfolder}/${script_name}
# delete test_subfolder only if empty
rmdir ./${test_subfolder}
```