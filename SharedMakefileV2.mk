# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# These make targets that are shared
# between all the projects in this repo.
# They will only function if executed inside a project directory.

# There are several variables that are used here.
# The expectation is to define these variables
# inside each project.

# Variables:
# MAX_RESOURCE_COUNT -- The Dafny report generator max resource count.
# 	This is is per project because the verification variability can differ.
# PROJECT_DEPENDENCIES -- List of dependencies for the project.
# 	It should be the list of top level directory names
# PROJECT_SERVICES -- List of names of each local service in the project
# SERVICE_NAMESPACE_<service> -- for each service in PROJECT_SERVICES,
#   the list of dependencies for that smithy namespace. It should be a list
#   of Model directories
# SERVICE_DEPS_<service> -- for each service in PROJECT_SERVICES,
#   the list of dependencies for that smithy namespace. It should be a list
#   of Model directories
# AWS_SDK_CMD -- the `--aws-sdk` command to generate AWS SDK style interfaces.
# STD_LIBRARY -- path from this file to the StandardLibrary Dafny project.
# SMITHY_DEPS -- path from this file to smithy dependencies, such as custom traits.

# This evaluates to the local path _of this file_.
# This means that these are the project roots
# that are shared by all libraries in this repo.
PROJECT_ROOT := $(abspath $(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
# This evaluates to the path of the current working directory.
# i.e. The specific library under consideration.
LIBRARY_ROOT := $(PWD)
# Smithy Dafny code gen needs to know
# where the smithy model is.
# This is generally in the same directory as the library.
# However in the case of a wrapped library,
# such as the test vectors
# the implementation MAY be in a different library
# than the model.
# By having two related variables
# test vector projects can point to
# the specific model they need
# but still build everything in their local library directory.
SMITHY_MODEL_ROOT := $(LIBRARY_ROOT)/Model

# Later versions of Dafny no longer default to adding "_Compile"
# to the names of modules when translating.
# Our target language code still assumes it does,
# so IF the /compileSuffix option is available in our verion of Dafny
# we need to provide it.
COMPILE_SUFFIX_OPTION_CHECK_EXIT_CODE := $(shell dafny /help | grep -q /compileSuffix; echo $$?)
ifeq ($(COMPILE_SUFFIX_OPTION_CHECK_EXIT_CODE), 0)
	COMPILE_SUFFIX_OPTION := -compileSuffix:1
else
	COMPILE_SUFFIX_OPTION :=
endif

# On macOS, sed requires an extra parameter of ""
OS := $(shell uname)
ifeq ($(OS), Darwin)
  SED_PARAMETER := ""
else
  SED_PARAMETER :=
endif


########################## Dafny targets

# Verify the entire project
verify:
	dafny \
		-vcsCores:$(CORES) \
		-compile:0 \
		-definiteAssignment:3 \
		-quantifierSyntax:3 \
		-unicodeChar:0 \
		-functionSyntax:3 \
		-verificationLogger:csv \
		-timeLimit:100 \
		-trace \
		`find . -name *.dfy`

# Verify single file FILE with text logger.
# This is useful for debugging resource count usage within a file.
# Use PROC to further scope the verification
verify_single:
	@: $(if ${CORES},,CORES=2);
	dafny \
		-vcsCores:$(CORES) \
		-compile:0 \
		-definiteAssignment:3 \
		-quantifierSyntax:3 \
		-unicodeChar:0 \
		-functionSyntax:3 \
		-verificationLogger:text \
		-timeLimit:100 \
		-trace \
		$(if ${PROC},-proc:*$(PROC)*,) \
		$(FILE)

#Verify only a specific namespace at env var $(SERVICE)
verify_service:
	@: $(if ${SERVICE},,$(error You must pass the SERVICE to generate for));
	dafny \
		-vcsCores:$(CORES) \
		-compile:0 \
		-definiteAssignment:3 \
		-quantifierSyntax:3 \
		-unicodeChar:0 \
		-functionSyntax:3 \
		-verificationLogger:csv \
		-timeLimit:100 \
		-trace \
		`find ./dafny/$(SERVICE) -name '*.dfy'` \

format:
	dafny format \
		--function-syntax 3 \
		--quantifier-syntax 3 \
		--unicode-char false \
		`find . -name '*.dfy'`

format-check:
	dafny format \
		--check \
		--function-syntax 3 \
		--quantifier-syntax 3 \
		--unicode-char false \
		`find . -name '*.dfy'`

dafny-reportgenerator:
	dafny-reportgenerator \
		summarize-csv-results \
		--max-resource-count $(MAX_RESOURCE_COUNT) \
		TestResults/*.csv

# Dafny helper targets

# On Python, `dafny build` adds Dafny runtime modules (ex. `_dafny.py`).
# Python runs `build` targets for the target module, and `transpile` targets for dependencies and tests.
#build_implementation:
#	dafny build \
#		-t:$(TARGET) \
#		./src/Index.dfy \
#		-o $(OUT) \
#		--quantifier-syntax:3 \
#		--function-syntax:3 \
#		--optimize-erasable-datatype-wrapper:false \
#		--unicode-char:false \
#		$(if $(strip $(STD_LIBRARY)) , --library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy, ) \
#		$(patsubst %, --library:$(PROJECT_ROOT)/%/src/Index.dfy, $(LIBRARIES))

build_implementation:
	dafny build \
		-t:$(TARGET) \
		./src/Index.dfy \
		-o $(OUT) \
		--quantifier-syntax:3 \
		--function-syntax:3 \
		--optimize-erasable-datatype-wrapper:false \
		--unicode-char:false \
		$(if $(strip $(STD_LIBRARY)) , --library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy, ) \
		$(patsubst %, --library:$(PROJECT_ROOT)/%/src/Index.dfy, $(LIBRARIES))

# Transpile the entire project's impl
_transpile_implementation_all: TRANSPILE_DEPENDENCIES=$(patsubst %, -library:$(PROJECT_ROOT)/%, $(PROJECT_INDEX))
_transpile_implementation_all: transpile_implementation

# The `$(OUT)` and $(TARGET) variables are problematic.
# Ideally they are different for every target call.
# However the way make evaluates variables
# having a target specific variable is hard.
# This all comes up because a project
# will need to also transpile its dependencies.
# This is worked around for now,
# by the fact that the `TARGET`
# for all these transpile calls will be the same.
# For `OUT` this is solved by making the paths relative.
# So that the runtime is express once
# and can be the same for all such runtimes.
# Since such targets are all shared,
# this is tractable.

# At this time is is *significatly* faster
# to give Dafny a single file
# that includes everything
# than it is to pass each file to the CLI.
# ~2m vs ~10s for our large projects.
# Also the expectation is that verification happens in the `verify` target
transpile_implementation:
	find ./dafny/**/src ./src -name 'Index.dfy' | sed -e 's/^/include "/' -e 's/$$/"/' | dafny \
		-stdin \
		-noVerify \
		-vcsCores:$(CORES) \
		-compileTarget:$(TARGET) \
		-spillTargetCode:3 \
		-compile:0 \
		-optimizeErasableDatatypeWrapper:0 \
		$(COMPILE_SUFFIX_OPTION) \
		-quantifierSyntax:3 \
		-unicodeChar:0 \
		-functionSyntax:3 \
		-useRuntimeLib \
		-out $(OUT) \
		$(if $(strip $(STD_LIBRARY)) , -library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy, ) \
		$(TRANSPILE_DEPENDENCIES)

# Transpile the entire project's tests
_transpile_test_all: TRANSPILE_DEPENDENCIES=$(if ${DIR_STRUCTURE_V2}, $(patsubst %, -library:dafny/%/src/Index.dfy, $(PROJECT_SERVICES)), -library:src/Index.dfy)
_transpile_test_all: transpile_test

transpile_test:
	find ./dafny/**/test ./test -name "*.dfy" -name '*.dfy' | sed -e 's/^/include "/' -e 's/$$/"/' | dafny \
		-stdin \
		-noVerify \
		-vcsCores:$(CORES) \
		-compileTarget:$(TARGET) \
		-spillTargetCode:3 \
		-runAllTests:1 \
		-compile:0 \
		-optimizeErasableDatatypeWrapper:0 \
		$(COMPILE_SUFFIX_OPTION) \
		-quantifierSyntax:3 \
		-unicodeChar:0 \
		-functionSyntax:3 \
		-useRuntimeLib \
		-out $(OUT) \
		$(if $(strip $(STD_LIBRARY)) , -library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy, ) \
		$(TRANSPILE_DEPENDENCIES)


# If we are not the StandardLibrary, transpile the StandardLibrary.
# Transpile all other dependencies
transpile_dependencies:
	$(if $(strip $(STD_LIBRARY)), $(MAKE) -C $(PROJECT_ROOT)/$(STD_LIBRARY) transpile_implementation_$(LANG), )
	$(patsubst %, $(MAKE) -C $(PROJECT_ROOT)/% transpile_implementation_$(LANG);, $(PROJECT_DEPENDENCIES))

########################## Code-Gen targets

# StandardLibrary is filtered out from dependent-model patsubst list;
#   Its model is contained in $(LIBRARY_ROOT)/model, not $(LIBRARY_ROOT)/../StandardLibrary/Model.

# The OUTPUT variables are created this way
# so that it is possible to run _parts_ of polymorph.
# Otherwise it is difficult to run/test only a Dafny change.
# Since they are defined per target
# a single target can decide what parts it wants to build.

_polymorph:
	@: $(if ${CODEGEN_CLI_ROOT},,$(error You must pass the path CODEGEN_CLI_ROOT: CODEGEN_CLI_ROOT=/[path]/[to]/smithy-dafny/codegen/smithy-dafny-codegen-cli));
	cd $(CODEGEN_CLI_ROOT); \
	./../gradlew run --args="\
	$(OUTPUT_DAFNY) \
	$(OUTPUT_JAVA) \
	$(OUTPUT_DOTNET) \
	$(OUTPUT_PYTHON) \
	--model $(if $(DIR_STRUCTURE_V2), $(LIBRARY_ROOT)/dafny/$(SERVICE)/Model, $(SMITHY_MODEL_ROOT)) \
	--dependent-model $(PROJECT_ROOT)/$(SMITHY_DEPS) \
	$(patsubst %, --dependent-model $(PROJECT_ROOT)/%/Model, $($(service_deps_var))) \
	--namespace $($(namespace_var)) \
	$(AWS_SDK_CMD) \
	$(OUTPUT_LOCAL_SERVICE_$(SERVICE)) \
	";

# Generates all target runtime code for all namespaces in this project.
.PHONY: polymorph_code_gen
polymorph_code_gen:
	for service in $(PROJECT_SERVICES) ; do \
		export service_deps_var=SERVICE_DEPS_$${service} ; \
		export namespace_var=SERVICE_NAMESPACE_$${service} ; \
		export SERVICE=$${service} ; \
		$(MAKE) _polymorph_code_gen || exit 1; \
	done

_polymorph_code_gen: OUTPUT_DAFNY=\
    --output-dafny $(if $(DIR_STRUCTURE_V2), $(LIBRARY_ROOT)/dafny/$(SERVICE)/Model, $(LIBRARY_ROOT)/Model) \
	--include-dafny $(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy
_polymorph_code_gen: OUTPUT_DOTNET=\
	$(if $(DIR_STRUCTURE_V2), --output-dotnet $(LIBRARY_ROOT)/runtimes/net/Generated/$(SERVICE)/, --output-dotnet $(LIBRARY_ROOT)/runtimes/net/Generated/)
_polymorph_code_gen: OUTPUT_JAVA=--output-java $(LIBRARY_ROOT)/runtimes/java/src/main/smithy-generated
_polymorph_code_gen: _polymorph

# Generates dafny code for all namespaces in this project
.PHONY: polymorph_dafny
polymorph_dafny:
	for service in $(PROJECT_SERVICES) ; do \
		export service_deps_var=SERVICE_DEPS_$${service} ; \
		export namespace_var=SERVICE_NAMESPACE_$${service} ; \
		export SERVICE=$${service} ; \
		$(MAKE) _polymorph_dafny || exit 1; \
	done

_polymorph_dafny: OUTPUT_DAFNY=\
    --output-dafny $(if $(DIR_STRUCTURE_V2), $(LIBRARY_ROOT)/dafny/$(SERVICE)/Model, $(LIBRARY_ROOT)/Model) \
	--include-dafny $(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy
_polymorph_dafny: _polymorph

# Generates dotnet code for all namespaces in this project
.PHONY: polymorph_dotnet
polymorph_dotnet:
	for service in $(PROJECT_SERVICES) ; do \
		export service_deps_var=SERVICE_DEPS_$${service} ; \
		export namespace_var=SERVICE_NAMESPACE_$${service} ; \
		export SERVICE=$${service} ; \
		$(MAKE) _polymorph_dotnet || exit 1; \
	done

_polymorph_dotnet: OUTPUT_DOTNET=\
    $(if $(DIR_STRUCTURE_V2), --output-dotnet $(LIBRARY_ROOT)/runtimes/net/Generated/$(SERVICE)/, --output-dotnet $(LIBRARY_ROOT)/runtimes/net/Generated/)
_polymorph_dotnet: _polymorph

# Generates java code for all namespaces in this project
.PHONY: polymorph_java
polymorph_java:
	for service in $(PROJECT_SERVICES) ; do \
		export service_deps_var=SERVICE_DEPS_$${service} ; \
		export namespace_var=SERVICE_NAMESPACE_$${service} ; \
		export SERVICE=$${service} ; \
		$(MAKE) _polymorph_java || exit 1; \
	done

_polymorph_java: OUTPUT_JAVA=--output-java $(LIBRARY_ROOT)/runtimes/java/src/main/smithy-generated
_polymorph_java: _polymorph

.PHONY: polymorph_python
polymorph_python:
	for service in $(PROJECT_SERVICES) ; do \
		export service_deps_var=SERVICE_DEPS_$${service} ; \
		export namespace_var=SERVICE_NAMESPACE_$${service} ; \
		export SERVICE=$${service} ; \
		export snakecase_dir=SNAKECASE_DIR_$${service} ; \
		$(MAKE) _polymorph_python || exit 1; \
	done

_polymorph_python: OUTPUT_PYTHON=--output-python $(LIBRARY_ROOT)/runtimes/python/src/main/smithy-generated
_polymorph_python: _polymorph
_polymorph_python:
	mv $(LIBRARY_ROOT)/runtimes/python/src/main/smithy-generated/$($(snakecase_dir))/*.py $(LIBRARY_ROOT)/runtimes/python/src/$($(snakecase_dir))/smithygenerated

########################## .NET targets

transpile_net: | transpile_implementation_net transpile_test_net transpile_dependencies_net

transpile_implementation_net: TARGET=cs
transpile_implementation_net: OUT=runtimes/net/ImplementationFromDafny
transpile_implementation_net: _transpile_implementation_all

transpile_test_net: TARGET=cs
transpile_test_net: OUT=runtimes/net/tests/TestsFromDafny
transpile_test_net: _transpile_test_all

transpile_dependencies_net: LANG=net
transpile_dependencies_net: transpile_dependencies

test_net:
	dotnet run \
		--project runtimes/net/tests/ \
		--framework net6.0

test_net_mac_intel:
	DYLD_LIBRARY_PATH="/usr/local/opt/openssl@1.1/lib" dotnet run \
		--project runtimes/net/tests/ \
		--framework net6.0

test_net_mac_brew:
	DYLD_LIBRARY_PATH="$(shell brew --prefix)/opt/openssl@1.1/lib/" dotnet run \
		--project runtimes/net/tests/ \
		--framework net6.0

setup_net:
	dotnet restore runtimes/net/

########################## Java targets

build_java: transpile_java mvn_local_deploy_dependencies
	gradle -p runtimes/java build

transpile_java: | transpile_implementation_java transpile_test_java transpile_dependencies_java

transpile_implementation_java: TARGET=java
transpile_implementation_java: OUT=runtimes/java/ImplementationFromDafny
transpile_implementation_java: _transpile_implementation_all _mv_implementation_java

transpile_test_java: TARGET=java
transpile_test_java: OUT=runtimes/java/TestsFromDafny
transpile_test_java: _transpile_test_all _mv_test_java

# Currently Dafny compiles to Java by changing the directory name.
# Java puts things under a `java` directory.
# To avoid `java/implementation-java` the code is generated and then moved.
_mv_implementation_java:
	rm -rf runtimes/java/src/main/dafny-generated
	mv runtimes/java/ImplementationFromDafny-java runtimes/java/src/main/dafny-generated
_mv_test_java:
	rm -rf runtimes/java/src/test/dafny-generated
	mkdir -p runtimes/java/src/test
	mv runtimes/java/TestsFromDafny-java runtimes/java/src/test/dafny-generated

transpile_dependencies_java: LANG=java
transpile_dependencies_java: transpile_dependencies

# If we are not StandardLibrary, locally deploy the StandardLibrary.
# Locally deploy all other dependencies 
mvn_local_deploy_dependencies:
	$(if $(strip $(STD_LIBRARY)), $(MAKE) -C $(PROJECT_ROOT)/$(STD_LIBRARY) mvn_local_deploy, )
	$(patsubst %, $(MAKE) -C $(PROJECT_ROOT)/% mvn_local_deploy;, $(PROJECT_DEPENDENCIES))

# The Java MUST all exist already through the transpile step.
mvn_local_deploy:
	gradle -p runtimes/java publishMavenLocalPublicationToMavenLocal 

# The Java MUST all exsist if we want to publish to CodeArtifact
mvn_ca_deploy:
	gradle -p runtimes/java publishMavenPublicationToPublishToCodeArtifactCIRepository

mvn_staging_deploy:
	gradle -p runtimes/java publishMavenPublicationToPublishToCodeArtifactStagingRepository

test_java:
    # run Dafny generated tests
	gradle -p runtimes/java runTests

########################## Python targets

#build_python: _python_underscore_dependency_extern_names
#build_python: _python_underscore_extern_names
build_python: build_implementation_python
build_python: transpile_test_python
build_python: transpile_dependencies_python
#build_python: _python_revert_underscore_extern_names
#build_python: _python_revert_underscore_dependency_extern_names
build_python: _mv_internaldafny_python
build_python: _remove_src_module_python
build_python: _rename_test_main_python

build_implementation_python: TARGET=py
build_implementation_python: OUT=runtimes/python/dafny_src
build_implementation_python: COMPILE_SUFFIX_OPTION=
build_implementation_python: transpile_implementation

# `transpile_implementation_python` is not directly used, but is indirectly used via `transpile_dependencies`
# The `transpile` target does NOT include the Dafny runtime library (_dafny.py) in the generated code
# while the `build` target does
transpile_implementation_python: transpile_dependencies_python
transpile_implementation_python: transpile_src_python
transpile_implementation_python: transpile_test_python
transpile_implementation_python: _mv_internaldafny_python
transpile_implementation_python: _remove_src_module_python

transpile_src_python: TARGET=py
transpile_src_python: OUT=runtimes/python/dafny_src
transpile_src_python: COMPILE_SUFFIX_OPTION=
transpile_src_python: transpile_implementation

transpile_test_python: TARGET=py
transpile_test_python: OUT=runtimes/python/__main__
transpile_test_python: COMPILE_SUFFIX_OPTION=
transpile_test_python: transpile_test

# Hacky workaround until Dafny supports per-language extern names.
# Replaces `.`s with `_`s in strings like `{:extern ".*"}`.
# This is flawed logic and should be removed, but is a reasonable band-aid for now.
# TODO: Once Dafny supports per-language extern names, remove and replace with Pythonic extern names.
# This is tracked in https://github.com/dafny-lang/dafny/issues/4322.
# This may require new Smithy-Dafny logic to generate Pythonic extern names.
_python_underscore_extern_names:
	find dafny -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/\./_/g' {} \;

#	find src -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/\./_/g' {} \;
#	find Model -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\.*"/s/\./_/g' {} \;
#	find test -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/\./_/g' {} \;

_python_underscore_dependency_extern_names:
    $(patsubst %, $(MAKE) -C $(PROJECT_ROOT)/% _python_underscore_extern_names;, $(LIBRARIES))

_python_revert_underscore_extern_names:
	find dafny -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/_/\./g' {} \;
#	find src -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/_/\./g' {} \;
#	find Model -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/_/\./g' {} \; 2>/dev/null
#	find test -regex ".*\.dfy" -type f -exec sed -i $(SED_PARAMETER) '/.*{:extern \".*\".*/s/_/\./g' {} \;

_python_revert_underscore_dependency_extern_names:
	$(patsubst %, $(MAKE) -C $(PROJECT_ROOT)/% _python_revert_underscore_extern_names;, $(LIBRARIES))

# Move Dafny-generated code into its expected location in the Python module
_mv_internaldafny_python:
	# Remove any previously generated Dafny code in src/, then copy in newly-generated code
	rm -rf runtimes/python/src/main/internaldafny/generated/
	mkdir runtimes/python/src/main/internaldafny/generated/
	mv runtimes/python/dafny_src-py/*.py runtimes/python/src/main/internaldafny/generated
	rm -rf runtimes/python/dafny_src-py
	# Remove any previously generated Dafny code in test/, then copy in newly-generated code
	rm -rf runtimes/python/test/internaldafny/generated
	mkdir runtimes/python/test/internaldafny/generated
	mv runtimes/python/__main__-py/*.py runtimes/python/test/internaldafny/generated
	rm -rf runtimes/python/__main__-py

# Versions of Dafny as of ~9/28 seem to ALWAYS write output to __main__.py,
#   regardless of the OUT parameter...?
# We should figure out what happened and get a workaround
# For now, always write OUT to __main__, then manually rename the primary file...
# TODO: Resolve this before releasing libraries
# Note the name internaldafny_test_executor is specifically chosen
# so as to not be picked up by pytest,
# which finds test_*.py or *_test.py files.
# This is neither, and will not be picked up by pytest.
# This file SHOULD not be run from a context that has not imported the wrapping shim,
#   otherwise the tests will fail.
# We write an extern which WILL be picked up by pytest.
# This extern will import the wrapping shim, then import this `internaldafny_test_executor` to run the tests.
_rename_test_main_python:
	mv runtimes/python/test/internaldafny/generated/__main__.py runtimes/python/test/internaldafny/generated/internaldafny_test_executor.py

_remove_src_module_python:
	# Remove the src/ `module_.py` file.
	# There is a race condition between the src/ and test/ installation of this file.
	# The file that is installed least recently is overwritten by the file installed most recently.
	# The test/ file contains code to execute tests. The src/ file is largely empty.
	# If the src/ file is installed most recently, tests will fail to run.
	# By removing the src/ file, we ensure the test/ file is always the installed file.
	rm runtimes/python/src/$(PYTHON_MODULE_NAME)/internaldafny/generated/module_.py

transpile_dependencies_python: LANG=python
transpile_dependencies_python: transpile_dependencies

test_python:
	rm -rf runtimes/python/.tox
	tox -c runtimes/python --verbose

########################## local testing targets

# These targets are added as a convenience for local development.
# If you experience weird behavior using these targets,
# fall back to the regular `build` or `test` targets.
# These targets MUST only be used for local testing,
# and MUST NOT be used in CI.

# Targets to transpile single local service for convenience.
# Specify the local service to build by passing a SERVICE env var.
# Note that this does not generate identical files as `transpile_implementation_java`

local_transpile_impl_java_single: TARGET=java
local_transpile_impl_java_single: OUT=runtimes/java/ImplementationFromDafny
local_transpile_impl_java_single: local_transpile_impl_single
	cp -R runtimes/java/ImplementationFromDafny-java/* runtimes/java/src/main/dafny-generated
	rm -rf runtimes/java/ImplementationFromDafny-java/

local_transpile_impl_net_single: TARGET=cs
local_transpile_impl_net_single: OUT=runtimes/net/ImplementationFromDafny
local_transpile_impl_net_single: local_transpile_impl_single

local_transpile_impl_single: deps_var=SERVICE_DEPS_$(SERVICE)
local_transpile_impl_single: TRANSPILE_TARGETS=./dafny/$(SERVICE)/src/$(FILE)
local_transpile_impl_single: TRANSPILE_DEPENDENCIES= \
		$(patsubst %, -library:$(PROJECT_ROOT)/%/src/Index.dfy, $($(deps_var))) \
		$(patsubst %, -library:$(PROJECT_ROOT)/%, $(PROJECT_INDEX)) \
		-library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy
local_transpile_impl_single: transpile_implementation

# Targets to transpile single local service for convenience.
# Specify the local service to build by passing a SERVICE env var.
# Note that this does not generate identical files as `transpile_test_java`,
# and will clobber tests generated by other services.

local_transpile_test_java_single: TARGET=java
local_transpile_test_java_single: OUT=runtimes/java/TestsFromDafny
local_transpile_test_java_single: local_transpile_test_single
	cp -R runtimes/java/TestsFromDafny-java/* runtimes/java/src/test/dafny-generated
	rm -rf runtimes/java/TestsFromDafny-java

local_transpile_test_net_single: TARGET=cs
local_transpile_test_net_single: OUT=runtimes/net/tests/TestsFromDafny
local_transpile_test_net_single: local_transpile_test_single

local_transpile_test_single: TRANSPILE_TARGETS=./dafny/$(SERVICE)/test/$(FILE)
local_transpile_test_single: TRANSPILE_DEPENDENCIES= \
		$(patsubst %, -library:dafny/%/src/Index.dfy, $(PROJECT_SERVICES)) \
		$(patsubst %, -library:$(PROJECT_ROOT)/%, $(PROJECT_INDEX)) \
		-library:$(PROJECT_ROOT)/$(STD_LIBRARY)/src/Index.dfy
local_transpile_test_single: transpile_test
