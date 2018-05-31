#!/bin/sh
# vim:et:ft=sh:sts=2:sw=2
#
# as tempalate used I'm
# https://github.com/kward/shunit2/blob/master/examples/mkdir_test.sh
#
# Copyright 2008 Kate Ward. All Rights Reserved.
# Released under the LGPL (GNU Lesser General Public License)
#
# Author: kate.ward@forestent.com (Kate Ward)
#
# Example unit test for the mkdir command.
#
# There are times when an existing shell script needs to be tested. In this
# example, we will test several aspects of the the mkdir command, but the
# techniques could be used for any existing shell script.

_testLineNo() {
	# This assert will have line numbers included (e.g. "ASSERT:[123] ...") if
	# they are supported.
	echo "_ASSERT_EQUALS_ macro value: ${_ASSERT_EQUALS_}"
	${_ASSERT_EQUALS_} '"not equal (you see LINE numbers)"' 1 2
	# This assert will not have line numbers included (e.g. "ASSERT: ...").
	assertEquals 'not equal (you see NO line numbers)' 1 2
}

testMinikubeIsInstalledLocal() {

	${minikubeCmd} version >${stdoutF} 2>${stderrF}
	rtrn=$?

	assertTrue 'expecting return code of 0 (true)' ${rtrn}

}

testStartMinikube() {

	${minikubeCmd} start >${stdoutF} 2>${stderrF}
	rtrn=$?

	assertTrue 'expecting return code of 0 (true)' ${rtrn}

}

testStopMinikube() {

	${minikubeCmd} stop >${stdoutF} 2>${stderrF}
	rtrn=$?

	assertTrue 'expecting return code of 0 (true)' ${rtrn}
}

testDeleteMinikube() {

	${minikubeCmd} delete >${stdoutF} 2>${stderrF}
	rtrn=$?

	assertTrue 'expecting return code of 0 (true)' ${rtrn}
}

_testMissingDirectoryCreation() {

	${mkdirCmd} "${testDir}" >${stdoutF} 2>${stderrF}
	rtrn=$?

	assertFalse 'expecting return code of 1 (false)' ${rtrn}

	th_assertTrueWithNoOutput ${rtrn} "${stdoutF}" "${stderrF}"

	assertTrue 'directory missing' "[ -d '${testDir}' ]"

}

_testExistingDirectoryCreationFails() {
	# Create a directory to test against.
	${mkdirCmd} "${testDir}"

	# Test for expected failure while trying to create directory that exists.
	${mkdirCmd} "${testDir}" >${stdoutF} 2>${stderrF}
	rtrn=$?
	assertFalse 'expecting return code of 1 (false)' ${rtrn}
	assertNull 'unexpected output to stdout' "$(cat ${stdoutF})"
	assertNotNull 'expected error message to stderr' "$(cat ${stderrF})"

	assertTrue 'directory missing' "[ -d '${testDir}' ]"
}

_testRecursiveDirectoryCreation() {
	testDir2="${testDir}/test2"

	${mkdirCmd} -p "${testDir2}" >${stdoutF} 2>${stderrF}
	rtrn=$?
	th_assertTrueWithNoOutput ${rtrn} "${stdoutF}" "${stderrF}"

	assertTrue 'first directory missing' "[ -d '${testDir}' ]"
	assertTrue 'second directory missing' "[ -d '${testDir2}' ]"
}

th_assertTrueWithNoOutput() {
	th_return_=$1
	th_stdout_=$2
	th_stderr_=$3

	assertFalse 'unexpected output to STDOUT' "[ -s '${th_stdout_}' ]"
	assertFalse 'unexpected output to STDERR' "[ -s '${th_stderr_}' ]"

	unset th_return_ th_stdout_ th_stderr_
}

oneTimeSetUp() {
	outputDir="${SHUNIT_TMPDIR}/output"
	mkdir "${outputDir}"
	stdoutF="${outputDir}/stdout"
	stderrF="${outputDir}/stderr"

	#command
	minikubeCmd='minikube'
	mkdirCmd='mkdir' # save command name in variable to make future changes easy
	testDir="${SHUNIT_TMPDIR}/some_test_dir"
}

tearDown() {
	rm -fr "${testDir}"
}

# Load and run shUnit2.
[ -n "${ZSH_VERSION:-}" ] && SHUNIT_PARENT=$0
. /usr/local/bin/shunit2
